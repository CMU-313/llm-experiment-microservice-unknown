import os
from ollama import Client

MODEL_NAME = "mistral:7b"

OLLAMA_URL = "http://128.2.220.229:11434"
client = Client(host=OLLAMA_URL)

TRANSLATION_CONTEXT = """\
    You are a professional translator for non-English text to English.

    Return ONLY the English translation of the user text.
    If the text is already English, return it unchagned.
    Preserve punctuation, line breaks, numbers, names, emojis.
    Copy URLs, code, @handles, #hashtags verbatim.
    Do not explain or add examples. Output the translation text only.
    """

CLASSIFICATION_CONTEXT = """\
    You are a language identifier.

    Return ONLY the English name of the predominant language in the user text.
    If the text is already in English, return English.
    No punctuation. No explanations.
    Ignore numbers, URLs, emojis, and code when deciding.
    """


def translate_content(content: str) -> tuple[bool, str]:
    try:
        translation = get_translation(content)
        language = get_language(content)

        # Basic checks for string output
        if (not (isinstance(translation, str))):
            return (False, "There was an error translating your text.")

        if (not (isinstance(language, str))):
            return (False, "There was an error detecting the language of your text.")

        is_english = False
        if language.lower() == "english":
            is_english = True

        return (is_english, translation)

    except Exception as e:
        # Catch any other unexpected errors during the LLM interaction
        print(f"An error occurred during translation (LLM error): {e}")
        return (False, "An unexpected error occurred while processing your request.")


def get_language(post: str) -> str:
    context = CLASSIFICATION_CONTEXT
    response = client.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": context
            },
            {
                "role": "user",
                "content": post
            }
        ]
    )
    return response.message.content


def get_translation(post: str) -> str:
    context = TRANSLATION_CONTEXT
    response = client.chat(
        model=MODEL_NAME,  # model name
        messages=[
            {
                "role": "system",
                "content": context
            },
            {
                "role": "user",
                "content": post
            }
        ]
    )
    return response.message.content
