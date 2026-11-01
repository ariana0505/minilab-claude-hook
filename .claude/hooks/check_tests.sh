#!/bin/sh
proyecto=${CLAUDE_PROJECT_DIR:-"$(dirname "$0")/../.."}
cd "$proyecto" || exit 2

resultado=$(python3 -m unittest -v 2>&1)
estado=$?

if [ "$estado" -ne 0 ]; then
    printf 'Los tests fallaron. Revisa el cambio antes de terminar:\n%s\n' "$resultado" >&2
    exit 2
fi

exit 0
