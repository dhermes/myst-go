# The `go:` Domain for Sphinx

## `go:alias-func`

- `:file: golembic/command/interfaces.go`
- `:line-number: 12`
- `:param-name 0: sqlDirectory`
- `:param-type 0: string`
- `:return-type 0: *golembic.Migrations`
- `:return-type 1: error`

## `go:const`

- `:file: golembic/command/postgres.go`
- `:line-number: 20`
- `:type: literal`
- `:literal: "PGPASSWORD"`

OR

- `:file: postgres/config.go`
- `:line-number: 33`
- `:type: literal`
- `:literal: 16`

OR

- `:file: postgres/config.go`
- `:line-number: 28`
- `:type: time.Duration`
- `:literal: 4 * time.Second`

## `go:constructor`

- `:file: apply.go`
- `:line-number: 11`
- `:for: ApplyConfig`
- `:param-name 0: opts`
- `:param-type 0: ...ApplyOption`
- `:return-type 0: *ApplyConfig`
- `:return-type 1: error`

## `go:struct`

- `:file: golembic/command/value.go`
- `:line-number: 21`

## `go:field`

- `:type: *time.Duration`

must be embedded within a `go:struct`

## `go:file`

- `:import fmt: fmt`
- `:import os: os`
- `:import strings: strings`
- `:import time: time`
- `:import cobra: github.com/spf13/cobra`
- `:import golembic: github.com/dhermes/golembic`
- `:import postgres: github.com/dhermes/golembic/postgres`

## `go:func`

- `:file: golembic/command/root.go`
- `:line-number: 14`
- `:param-name 0: rm`
- `:param-type 0: RegisterMigrations`
- `:return-type 0: *cobra.Command`
- `:return-type 1: error`

OR

- `:file: duration.go`
- `:line-number: 10`
- `:param-name 0: d`
- `:param-type 0: time.Duration`
- `:param-name 1: base`
- `:param-type 1: time.Duration`
- `:return-type 0: int64`
- `:return-type 1: error`

## `go:interface`

- `:file: interfaces.go`
- `:line-number: 31`

## `go:interface-method`

- `:param-name 0: name`
- `:param-type 0: string`
- `:return-type 0: string`

OR

- `:param-name 0: format`
- `:param-type 0: string`
- `:param-name 1: a`
- `:param-type 1: ...interface{}`
- `:return-name 0: n`
- `:return-type 0: string`
- `:return-name 1: err`
- `:return-type 1: error`

must be embedded within a `go:interface`

## `go:method`

- `:file: golembic/command/value.go`
- `:line-number: 27`
- `:receiver: *RoundDuration`
- `:return-type 0: string`

OR

- `:file: manager.go`
- `:line-number: 293`
- `:receiver: *Manager`
- `:param-name 0: ctx`
- `:param-type 0: context.Context`
- `:return-name 0: revision`
- `:return-type 0: string`
- `:return-name 1: createdAt`
- `:return-type 1: time.Time`
- `:return-name 2: err`
- `:return-type 2: error`

OR

- `:file: postgres/config.go`
- `:line-number: 94`
- `:receiver: Config`
- `:return-type 0: string`
- `:return-type 1: error`

## `go:package`

- `:file: postgres/doc.go`
- `:line-number: 1`

## `go:var`

- `:file: postgres/errors.go`
- `:line-number: 10`
- `:type: error`
