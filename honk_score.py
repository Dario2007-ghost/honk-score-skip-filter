def honk_score(watch_time, video_length):
    if watch_time < 10:
        return 0, "SKIP - descartado para ahorrar cómputo"
    completion = watch_time / video_length
    if completion >= 0.8:
        return 100, "HIGH - ver completo"
    elif completion >= 0.4:
        return 60, "MEDIUM - ver resumen"
    else:
        return 20, "LOW - ignorar"

print(honk_score(5, 60))
print(honk_score(35, 60))
print(honk_score(55, 60))
