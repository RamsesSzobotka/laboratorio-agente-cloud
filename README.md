# laboratorio-agente-cloud

Laboratorio #12 — Tópicos Especiales II: agente cloud de desarrollo asistido por IA.

Proyecto mínimo de gestión de tareas en Python, usado como base para delegar un issue a un agente cloud (GitHub Copilot cloud agent) y revisar su Pull Request.

## Archivos

- `tasks.py` — lógica: `agregar_tarea`, `completar_tarea`, `pendientes`.
- `app.py` — ejemplo de uso por consola.
- `tests/test_tasks.py` — pruebas con `unittest`.

## Ejecutar

```
python app.py
python -m unittest discover -s tests
```
