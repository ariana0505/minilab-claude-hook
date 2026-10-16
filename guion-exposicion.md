# Guion de exposición: 10 minutos

Este guion prepara la demostración ante el tutor. La ejecución dentro de Claude Code sigue pendiente hasta iniciar sesión; no se debe presentar la prueba manual como una ejecución del evento del hook.

| Tiempo | Qué mostrar y explicar |
|---|---|
| 0:00–1:00 | Problema: una referencia duplicada debe rechazarse aunque el diccionario conserve una sola entrada. |
| 1:00–2:00 | Repositorio público y alcance: pagos simulados en memoria, sin conexión a Yape. |
| 2:00–3:00 | `pagos.py`, líneas 1–10: validaciones y retorno `False` en la línea 7. |
| 3:00–4:00 | `test_pagos.py`, líneas 12–16: el test exige `False` y una sola entrada. |
| 4:00–5:00 | `.claude/settings.json`, líneas 3–19: cuándo se ejecuta el hook. `.claude/hooks/check_tests.sh`, líneas 2–9: tests y código de salida 2. |
| 5:00–8:00 | Demostración en Claude Code: mostrar tres tests correctos; pedir el cambio temporal a `return True`; señalar el fallo recibido por el hook; restaurar `return False` y mostrar tres tests correctos. Guardar la transcripción. |
| 8:00–9:00 | Autoría y verificación: la autora eligió el caso y revisa el resultado; Codex preparó y probó el proyecto; Claude Code debe mostrar la edición y reparación en vivo. |
| 9:00–10:00 | Límites y preguntas: no bloquea commits ni verifica transferencias; explicar qué requeriría el producto real. |

Si la demostración en Claude Code falla por autenticación, mostrar `evidencia.md` como prueba del script y explicar con claridad que aún falta comprobar el evento en la CLI.
