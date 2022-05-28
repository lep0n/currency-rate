from django.shortcuts import render
import requests

# Create your views here.


def index(request):
    response = requests.get(url="https://api.exchangerate-api.com/v4/latest/USD").json()
    currencies = response.get("rates")

    if request.method == "GET":
        context = {
            "currencies": currencies,
        }

        return render(request, "index.html", context)

    if request.method == "POST":
        try:
            amount = float(request.POST.get("amount"))

        except ValueError:
            return render(request, "index.html", {"currencies": currencies})

        from_curr = request.POST.get("from-curr")
        to_curr = request.POST.get("to-curr")

        converted = f"{(currencies[to_curr] / currencies[from_curr]) * amount:.2f}"

        context = {
            "currencies": currencies,
            "from_curr": from_curr,
            "to_curr": to_curr,
            "amount": amount,
            "converted": converted,
        }

        return render(request, "index.html", context)
