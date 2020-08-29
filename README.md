# `myst-go`

> Beautiful Go Documentation in Sphinx via MyST-Parser

## Goals

- [ ] Write custom Sphinx domain for Go
- [ ] Manually (i.e. by hand) translate godoc for a package into Markdown and
      render with MyST-Parser (and the custom domain)
- [ ] Write Go package to auto-generate markdown files in the same fashion
      the manual translation proceeded
- [ ] Use `cgo` to build `libmystgo` shared library and include it in Python
      wheels so that Sphinx can autogenerate markdown without a full Go
      toolchain included

## Elements in Go Domain

- Primitive Types
  - [ ] `bool`
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
  - [ ] `float32`
  - [ ] `float64`
  - [ ] `complex64`
  - [ ] `complex128`
  - [ ] `bytes`
  - [ ] `string`
- Container Types
  - [ ] `map`
  - [ ] `slice`
  - [ ] `struct`
  - [ ] `interface`
  - [ ] `chan`
- Values
  - [ ] `const`
  - [ ] `var`
- [ ] Function
- [ ] Method
- [ ] Package

## Prior Art

- [godocjson][1]: AST parser to extract godoc from source files
- [sphinxcontrib-golangdomain][2]: An "old" custom Sphinx domain for Go,
  written for Python 2.7 before Sphinx 2.0 was released

[1]: https://github.com/readthedocs/godocjson
[2]: https://bitbucket.org/ymotongpoo/sphinxcontrib-golangdomain
