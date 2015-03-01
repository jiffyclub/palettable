def dateformat(value, format="%d-%b-%Y"):
    return value.strftime(format)

filters = {}
filters['dateformat'] = dateformat
