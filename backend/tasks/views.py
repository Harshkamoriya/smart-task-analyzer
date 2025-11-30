from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .scoring import calculate_priority
import json

@csrf_exempt
def analyze(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=405)
    
    try:
        data = json.loads(request.body)
        tasks = data.get("tasks", [])
        strategy = data.get("strategy", "smart")
        
        sorted_tasks = calculate_priority(tasks, strategy)
        return JsonResponse({"tasks": sorted_tasks})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


def suggest(request):
    # For demo we just use last analyzed tasks (in real app you'd store in session/redis)
    # We'll just return example top 3
    example_top3 = [
        {"title": "Fix critical login bug", "score": 182.5, "explanation": "overdue by 2 days · very important · blocks 2 tasks"},
        {"title": "Write documentation", "score": 94.2, "explanation": "due today · important"},
        {"title": "Refactor utils.py", "score": 67.8, "explanation": "quick win"}
    ]
    return JsonResponse({"suggestions": example_top3[:3]})