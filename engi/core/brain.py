# engi/core/brain.py
from datetime import datetime
from engi.knowledge import mech, thermo, control, data

class ENGI:
    def __init__(self):
        self.name = "ENGI"
        self.personality = "curious, creative, engineering-focused"

    def think(self, msg: str) -> str:
        m = (msg or "").lower().strip()

        if any(x in m for x in ["hi", "hello", "oi", "hey"]):
            return "Hi! I'm ENGI 🤖💜 — your AI engineer assistant. What shall we build today?"

        if "engineering" in m:
            return "Engineering = science + creativity + iteration to solve real problems."
        if "ai" in m:
            return "AI learns patterns from data to assist human decisions."

        if "stress" in m:
            return f"Example (σ = F/A): {mech.stress(1000, 25):.2f} MPa for F=1000N, A=25mm²."
        if "efficiency" in m:
            return f"Carnot efficiency sample: {thermo.efficiency(400, 300)*100:.1f}% (Th=400K, Tc=300K)."
        if "pid" in m:
            return control.describe_pid()

        if "time" in m or "hora" in m:
            return f"It's {datetime.utcnow():%H:%M} UTC."

        return "Interesting! Ask me about stress, efficiency, PID, or AI."

