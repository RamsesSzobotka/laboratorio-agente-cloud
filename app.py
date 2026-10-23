from tasks import agregar_tarea, completar_tarea, eliminar_tarea, pendientes

tareas = []
agregar_tarea(tareas, "Estudiar agentes cloud", "estudio")
agregar_tarea(tareas, "Preparar laboratorio", "facultad")
completar_tarea(tareas, 1)
eliminar_tarea(tareas, 2)

for tarea in pendientes(tareas):
    print(f'- {tarea["id"]}: {tarea["titulo"]}')
