# `myst-go`

> Beautiful Go Documentation in Sphinx via MyST-Parser

## Goals

- [ ] Write custom Sphinx domain for Go
- [x] Manually (i.e. by hand) translate godoc for a package into Markdown
- [ ] Render manually translated godoc with MyST-Parser (and the custom domain)
- [ ] Write Go package to auto-generate markdown files in the same fashion
      the manual translation proceeded
- [ ] Use `cgo` to build `libmystgo` shared library and include it in Python
      wheels so that Sphinx can autogenerate markdown without a full Go
      toolchain included (suggest: use `MYSTGO_` prefix for symbols)

## Elements in Go Domain

- Basic Types
  - [ ] Literal (i.e. a `const` without a type)
  - [ ] `bool`
  - [ ] `string`
  - [ ] `int`
  - [ ] `int8`
  - [ ] `int16`
  - [ ] `int32`
  - [ ] `int64`
  - [ ] `uint`
  - [ ] `uint8`
  - [ ] `uint16`
  - [ ] `uint32`
  - [ ] `uint64`
  - [ ] `uintptr`
  - [ ] `byte`
  - [ ] `rune`
  - [ ] `float32`
  - [ ] `float64`
  - [ ] `complex64`
  - [ ] `complex128`
- Non-Basic Types
  - [ ] `map`
  - [ ] `slice`
  - [ ] `struct`
  - [ ] `interface`
  - [ ] `chan`
  - [ ] Alias
  - [ ] Variadic Input
  - [ ] Named Returns
  - [ ] Struct-embedding (`:embed-type 0:`)
- Values
  - [ ] `const`
  - [ ] `var`
- [ ] Imports
- [ ] Function
- [ ] Method
- [ ] Package
- [ ] Cross-references
- [ ] `objects.inv` support (`sphinx.ext.intersphinx`)
- [ ] Links to source on GitHub / etc.
- [ ] Noting explicit compile-time type assertions (this may be too challening
      to do)

## References

- [go/types][4] package, [example][3] and [tour][5]

## Prior Art

- [godocjson][1]: AST parser to extract godoc from source files
- [sphinxcontrib-golangdomain][2]: An "old" custom Sphinx domain for Go,
  written for Python 2.7 before Sphinx 2.0 was released

[1]: https://github.com/readthedocs/godocjson
[2]: https://bitbucket.org/ymotongpoo/sphinxcontrib-golangdomain
[3]: https://github.com/golang/example/tree/master/gotypes#types
[4]: https://golang.org/pkg/go/types/
[5]: https://tour.golang.org/basics/11
