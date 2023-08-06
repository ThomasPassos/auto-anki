from dataclasses import dataclass, field
from typing import List, Tuple

import requests


# Dataclass que simula uma palavra
@dataclass
class Word:
    word: str
    word_class: str
    phonetic: str = ""
    meanings: List[Tuple[str, str]] = field(default_factory=list)


# Classe responsável por se conectar e puxar os dados da API:
class DictionaryConnector:
    data_model = List[Tuple[str, str]]
    __dictionary_path = "https://api.dictionaryapi.dev/api/v2/entries/en/"
    
    def __init__(self, word_list: data_model):
        self.word_list = word_list
        self.json_list = []
        self.words = []

    def _generate_word_object(self, word_list: data_model):
        """
        Receive a data_model and create Word objects with the data.
        """
        for word_tuple in word_list:
            word = Word(word_tuple[0], word_tuple[1])
            self.words.append(word)

    # TODO - Teste
    def _get_json_list(self):
        """
        Get the json with word information by the Free Dictionary API.
        """
        for word_object in self.words:
            word = word_object.word
            try:
                request = requests.get(self.__dictionary_path + word)
                request.raise_for_status()
            except requests.exceptions.HTTPError:
                word_json = {"error_4XX": "word not found"}
                self.json_list.append(word_json)
            else:
                word_json = request.json()
                self.json_list.append(word_json)

    # TODO - Teste
    def _get_word_atributes(self):
        """
        Update the Word object atributes phonetic and meanings,
        the latter with a tuple containing meaning and example.
        """
        for word, json in zip(self.words, self.json_list):
            if "error_4XX" not in json:
                phonetic = json[0]["phonetic"]
                word.phonetic = phonetic
                for word_dict in json:
                    for meaning_item in word_dict["meanings"]:
                        gramatical_class = meaning_item["partOfSpeech"]
                        if gramatical_class == word.word_class:
                            for definition in meaning_item["definitions"]:
                                meaning = definition["definition"]
                                if "example" in definition:
                                    example = definition["example"]
                                else:
                                    example = "without example"
                                word.meanings.append((meaning, example))

    def get_words_list(self) -> List[Word]:
        """
        Receive a data_model with word and word class, and
        return a list of Word objects.

        Example:
            params:
                word_list: [("water", "noun"), ...]
            return:
                words: [Word(word="water", word_class="noun", ...), ...].
        """
        self._generate_word_object(self.word_list)
        self._get_json_list()
        self.get_word_atributes()
        return self.words
