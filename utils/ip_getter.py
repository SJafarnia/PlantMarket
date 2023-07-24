from django.http import HttpRequest


def get_ip(req: HttpRequest):

    x_forwarded_for = req.META.get("HTTP_X_FORWARDED_FOR")

    if x_forwarded_for:
        ip = x_forwarded_for.plit(",")[0]
    else:
        ip = req.META.get("REMOTE_ADDR")
        
    return ip
