from src.translator import get_language, get_translation, translate_content
import pytest
from sentence_transformers import SentenceTransformer

from test.unit.utils import eval_single_response_classification, eval_single_response_complete, eval_single_response_translation, evaluate

COMBINED_SCORE_THRESHOLD = 0.56
CLASSIFICATION_SCORE_THRESHOLD = 0.75
TRANSLATION_SCORE_THRESHOLD = 0.7

@pytest.fixture(scope="session")
def sentence_model():
    return SentenceTransformer("all-MiniLM-L6-v2")


def test_classification_eval_set():
    assert evaluate(get_language, lambda expected, response: eval_single_response_classification(expected, response), CLASSIFICATION_EVAL_SET) > CLASSIFICATION_SCORE_THRESHOLD

def test_translation_eval_set(sentence_model):
    assert evaluate(get_translation, lambda expected, response: eval_single_response_translation(expected, response, sentence_model), TRANSLATION_EVAL_SET) > TRANSLATION_SCORE_THRESHOLD
    
def test_complete_eval_set(sentence_model):
    assert evaluate(translate_content, lambda expected, response: eval_single_response_complete(expected, response, sentence_model), COMPLETE_EVAL_SET) > COMBINED_SCORE_THRESHOLD


CLASSIFICATION_EVAL_SET = [
    {
        "post": "Hier ist dein erstes Beispiel.",
        "expected_answer": "German"
    },
    {
        "post": "¿Cómo estás hoy?",
        "expected_answer": "Spanish"
    },
    {
        "post": "Ceci est un test de traduction automatique.",
        "expected_answer": "French"
    },
    {
        "post": "私は昨日映画を見ました。",
        "expected_answer": "Japanese"
    },
    {
        "post": "Это отличный способ выучить новый язык.",
        "expected_answer": "Russian"
    },
    {
        "post": "Non vedo l’ora di viaggiare in Italia quest’estate!",
        "expected_answer": "Italian"
    },
    {
        "post": "今天的天气非常好，我们去公园吧。",
        "expected_answer": "Chinese"
    },
    {
        "post": "هل يمكنك مساعدتي في العثور على أقرب محطة للحافلات؟",
        "expected_answer": "Arabic"
    },
    {
        "post": "Hvilken tid møtes vi i morgen?",
        "expected_answer": "Norwegian"
    },
    {
        "post": "Obrigado por me enviar o relatório tão rapidamente.",
        "expected_answer": "Portuguese"
    },
    {
        "post": "मैं अपने दोस्त से मिलने दिल्ली जा रहा हूँ।",
        "expected_answer": "Hindi"
    }
]

TRANSLATION_EVAL_SET = [
    {
        "post": "Hier ist dein erstes Beispiel.",
        "expected_answer": "Here is your first example."
    },
    {
        "post": "¿Cómo estás hoy?",
        "expected_answer": "How are you today?"
    },
    {
        "post": "Ceci est un test de traduction automatique.",
        "expected_answer": "This is a test of automatic translation."
    },
    {
        "post": "私は昨日映画を見ました。",
        "expected_answer": "I watched a movie yesterday."
    },
    {
        "post": "Это отличный способ выучить новый язык.",
        "expected_answer": "This is an excellent way to learn a new language."
    },
    {
        "post": "Non vedo l’ora di viaggiare in Italia quest’estate!",
        "expected_answer": "I can't wait to travel to Italy this summer!"
    },
    {
        "post": "今天的天气非常好，我们去公园吧。",
        "expected_answer": "The weather is very nice today, let's go to the park."
    },
    {
        "post": "هل يمكنك مساعدتي في العثور على أقرب محطة للحافلات؟",
        "expected_answer": "Can you help me find the nearest bus station?"
    },
    {
        "post": "Hvilken tid møtes vi i morgen?",
        "expected_answer": "What time are we meeting tomorrow?"
    },
    {
        "post": "Obrigado por me enviar o relatório tão rapidamente.",
        "expected_answer": "Thank you for sending me the report so quickly."
    },
    {
        "post": "मैं अपने दोस्त से मिलने दिल्ली जा रहा हूँ।",
        "expected_answer": "I am going to Delhi to meet my friend."
    }
]

COMPLETE_EVAL_SET = [
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
        "post": "asdfghjkl",
        "expected_answer": (False, "asdfghjkl") #Unintelligible input
    },
    {
        "post": "ϗψξζηθωϻϱϵϕϑλκμπσςδl",
        "expected_answer": (False, "ϗψξζηθωϻϱϵϕϑλκμπσςδ") #Random Greek Letters
    },

    {
        "post": "12345",
        "expected_answer": (False, "12345") #Numbers
    },
    {
        "post": "!@#$%^",
        "expected_answer": (False, "!@#$%^") #Symbols
    },
    {
        "post": " ",
        "expected_answer": (False, " ") #Whitespace
    },
    {
        "post": "",
        "expected_answer": (False, "") #Empty String
    },
    {
        "post": "\n",
        "expected_answer": (False, "\n") #Newline
    },
    {
        "post": "こんにちは世界",
        "expected_answer": (False, "Hello world")
    }
]
