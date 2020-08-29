"""Custom Sphinx domain for the Go programming language."""


import sphinx.domains
import sphinx.locale
import sphinx.roles


class GoCallable:
    # TODO
    pass


class GoPackage:
    # TODO
    pass


class GoXRefRole(sphinx.roles.XRefRole):
    # TODO
    pass


class GoDomain(sphinx.domains.Domain):
    """Go language domain."""

    name = "go"
    label = "Go"

    object_types = {
        "function": sphinx.domains.ObjType(
            sphinx.locale._("function"), "func"
        ),
        "method": sphinx.domains.ObjType(sphinx.locale._("method"), "meth"),
        "package": sphinx.domains.ObjType(sphinx.locale._("package"), "pkg"),
    }
    directives = {
        "function": GoCallable,
        "method": GoCallable,
        "package": GoPackage,
    }
    roles = {
        "func": GoXRefRole(fix_parens=True),
        "meth": GoXRefRole(fix_parens=True),
        "pkg": GoXRefRole(),
    }


def setup(app):
    """Register this domain and return metadata about the domain.

    Args:
        app (sphinx.application.Sphinx): The root application object.

    Returns:
        dict: Metadata about the domain
    """
    app.add_domain(GoDomain)

    return {
        "version": "0.0.1",
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
