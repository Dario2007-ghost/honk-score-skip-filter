# honk-score-skip-filter

Filtro diminuto que ahorra cómputo en Reels/TikToks descartando skips <10s.

## Cómo funciona
- Si watch_time < 10s → score 0 (SKIP)
- Si completion >= 80% → 100 (HIGH)
- Si completion >= 40% → 60 (MEDIUM)
- Si no → 20 (LOW)

## Ejemplo
```python
honk_score(5, 60)   # (0, "SKIP")
honk_score(35, 60)  # (60, "MEDIUM")
honk_score(55, 60)  # (100, "HIGH")
