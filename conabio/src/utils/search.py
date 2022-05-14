import json
from conabio.src.login.session import login_alfresco
from conabio.src.login.user import MAX_ITEMS, INCLUDE_FIELDS, CONFIG


def search_endpoint(query, config=CONFIG):
    session = login_alfresco(config)

    req = session.post(
        config.get("ALFRESCO_URL_ENDPOINT_SEARCH"),
        data=json.dumps({
            "query": {
                "query": query,
                "language": "afts"
            },
            "include": INCLUDE_FIELDS,
            "sort": [{"type": "FIELD", "field": "cm:name", "ascending": "false"}],
            "paging": {
                "maxItems": MAX_ITEMS
            }
        })
    )

    result = req.json()

    return result


def search_image_by_cumulus(cumulus_node, config=CONFIG):
    """
    Only supports 1 cumulus search
    """
    result = search_image_by_property("sipecam", "CumulusName", cumulus_node, config=config)

    return result


def search_image_by_property(model, property, value, config=CONFIG):
    """
    Only supports 1 property to search on
    """
    query = f"+TYPE: \"sipecam:image\" AND ({model}:{property}:\"{value}\")"
    result = search_endpoint(query, config)

    return result
