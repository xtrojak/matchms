def has_valid_inchi(spectrum):

    """Return True if input is a valid inchi string."""

    empty_entry_types = [
        "N/A",
        "n/a",
        "n\a",
        "NA",
        0,
        "0",
        '""',
        "",
        "nodata",
        '"InChI=n/a"',
        '"InChI="',
        "InChI=1S/N\n",
        "\t\r\n"
    ]

    inchi = spectrum.get("inchi")

    if inchi is None:
        return False

    if inchi in empty_entry_types:
        return False

    if len(inchi) < 12:
        return False

    return True
