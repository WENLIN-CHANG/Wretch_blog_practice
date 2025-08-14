from django.shortcuts import render


def new(request):
    plan = request.GET.get("plan")

    # 擋非預期方案
    VALID_PLANS = ["a", "b", "c"]
    if plan.lower() not in VALID_PLANS:
        plan = "a"

    return render(request, "payments/new.html", {"plan": plan})


def index(request):
    pass
