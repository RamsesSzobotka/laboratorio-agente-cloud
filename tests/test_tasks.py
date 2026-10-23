import unittest
from tasks import agregar_tarea, completar_tarea, eliminar_tarea, pendientes


class TestTasks(unittest.TestCase):
    def test_agregar_tarea(self):
        tareas = []
        tarea = agregar_tarea(tareas, "Leer documentación", "estudio")
        self.assertEqual(tarea["titulo"], "Leer documentación")
        self.assertEqual(tarea["categoria"], "estudio")
        self.assertFalse(tarea["completada"])

    def test_agregar_tarea_categoria_vacia(self):
        tareas = []
        with self.assertRaises(ValueError):
            agregar_tarea(tareas, "Leer documentación", "   ")

    def test_completar_tarea(self):
        tareas = []
        agregar_tarea(tareas, "Practicar", "estudio")
        completar_tarea(tareas, 1)
        self.assertEqual(pendientes(tareas), [])

    def test_eliminar_tarea_exitosa(self):
        tareas = []
        agregar_tarea(tareas, "Practicar Python", "Estudio")
        tarea_a_eliminar = agregar_tarea(tareas, "Comprar cuaderno", "Facultad")

        eliminada = eliminar_tarea(tareas, tarea_a_eliminar["id"])

        self.assertEqual(eliminada, tarea_a_eliminar)
        self.assertEqual(len(tareas), 1)
        self.assertEqual(tareas[0]["titulo"], "Practicar Python")

    def test_eliminar_tarea_id_inexistente_no_modifica_lista(self):
        tareas = []
        agregar_tarea(tareas, "Practicar Python", "Estudio")
        estado_inicial = [t.copy() for t in tareas]

        with self.assertRaisesRegex(ValueError, "Tarea no encontrada"):
            eliminar_tarea(tareas, 99)

        self.assertEqual(tareas, estado_inicial)

    def test_agregar_tarea_no_reutiliza_id_tras_eliminar(self):
        tareas = []
        agregar_tarea(tareas, "Tarea 1", "Estudio")
        agregar_tarea(tareas, "Tarea 2", "Estudio")
        eliminar_tarea(tareas, 1)

        nueva = agregar_tarea(tareas, "Tarea 3", "Estudio")

        self.assertEqual(nueva["id"], 3)

    def test_pendientes_filtra_por_categoria_sin_mayusculas(self):
        tareas = []
        agregar_tarea(tareas, "Practicar Python", "Estudio")
        agregar_tarea(tareas, "Comprar cuaderno", "Facultad")
        agregar_tarea(tareas, "Leer paper", "estudio")
        completar_tarea(tareas, 3)

        filtradas = pendientes(tareas, "eStuDio")
        self.assertEqual(len(filtradas), 1)
        self.assertEqual(filtradas[0]["titulo"], "Practicar Python")

    def test_pendientes_categoria_inexistente_devuelve_lista_vacia(self):
        tareas = []
        agregar_tarea(tareas, "Practicar Python", "Estudio")
        agregar_tarea(tareas, "Comprar cuaderno", "Facultad")

        filtradas = pendientes(tareas, "salud")
        self.assertEqual(filtradas, [])

    def test_pendientes_categoria_en_blanco_devuelve_lista_vacia(self):
        tareas = []
        agregar_tarea(tareas, "Practicar Python", "Estudio")
        agregar_tarea(tareas, "Comprar cuaderno", "Facultad")

        filtradas = pendientes(tareas, "   ")
        self.assertEqual(filtradas, [])


if __name__ == "__main__":
    unittest.main()
