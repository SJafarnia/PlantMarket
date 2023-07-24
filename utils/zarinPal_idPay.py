# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import redirect
import requests
import json
import os

ZP_API_REQUEST = "https://sandbox.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://sandbox.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://sandbox.zarinpal.com/pg/StartPay/"


IDPAYREQ = "https://api.idpay.ir/v1.1/payment"
IDPAYVERIFY = "https://api.idpay.ir/v1.1/payment/verify"

IDPAYHEADER = {
    "accept": "application/json",
    "content-type": "application/json",
    "X-API-KEY": "6a7f99eb-7c20-4412-a972-6dfb7cd253a4",
    "X-SANDBOX": "1",
}

MERCHANT = os.environ.get("ZARINPAL")
# ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
# ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
# ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"
# AMOUNT = 11000  # Rial / Required
# description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
# email = 'email@example.com'  # Optional
# mobile = '09123456789'  # Optional
# Important: need to edit for realy server.
# CallbackURL = 'http://localhost:8000/verify/'


def send_payment_request(price, CallbackURL, desc, mobile, email):
    req_data = {
        "merchant_id": MERCHANT,
        "amount": int(price),
        "callback_url": CallbackURL,
        "description": desc,
        # "metadata": {"mobile": mobile, "email": email}
    }
    req_header = {"accept": "application/json", "content-type": "application/json"}
    req = requests.post(
        url=ZP_API_REQUEST, data=json.dumps(req_data), headers=req_header
    )
    # authority = req.json()['data']['authority']
    # authority = req.json()
    print(json.dumps(req_data))
    print(req)


def send_payment_request_idpay(order_id, price, c_name, phone, mail, desc, CallbackURL):
    req_data = {
        "order_id": int(order_id),
        "amount": int(price),
        "name": c_name,
        "phone": phone,
        "mail": mail,
        "desc": desc,
        "callback": CallbackURL,
    }

    req = requests.post(url=IDPAYREQ, data=json.dumps(req_data), headers=IDPAYHEADER)
    pobj = req.json()
    payment_list = [pobj["id"], pobj["link"]]

    return payment_list


def send_verify_idpay(pay_id, order_id):
    req_data = {"id": pay_id, "order_id": order_id}

    req = requests.post(url=IDPAYVERIFY, data=json.dumps(req_data), headers=IDPAYHEADER)

    pobj = req.json()
    rep = [
        pobj["status"],
        pobj["id"],
        pobj["track_id"],
        {"payment": pobj["payment"]["track_id"]},
    ]
    return rep

