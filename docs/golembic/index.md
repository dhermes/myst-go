# `github.com/dhermes/golembic`

<!-- Exported members from `apply.go` -->

````{go:struct} ApplyConfig

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
:struct: ApplyConfig
:type opts: ...ApplyOption
:location opts: github.com/dhermes/golembic
:return 0: *ApplyConfig
:returnloc 0: github.com/dhermes/golembic
:return 1: error

NewApplyConfig creates a new `ApplyConfig` and applies options.
```

```{go:func} OptApplyVerifyHistory
:type verify: bool
:return 0: ApplyOption
:returnloc 0: github.com/dhermes/golembic

OptApplyVerifyHistory sets `VerifyHistory` on an `ApplyConfig`.
```

```{go:func} OptApplyRevision
:type revision: string
:return 0: ApplyOption
:returnloc 0: github.com/dhermes/golembic

OptApplyRevision sets `Revision` on an `ApplyConfig`.
```

<!-- From `doc.go` -->

```{go:package} github.com/dhermes/golembic

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

Placeholder

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