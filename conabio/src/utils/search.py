import json
from conabio.src.login.session import login_alfresco
from conabio.src.login.user import MAX_ITEMS
from conabio.src.utils.save import save_json, save_list_as_csv
from conabio.src.utils.read import read_json


def parse_range_date_to_query_value(min_date, max_date):
    """
    Parse min and max date to a value that Alfresco can use
    to search in date ranges
    :param min_date:
    :param max_date:
    :return:
    """
    return f"[{min_date} TO {max_date}]"


class SipecamAlfresco:
    MAX_ITEMS = 5000

    def __init__(self, model_type, config):
        """
        :param model_type: Audio, Image or Video
        :param config: config must have ALFRESCO_API_KEY and ALFRESCO_API_ENDPOINT keys
        """
        self.config = config
        self.model_type = model_type
        self.query =  f"+TYPE: \"sipecam:{model_type}\""
        self.session = login_alfresco(self.config.get("ALFRESCO_API_KEY"))
        self.result = None
        self.output_path = "."
        self.saved_files = []

    def add_query_property(self, property, value):
        """
        Add a property to the alfresco query (afts language)
        :param property:
        :param value:
        :return:
        """
        self.query = f"{self.query} AND +(sipecam:{property}:{value})"

    def save_result(self, file_path_name, overwrite=True):
        """
        Save the json result according to the output path and file path complete
        :param file_path_name:
        :param overwrite:
        :return:
        """
        save_json(self.result, file_path_name, overwrite)
        self.saved_files.append(file_path_name)

    def reset_saved_files(self):
        """
        Reset the list of saved files
        :return:
        """
        self.saved_files = []

    def search(self, skipcount=0):
        """
        request the post consultation according to the query
        :param skipcount: default is 0, meaning first results
        :return:
        """
        INCLUDE_FIELDS = ["properties", "path"]

        req = self.session.post(
            self.config.get("ALFRESCO_API_ENDPOINT"),
            data=json.dumps({
                "query": {
                    "query": self.query,
                    "language": "afts"
                },
                "include": INCLUDE_FIELDS,
                "sort": [{"type": "FIELD", "field": "cm:name", "ascending": "false"}],
                "paging": {
                    "maxItems": MAX_ITEMS,
                    "skipCount": skipcount
                }
            })
        )
        self.result = req.json()

    def set_output_path(self, outputpath):
        """
        Set output path, default is in place
        :param outputpath:
        :return:
        """
        self.output_path = outputpath

    def exahustive_search(self, overwrite=True):
        """
        Exhaustive search implies saving all the results in the output path

        :param overwrite:
        :return:
        """
        skipcount = 0
        end_of_pagination = False

        # A cumulus can have more than the MAX_ITEMS allowed in the pagination, so
        # a loop is necessary.
        while not end_of_pagination:

            self.search(skipcount)
            try:
                if not self.result["list"]["pagination"]["hasMoreItems"]:
                    end_of_pagination = True
            except:
                if self.result["error"]:
                    raise Exception(self.result["error"])

            file_name = f"{self.output_path}/search_result_{self.model_type}_{skipcount}.json"
            # Every pagination will be saved as a json
            self.save_result(file_name, overwrite)
            skipcount += MAX_ITEMS

    def extract_paths(self):
        """
        Extract paths found in the results, and extract them in a csv file
        :return:
        """
        path_list = []
        # Afterward we only want to extract the path in order to find easily the files
        for json_file in self.saved_files:
            result = read_json(json_file)

            # totalItems = result["list"]["pagination"]["totalItems"]
            entries_list = (result["list"]["entries"])

            for entry in entries_list:
                complete_path = f'{entry["entry"]["path"]["name"]}/{entry["entry"]["name"]}'

                # This replacement name will depend on your mounting path: but according to our documentation
                # the data can be found in the open data sipecam bucket
                complete_path = complete_path.replace("/Company Home/Sites/sipecam/documentLibrary/", f"data/")
                path_list.append([complete_path])

        path_csv = f"{self.output_path}/{self.model_type}_path_extract.csv"
        save_list_as_csv(path_csv, ["item"], path_list)
