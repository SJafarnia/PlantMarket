
def seperator(objects, num) -> list:

    """ separates list objects in groups of 'num' """

    groups = []
    for item in range(0, len(objects), num):
        groups.append(objects[item: item + num])
    return groups

