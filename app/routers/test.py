from fastapi import APIRouter, HTTPException, Depends
from typing import Dict, Any

from app.schemas.test import (
    TestSession,
    QuestionResponse,
    AnswerSubmission,
    TestSummary
)
from app.services.test_session import TestSessionService

router = APIRouter()

@router.post("/start", response_model=TestSession)
async def start_test(category: str):
    """Start a new test session"""
    try:
        session = await TestSessionService.create_session(category)
        return session
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{session_id}/next", response_model=QuestionResponse)
async def get_next_question(session_id: str):
    """Get the next question for the test session"""
    try:
        question = await TestSessionService.get_next_question(session_id)
        return question
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/{session_id}/submit", response_model=Dict[str, Any])
async def submit_answer(
    session_id: str,
    submission: AnswerSubmission
):
    """Submit an answer for the current question"""
    try:
        result = await TestSessionService.submit_answer(
            session_id,
            submission.question_id,
            submission.answer_id
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/{session_id}/end", response_model=TestSummary)
async def end_test(session_id: str):
    """End the test session and get summary"""
    try:
        summary = await TestSessionService.end_session(session_id)
        return summary
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) 