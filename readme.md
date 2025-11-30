# Smart Task Analyzer – Singularium Internship 2025

## Algorithm Explanation (450 words)

I designed a weighted scoring algorithm that balances four real-world factors:

1. Urgency → Overdue tasks get massive penalty (+0.5 per day overdue)
2. Importance → Direct multiplier (1–10 → 0.1–1.0)
3. Quick wins → Low effort gets bonus via inverse weighting
4. Dependencies → +8 points per task that depends on this one
5. Cycle detection → Tasks in circular dependencies lose 20 points + warning

Final formula (Smart Balance):


This creates natural behavior:
- A task overdue by 3 days with importance 9 → ~200+ score (do it NOW)
- A 1-hour task with importance 6 → beats a 8-hour task with importance 8
- Tasks blocking others jump ahead
- Circular dependencies are detected and penalized

The algorithm is fully configurable – just change the strategy parameter.

## Design Decisions & Trade-offs
- No database → pure in-memory for speed and simplicity (assignment doesn't require persistence)
- IDs auto-generated if missing → robust against malformed input
- Comprehensive error handling and validation
- Cycle detection using DFS (O(V+E)) – catches circular dependencies early
- Human-readable explanations generated automatically

## Time Breakdown
- Algorithm design & testing: 1h 20m
- Django backend + API: 50m
- Frontend (Tailwind): 50m
- README + polish: 30m
Total: ~3h 30m

## Setup Instructions
```bash
cd backend
python manage.py runserver