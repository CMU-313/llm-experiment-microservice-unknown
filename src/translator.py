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
    You are a language classifier. Detect the language of the given text in user's content and reply with one word ONLY the English name of that language.

    The following are examples of expected input and output. Do not return the examples and do not classify this context text, only the users'.

    Example:
    INPUT:Bonjour, je m'appelle Bob
    OUTPUT:French

    INPUT:Können Sie mir bitte helfen?
    OUTPUT:German
    """


def translate_content(content: str) -> tuple[bool, str]:
    try:
        # no need to translate if detected as english
        language = get_language(content) 
        if (not (isinstance(language, str))):
            return (False, "There was an error detecting the language of your text.")

        if language.lower().strip() == "english" :
            return (True, content)
        
        translation = get_translation(content)
        # Basic checks for string output
        if (not (isinstance(translation, str))):
            return (False, "There was an error translating your text.")

        # is_english = False
        # if language.lower().strip() == "english":
        #     is_english = True

        return (False, translation)

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
        ],
        options={"temperature": 0.0, "top_p": 0.0, "num_predict": 8}
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
        ],
    )
    return response.message.content
