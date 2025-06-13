class Robot:
    def __init__(self, id, model):
        self.id = id
        self.model = model
        self.assigned = False  # Empieza disponible

    def assign(self):
        if self.assigned:
            print(f"El robot {self.model} ya está asignado")
        else:
            self.assigned = True
            print(f"El robot {self.model} ha sido asignado")

    def release(self):
        if self.assigned:
            self.assigned = False
            print(f"El robot {self.model} ha sido liberado y está disponible")
        else:            
            print(f"El robot {self.model} ya estaba disponible")

    def status(self):
        return self.assigned
    
    def respond_to_human(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase.")
    
    def describe(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase.")

class EmpatheticRobot(Robot):
    def respond_to_human(self):
        if not self.assigned:
            return f"Hola, soy el robot empático {self.model}. Estoy aquí para escucharte y ayudarte 😊"
        else:
            return f"Hola, soy el robot empático {self.model}, pero ahora mismo estoy ayudando a otro humano."

    def describe(self):
        return ("Soy un robot empático, especializado en apoyar emocionalmente a los humanos.")

class HumanUser:
    def __init__(self, name):
        self.name = name
        self.interacted_robots = []

    def interact(self, robot: Robot):
        if not robot.status():  # Si está disponible
            robot.assign()
            print(robot.respond_to_human())
            self.interacted_robots.append(robot)
        else:
            print(f"{self.name}, el robot {robot.model} no está disponible ahora.")

    def release_robot(self, robot: Robot):
        robot.release()

    def history(self):
        print(f"Robots con los que {self.name} ha interactuado:")
        for r in self.interacted_robots:
            print(f"- {r.model} ({r.id})")

# Ejemplo de uso
robot1 = EmpatheticRobot("E01", "Harmony")

human1 = HumanUser("Elena")

human1.interact(robot1)  # Debería asignar e interactuar
human1.history()         # Muestra historial
human1.release_robot(robot1)  # Libera al robot
