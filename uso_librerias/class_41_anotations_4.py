from typing import Optional

def find_employee(employee_ids: list[int], employee_id: int) -> Optional[int]:

    """
    Busca un ID de un empleado en una lista de IDS y devuelve el valor si existe.

    Parámetros
    employee_ids (list[int]: Lista de IDs de empleados)
    emplotee_id (int): ID a buscar

    Retorna
    Optiona[int]: el ID encontrado o None si no existe
    """

    if employee_id in employee_ids:
        return employee_id
    return None