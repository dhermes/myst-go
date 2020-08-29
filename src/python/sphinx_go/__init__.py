"""Custom Sphinx domain for the Go programming language."""


import sphinx.domains


class GoDomain(sphinx.domains.Domain):
    pass


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
