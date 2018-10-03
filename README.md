# in-class-10-03

starting point: <https://github.com/umn-5117-f18/in-class-10-03>

[notes](https://docs.google.com/document/d/1YK-6FpHgv-ARIUZJPCaFPZeYHROruCHXGz9fDyG-dPc/edit#heading=h.j00h7h8iq9vz)

heroku setup:

```
heroku create
heroku addons:create heroku-postgresql:hobby-dev
# use `heroku pg:psql` and run `\i 'schema.sql'`
git push heroku master
heroku open
```

Auth0 setup (<https://auth0.com>): 
```
Sign up for a free Auth0 account 
Go to your Application Settings section in the Auth0 dashboard
Use the variables to fill in your .env file
```

local setup:

```
# setup
pipenv install
# create .env with datastore connection params (see .env.example)

# run
pipenv shell
heroku local dev
```

heroku commands:

```
heroku logs --tail
heroku pg:psql
```
