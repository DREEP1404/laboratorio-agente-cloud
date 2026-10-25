import unittest
from tasks import agregar_tarea, completar_tarea, eliminar_tarea, pendientes

class TestTasks(unittest.TestCase):
    def test_agregar_tarea(self):
        tareas = []
        tarea = agregar_tarea(tareas, "Leer documentación", "Estudio")
        self.assertEqual(tarea["titulo"], "Leer documentación")
        self.assertEqual(tarea["categoria"], "Estudio")
        self.assertFalse(tarea["completada"])

    def test_agregar_tarea_categoria_vacia(self):
        tareas = []
        with self.assertRaises(ValueError):
            agregar_tarea(tareas, "Leer documentación", " ")

    def test_completar_tarea(self):
        tareas = []
        agregar_tarea(tareas, "Practicar", "Estudio")
        completar_tarea(tareas, 1)
        self.assertEqual(pendientes(tareas), [])

    def test_pendientes_filtra_por_categoria_sin_mayusculas(self):
        tareas = []
        agregar_tarea(tareas, "Leer documentación", "Estudio")
        agregar_tarea(tareas, "Preparar laboratorio", "Laboratorio")
        agregar_tarea(tareas, "Repasar conceptos", "ESTUDIO")
        completar_tarea(tareas, 3)

        filtradas = pendientes(tareas, "estudio")
        self.assertEqual(len(filtradas), 1)
        self.assertEqual(filtradas[0]["titulo"], "Leer documentación")

    def test_pendientes_categoria_inexistente_devuelve_vacia(self):
        tareas = []
        agregar_tarea(tareas, "Leer documentación", "Estudio")
        agregar_tarea(tareas, "Preparar laboratorio", "Laboratorio")

        filtradas = pendientes(tareas, "Salud")
        self.assertEqual(filtradas, [])

    def test_eliminar_tarea_existente(self):
        tareas = []
        tarea_1 = agregar_tarea(tareas, "Leer documentación", "Estudio")
        agregar_tarea(tareas, "Preparar laboratorio", "Laboratorio")

        eliminada = eliminar_tarea(tareas, tarea_1["id"])
        self.assertEqual(eliminada["titulo"], "Leer documentación")
        self.assertEqual(len(tareas), 1)
        self.assertEqual(tareas[0]["titulo"], "Preparar laboratorio")

    def test_eliminar_tarea_id_inexistente(self):
        tareas = []
        agregar_tarea(tareas, "Leer documentación", "Estudio")

        with self.assertRaises(ValueError):
            eliminar_tarea(tareas, 99)

if __name__ == "__main__":
    unittest.main()
