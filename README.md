# Hookstest

Un repositorio mínimo para experimentar con el comportamiento de hooks. Úsalo como un entorno de prueba para verificar cuándo se ejecutan los hooks y qué datos reciben.

## Qué es esto
- Un repositorio Git pequeño para probar scripts de hooks
- Un lugar seguro para prototipar e iterar sobre la lógica de hooks
- No es un proyecto de producción

## Inicio rápido
1. Clona el repositorio.
2. Agrega un script de hook en `.git/hooks/` (los hooks son locales a tu clon).
3. Haz un cambio y ejecuta la acción de Git que debería activar el hook.

## Ejemplo: hook `pre-commit`
Crea un hook simple que bloquee commits que contengan la palabra `WIP`:

```bash
cat <<'HOOK' > .git/hooks/pre-commit
#!/usr/bin/env bash
if git diff --cached --name-only | xargs -I{} grep -n "WIP" {} >/dev/null 2>&1; then
  echo "Commit blocked: remove WIP before committing."
  exit 1
fi
HOOK

chmod +x .git/hooks/pre-commit
```

Ahora intenta hacer commit de un archivo que contenga `WIP` para ver el hook en acción.

## Consejos
- Los hooks no se versionan con el repositorio de forma predeterminada.
- Para compartir hooks entre compañeros, considera un directorio `scripts/` y un script de instalación que coloque los hooks en `.git/hooks/`.

## Contribuir
Abre un issue o envía un PR si tienes mejoras o ejemplos adicionales de hooks.
