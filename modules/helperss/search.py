import jmespath


def get_address(data):
    return jmespath.search("people[].address[:2]", data)
