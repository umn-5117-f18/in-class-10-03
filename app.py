import os

import json
from six.moves.urllib.request import urlopen
from six.moves.urllib.parse import urlencode
from functools import wraps

from flask import Flask, abort, jsonify, redirect, render_template, request, url_for, make_response, session, g
import psycopg2

import db
import auth


app = Flask(__name__)


@app.before_first_request
def initialize():
    db.setup()
    auth.setup()
    global auth0
    auth0 = auth.auth0


# Protected Page. Only accessible after login
def requires_auth(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    if 'profile' not in session:
      # Redirect to Login page here
      return redirect('/')
    return f(*args, **kwargs)

  return decorated


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

@app.route('/')
def home():
    with db.get_db_cursor() as cur:
        cur.execute("SELECT * FROM movie")
        movies = [record for record in cur]
    return render_template("home.html", movies=movies)

@app.route('/movies/<movie_id>')
def movie(movie_id):
    with db.get_db_cursor() as cur:
        cur.execute("SELECT * FROM movie where movie_id=%s", (movie_id,))
        movie = cur.fetchone()

    if not movie:
        return abort(404)

    return render_template("movie.html", movie=movie)

@app.route('/genres/<genre>')
def genre(genre):
    with db.get_db_cursor() as cur:
        cur.execute("SELECT * FROM movie where genre=%s", (genre,))
        movies = [record for record in cur]
    return render_template("home.html", movies=movies)

@app.route('/search')
def search():
    query = request.args.get('query')
    if not query:
        # TODO flash
        redirect('home')

    with db.get_db_cursor() as cur:
        # XXX: hack for query wildcard characters w/ correct escaping
        query_wildcard = f"%{query}%"
        cur.execute("SELECT * FROM movie where title ilike (%s)", (query_wildcard,))
        movies = [record for record in cur]
    return render_template("home.html", movies=movies)


# Auth0 callback after login
@app.route('/callback')
def callback_handling():
    # Handles response from token endpoint
    auth0.authorize_access_token()
    resp = auth0.get('userinfo')
    userinfo = resp.json()

    # Store the user information in flask session.
    session['jwt_payload'] = userinfo
    session['profile'] = {
        'user_id': userinfo['sub'],
        'name': userinfo['name'],
        'picture': userinfo['picture']
    }
    return redirect('/')

# Profile Page
@app.route('/profile')
@requires_auth
def profile():
    return render_template('profile.html',
                           userinfo=session['profile'],
                           userinfo_pretty=json.dumps(session['jwt_payload'], indent=4))
# Auth0 Login
@app.route('/login')
def login():
    return auth0.authorize_redirect(redirect_uri='http://localhost:5000/callback', audience=os.environ['AUTH0_DOMAIN']+'/userinfo')

# Auth0 Logout
@app.route('/logout')
def logout():
    # Clear session stored data
    session.clear()
    # Redirect user to logout endpoint
    params = {'returnTo': url_for('home', _external=True), 'client_id': os.environ['CLIENT_ID']}
    app.logger.info(auth0.api_base_url + '/v2/logout?' + urlencode(params))
    return redirect(auth0.api_base_url + '/v2/logout?' + urlencode(params))

if __name__ == '__main__':
    pass
