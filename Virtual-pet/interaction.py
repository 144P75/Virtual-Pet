import requests
from typing import Dict, Any

class Interaction:
    DOG_API_URL = "https://dog.ceo/api/breeds/image/random"
    CAT_FACT_URL = "https://catfact.ninja/fact"

    def fetch_dog_image(self) -> Dict[str, Any]:
        try:
            resp = requests.get(self.DOG_API_URL, timeout=10)
            resp.raise_for_status()
            data = resp.json()
            return {"type": "dog_image", "detail": data.get("message"), "ok": True}
        except requests.exceptions.RequestException as e:
            return {"type": "dog_image", "detail": f"ไม่สามารถเชื่อมต่อ Dog API ได้ ({e})", "ok": False}

    def fetch_cat_fact(self) -> Dict[str, Any]:
        try:
            resp = requests.get(self.CAT_FACT_URL, timeout=10)
            resp.raise_for_status()
            data = resp.json()
            return {"type": "cat_fact", "detail": data.get("fact"), "ok": True}
        except requests.exceptions.RequestException as e:
            return {"type": "cat_fact", "detail": f"ไม่สามารถเชื่อมต่อ Cat Fact API ได้ ({e})", "ok": False}