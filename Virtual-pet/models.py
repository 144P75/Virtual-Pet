from datetime import datetime, timezone
from typing import Dict, Any, Optional, List

HUNGER_DECAY_PER_HOUR = 4.0
ENERGY_DECAY_PER_HOUR = 3.0

def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()

class MoodTracker:
    @staticmethod
    def compute_mood(hunger: float, energy: float) -> str:
        avg = (hunger + energy) / 2
        if avg >= 75:
            return "มีความสุขสดใส (Happy)"
        elif avg >= 50:
            return "ผ่อนคลายสบายดี (Content)"
        elif avg >= 25:
            return "หงุดหงิด/หิว (Grumpy)"
        else:
            return "เหนื่อยล้า/หมดแรง (Exhausted)"

class Pet:
    def __init__(
        self,
        name: str,
        hunger: float = 100.0,
        energy: float = 100.0,
        last_updated: Optional[str] = None,
        last_interaction: Optional[str] = None,
        history: Optional[List[Dict[str, Any]]] = None,
    ):
        self.name = name
        self.hunger = hunger
        self.energy = energy
        self.last_updated = last_updated or _now_iso()
        self.last_interaction = last_interaction
        self.history: List[Dict[str, Any]] = history or []
        self.mood = MoodTracker.compute_mood(self.hunger, self.energy)

    def apply_decay(self) -> None:
        try:
            last = datetime.fromisoformat(self.last_updated)
        except (ValueError, TypeError):
            last = datetime.now(timezone.utc)

        now = datetime.now(timezone.utc)
        elapsed_hours = max((now - last).total_seconds() / 3600.0, 0.0)

        self.hunger = max(self.hunger - HUNGER_DECAY_PER_HOUR * elapsed_hours, 0.0)
        self.energy = max(self.energy - ENERGY_DECAY_PER_HOUR * elapsed_hours, 0.0)
        self.last_updated = _now_iso()
        self.mood = MoodTracker.compute_mood(self.hunger, self.energy)

    def _log(self, action_type: str, detail: Optional[str] = None) -> None:
        self.history.append({
            "timestamp": _now_iso(),
            "type": action_type,
            "detail": detail,
        })

    def feed(self, amount: float = 20.0) -> None:
        self.apply_decay()
        self.hunger = min(self.hunger + amount, 100.0)
        self.mood = MoodTracker.compute_mood(self.hunger, self.energy)
        self._log("feed", f"ให้อาหารเพิ่มพลังงานความหิว {amount}")

    def play(self, energy_cost: float = 15.0, hunger_cost: float = 5.0) -> None:
        self.apply_decay()
        self.energy = max(self.energy - energy_cost, 0.0)
        self.hunger = max(self.hunger - hunger_cost, 0.0)
        self.mood = MoodTracker.compute_mood(self.hunger, self.energy)
        self._log("play", f"เล่นกับสัตว์เลี้ยง (สูญเสียพลังงาน {energy_cost})")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "hunger": round(self.hunger, 2),
            "energy": round(self.energy, 2),
            "mood": self.mood,
            "last_interaction": self.last_interaction,
            "last_updated": self.last_updated,
            "history": self.history,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Pet":
        return cls(
            name=data.get("name", "Unnamed"),
            hunger=data.get("hunger", 100.0),
            energy=data.get("energy", 100.0),
            last_updated=data.get("last_updated"),
            last_interaction=data.get("last_interaction"),
            history=data.get("history", []),
        )