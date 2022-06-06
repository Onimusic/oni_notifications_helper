def urlencode(string: str) -> str:
    """
    Encoda a string passada como parâmetro para url.
    Args:
        string: Texto que será encodado.

    Returns: Texto encodado para urls.
    """
    import urllib.parse
    return urllib.parse.quote(string)
