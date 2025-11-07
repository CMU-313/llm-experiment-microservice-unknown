from src.translator import translate_content


def test_chinese():
    is_english, translated_content = translate_content("这是一条中文消息")
    assert is_english == False
    assert translated_content == "This is a Chinese message"


def test_llm_english_response():
    _check_test_case_list(english_to_english_examples)

def test_llm_non_english_response():
    _check_test_case_list(non_english_to_english_examples)

def test_llm_gibberish_response():
    _check_test_case_list(gibberish_examples)


def _check_test_case_list(test_cases):
    for test in test_cases:
        post = test["post"]
        expected_answer = test["expected_answer"]
        is_english, translated_content = translate_content(post)
        assert is_english == expected_answer[0], f"Expected {expected_answer[0]} for input '{post}', but got {is_english}"
        assert translated_content == expected_answer[1], f"Expected '{expected_answer[1]}' for input '{post}', but got {translated_content}"


english_to_english_examples = [
    {
        "post": "I will talk to you later after the conference call.",
        "expected_answer": (True, "I will talk to you later after the conference call.")
    },
    {
        "post": "The cat in the hat knows a lot about that",
        "expected_answer": (True, "The cat in the hat knows a lot about that")
    },
    {
        "post": "Hello, how are you?",
        "expected_answer": (True, "Hello, how are you?")
    },
    {
        "post": "This is a simple sentence.",
        "expected_answer": (True, "This is a simple sentence.")
    },
    {
        "post": "I like to read books.",
        "expected_answer": (True, "I like to read books.")
    },
    {
        "post": "What is your name?",
        "expected_answer": (True, "What is your name?")
    },
    {
        "post": "Where do you live?",
        "expected_answer": (True, "Where do you live?")
    },
    {
        "post": "Tell me a joke.",
        "expected_answer": (True, "Tell me a joke.")
    },
    {
        "post": "Thank you for your help.",
        "expected_answer": (True, "Thank you for your help.")
    },
    {
        "post": "Have a good day.",
        "expected_answer": (True, "Have a good day.")
    },
    {
        "post": "See you later.",
        "expected_answer": (True, "See you later.")
    },
    {
        "post": "That's a great idea!",
        "expected_answer": (True, "That's a great idea!")
    },
    {
        "post": "I am very happy today.",
        "expected_answer": (True, "I am very happy today.")
    },
    {
        "post": "The sun is shining.",
        "expected_answer": (True, "The sun is shining.")
    },
    {
        "post": "It is raining outside.",
        "expected_answer": (True, "It is raining outside.")
    },
    {
        "post": "I am learning to code.",
        "expected_answer": (True, "I am learning to code.")
    },
    {
        "post": "This is a beautiful day.",
        "expected_answer": (True, "This is a beautiful day.")
    },
    {
        "post": "What time is it?",
        "expected_answer": (True, "What time is it?")
    }
]

non_english_to_english_examples = [
    {
        "post": "Hier ist dein erstes Beispiel.",
        "expected_answer": (False, "This is your first example.")
    },
    {
        "post": "¿Cómo estás hoy?",
        "expected_answer": (False, "How are you today?")
    },
    {
        "post": "Ceci est un test de traduction automatique.",
        "expected_answer": (False,"This is a test of automatic translation.")
    },
    {
        "post": "私は昨日映画を見ました。",
        "expected_answer": (False,"I watched a movie yesterday.")
    },
    {
        "post": "Это отличный способ выучить новый язык.",
        "expected_answer": (False,"This is an excellent way to learn a new language.")
    },
    {
        "post": "Non vedo l’ora di viaggiare in Italia quest’estate!",
        "expected_answer": (False,"I can't wait to travel to Italy this summer!")
    },
    {
        "post": "今天的天气非常好，我们去公园吧。",
        "expected_answer": (False,"The weather is very nice today, let's go to the park.")
    },
    {
        "post": "هل يمكنك مساعدتي في العثور على أقرب محطة للحافلات؟",
        "expected_answer": (False,"Can you help me find the nearest bus station?")
    },
    {
        "post": "Hvilken tid møtes vi i morgen?",
        "expected_answer": (False,"What time are we meeting tomorrow?")
    },
    {
        "post": "Obrigado por me enviar o relatório tão rapidamente.",
        "expected_answer": (False,"Thank you for sending me the report so quickly.")
    },
    {
        "post": "मैं अपने दोस्त से मिलने दिल्ली जा रहा हूँ।",
        "expected_answer": (False,"I am going to Delhi to meet my friend.")
    },
    {
        "post": "Estoy aprendiendo español.",
        "expected_answer": (False, "I am learning Spanish.")
    },
    {
        "post": "Je suis très content.",
        "expected_answer": (False, "I am very happy.")
    },
    {
        "post": "Ich spreche ein bisschen Deutsch.",
        "expected_answer": (False, "I speak a little German.")
    },
    {
        "post": "私は日本語を話します。",
        "expected_answer": (False, "I speak Japanese.")
    },
    {
        "post": "Я говорю по-русски.",
        "expected_answer": (False, "I speak Russian.")
    },
    {
        "post": "Parlo un po' di italiano.",
        "expected_answer": (False, "I speak a little Italian.")
    },
    {
        "post": "我说一点中文。",
        "expected_answer": (False, "I speak a little Chinese.")
    },
    {
        "post": "أتكلم العربية قليلا.",
        "expected_answer": (False, "I speak a little Arabic.")
    },
    {
        "post": "Jeg snakker litt norsk.",
        "expected_answer": (False, "I speak a little Norwegian.")
    },
    {
        "post": "Falo um pouco de português.",
        "expected_answer": (False, "I speak a little Portuguese.")
    },
    {
        "post": "मैं थोड़ी हिंदी बोलता हूँ।",
        "expected_answer": (False, "I speak a little Hindi.")
    },
     {
        "post": "안녕하세요?",
        "expected_answer": (False, "Hello?")
    },
    {
        "post": "สวัสดีครับ",
        "expected_answer": (False, "Hello (male speaker)")
    },
    {
        "post": "你好",
        "expected_answer": (False, "Hello")
    },
    {
        "post": "привет",
        "expected_answer": (False, "Hello")
    },
    {
        "post": "مرحبا",
        "expected_answer": (False, "Hello")
    },
    {
        "post": "こんにちは世界",
        "expected_answer": (False, "Hello world")
    }
]

gibberish_examples = [
    {
        "post": "asdfghjkl",
        "expected_answer": (False, "asdfghjkl") # Unintelligible input will likely not be translated meaningfully
    },
    {
        "post": "12345",
        "expected_answer": (False, "12345") # Numbers likely won't be translated
    },
    {
        "post": "!@#$%^",
        "expected_answer": (False, "!@#$%^") # Symbols won't be translated
    },
    {
        "post": " ",
        "expected_answer": (False, " ") # Empty or whitespace-only strings won't be translated
    }
]
