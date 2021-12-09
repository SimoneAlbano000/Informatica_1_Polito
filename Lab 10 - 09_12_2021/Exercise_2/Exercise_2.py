# The file will do some I/O stuff

with open("input.txt", "r") as input_data:
    buffer = []
    for line in input_data:
        buffer.append(line) 

# Reverse the buffer
buffer[len(buffer)-1] += "\n"
buffer.reverse()

with open("output.txt", "w") as output_data:
    for i, data in enumerate(buffer):
        output_data.write(data)