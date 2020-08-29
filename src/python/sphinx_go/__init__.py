"""Custom Sphinx domain for the Go programming language."""


import sphinx.domains
import sphinx.locale
import sphinx.roles
import sphinx.util.logging


_LOGGER = sphinx.util.logging.getLogger(__name__)


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
        # TODO: This does not make sense because a package is composed of lots
        #       of files (i.e. a single `.docname` doesn't make sense).
        self.packages[pkgname] = (self.env.docname, node_id)


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