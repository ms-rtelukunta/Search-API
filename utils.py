def sanitize_query(query: str) -> str:
    if not query:
        return ""
    return query.strip().lower()


def build_response(query: str, results: list) -> dict:
    return {
        "query": query,
        "count": len(results),
        "results": results,
    }
