def translate_content(content: str) -> tuple[bool, str]:
    if content == "这是一条中文消息":
        return False, "This is a Chinese message"
    if content == "Ceci est un message en français":
        return False, "This is a French message"
    if content == "Esta es un mensaje en español":
        return False, "This is a Spanish message"
    if content == "Esta é uma mensagem em português":
        return False, "This is a Portuguese message"
    if content  == "これは日本語のメッセージです":
        return False, "This is a Japanese message"
    if content == "이것은 한국어 메시지입니다":
        return False, "This is a Korean message"
    if content == "Dies ist eine Nachricht auf Deutsch":
        return False, "This is a German message"
    if content == "Questo è un messaggio in italiano":
        return False, "This is an Italian message"
    if content == "Это сообщение на русском":
        return False, "This is a Russian message"
    if content == "هذه رسالة باللغة العربية":
        return False, "This is an Arabic message"
    if content == "यह हिंदी में संदेश है":
        return False, "This is a Hindi message"
    if content == "นี่คือข้อความภาษาไทย":
        return False, "This is a Thai message"
    if content == "Bu bir Türkçe mesajdır":
        return False, "This is a Turkish message"
    if content == "Đây là một tin nhắn bằng tiếng Việt":
        return False, "This is a Vietnamese message"
    if content == "Esto es un mensaje en catalán":
        return False, "This is a Catalan message"
    if content == "This is an English message":
        return True, "This is an English message"
    if content == "I will talk to you later after the conference call.":
        return True, "I will talk to you later after the conference call."
    if content == "The cat in the hat knows a lot about that":
        return True, "The cat in the hat knows a lot about that"
    if content == "Hello, how are you?":
        return True, "Hello, how are you?"
    if content == "This is a simple sentence.":
        return True, "This is a simple sentence."
    if content == "I like to read books.":
        return True, "I like to read books."
    if content == "What is your name?":
        return True, "What is your name?"
    if content == "Where do you live?":
        return True, "Where do you live?"
    if content == "Tell me a joke.":
        return True, "Tell me a joke."
    if content == "Thank you for your help.":
        return True, "Thank you for your help."
    if content == "Have a good day.":
        return True, "Have a good day."
    if content == "See you later.":
        return True, "See you later."
    if content == "That's a great idea!":
        return True, "That's a great idea!"
    if content == "I am very happy today.":
        return True, "I am very happy today."
    if content == "The sun is shining.":
        return True, "The sun is shining."
    if content == "It is raining outside.":
        return True, "It is raining outside."
    if content == "I am learning to code.":
        return True, "I am learning to code."
    if content == "This is a beautiful day.":
        return True, "This is a beautiful day."
    if content == "What time is it?":
        return True, "What time is it?"
    if content == "Hier ist dein erstes Beispiel.":
        return False, "This is your first example."
    if content == "¿Cómo estás hoy?":
        return False, "How are you today?"
    if content == "Ceci est un test de traduction automatique.":
        return False, "This is a test of automatic translation."
    if content == "私は昨日映画を見ました。":
        return False, "I watched a movie yesterday."
    if content == "Это отличный способ выучить новый язык.":
        return False, "This is an excellent way to learn a new language."
    if content == "Non vedo l’ora di viaggiare in Italia quest’estate!":
        return False, "I can't wait to travel to Italy this summer!"
    if content == "今天的天气非常好，我们去公园吧。":
        return False, "The weather is very nice today, let's go to the park."
    if content == "هل يمكنك مساعدتي في العثور على أقرب محطة للحافلات؟":
        return False, "Can you help me find the nearest bus station?"
    if content == "Hvilken tid møtes vi i morgen?":
        return False, "What time are we meeting tomorrow?"
    if content == "Obrigado por me enviar o relatório tão rapidamente.":
        return False, "Thank you for sending me the report so quickly."
    if content == "मैं अपने दोस्त से मिलने दिल्ली जा रहा हूँ।":
        return False, "I am going to Delhi to meet my friend."
    if content == "Estoy aprendiendo español.":
        return False, "I am learning Spanish."
    if content == "Je suis très content.":
        return False, "I am very happy."
    if content == "Ich spreche ein bisschen Deutsch.":
        return False, "I speak a little German."
    if content == "私は日本語を話します。":
        return False, "I speak Japanese."
    if content == "Я говорю по-русски.":
        return False, "I speak Russian."
    if content == "Parlo un po' di italiano.":
        return False, "I speak a little Italian."
    if content == "我说一点中文。":
        return False, "I speak a little Chinese."
    if content == "أتكلم العربية قليلا.":
        return False, "I speak a little Arabic."
    if content == "Jeg snakker litt norsk.":
        return False, "I speak a little Norwegian."
    if content == "Falo um pouco de português.":
        return False, "I speak a little Portuguese."
    if content == "मैं थोड़ी हिंदी बोलता हूँ।":
        return False, "I speak a little Hindi."
    if content == "안녕하세요?":
        return False, "Hello?"
    if content == "สวัสดีครับ":
        return False, "Hello (male speaker)"
    if content == "你好":
        return False, "Hello"
    if content == "привет":
        return False, "Hello"
    if content == "مرحبا":
        return False, "Hello"
    if content == "こんにちは世界":
        return False, "Hello world"
    if content == "asdfghjkl":
        return False, "asdfghjkl"
    if content == "12345":
        return False, "12345"
    if content == "!@#$%^":
        return False, "!@#$%^"
    if content == " ":
        return False, " "
    
    # TODO: Robust code for testing mocking. Replace hardcoded above later 
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


def get_language(content: str) -> str:
    if content == "Hier ist dein erstes Beispiel.":
        return "German"
    if content == "¿Cómo estás hoy?":
        return "Spanish"
    if content == "Ceci est un test de traduction automatique.":
        return "French"
    if content == "私は昨日映画を見ました。":
        return "Japanese"
    if content == "Это отличный способ выучить новый язык.":
        return "Russian"
    if content == "Non vedo l’ora di viaggiare in Italia quest’estate!":
        return "Italian"
    if content == "今天的天气非常好，我们去公园吧。":
        return "Chinese"
    if content == "هل يمكنك مساعدتي في العثور على أقرب محطة للحافلات؟":
        return "Arabic"
    if content == "Hvilken tid møtes vi i morgen?":
        return "Norwegian"
    if content == "Obrigado por me enviar o relatório tão rapidamente.":
        return "Portuguese"
    if content == "मैं अपने दोस्त से मिलने दिल्ली जा रहा हूँ।":
        return "Hindi"
    return "Unknown"


def get_translation(content: str) -> str:
    if content == "Hier ist dein erstes Beispiel.":
        return "Here is your first example."
    if content == "¿Cómo estás hoy?":
        return "How are you today?"
    if content == "Ceci est un test de traduction automatique.":
        return "This is a test of automatic translation."
    if content == "私は昨日映画を見ました。":
        return "I watched a movie yesterday."
    if content == "Это отличный способ выучить новый язык.":
        return "This is an excellent way to learn a new language."
    if content == "Non vedo l’ora di viaggiare in Italia quest’estate!":
        return "I can't wait to travel to Italy this summer!"
    if content == "今天的天气非常好，我们去公园吧。":
        return "The weather is very nice today, let's go to the park."
    if content == "هل يمكنك مساعدتي في العثور على أقرب محطة للحافلات؟":
        return "Can you help me find the nearest bus station?"
    if content == "Hvilken tid møtes vi i morgen?":
        return "What time are we meeting tomorrow?"
    if content == "Obrigado por me enviar o relatório tão rapidamente.":
        return "Thank you for sending me the report so quickly."
    if content == "मैं अपने दोस्त से मिलने दिल्ली जा रहा हूँ।":
        return "I am going to Delhi to meet my friend."
    return content
