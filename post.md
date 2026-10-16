# Un hook que detecta un pago duplicado mal informado

## Problema

En un minimarket, una referencia de pago ayuda a reconocer una operación que ya se registró. Si una persona vuelve a presentar la misma referencia, el sistema no debería informar que aceptó otro pago. Este minilab reduce el caso a un diccionario en memoria: la clave es la referencia y el valor es el monto en céntimos. En `pagos.py`, la línea 6 identifica una clave existente y la línea 7 devuelve `False`. El segundo test de `test_pagos.py` comprueba precisamente esa respuesta. El ejemplo no consulta Yape ni prueba si una transferencia ocurrió; solo comprueba la decisión de la función ante una referencia repetida.

## Funcionamiento interno

Configuré `.claude/settings.json` para llamar a `.claude/hooks/check_tests.sh` en dos momentos. `PostToolUse` coincide con las herramientas `Write` y `Edit` y ejecuta el script después de una edición. `Stop` lo ejecuta antes de que Claude Code termine su respuesta. El script cambia al directorio del proyecto mediante `CLAUDE_PROJECT_DIR`, ejecuta `python3 -m unittest -v` y guarda tanto la salida como el código de retorno. Si la suite falla, imprime el resultado en stderr y sale con código 2; si pasa, sale con código 0. La [documentación oficial](https://code.claude.com/docs/en/hooks) indica que el código 2 entrega ese error a Claude y, en `Stop`, le pide continuar. El hook comprueba y comunica: no revierte archivos automáticamente. Los cuatro archivos de código y configuración suman 71 líneas.

## Fallo observado

Primero ejecuté la suite con `return False`: pasaron los tres tests. Después cambié temporalmente esa línea por `return True`, sin modificar `test_pagos.py`. Falló solo `test_no_registra_dos_veces_la_misma_referencia`, en su aserción de la línea 15. La salida incluyó `AssertionError: True is not false` y `FAILED (failures=1)`. El script del hook imprimió `Los tests fallaron. Revisa el cambio antes de terminar:` y terminó con código 2. La causa es concreta: aunque el diccionario sigue teniendo un único pago, la función afirma incorrectamente que aceptó el segundo registro. Restauré `return False`; los tres tests volvieron a pasar y el script salió con código 0. `evidencia.md` conserva las salidas abreviadas de las tres fases.

## Decisiones y límites

Intenté dar a Claude Code la petición de provocar y reparar el fallo. La instalación respondió `Not logged in · Please run /login` antes de cualquier llamada a `Write` o `Edit`. Por tanto, Claude Code no cambió el archivo ni vio la salida de un evento del hook en esta ejecución. Yo decidí hacer la edición controlada, ejecutar la suite y el script, verificar sus códigos de salida y restaurar el código. Esta distinción importa para una demostración honesta: falta repetir la petición en una sesión autenticada y guardar su transcripción. Para el producto real, habría que integrar una fuente de pagos verificable, persistencia y control de concurrencia; este hook solo vigila los tests de la función simulada.
