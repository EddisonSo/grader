from container_client import ContainerService

container_service = ContainerService()

containers = set()

while(True):
    command = input("Command: ")
    if command.lower() == "c":
        containers.add(container_service.create_container().container_id)
    elif command.lower() == "d":
        container_id = input("Input container_id: ")
        container_service.delete_container(container_id)
        containers.remove(container_id)
    elif command.lower() == "da":
        for i in containers:
            container_service.delete_container(i)
            containers.remove(i)
    elif command.lower() == "l":
        for i in containers:
            print(f"container_id: {i}")
    else:
        print("unknown command!")
