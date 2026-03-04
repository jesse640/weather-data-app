import json
from services.collection_service import collect_weather

def handler(request):
    # city = request.args.get("city", "Sydney")

    data = collect_weather()

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(data)
    }
