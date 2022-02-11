from utils import join

def append_on_file(data, file):
    file = open(file, "a")
    data_extracted = extract_data(data)
    new_object = parse_to_string(data_extracted)
    file.write(new_object)
    file.close()

def write_on_file(data, file):
    file = open(file, 'w')
    file.write(join(data))
    file.close()

def parse_to_string(data, index=0):
    if index == len(data) - 1:
        return str(data[index]) + "\n"
    return data[index] + "," + parse_to_string(data, index + 1)

def extract_data(data):
    return [data[value] for value in data]


def read_from_file(file):
    file = open(file, "r")
    lines = file.readlines()
    file.close()
    return lines

