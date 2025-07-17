#Decorador valida si empleado tiene tol específico
def check_access(required_role):
    def decorator(func):
        def wrapper(employee):
            #Comprobar si el rol del empleado coincide con el requerido
            if employee.get('role') == required_role:
                return func(employee)
            else:
                print(f'Acceso denegadom solo {required_role} puede realizar esta acción')
        return wrapper
    return decorator
    
def log_action(func):
    def wrapper(employee):
        print(f'Registando acción para el empleado {employee['name']}')
        return func(employee)
    return wrapper


@check_access('admin')
@log_action
def delete_employee(employee):
    print(f'El empleado {employee['name']} ha sido eliminado')

admin = {'name': 'Carlos', 'role': 'admin'}
employee = {'name': 'Ana', 'role': 'employee'}

#delete_employee(admin)
delete_employee(employee)