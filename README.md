# Minilab de Claude Code: detectar un test fallido

Este ejemplo registra pagos simulados por referencia en un diccionario. Si la referencia ya existe, `registrar_pago` devuelve `False` y conserva el único registro. Los montos están en céntimos: `1500` representa 15 unidades monetarias.

## Archivos

- `pagos.py`: valida referencia y monto; registra el pago o rechaza una referencia repetida.
- `test_pagos.py`: comprueba el registro, el rechazo del duplicado y el monto no positivo.
- `.claude/settings.json`: conecta el script con los eventos `PostToolUse` para `Write|Edit` y `Stop`.
- `.claude/hooks/check_tests.sh`: ejecuta la suite y devuelve código 2 con el error en stderr si falla.
- `evidencia.md`: transcripción breve de las tres fases de la prueba y del intento con Claude Code.
- `post.md`: relato de la ejecución y sus límites.

## Ejecución

Ejecuta estos tres comandos desde la carpeta que contiene `minilab-claude-hook`:

```sh
cd minilab-claude-hook
python3 -m unittest -v
claude
```

La suite debe terminar con `Ran 3 tests` y `OK`. Si Claude Code solicita confiar en la carpeta, acéptala para que cargue los hooks del proyecto.

## Reproducir el fallo

Dentro de Claude Code, usa esta petición:

> Para demostrar el hook, cambia temporalmente en pagos.py la línea return False del caso de referencia repetida por return True. No cambies los tests. Observa el error que devuelve el hook y después restaura return False.

El test `test_no_registra_dos_veces_la_misma_referencia` debe fallar con `AssertionError: True is not false`. El script comunica el fallo mediante stderr y sale con código 2. Tras restaurar `return False`, los tres tests vuelven a pasar. Según la [documentación de hooks de Claude Code](https://code.claude.com/docs/en/hooks), `PostToolUse` se ejecuta después de la edición y un `Stop` que sale con código 2 pide a Claude continuar. El hook no revierte la edición ni impide un commit.

En esta ejecución se verificaron las tres fases y el código de salida del script **manualmente**. El intento de demostración dentro de Claude Code se detuvo antes de editar porque la instalación respondió `Not logged in · Please run /login`. Por eso `evidencia.md` distingue la prueba del script de una ejecución real de los eventos de Claude Code. Cuando haya una sesión iniciada, usa la petición anterior y conserva la transcripción del evento para completar esa parte de la demostración.

Este minilab comprueba una función en memoria. No integra Yape, no confirma transferencias y no ofrece persistencia ni protección frente a concurrencia.
