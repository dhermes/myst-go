# `github.com/dhermes/golembic`

<!-- Exported members from `apply.go` -->

```{go:file} apply.go

```

````{go:struct} ApplyConfig
:file: apply.go
:line-number: 5

ApplyConfig provides configurable fields for "up" commands that will apply
migrations.

```{go:field} VerifyHistory
:type: bool
```

```{go:field} Revision
:type: string
```
````

<!-- --- -->

```{go:ctor} NewApplyConfig
:file: apply.go
:line-number: 11
:for: ApplyConfig
:param-name 0: opts
:param-type 0: ...ApplyOption
:return-type 0: *ApplyConfig
:return-type 1: error

NewApplyConfig creates a new `ApplyConfig` and applies options.
```

```{go:func} OptApplyVerifyHistory
:file: apply.go
:line-number: 24
:param-name 0: verify
:param-type 0: bool
:return-type 0: ApplyOption

OptApplyVerifyHistory sets `VerifyHistory` on an `ApplyConfig`.
```

```{go:func} OptApplyRevision
:file: apply.go
:line-number: 32
:param-name 0: revision
:param-type 0: string
:return-type 0: ApplyOption

OptApplyRevision sets `Revision` on an `ApplyConfig`.
```

<!-- From `doc.go` -->

```{go:file} doc.go

```

```{go:package} github.com/dhermes/golembic
:file: doc.go
:line-number: 1

Package golembic is intended to provide tooling for managing SQL migrations in Go.

The underlying principles of golembic are as follows:

- Migrations should follow a straight line (from some root); this line should
  be verified to avoid merge conflicts causing "branching"
- The "current" state of the world will be tracked in a `migrations` table
  containing all migrations that have been applied.
- A series of migrations should be easy to use both in a script or as part
  of a larger piece of Go code
- Avoid all import time side effects caused either by importing a package that
  uses `init()` or by requiring migrations files to use `init()`
- Down migrations are not supported. The idea being that the risk of data loss
  from a down migration is not worth it and that writing down migrations can
  be more challening than writing up migrations.

The design allows for running "arbitrary" code inside migrations
so that even non-SQL tasks can be tracked as a "run-once" migration.

The name is a portmanteau of Go (the programming language) and `alembic`, the
Python migrations package. The name `alembic` itself is motivated by the
foundational ORM SQLAlchemy (an alembic is a distilling apparatus used by
alchemists).
```

<!-- Exported members from `duration.go` -->

```{go:file} duration.go
:import fmt: fmt
:import time: time
```

```{go:func} ToRoundDuration
:file: duration.go
:line-number: 10
:param-name 0: d
:param-type 0: time.Duration
:param-name 1: base
:param-type 1: time.Duration
:return-type 0: int64
:return-type 1: error

ToRoundDuration converts a duration to an **exact** multiple of some base
duration or errors if round off is required.
```

<!-- Exported members from `errors.go` -->

```{go:file} errors.go
:import errors: errors
```

```{go:var} ErrDurationConversion
:file: errors.go
:line-number: 11
:type: error

ErrDurationConversion is the error returned when a duration cannot be
converted to multiple of some base (e.g. milliseconds or seconds)
without round off.
```

```{go:var} ErrNotRoot
:file: errors.go
:line-number: 14
:type: error

ErrNotRoot is the error returned when attempting to start a sequence of
migration with a non-root migration.
```

```{go:var} ErrMissingRevision
:file: errors.go
:line-number: 17
:type: error

ErrMissingRevision is the error returned when attempting to register a migration
with no revision.
```

```{go:var} ErrNoPrevious
:file: errors.go
:line-number: 20
:type: error

ErrNoPrevious is the error returned when attempting to register a migration
with no previous.
```

```{go:var} ErrPreviousNotRegistered
:file: errors.go
:line-number: 23
:type: error

ErrPreviousNotRegistered is the error returned when attempting to register
a migration with a previous that is not yet registered.
```

```{go:var} ErrAlreadyRegistered
:file: errors.go
:line-number: 26
:type: error

ErrAlreadyRegistered is the error returned when a migration has already been
registered.
```

```{go:var} ErrNilInterface
:file: errors.go
:line-number: 29
:type: error

ErrNilInterface is the error returned when a value satisfying an interface
is nil in a context where it is not allowed.
```

```{go:var} ErrMigrationNotRegistered
:file: errors.go
:line-number: 32
:type: error

ErrMigrationNotRegistered is the error returned when no migration has been
registered for a given revision.
```

```{go:var} ErrMigrationMismatch
:file: errors.go
:line-number: 35
:type: error

ErrMigrationMismatch is the error returned when the migration stored in
SQL does not match the registered migration.
```

```{go:var} ErrCannotInvokeUp
:file: errors.go
:line-number: 38
:type: error

ErrCannotInvokeUp is the error returned when a migration cannot invoke the
up function (e.g. if it is `nil`).
```

<!-- Exported members from `interfaces.go` -->

```{go:file} interfaces.go
:import context: context
:import sql: database/sql
```

```{go:alias} UpMigration
:file: interfaces.go
:line-number: 18
:type: func
:param-type 0: context.Context
:param-type 1: *sql.Tx
:return-type 0: error

UpMigration defines a function interface to be used for up / forward
migrations. The SQL transaction will be started **before** `UpMigration`
is invoked and will be committed **after** the `UpMigration` exits without
error. In addition to the contents of `UpMigration`, a row will be written
to the migrations metadata table as part of the transaction.

The expectation is that the migration runs SQL statements within the
transaction. If a migration cannot run inside a transaction, e.g. a
`CREATE UNIQUE INDEX CONCURRENTLY` statement, then the `UpMigration`
interface should be used.
```

```{go:alias} UpMigrationConn
:file: interfaces.go
:line-number: 23
:type: func
:param-type 0: context.Context
:param-type 1: *sql.Conn
:return-type 0: error

UpMigrationConn defines a function interface to be used for up / forward
migrations. This is the non-transactional form of `UpMigration` and
should only be used in rare situations.
```

````{go:interface} EngineProvider
:file: interfaces.go
:line-number: 31

EngineProvider describes the interface required for a database engine.

```{go:method} QuoteIdentifier
:param-name 0: name
:param-type 0: string
:return-type 0: string

QuoteIdentifier quotes an identifier, such as a table name, for usage
in a query.
```

```{go:method} QuoteLiteral
:param-name 0: literal
:param-type 0: string
:return-type 0: string

QuoteLiteral quotes a literal, such as `2023-01-05 15:00:00Z`, for usage
in a query.
```

```{go:method} Open
:return-type 0: *sql.DB
:return-type 1: error

Open creates a database connection for the engine provider.
```

```{go:method} TableExistsSQL
:return-type 0: string

TableExistsSQL returns a SQL query that can be used to determine if a
table exists. It is expected to use a clause such as `WHERE tablename = $1`
to filter results.
```
````

````{go:interface} PrintfReceiver
:file: interfaces.go
:line-number: 47

PrintfReceiver is a generic interface for logging and printing.

```{go:method} Printf
:param-name 0: format
:param-type 0: string
:param-name 1: a
:param-type 1: ...interface{}
:return-name 0: n
:return-type 0: string
:return-name 1: err
:return-type 1: error
```
````

```{go:alias} ManagerOption
:file: interfaces.go
:line-number: 52
:type: func
:param-type 0: *Manager
:return-type 0: error

ManagerOption describes options used to create a new manager.
```

```{go:alias} MigrationOption
:file: interfaces.go
:line-number: 55
:type: func
:param-type 0: *Migration
:return-type 0: error

MigrationOption describes options used to create a new migration.
```

```{go:alias} ApplyOption
:file: interfaces.go
:line-number: 58
:type: func
:param-type 0: *ApplyConfig
:return-type 0: error

ApplyOption describes options used to create a apply configuration.
```

<!-- Exported members from `log.go` -->

```{go:file} log.go

```

<!-- Exported members from `manager.go` -->

```{go:file} manager.go
:import context: context
:import sql: database/sql
:import fmt: fmt
:import time: time
```

<!-- Exported members from `manager_options.go` -->

```{go:file} manager_options.go
:import sql: database/sql
```

<!-- Exported members from `migration.go` -->

```{go:file} migration.go
:import context: context
:import sql: database/sql
:import fmt: fmt
:import time: time
```

<!-- Exported members from `migration_options.go` -->

```{go:file} migration_options.go
:import context: context
:import sql: database/sql
:import ioutil: io/ioutil
```

<!-- Exported members from `migrations.go` -->

```{go:file} migrations.go
:import fmt: fmt
:import sync: sync
```

<!-- Exported members from `quote.go` -->

```{go:file} quote.go
:import strings: strings
```

<!-- Exported members from `sql.go` -->

```{go:file} sql.go
:import context: context
:import sql: database/sql
:import fmt: fmt
:import time: time
```

<!-- Exported members from `table.go` -->

```{go:file} table.go
:import context: context
:import sql: database/sql
:import fmt: fmt
```
