import requests


# Classe responsável por se conectar e puxar os dados da API:
class DictionaryConnector:
    __dictionary_path = "https://api.dictionaryapi.dev/api/v2/entries/en/"
    json_list = []
    word_dicts_list = []

    def get_json_list(self, word_list: list):
        """
        Receive a list with tuples of lenght 2, and update the json
        of the data about them in the dict API.
        """
        for word in word_list:
            word = word[0]
            word_json = requests.get(self.__dictionary_path + word).json()
            self.json_list.append(word_json)

    def get_basic_word_data(self):
        """
        Receive a list of jsons obtained by the function "get_json_list" and
        update word_dicts_list property with the word and its phonetic within a list.
        """
        for json in self.json_list:
            word = json[0]["word"]
            phonetic = json[0]["phonetic"]
            self.word_dicts_list.append({"word": word, "phonetic": phonetic})

    def get_word_meaning(self, word_list: list):
        """
        Receive a word_list and update the word_dicts_list with
        a list of tuples with meanings and examples.
        """
        meanings = []
        for iterator, json in enumerate(self.json_list):
            for word in json:
                for meaning_item in word["meanings"]:
                    gramatical_class = meaning_item["partOfSpeech"]
                    if gramatical_class == word_list[iterator][1]:
                        for definition in meaning_item["definitions"]:
                            meaning = definition["definition"]
                            if "example" in definition:
                                example = definition["example"]
                            else:
                                example = "without example"
                            meanings.append((meaning, example))
            self.word_dicts_list[iterator]["meaning-example"] = meanings

    def get_words_list(self, word_list: list) -> list:
        """
        Receive a list of tuples with word and gramatical class per tuple, and
        return a list of dicts including word meanings and its examples, and
        phonetic of the word.

        Example:
            params:
                word_list: [("water, noun")]
            return:
                dict: {"word": "water",
                       "phonetic": "/ˈwɔːtər/",
                       "meaning-example": [(definition, example)]}.
        """
        self.get_json_list(word_list)
        self.get_basic_word_data()
        self.get_word_meaning(word_list)
        return self.word_dicts_list
