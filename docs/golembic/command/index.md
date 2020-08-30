# `github.com/dhermes/golembic/command`

<!-- Exported members from `doc.go` -->

```{go:file} golembic/command/doc.go

```

```{go:package} github.com/dhermes/golembic/command
:file: golembic/command/doc.go
:line-number: 1

Package command provides helpers to create a binary / command from
a migration sequence.
```

<!-- Exported members from `interfaces.go` -->

```{go:file} golembic/command/interfaces.go
:import golembic: github.com/dhermes/golembic
```

```{go:alias} UpMigration
:file: golembic/command/interfaces.go
:line-number: 12
:type: func
:param-name 0: sqlDirectory
:param-type 0: string
:return-type 0: *golembic.Migrations
:return-type 1: error

RegisterMigrations defines a function interface that registers an entire
sequence of migrations. The only input is a directory where `.sql` files
may be stored. Functions satisfying this interface are intended to be used
to lazily create migrations after flag parsing provides the SQL directory
as input.
```

<!-- Exported members from `postgres.go` -->

```{go:file} golembic/command/postgres.go
:import fmt: fmt
:import os: os
:import strings: strings
:import time: time
:import cobra: github.com/spf13/cobra
:import golembic: github.com/dhermes/golembic
:import postgres: github.com/dhermes/golembic/postgres
```

<!-- Exported members from `provider.go` -->

```{go:file} golembic/command/provider.go
:import context: context
:import fmt: fmt
:import strings: strings
:import cobra: github.com/spf13/cobra
:import golembic: github.com/dhermes/golembic
```

<!-- Exported members from `root.go` -->

```{go:file} golembic/command/root.go
:import errors: errors
:import cobra: github.com/spf13/cobra
:import golembic: github.com/dhermes/golembic
```

<!-- Exported members from `value.go` -->

```{go:file} golembic/command/value.go
:import fmt: fmt
:import time: time
:import pflag: github.com/spf13/pflag
:import golembic: github.com/dhermes/golembic
```
