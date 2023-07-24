def services(service):
    inp = service.split("#")
    tags = []
    for item in inp:
        tag = item.strip()
        if tag != "":
            if " " in tag:
                n_spaced_tag = tag.split(" ")
                for s_taged in n_spaced_tag:
                    tags.append(s_taged)
            else:
                tags.append(tag)
    return tags
