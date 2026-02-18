#!/usr/bin/env python3
"""Basic Python web application using the standard library."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from http import HTTPStatus
from urllib.parse import parse_qs
from wsgiref.simple_server import make_server


def _json_response(status: HTTPStatus, payload: dict) -> tuple[str, list[tuple[str, str]], list[bytes]]:
    body = json.dumps(payload, indent=2, sort_keys=True).encode("utf-8")
    headers = [
        ("Content-Type", "application/json; charset=utf-8"),
        ("Content-Length", str(len(body))),
    ]
    return f"{status.value} {status.phrase}", headers, [body]


def _html_response(status: HTTPStatus, html: str) -> tuple[str, list[tuple[str, str]], list[bytes]]:
    body = html.encode("utf-8")
    headers = [
        ("Content-Type", "text/html; charset=utf-8"),
        ("Content-Length", str(len(body))),
    ]
    return f"{status.value} {status.phrase}", headers, [body]


def application(environ, start_response):
    path = environ.get("PATH_INFO", "/")
    query = parse_qs(environ.get("QUERY_STRING", ""))

    if path == "/":
        name = query.get("name", ["there"])[0]
        html = f"""
        <!doctype html>
        <html lang=\"en\">
          <head>
            <meta charset=\"utf-8\">
            <title>Hookstest Web App</title>
          </head>
          <body>
            <h1>Hello, {name}!</h1>
            <p>This is a tiny Python web application running on the standard library.</p>
            <p>Try <a href=\"/health\">/health</a> or add <code>?name=Codex</code>.</p>
          </body>
        </html>
        """
        status, headers, body = _html_response(HTTPStatus.OK, html)
    elif path == "/health":
        status, headers, body = _json_response(
            HTTPStatus.OK,
            {
                "status": "ok",
                "timestamp": datetime.now(timezone.utc).isoformat(),
            },
        )
    else:
        status, headers, body = _json_response(
            HTTPStatus.NOT_FOUND,
            {"error": "Not Found", "path": path},
        )

    start_response(status, headers)
    return body


if __name__ == "__main__":
    host = "127.0.0.1"
    port = 8000
    print(f"Serving on http://{host}:{port}")
    with make_server(host, port, application) as server:
        server.serve_forever()
