from src.translator import translate_content

from mock import patch

def test_unexpected_language():
    # We will mock the functions get_translation and get_language directly within translate_content
    with patch("src.translator.get_translation") as mock_get_translation, patch("src.translator.get_language") as mock_get_language:
        mock_get_translation.return_value = "I don't understand your request"
        mock_get_language.return_value = "I don't understand your request"
        #This would not return an error because the API call for translation and language are both valid strings
        assert(translate_content("Hier ist Ihr fehlerhaftes Beispiel.")==(False,"I don't understand your request"))

        mock_get_translation.return_value = 1234
        mock_get_language.return_value = "German"
        #This returns an error because the translation type is not a string
        assert (translate_content("Hier ist Ihr fehlerhaftes Beispiel.")==(False,"There was an error translating your text."))

        mock_get_translation.return_value = "Translation"
        mock_get_language.return_value = 1234
        #This returns an error because the language type is not a string
        assert (translate_content("Hier ist Ihr fehlerhaftes Beispiel.")==(False,"There was an error detecting the language of your text."))


        mock_get_translation.return_value = None
        mock_get_language.return_value = "German"
        #This returns an error because the translation type is not a string
        assert (translate_content("Hier ist Ihr fehlerhaftes Beispiel.")==(False,"There was an error translating your text."))

        mock_get_translation.return_value = "Translation"
        mock_get_language.return_value = None
        #This returns an error because the language type is not a string
        assert (translate_content("Hier ist Ihr fehlerhaftes Beispiel.")==(False,"There was an error detecting the language of your text."))

        mock_get_translation.return_value = ""
        mock_get_language.return_value = ""
        #This would not return an error because the API calls for translation and language are both valid strings
        assert (translate_content("Hier ist Ihr fehlerhaftes Beispiel.")==(False,""))

        mock_get_translation.return_value = "12345"
        mock_get_language.return_value = "English"
        #This would not return an error because the API call for translation and language are both valid strings
        assert (translate_content("Hier ist Ihr fehlerhaftes Beispiel.")==(True,"12345"))

        mock_get_translation.return_value = ["This is a translation"]
        mock_get_language.return_value = ["English"]
        #This returns an error (first) because the translation type is not a string
        assert (translate_content("Hier ist Ihr fehlerhaftes Beispiel.")==(False,"There was an error translating your text."))
