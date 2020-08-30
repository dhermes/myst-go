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

```{go:constructor} NewApplyConfig
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

```{go:interface-method} QuoteIdentifier
:param-name 0: name
:param-type 0: string
:return-type 0: string

QuoteIdentifier quotes an identifier, such as a table name, for usage
in a query.
```

```{go:interface-method} QuoteLiteral
:param-name 0: literal
:param-type 0: string
:return-type 0: string

QuoteLiteral quotes a literal, such as `2023-01-05 15:00:00Z`, for usage
in a query.
```

```{go:interface-method} Open
:return-type 0: *sql.DB
:return-type 1: error

Open creates a database connection for the engine provider.
```

```{go:interface-method} TableExistsSQL
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

```{go:interface-method} Printf
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

```{go:const} DefaultMetadataTable
:file: manager.go
:line-number: 13
:type: literal
:literal: "golembic_migrations"

DefaultMetadataTable is the default name for the table used to store
metadata about migrations.
```

```{go:constructor} NewManager
:file: manager.go
:line-number: 17
:for: Manager
:param-name 0: opts
:param-type 0: ...ManagerOption
:return-type 0: *Manager
:return-type 1: error

NewManager creates a new manager for orchestrating migrations.
```

````{go:struct} Manager
:file: manager.go
:line-number: 35

Manager orchestrates database operations done via `Up` / `UpConn` as well as
supporting operations such as creating a table for migration metadata and
writing rows into that metadata table during a migration.

```{go:field} MetadataTable
:type: string

MetadataTable is the name of the table that stores migration metadata.
The expected default value (`DefaultMetadataTable`) is
"golembic_migrations".
```

```{go:field} ConnectionPool
:type: *sql.DB

ConnectionPool is a cache-able pool of connections to the database.
```

```{go:field} Provider
:type: EngineProvider

Provider delegates all actions to an abstract SQL database engine, with
the expectation that the provider also encodes connection information.
```

```{go:field} Sequence
:type: *Migrations

Sequence is the collection of registered migrations to be applied,
verified, described, etc. by this manager.
```

```{go:field} Log
:type: PrintfReceiver

Log is used for printing output
```
````

```{go:method} NewConnectionPool
:file: manager.go
:line-number: 54
:receiver: *Manager
:param-name 0: ctx
:param-type 0: context.Context
:return-type 0: *sql.DB
:return-type 1: error

NewConnectionPool creates a new database connection pool and validates that
it can ping the DB.
```

```{go:method} CloseConnectionPool
:file: manager.go
:line-number: 70
:receiver: *Manager
:return-type 0: error

CloseConnectionPool closes the connection pool and removes it, if one is
set / cached on the current manager.
```

```{go:method} EnsureConnectionPool
:file: manager.go
:line-number: 86
:receiver: *Manager
:param-name 0: ctx
:param-type 0: context.Context
:return-type 0: *sql.DB
:return-type 1: error

EnsureConnectionPool returns a cached database connection pool (if already
set) or invokes `NewConnection()` to create a new one.
```

```{go:method} EnsureMigrationsTable
:file: manager.go
:line-number: 102
:receiver: *Manager
:param-name 0: ctx
:param-type 0: context.Context
:return-type 0: error

EnsureMigrationsTable checks that the migrations metadata table exists
and creates it if not.
```

```{go:method} InsertMigration
:file: manager.go
:line-number: 107
:receiver: *Manager
:param-name 0: ctx
:param-type 0: context.Context
:param-name 1: tx
:param-type 1: *sql.Tx
:param-name 2: migration
:param-type 2: Migration
:return-type 0: error

InsertMigration inserts a migration into the migrations metadata table.
```

```{go:method} NewTx
:file: manager.go
:line-number: 127
:receiver: *Manager
:param-name 0: ctx
:param-type 0: context.Context
:return-type 0: *sql.Tx
:return-type 1: error

NewTx creates a new transaction after ensuring there is an existing
connection.
```

```{go:method} ApplyMigration
:file: manager.go
:line-number: 137
:receiver: *Manager
:param-name 0: ctx
:param-type 0: context.Context
:param-name 1: migration
:param-type 1: Migration
:return-name 0: err
:return-type 0: error

ApplyMigration creates a transaction that runs the "Up" migration.
```

```{go:method} Up
:file: manager.go
:line-number: 195
:receiver: *Manager
:param-name 0: ctx
:param-type 0: context.Context
:param-name 1: opts
:param-type 1: ...ApplyOption
:return-type 0: error

Up applies all migrations that have not yet been applied.
```

```{go:method} UpOne
:file: manager.go
:line-number: 229
:receiver: *Manager
:param-name 0: ctx
:param-type 0: context.Context
:param-name 1: opts
:param-type 1: ...ApplyOption
:return-type 0: error

UpOne applies the **next** migration that has yet been applied, if any.
```

```{go:method} UpTo
:file: manager.go
:line-number: 251
:receiver: *Manager
:param-name 0: ctx
:param-type 0: context.Context
:param-name 1: opts
:param-type 1: ...ApplyOption
:return-type 0: error

UpTo applies all migrations that have yet to be applied up to (and
including) a revision, if any. This expects the `ApplyConfig` revision to
be set in `opts`.
```

```{go:method} Latest
:file: manager.go
:line-number: 293
:receiver: *Manager
:param-name 0: ctx
:param-type 0: context.Context
:return-name 0: revision
:return-type 0: string
:return-name 1: createdAt
:return-type 1: time.Time
:return-name 2: err
:return-type 2: error

Latest determines the revision and timestamp of the most recently applied
migration.

NOTE: This assumes, but does not check, that the migrations metadata table
exists.
```

```{go:method} GetVersion
:file: manager.go
:line-number: 359
:receiver: *Manager
:param-name 0: ctx
:param-type 0: context.Context
:param-name 0: opts
:param-type 0: ...ApplyOption
:return-type 0: *Migration
:return-type 1: error

GetVersion returns the migration that corresponds to the version that was
most recently applied.
```

```{go:method} Verify
:file: manager.go
:line-number: 396
:receiver: *Manager
:param-name 0: ctx
:param-type 0: context.Context
:return-name 0: err
:return-type 0: error

Verify checks that the rows in the migrations metadata table match the
sequence.
```

```{go:method} Version
:file: manager.go
:line-number: 479
:receiver: *Manager
:param-name 0: ctx
:param-type 0: context.Context
:param-name 1: opts
:param-type 1: ...ApplyOption
:return-type 0: error

Version displays the revision of the most recent migration to be applied
```

```{go:method} IsApplied
:file: manager.go
:line-number: 500
:receiver: *Manager
:param-name 0: ctx
:param-type 0: context.Context
:param-name 1: tx
:param-type 1: *sql.Tx
:param-name 2: migration
:param-type 2: Migration
:return-type 0: bool
:return-type 1: error

IsApplied checks if a migration has already been applied.

NOTE: This assumes, but does not check, that the migrations metadata table
exists.
```

<!-- Exported members from `manager_options.go` -->

```{go:file} manager_options.go
:import sql: database/sql
```

```{go:func} OptManagerMetadataTable
:file: manager_options.go
:line-number: 8
:param-name 0: table
:param-type 0: string
:return-type 0: ManagerOption

OptManagerMetadataTable sets the metadata table name on a manager.
```

```{go:func} OptManagerConnectionPool
:file: manager_options.go
:line-number: 16
:param-name 0: pool
:param-type 0: *sql.DB
:return-type 0: ManagerOption

OptManagerConnectionPool sets the connection pool on a manager.
```

```{go:func} OptManagerProvider
:file: manager_options.go
:line-number: 24
:param-name 0: provider
:param-type 0: EngineProvider
:return-type 0: ManagerOption

OptManagerProvider sets the provider on a manager.
```

```{go:func} OptManagerSequence
:file: manager_options.go
:line-number: 32
:param-name 0: migrations
:param-type 0: *Migrations
:return-type 0: ManagerOption

OptManagerSequence sets the migrations sequence on a manager.
```

<!-- Exported members from `migration.go` -->

```{go:file} migration.go
:import context: context
:import sql: database/sql
:import fmt: fmt
:import time: time
```

````{go:struct} Migration
:file: migration.go
:line-number: 12

Migration represents an individual migration to be applied; typically as
a set of SQL statements.

```{go:field} Previous
:type: string

Previous is the revision identifier for the migration immediately
preceding this one. If absent, this indicates that this migration is
the "base" or "root" migration.
```

```{go:field} Revision
:type: string

Revision is an opaque name that uniquely identifies a migration. It
is required for a migration to be valid.
```

```{go:field} Description
:type: string

Description is a long form description of why the migration is being
performed. It is intended to be used in "describe" scenarios where
a long form "history" of changes is presented.
```

```{go:field} Up
:type: UpMigration

Up is the function to be executed when a migration is being applied. Either
this field or `UpConn` are required (not both) and this field should be
the default choice in most cases. This function will be run in a transaction
that also writes a row to the migrations metadata table to signify that
this migration was applied.
```

```{go:field} UpConn
:type: UpMigrationConn

UpConn is the non-transactional form of `Up`. This should be used in
rare situations where a migration cannot run inside a transaction, e.g.
a `CREATE UNIQUE INDEX CONCURRENTLY` statement.
```

```{go:field} CreatedAt
:type: time.Time

CreatedAt is intended to be used for migrations retrieved via a SQL
query to the migrations metadata table.
```
````

```{go:constructor} NewMigration
:file: migration.go
:line-number: 40
:for: Migration
:param-name 0: opts
:param-type 0: ...MigrationOption
:return-type 0: *Migration
:return-type 1: error

NewMigration creates a new migration from a variadic slice of options.
```

```{go:method} Like
:file: migration.go
:line-number: 53
:receiver: Migration
:param-name 0: other
:param-type 0: Migration
:return-type 0: bool

Like is "almost" an equality check, it compares the `Previous` and `Revision`.
```

```{go:method} Compact
:file: migration.go
:line-number: 58
:receiver: Migration
:return-type 0: string

Compact gives a "limited" representation of the migration
```

```{go:method} InvokeUp
:file: migration.go
:line-number: 72
:receiver: Migration
:param-name 0: ctx
:param-type 0: context.Context
:param-name 1: pool
:param-type 1: *sql.DB
:param-name 2: tx
:param-type 2: *sql.Tx
:return-type 0: error

InvokeUp dispatches to `Up` or `UpConn`, depending on which is set. If both
or neither is set, that is considered an error. If `UpConn` needs to be invoked,
this lazily creates a new connection from a pool. It's crucial that the pool
sets the relevant timeouts when creating a new connection to make sure
migrations don't cause disruptions in application performance due to
accidentally holding locks for an extended period.
```

<!-- Exported members from `migration_options.go` -->

```{go:file} migration_options.go
:import context: context
:import sql: database/sql
:import ioutil: io/ioutil
```

```{go:func} OptPrevious
:file: migration_options.go
:line-number: 10
:param-name 0: previous
:param-type 0: string
:return-type 0: MigrationOption

OptPrevious sets the previous on a migration.
```

```{go:func} OptRevision
:file: migration_options.go
:line-number: 18
:param-name 0: revision
:param-type 0: string
:return-type 0: MigrationOption

OptRevision sets the revision on a migration.
```

```{go:func} OptDescription
:file: migration_options.go
:line-number: 30
:param-name 0: description
:param-type 0: string
:return-type 0: MigrationOption

OptDescription sets the description on a migration.
```

```{go:func} OptUp
:file: migration_options.go
:line-number: 38
:param-name 0: up
:param-type 0: UpMigration
:return-type 0: MigrationOption

OptUp sets the `up` function on a migration.
```

```{go:func} OptUpFromSQL
:file: migration_options.go
:line-number: 51
:param-name 0: statement
:param-type 0: string
:return-type 0: MigrationOption

OptUpFromSQL returns an option that sets the `up` function to execute a
SQL statement.
```

```{go:func} OptUpFromFile
:file: migration_options.go
:line-number: 65
:param-name 0: filename
:param-type 0: string
:return-type 0: MigrationOption

OptUpFromFile returns an option that sets the `up` function to execute a
SQL statement that is stored in a file.
```

```{go:func} OptUpConn
:file: migration_options.go
:line-number: 75
:param-name 0: up
:param-type 0: UpMigrationConn
:return-type 0: MigrationOption

OptUpConn sets the non-transactional `up` function on a migration.
```

```{go:func} OptUpConnFromSQL
:file: migration_options.go
:line-number: 88
:param-name 0: statement
:param-type 0: string
:return-type 0: MigrationOption

OptUpConnFromSQL returns an option that sets the non-transctional `up`
function to execute a SQL statement.
```

```{go:func} OptUpConnFromFile
:file: migration_options.go
:line-number: 102
:param-name 0: filename
:param-type 0: string
:return-type 0: MigrationOption

OptUpConnFromFile returns an option that sets the non-transctional `up`
function to execute a SQL statement that is stored in a file.
```

```{go:func} OptAlwaysError
:file: migration_options.go
:line-number: 112
:param-name 0: err
:param-type 0: error
:return-type 0: MigrationOption

OptAlwaysError returns an option that always returns an error.
```

<!-- Exported members from `migrations.go` -->

```{go:file} migrations.go
:import fmt: fmt
:import sync: sync
```

```{go:struct} Migrations
:file: migrations.go
:line-number: 9

Migrations represents a sequence of migrations to be applied.
```

```{go:constructor} NewSequence
:file: migrations.go
:line-number: 16
:for: Migrations
:param-name 0: root
:param-type 0: Migration
:return-type 0: *Migrations
:return-type 1: error

NewSequence creates a new sequence of migrations rooted in a single
base / root migration.
```

```{go:method} Register
:file: migrations.go
:line-number: 41
:receiver: *Migrations
:param-name 0: migration
:param-type 0: Migration
:return-type 0: error

Register adds a new migration to an existing sequence of migrations, if
possible. The new migration must have a previous migration and have a valid
revision that is not already registered.
```

```{go:method} RegisterMany
:file: migrations.go
:line-number: 70
:receiver: *Migrations
:param-name 0: ms
:param-type 0: ...Migration
:return-type 0: error

RegisterMany attempts to register multiple migrations (in order) with an
existing sequence.
```

```{go:method} RegisterManyOpt
:file: migrations.go
:line-number: 85
:receiver: *Migrations
:param-name 0: manyOpts
:param-type 0: ...[]MigrationOption
:return-type 0: error

RegisterManyOpt attempts to register multiple migrations (in order) with an
existing sequence. It differs from `RegisterMany()` in that the construction
of `Migration` objects is handled directly here by taking a slice of
option slices.
```

```{go:method} Root
:file: migrations.go
:line-number: 109
:receiver: *Migrations
:return-type 0: Migration

Root does a linear scan of every migration in the sequence and returns
the root migration. In the "general" case such a scan would be expensive, but
the number of migrations should always be a small number.

NOTE: This does not verify or enforce the invariant that there must be
exactly one migration without a previous migration. This invariant is enforced
by the exported methods such as `Register()` and `RegisterMany()` and the
constructor `NewSequence()`.
```

```{go:method} All
:file: migrations.go
:line-number: 128
:receiver: *Migrations
:return-type 0: []Migration

All produces the migrations in the sequence, in order.

NOTE: This does not verify or enforce the invariant that there must be
exactly one migration without a previous migration. This invariant is enforced
by the exported methods such as `Register()` and `RegisterMany()` and the
constructor `NewSequence()`.
```

```{go:method} Since
:file: migrations.go
:line-number: 158
:receiver: *Migrations
:param-name 0: revision
:param-type 0: string
:return-type 0: []Migration
:return-type 1: error

Since returns the migrations that occur **after** `revision`.

This utilizes `All()` and returns all migrations after the one that
matches `revision`. If none match, an error will be returned. If
`revision` is the **last** migration, the migrations returned will be an
empty slice.
```

```{go:method} Until
:file: migrations.go
:line-number: 186
:receiver: *Migrations
:param-name 0: revision
:param-type 0: string
:return-type 0: []Migration
:return-type 1: error

Until returns the migrations that occur **before** `revision`.

This utilizes `All()` and returns all migrations up to and including the one
that matches `revision`. If none match, an error will be returned.
```

```{go:method} Between
:file: migrations.go
:line-number: 210
:receiver: *Migrations
:param-name 0: since
:param-type 0: string
:param-name 1: until
:param-type 1: string
:return-type 0: []Migration
:return-type 1: error

Between returns the migrations that occur between two revisions.

This can be seen as a combination of `Since()` and `Until()`.
```

```{go:method} Revisions
:file: migrations.go
:line-number: 249
:receiver: *Migrations
:return-type 0: []string

Revisions produces the revisions in the sequence, in order.

This utilizes `All()` and just extracts the revisions.
```

```{go:method} Describe
:file: migrations.go
:line-number: 263
:receiver: *Migrations
:param-name 0: log
:param-type 0: PrintfReceiver

Describe displays all of the registered migrations (with descriptions).
```

```{go:method} Get
:file: migrations.go
:line-number: 289
:receiver: *Migrations
:param-name 0: revision
:param-type 0: string
:return-type 0: *Migration

Get retrieves a revision from the sequence, if present. If not, returns
`nil`.
```

<!-- Exported members from `quote.go` -->

```{go:file} quote.go
:import strings: strings
```

```{go:func} QuoteIdentifier
:file: quote.go
:line-number: 17
:param-name 0: name
:param-type 0: string
:return-type 0: string

QuoteIdentifier quotes an identifier, such as a table name, for usage
in a query.

This implementation is vendored in here to avoid the side effects of
importing `github.com/lib/pq`.

See:
- https://github.com/lib/pq/blob/v1.8.0/conn.go#L1564-L1581
- https://www.sqlite.org/lang_keywords.html
- https://github.com/ronsavage/SQL/blob/a67e7eaefae89ed761fa4dcbc5431ec9a235a6c8/sql-99.bnf#L412
```

```{go:func} QuoteLiteral
:file: quote.go
:line-number: 36
:param-name 0: literal
:param-type 0: string
:return-type 0: string

QuoteLiteral quotes a literal, such as `2023-01-05 15:00:00Z`, for usage
in a query.

This implementation is vendored in here to avoid the side effects of
importing `github.com/lib/pq`.

See:
- https://github.com/lib/pq/blob/v1.8.0/conn.go#L1583-L1614
- https://www.sqlite.org/lang_keywords.html
- https://github.com/ronsavage/SQL/blob/a67e7eaefae89ed761fa4dcbc5431ec9a235a6c8/sql-99.bnf#L758-L761
- https://github.com/ronsavage/SQL/blob/a67e7eaefae89ed761fa4dcbc5431ec9a235a6c8/sql-99.bnf#L290
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
