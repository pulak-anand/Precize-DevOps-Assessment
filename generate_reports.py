import requests

def fetch_top_downloaded_models():
    response = requests.get("https://huggingface.co/api/models")
    models_data = response.json()
    models = models_data.get("models", [])
    sorted_models = sorted(models, key=lambda x: x.get("downloads", 0), reverse=True)
    return sorted_models[:10]

def generate_report(models):
    print("Top 10 Downloaded Models:")
    for idx, model in enumerate(models, start=1):
        print(f"{idx}. Name: {model.get('modelId', 'N/A')}, Downloads: {model.get('downloads', 'N/A')}, Model Type: {model.get('modelType', 'N/A')}")

if __name__ == "__main__":
    top_downloaded_models = fetch_top_downloaded_models()
    generate_report(top_downloaded_models)
