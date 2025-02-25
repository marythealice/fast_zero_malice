launch info
Waiting for launch data... Done
Created app 'fast-zero-malice' in organization 'personal'
Admin URL: https://fly.io/apps/fast-zero-malice
Hostname: fast-zero-malice.fly.dev
Setting FLY_API_TOKEN secret in GitHub repository settings
Creating postgres cluster in organization personal
Creating app...
Setting secrets on app fast-zero-malice-db...
Provisioning 1 of 1 machines with image flyio/postgres-flex:17.2@sha256:f4301ae20d193ab3c3539eb9df9a8f8d3736dd331aeec1bfb2e34b539dc353c5
Waiting for machine to start...
Machine 2874437b3e9128 is created
==> Monitoring health checks
  Waiting for 2874437b3e9128 to become healthy (started, 3/3)

Postgres cluster fast-zero-malice-db created
  Username:    postgres
  Password:    mQkoaJH39P5T1v7
  Hostname:    fast-zero-malice-db.internal
  Flycast:     fdaa:10:fb10:0:1::4
  Proxy port:  5432
  Postgres port:  5433
  Connection string: postgres://postgres:mQkoaJH39P5T1v7@fast-zero-malice-db.flycast:5432

Save your credentials in a secure place -- you won't be able to see them again!

Connect to postgres
Any app within the nantesmalice@gmail.com organization can connect to this Postgres using the above connection string

Now that you've set up Postgres, here's what you need to understand: https://fly.io/docs/postgres/getting-started/what-you-should-know/
Checking for existing attachments
Registering attachment
Creating database
Creating user

Postgres cluster fast-zero-malice-db is now attached to fast-zero-malice
The following secret was added to fast-zero-malice:
  DATABASE_URL=postgres://fast_zero_malice:7u4KQRCfa0XqbkR@fast-zero-malice-db.flycast:5432/fast_zero_malice?sslmode=disable
Postgres cluster fast-zero-malice-db is now attached to fast-zero-malice

postgresql+psycopg://fast_zero_malice:7u4KQRCfa0XqbkR@fast-zero-malice-db.flycast:5432/fast_zero_malice