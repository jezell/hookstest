# Guía de contribución

Gracias por tu interés en contribuir a Hookstest. Este repositorio es intencionalmente pequeño y sirve para experimentar con hooks de Git. Las contribuciones deben mantener esa simplicidad.

## Preparación del entorno
1. Clona el repositorio.
2. Verifica que tienes Git instalado.
3. Si vas a probar hooks, recuerda que los hooks viven en tu clon local dentro de `.git/hooks/`.

## Estándares de código y estilo
- Mantén los ejemplos y scripts lo más simples posible.
- Prefiere `bash` portable (`#!/usr/bin/env bash`) y evita dependencias externas innecesarias.
- Documenta los ejemplos con comentarios breves cuando no sean obvios.
- Usa Markdown claro y consistente para la documentación.

## Pruebas
Este repositorio no tiene un sistema de pruebas automatizadas. Si agregas un hook o ejemplo:
- Describe cómo probarlo en el texto del PR o en la documentación.
- Verifica manualmente el comportamiento antes de enviar.

## Proceso de Pull Request
1. Crea una rama desde `main`.
2. Haz cambios pequeños y enfocados.
3. Actualiza la documentación si agregas o cambias ejemplos.
4. Abre un PR describiendo:
   - Qué problema resuelve o qué mejora aporta.
   - Cómo se probó (pasos manuales o comandos).
5. Si tu PR responde a un issue, enlázalo en la descripción.

## Qué tipo de contribuciones se aceptan
- Nuevos ejemplos de hooks (pre-commit, commit-msg, pre-push, etc.).
- Mejoras a la documentación.
- Scripts auxiliares simples para instalar o ejecutar hooks.

Si tienes dudas, abre un issue primero.
