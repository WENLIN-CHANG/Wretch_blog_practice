from django.shortcuts import render, redirect
import braintree
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from dotenv import load_dotenv
import os

load_dotenv()


PLAN_PRICE = {
    "a":10,
    "b":50,
    "c":100,
}

def new(request):
    plan = request.GET.get("plan")

    # 擋非預期方案
    VALID_PLANS = ["a", "b", "c"]
    if plan is None or plan.lower() not in VALID_PLANS:
        plan = "a"

    token = gateway().client_token.generate()

    return render(request, "payments/new.html", {"plan": plan, "token": token, "price": PLAN_PRICE.get(plan)})


@require_POST
@login_required
def index(request):
    nonce = request.POST.get("nonce")
    plan = request.POST.get("plan")

    result = gateway().transaction.sale(
        {
            "amount": PLAN_PRICE.get(plan),
            "payment_method_nonce": nonce
        }
    )

    if result.is_success:
        messages.success(request, "交易完成")
    else:
        messages.error(request, "交易錯誤")

    return redirect("articles:index")


def gateway():
    return braintree.BraintreeGateway(
        braintree.Configuration(
            environment=braintree.Environment.Sandbox,
            merchant_id=os.getenv("merchant_id"),
            public_key=os.getenv("public_key"),
            private_key=os.getenv("private_key"),
        )
    )
