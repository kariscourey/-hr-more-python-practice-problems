def read_json_data(filename):

    json_data = None

    #  open and read file
    with open(filename) as f:
        json_data = f.read()

    if json_data:
        return json.loads(json_data)

    # decode json format

    # return data


print(read_json_data("test.json"))
