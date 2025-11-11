import os
from ollama import Client

MODEL_NAME = "gemma3:1b"

OLLAMA_URL = "http://localhost:11434"
client = Client(host=OLLAMA_URL)

TRANSLATION_CONTEXT = """\
    You are a language translator.  Translate the ENTIRE input from user into english and return ONLY that

    The following are examples of expected input and output.

    Examples:
    INPUT: Bonjour, je m'appelle Bob
    OUTPUT: Hello, my name is Bob.

    INPUT: Können Sie mir bitte helfen?
    OUTPUT: Can you please help me?
    """

CLASSIFICATION_CONTEXT = """\
    You are a language classifier. Detect the language of the given text in user's content and reply with one word ONLY the English name of that language.

    Example:
    INPUT: Bonjour, je m'appelle Bob
    OUTPUT: French

    INPUT: Können Sie mir bitte helfen?
    OUTPUT: German
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
    if MODEL_NAME=="mistral:7b":
      return response.message.content[1:]
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
    if MODEL_NAME=="mistral:7b":
      return response.message.content[1:]
    return response.message.content
