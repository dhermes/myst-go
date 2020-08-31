# https://github.com/sphinx-contrib/cmakedomain/blob/df970be527b41842939d2368195ab3aed8428428/sphinxcontrib/cmakedomain.py
# https://github.com/santoslab/aadl-translator/blob/baf48cc0f078b35c183d9ee96aa8d150a1c023a0/mdcf-architect-documentation/src/site/sphinx/util/AADLDomain.py


import sphinxcontrib.domaintools
import sphinx.util.docfields


def setup(app):
    """

    Args:
        app (sphinx.application.Sphinx):

    Returns:
        dict:
    """
    wild_domain = sphinxcontrib.domaintools.custom_domain(
        class_name="WildDomain",
        name="wild",
        label="Wild",
        elements={
            "vegetation": {
                "objname": "Vegetation",
                "role": "veg",
                "indextemplate": "Veg: %r",
                # parse_node(env, sig, signode)
                "fields": [
                    sphinx.util.docfields.Field(
                        name="leaf-count",
                        names=["leaf-count"],
                        label="Leaf Count",
                        has_arg=True,
                        # rolename
                        # bodyrolename
                    ),
                    # sphinx.util.docfields.TypedField(
                    #     name="leaf-count",
                    #     names=["leaf-count"],
                    #     typenames=["leaf-count"],
                    #     label="Leaf Count",
                    #     # rolename
                    #     # typerolename
                    #     can_collapse=True,
                    # ),
                    # sphinx.util.docfields.GroupedField(
                    #     name="color",
                    #     names=["color"],
                    #     label="Colors",
                    #     # rolename
                    #     can_collapse=True,
                    # ),
                ],
            },
            # "predator": {
            #     "objname": "Predator",
            #     "role": "predator",
            #     "indextemplate": "Preddd: %r",
            #     "fields": [],
            # },
            # "weather": {
            #     "objname": "Weather",
            #     "role": "weather",
            #     "indextemplate": "WeATHER: %r",
            #     "fields": [],
            # },
        },
    )
    app.add_domain(wild_domain)

    return {
        "version": "0.0.1",
        "env_version": 1,
        "parallel_read_safe": False,
        "parallel_write_safe": False,
    }


# `objname`       - Long name of the entry, defaults to entry's key
# `role`          - role name, defaults to entry's key
# `indextemplate` - e.g. ``pair: %s; Make Target``, where %s will be
# `parse_node`    - a function with signature ``(env, sig, signode)``,
# `fields`        - A list of fields where parsed fields are mapped to. this
# `ref_nodeclass` -
#
# sphinx.util.docfields.Field
# sphinx.util.docfields.GroupedField
# sphinx.util.docfields.TypedField
