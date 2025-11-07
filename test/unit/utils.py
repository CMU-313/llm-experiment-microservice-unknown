from sentence_transformers import SentenceTransformer
from typing import Callable, Any

def evaluate(query_fn: Callable[[Any], Any], eval_fn: Callable[[Any, Any], float], test_cases: list[dict[str, Any]]) -> float:
    '''
    Computes an aggregate score of the chosen evaluation metric across the given dataset. Calls the query_fn function to generate
    LLM outputs for each of the posts in the evaluation dataset, and calls eval_single_response to calculate the metric.
    '''
    total_score = 0
    for item in test_cases:
        llm_response = query_fn(item["post"])
        total_score += eval_fn(item["expected_answer"], llm_response)
    return (total_score/len(test_cases))

def eval_single_response_classification(expected_answer: str, llm_response: str) -> float:
    if expected_answer.lower()==llm_response.lower():
        return 1.0
    else:
        return 0.0

def eval_single_response_translation(expected_answer: str, llm_response: str, model: SentenceTransformer) -> float:
    '''Compares an LLM response to the expected answer from the evaluation dataset using one of the text comparison metrics.'''
    sentences=[expected_answer, llm_response]
    embeddings = model.encode(sentences)
    return float(model.similarity(embeddings[0],embeddings[1])[0][0])

def eval_single_response_complete(expected_answer: tuple[bool, str], llm_response: tuple[bool, str], model: SentenceTransformer) -> float:
    '''Compares an LLM response to the expected answer from the evaluation dataset using one of the text comparison metrics.'''
    is_english_score = 0.0
    if (expected_answer[0] == llm_response[0]):
        is_english_score=1.0
        
    eval_score_translation = eval_single_response_translation(expected_answer[1],llm_response[1], model)

    return is_english_score * eval_score_translation 
