from pydantic import BaseModel
from typing import List, Dict, Any
from enum import Enum

class QuestionType(str, Enum):
    MULTIPLE_CHOICE = "multiple_choice"
    TRUE_FALSE = "true_false"
    MATH = "math"

class Answer(BaseModel):
    id: str
    text: str
    correct: bool
    explanation: str

class Question(BaseModel):
    id: str
    type: QuestionType
    text: str
    answers: List[Answer]
    category: str

class QuestionResponse(BaseModel):
    category: str
    question: Question

class AnswerSubmission(BaseModel):
    question_id: str
    answer_id: str

class CategoryPerformance(BaseModel):
    correct: int
    incorrect: int

class TestSession(BaseModel):
    session_id: str
    category: str
    category_performance: Dict[str, CategoryPerformance]
    question_history: List[Dict[str, Any]]

class TestSummary(BaseModel):
    session_id: str
    total_questions: int
    correct_answers: int
    category_breakdown: Dict[str, CategoryPerformance]
    completion_time: float
    recommendations: List[str] 