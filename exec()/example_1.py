global_namespace = {'x': 2}
local_namespace = {}

exec("y = x + 3", global_namespace, local_namespace)
print("Local Namespace : ", local_namespace)
print("Value of y : ", local_namespace['y'])
