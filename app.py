from core.api.nltk import NLTK
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
word = NLTK()

test = word.convert_text_infinitive(
	"In a quiet village, a curious cat named Whiskers discovered a hidden garden. There, he found a magical flower "
	"that granted him the ability to speak. Whiskers shared tales of adventure with the villagers, enchanting them "
	"with his stories. One day, he told a story so captivating that the village became a famous storytelling hub. "
	"Whiskers, now a legend, continued to inspire joy and wonder in the hearts of all who visited.")


@app.get("/")
def read_root():
	return {"message": "Welcome to FastAPI"}


@app.post("/items/")
def create_item(item: dict):
	return {"item": item}


class SentenceRequest(BaseModel):
	sentence: str


@app.post("/verbs/", response_model=None)
def extract_verbs(request: SentenceRequest):
	text = request.sentence
	result = word.convert_text_infinitive(text)
	return {"sentence": text, "result": result}
