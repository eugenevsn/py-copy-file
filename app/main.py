def copy_file(command: str) -> None:
    args = command.split()
    if len(args) == 3 and args[0] == "cp":

        source = args()[1]
        destination = args()[2]

        if source == destination:
            return

        with open(source, "r") as source_file, \
             open(destination, "w") as out_file:
            out_file.write(source_file.read())
