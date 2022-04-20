import json


def save_json(dictionary, file_name, overwrite=True):
    """
    Save json file from dictionary object in results folder

    :parameter dictionary : dictionary to convert to json
    :parameter file_name : filename to save json file (include extension)
    :parameter overwrite : boolean, default is True
    """
    # Serializing json
    json_object = json.dumps(dictionary, indent=4)
    outcome = "w"

    if not overwrite:
        outcome = "w+"

    # Writing to sample.json
    with open(f"./results/{file_name}", outcome) as outfile:
        outfile.write(json_object)
