from collections import deque

def manage_delivery_queue() -> deque:

    #Crea una cola para gestionar entregas de productos
    delivery_queue = deque(['order_1', 'oderder_2', 'order_3'])
    delivery_queue.append('order_4') #agregar al final de la cola
    delivery_queue.appendleft('order_0') # Agrega al inicio de la lista
    delivery_queue.pop() #Elimina al final el utimo
    delivery_queue.popleft() #Elimina el primero de la lista
    return delivery_queue

queue =  manage_delivery_queue()
print(queue)
