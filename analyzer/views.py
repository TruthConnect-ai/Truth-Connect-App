import requests
from django.shortcuts import render
from django.http import JsonResponse

EXTERNAL_API_URL = "https://example.com/api/classify"  # Placeholder

def analyze_view(request):
    if request.method == "POST":
        text = request.POST.get("text", "")
        try:
            response = requests.post(EXTERNAL_API_URL, json={"text": text}, timeout=5)
            result = response.json().get("verdict", "unknown")
        except Exception:
            result = "error contacting classification service"
        return JsonResponse({"verdict": result})
    return render(request, "analyzer/form.html")
