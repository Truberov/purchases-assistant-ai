from fastapi import APIRouter, Depends, HTTPException, Request, Path, Body
from pydantic import UUID4
from starlette import status

from assistant.schemas import QuestionCreateRequest, QuestionAnswer
from assistant.utils.qa import get_retrival_qa

api_router = APIRouter(tags=["QA"])


@api_router.post(
    "/",
    response_model=QuestionAnswer,
    status_code=status.HTTP_200_OK,
)
async def ask(
    _: Request,
    question: QuestionCreateRequest = Body(...),
    retrival=Depends(get_retrival_qa)
):
    result = await retrival.ainvoke(question.question)
    answer = result.get("result")
    context = [doc.page_content for doc in result.get("source_documents")]
    return QuestionAnswer(answer=answer, context=context)
