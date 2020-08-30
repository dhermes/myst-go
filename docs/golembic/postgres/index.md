# `github.com/dhermes/golembic/postgres`

<!-- Exported members from `config.go` -->

```{go:file} postgres/config.go
:import fmt: fmt
:import url: net/url
:import time: time
:import golembic: github.com/dhermes/golembic
```

```{go:const} DefaultHost
:file: postgres/config.go
:line-number: 14
:type: literal
:literal: "localhost"

DefaultHost is the default database hostname, typically used
when developing locally.
```

```{go:const} DefaultPort
:file: postgres/config.go
:line-number: 16
:type: literal
:literal: "5432"

DefaultPort is the default postgres port.
```

```{go:const} DefaultDatabase
:file: postgres/config.go
:line-number: 19
:type: literal
:literal: "postgres"

DefaultDatabase is the default database to connect to, we use
`postgres` to not pollute the template databases.
```

```{go:const} DefaultDriverName
:file: postgres/config.go
:line-number: 24
:type: literal
:literal: "postgres"

DefaultDriverName is the default SQL driver to be used when creating
a new database connection pool via `sql.Open()`. This default driver
is expected to be registered by importing `github.com/lib/pq`.
```

```{go:const} DefaultLockTimeout
:file: postgres/config.go
:line-number: 28
:type: time.Duration
:literal: 4 * time.Second

DefaultLockTimeout is the default timeout to use when attempting to
acquire a lock.
```

```{go:const} DefaultStatementTimeout
:file: postgres/config.go
:line-number: 31
:type: time.Duration
:literal: 5 * time.Second

DefaultStatementTimeout is the default timeout to use when invoking a
SQL statement.
```

```{go:const} DefaultIdleConnections
:file: postgres/config.go
:line-number: 33
:type: literal
:literal: 16

DefaultIdleConnections is the default number of idle connections.
```

```{go:const} DefaultMaxConnections
:file: postgres/config.go
:line-number: 35
:type: literal
:literal: 32

DefaultMaxConnections is the default maximum number of connections.
```

```{go:const} DefaultMaxLifetime
:file: postgres/config.go
:line-number: 40
:type: time.Duration
:literal: time.Duration(0)

DefaultMaxLifetime is the default maximum lifetime of driver connections.

If max lifetime <= 0, connections are not closed due to a connection's age.
See: https://github.com/golang/go/blob/go1.15/src/database/sql/sql.go#L940
```

````{go:struct} Config
:file: postgres/config.go
:line-number: 44

Config is a set of connection config options.

```{go:field} ConnectionString
:type: string

ConnectionString is a fully formed connection string.
```

```{go:field} Host
:type: string

Host is the server to connect to.
```

```{go:field} Port
:type: string

Port is the port to connect to.
```

```{go:field} Database
:type: string

Database is the database name
```

```{go:field} Schema
:type: string

Schema is the application schema within the database, defaults to `public`.
```

```{go:field} Username
:type: string

Username is the username for the connection via password auth.
```

```{go:field} Password
:type: string

Password is the password for the connection via password auth.
```

```{go:field} SSLMode
:type: string

SSLMode is the SSL mode for the connection.
```

```{go:field} DriverName
:type: string

DriverName specifies the name of SQL driver to be used when creating
a new database connection pool via `sql.Open()`. The default driver
is expected to be registered by importing `github.com/lib/pq`, however
we may want to support other drivers that are wire compatible, such
as `github.com/jackc/pgx`.
```

```{go:field} ConnectTimeout
:type: time.Duration

ConnectTimeout determines the maximum wait for connection. The minimum
allowed timeout is 2 seconds, so anything below is treated the same
as unset.

See: https://www.postgresql.org/docs/10/libpq-connect.html#LIBPQ-CONNECT-CONNECT-TIMEOUT
```

```{go:field} LockTimeout
:type: time.Duration

LockTimeout is the timeout to use when attempting to acquire a lock.

See: https://www.postgresql.org/docs/current/runtime-config-client.html#GUC-LOCK-TIMEOUT
```

```{go:field} StatementTimeout
:type: time.Duration

StatementTimeout is the timeout to use when invoking a SQL statement.

See: https://www.postgresql.org/docs/current/runtime-config-client.html#GUC-STATEMENT-TIMEOUT
```

```{go:field} IdleConnections
:type: int

IdleConnections is the number of idle connections.
```

```{go:field} MaxConnections
:type: int

MaxConnections is the maximum number of connections.
```

```{go:field} MaxLifetime
:type: time.Duration

MaxLifetime is the maximum time a connection can be open.
```
````

```{go:method} GetConnectionString
:file: postgres/config.go
:line-number: 94
:receiver: Config
:return-type 0: string
:return-type 1: error

GetConnectionString creates a PostgreSQL connection string from the config.
If `ConnectionString` is already cached on the `Config`, it will be returned
immediately.
```

```{go:func} SetTimeoutMilliseconds
:file: postgres/config.go
:line-number: 181
:param-name 0: q
:param-type 0: url.Values
:param-name 1: name
:param-type 1: string
:param-name 2: d
:param-type 2: time.Duration
:return-type 0: error

SetTimeoutMilliseconds sets a timeout value in connection string query parameters.

Valid units for this parameter in PostgresSQL are "ms", "s", "min", "h"
and "d" and the value should be between 0 and 2147483647ms. We explicitly
cast to milliseconds but leave validation on the value to PostgreSQL.

  golembic=> BEGIN;
  BEGIN
  golembic=> SET LOCAL lock_timeout TO '4000ms';
  SET
  golembic=> SHOW lock_timeout;
   lock_timeout
  --------------
   4s
  (1 row)
  --
  golembic=> SET LOCAL lock_timeout TO '4500ms';
  SET
  golembic=> SHOW lock_timeout;
   lock_timeout
  --------------
   4500ms
  (1 row)
  --
  golembic=> COMMIT;
  COMMIT

See:
- https://www.postgresql.org/docs/current/runtime-config-client.html#GUC-LOCK-TIMEOUT
- https://www.postgresql.org/docs/current/runtime-config-client.html#GUC-STATEMENT-TIMEOUT
```

```{go:func} SetTimeoutSeconds
:file: postgres/config.go
:line-number: 199
:param-name 0: q
:param-type 0: url.Values
:param-name 1: name
:param-type 1: string
:param-name 2: d
:param-type 2: time.Duration
:return-type 0: error

SetTimeoutSeconds sets a timeout value in connection string query parameters.

This timeout is expected to be an exact number of seconds (as an integer)
so we convert `d` to an integer first and set the value as a query parameter
without units.

See:
- https://www.postgresql.org/docs/current/runtime-config-client.html#GUC-LOCK-TIMEOUT
```

<!-- Exported members from `doc.go` -->

```{go:file} postgres/doc.go

```

```{go:package} github.com/dhermes/golembic/postgres
:file: postgres/doc.go
:line-number: 1

Package postgres provides PostgreSQL helpers for golembic.
```

<!-- Exported members from `errors.go` -->

```{go:file} postgres/errors.go
:import errors: errors
```

```{go:var} ErrNegativeTimeout
:file: postgres/errors.go
:line-number: 10
:type: error

ErrNegativeTimeout is the error returned when a timeout duration cannot
be negative.
```

```{go:var} ErrNegativeCount
:file: postgres/errors.go
:line-number: 13
:type: error

ErrNegativeCount is the error returned when a configured count cannot
be negative.
```

<!-- Exported members from `options.go` -->

```{go:file} postgres/options.go
:import fmt: fmt
:import time: time
```

```{go:alias} Option
:file: postgres/options.go
:line-number: 9
:type: func
:param-type 0: *Config
:return-type 0: error

Option describes options used to create a new config for a SQL provider.
```

```{go:func} OptHost
:file: postgres/options.go
:line-number: 12
:param-name 0: host
:param-type 0: string
:return-type 0: Option

OptHost sets the `Host` on a `Config`.
```

```{go:func} OptPort
:file: postgres/options.go
:line-number: 20
:param-name 0: port
:param-type 0: string
:return-type 0: Option

OptPort sets the `Port` on a `Config`.
```

```{go:func} OptDatabase
:file: postgres/options.go
:line-number: 28
:param-name 0: database
:param-type 0: string
:return-type 0: Option

OptDatabase sets the `Database` on a `Config`.
```

```{go:func} OptSchema
:file: postgres/options.go
:line-number: 36
:param-name 0: schema
:param-type 0: string
:return-type 0: Option

OptSchema sets the `Schema` on a `Config`.
```

```{go:func} OptUsername
:file: postgres/options.go
:line-number: 44
:param-name 0: username
:param-type 0: string
:return-type 0: Option

OptUsername sets the `Username` on a `Config`.
```

```{go:func} OptPassword
:file: postgres/options.go
:line-number: 52
:param-name 0: password
:param-type 0: string
:return-type 0: Option

OptPassword sets the `Password` on a `Config`.
```

```{go:func} OptConnectTimeout
:file: postgres/options.go
:line-number: 60
:param-name 0: d
:param-type 0: time.Duration
:return-type 0: Option

OptConnectTimeout sets the `ConnectTimeout` on a `Config`.
```

```{go:func} OptSSLMode
:file: postgres/options.go
:line-number: 73
:param-name 0: sslMode
:param-type 0: string
:return-type 0: Option

OptSSLMode sets the `SSLMode` on a `Config`.
```

```{go:func} OptDriverName
:file: postgres/options.go
:line-number: 81
:param-name 0: name
:param-type 0: string
:return-type 0: Option

OptDriverName sets the `DriverName` on a `Config`.
```

```{go:func} OptLockTimeout
:file: postgres/options.go
:line-number: 89
:param-name 0: d
:param-type 0: time.Duration
:return-type 0: Option

OptLockTimeout sets the `LockTimeout` on a `Config`.
```

```{go:func} OptStatementTimeout
:file: postgres/options.go
:line-number: 102
:param-name 0: d
:param-type 0: time.Duration
:return-type 0: Option

OptStatementTimeout sets the `StatementTimeout` on a `Config`.
```

```{go:func} OptIdleConnections
:file: postgres/options.go
:line-number: 115
:param-name 0: count
:param-type 0: int
:return-type 0: Option

OptIdleConnections sets the `IdleConnections` on a `Config`.
```

```{go:func} OptMaxConnections
:file: postgres/options.go
:line-number: 128
:param-name 0: count
:param-type 0: int
:return-type 0: Option

OptMaxConnections sets the `MaxConnections` on a `Config`.
```

```{go:func} OptMaxLifetime
:file: postgres/options.go
:line-number: 141
:param-name 0: d
:param-type 0: time.Duration
:return-type 0: Option

OptMaxLifetime sets the `MaxLifetime` on a `Config`.
```

```{go:func} OptAlwaysError
:file: postgres/options.go
:line-number: 154
:param-name 0: err
:param-type 0: error
:return-type 0: Option

OptAlwaysError returns an option that always returns an error.
```

<!-- Exported members from `provider.go` -->

```{go:file} postgres/provider.go
:import sql: database/sql
:import fmt: fmt
:import golembic: github.com/dhermes/golembic
```
