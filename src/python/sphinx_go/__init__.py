"""Custom Sphinx domain for the Go programming language."""


import sphinx.domains
import sphinx.locale
import sphinx.roles
import sphinx.util.logging


_LOGGER = sphinx.util.logging.getLogger(__name__)


class GoNotImplemented:
    # TODO
    pass


class GoCallable:
    # TODO
    pass


class GoPackage:
    # TODO
    pass


class GoXRefRole(sphinx.roles.XRefRole):
    def process_link(self, env, refnode, has_explicit_title, title, target):
        """Process a cross reference, e.g. for relative references.

        Args:
            env (sphinx.environment.BuildEnvironment): The current build
                environment.
            refnode (docutils.nodes.Element): The node being referred to.
            has_explicit_title (bool): Flag indicating if the reference has
                an explicit title.
            title (str): Title of the reference.
            target (str): Target for the reference

        Returns:
            Tuple[str, str]: Pair of

            * Title (for display purposes) of the cross referenced item
            * Actual target (after processing)
        """
        refnode["go:interface"] = env.ref_context.get("go:interface")
        refnode["go:struct"] = env.ref_context.get("go:struct")
        refnode["go:package"] = env.ref_context.get("go:package")
        if not has_explicit_title:
            title = title.lstrip(".")
            target = target.lstrip("~")
            if title[:1] == "~":
                title = title[1:]
                dot = title.rfind(".")
                if dot != -1:
                    title = title[dot + 1 :]

        if target[:1] == ".":
            target = target[1:]
            refnode["refspecific"] = True

        return title, target


class GoDomain(sphinx.domains.Domain):
    """Go language domain."""

    name = "go"
    label = "Go"

    object_types = {
        "alias-func": sphinx.domains.ObjType(
            sphinx.locale._("alias-func"), "type"
        ),
        "const": sphinx.domains.ObjType(sphinx.locale._("constant"), "value"),
        "constructor": sphinx.domains.ObjType(
            sphinx.locale._("constructor"), "func"
        ),
        "field": sphinx.domains.ObjType(sphinx.locale._("field"), "field"),
        # NOTE: `file` will not be rendered
        "func": sphinx.domains.ObjType(sphinx.locale._("function"), "func"),
        "interface": sphinx.domains.ObjType(
            sphinx.locale._("interface"), "type"
        ),
        "interface-method": sphinx.domains.ObjType(
            sphinx.locale._("interface-method"), "method"
        ),
        "method": sphinx.domains.ObjType(sphinx.locale._("method"), "method"),
        "package": sphinx.domains.ObjType(
            sphinx.locale._("package"), "package"
        ),
        "struct": sphinx.domains.ObjType(sphinx.locale._("struct"), "type"),
        "var": sphinx.domains.ObjType(sphinx.locale._("variable"), "value"),
    }
    directives = {
        "alias-func": GoNotImplemented,
        "const": GoNotImplemented,
        "constructor": GoNotImplemented,
        "field": GoNotImplemented,
        "file": GoNotImplemented,
        "func": GoCallable,
        "interface": GoNotImplemented,
        "interface-method": GoCallable,
        "method": GoCallable,
        "package": GoPackage,
        "struct": GoNotImplemented,
        "var": GoNotImplemented,
    }
    roles = {
        "field": GoXRefRole(),
        "func": GoXRefRole(fix_parens=True),
        "method": GoXRefRole(fix_parens=True),
        "package": GoXRefRole(),
        "type": GoXRefRole(),
        "value": GoXRefRole(),
    }
    initial_data = {
        "objects": {},  # fullname -> docname, node_id, objtype
        "packages": {},  # pkgname -> docname, node_id
    }

    @property
    def objects(self):
        """Return the objects associated with the domain.

        Returns:
            Dict[str, Tuple[str, str, str]]: A mapping where keys are the
            full name of an object and the values are a triple of

            * document name
            * node ID
            * object type
        """
        return self.data.setdefault("objects", {})

    def note_object(self, fullname, objtype, node_id, location=None):
        """Keep track / take note of a new object.

        Args:
            fullname (str): The full name of the object.
            objtype (str): The type of object being noted.
            node_id (str): The ID of the document node.
            location (Optional[Any]): Extra optional context to be passed to
                the logger.
        """
        if fullname in self.objects:
            docname = self.objects[fullname][0]
            _LOGGER.warning(
                sphinx.locale.__(
                    "duplicate %s description of %s, other %s in %s"
                ),
                objtype,
                fullname,
                objtype,
                docname,
                location=location,
            )

        self.objects[fullname] = (self.env.docname, node_id, objtype)

    @property
    def packages(self):
        """Return the packages associated with the domain.

        Returns:
            Dict[str, Tuple[List[str], str]]: A mapping where keys are the
            package import path and the values are a pair of

            * filenames in the package
            * node ID
        """
        return self.data.setdefault("packages", {})

    def note_package(self, pkgname, node_id):
        """Keep track / take note of a new package.

        Args:
            pkgname (str): The import name of the package.
            node_id (str): The ID of the document node.
        """
        # TODO: This ma not make sense because a package is composed of lots
        #       of files (i.e. a single `.docname` doesn't make sense).
        #       Need to verify that `self.env.docname` is a Sphinx document not
        #       a Go document.
        self.packages[pkgname] = (self.env.docname, node_id)

    def clear_doc(self, docname):
        """Remove all members defined in a Sphinx document.

        Args:
            docname (str): The name of a Sphinx document.
        """
        for fullname, (pkg_docname, _, _) in list(self.objects.items()):
            if pkg_docname == docname:
                del self.objects[fullname]

        for pkgname, (pkg_docname, _) in list(self.packages.items()):
            if pkg_docname == docname:
                del self.packages[pkgname]


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
        "parallel_read_safe": False,
        "parallel_write_safe": False,
    }
