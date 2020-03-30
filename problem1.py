def p1(url):
    """
    :param url: a string representing a url in the form "protocol://domain/path"
    :return: a Python dict representing the url with keys "protocol", "domain", "path"
    if any part of the url is missing, a blank string will be returned
    assumption: a string will contain at most 1 instance of "://"
    assumption: a string that does not contain "://" will be assumed to include no protocol, only domain and possibly path
    """
    ret = {"protocol": "", "domain": "", "path": ""}
    if "://" in url:
        ret["protocol"] = url.split("://")[0]
        url = url.split("://")[1]
    ret["domain"] = url.split("/", 1)[0]  # max of one split
    if(len(url.split("/", 1)) == 2):
        ret["path"] = url.split("/", 1)[1]
    return ret
