import json


def save_json(dictionary, file_path_name, overwrite=True):
    """

    """
    # Serializing json
    json_object = json.dumps(dictionary, indent=4)

    outcome = "w"

    if not overwrite:
        outcome = "w+"

    # Writing to sample.json
    with open(f"{file_path_name}", outcome) as outfile:
        outfile.write(json_object)


def save_list_as_csv(path, header, list_path, overwrite=True):
    import csv
    write_mode = "w"
    if not overwrite:
        write_mode = "w+"

    with open(path, write_mode) as f:
        write = csv.writer(f)
        write.writerow(header)
        write.writerows(list_path)
