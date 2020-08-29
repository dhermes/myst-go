# `github.com/dhermes/golembic`

<!-- Exported members from `apply.go` -->

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
:type opts: ...ApplyOption
:location opts: github.com/dhermes/golembic
:return-type 0: *ApplyConfig
:return-location 0: github.com/dhermes/golembic
:return-type 1: error

NewApplyConfig creates a new `ApplyConfig` and applies options.
```

```{go:func} OptApplyVerifyHistory
:file: apply.go
:line-number: 24
:type verify: bool
:return-type 0: ApplyOption
:return-location 0: github.com/dhermes/golembic

OptApplyVerifyHistory sets `VerifyHistory` on an `ApplyConfig`.
```

```{go:func} OptApplyRevision
:file: apply.go
:line-number: 32
:type revision: string
:return-type 0: ApplyOption
:return-location 0: github.com/dhermes/golembic

OptApplyRevision sets `Revision` on an `ApplyConfig`.
```

<!-- From `doc.go` -->

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

```{go:func} ToRoundDuration
:file: duration.go
:line-number: 10
:type d: time.Duration
:location d: time
:type base: time.Duration
:location base: time
:return-type 0: int64
:return-type 1: error

ToRoundDuration converts a duration to an **exact** multiple of some base
duration or errors if round off is required.
```

<!-- Exported members from `errors.go` -->

Placeholder

<!-- Exported members from `interfaces.go` -->

Placeholder

<!-- Exported members from `log.go` -->

Placeholder

<!-- Exported members from `manager.go` -->

Placeholder

<!-- Exported members from `manager_options.go` -->

Placeholder

<!-- Exported members from `migration.go` -->

Placeholder

<!-- Exported members from `migration_options.go` -->

Placeholder

<!-- Exported members from `migrations.go` -->

Placeholder

<!-- Exported members from `quote.go` -->

Placeholder

<!-- Exported members from `sql.go` -->

Placeholder

<!-- Exported members from `table.go` -->

Placeholder
