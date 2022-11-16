import time
import os
from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI, File, UploadFile
from happytransformer import HappyGeneration
from happytransformer import GENSettings 
from happytransformer import GENTrainArgs

app = FastAPI(root_path="/")

# AI Model
generator = HappyGeneration("GPT-NEO", "EleutherAI/gpt-neo-125M")
args = GENSettings(no_repeat_ngram_size=2)


# self configure the result
class Input_GPT_Neo_1_3B(BaseModel):
    prompt: str
    #max_length: int
    #do_sample: bool
    #temperature: float


class Output(BaseModel):
    output: str
    #status: str
    #error_message: str
    loading_time_seconds: float


os_root_path = os.environ.get('ROOT_PATH')
print(os_root_path)



# get the requests for the AI to respond
@app.post("/input")
async def input_text(input: Input_GPT_Neo_1_3B):
    start_time = time.time()
    print("Loading ...")
    result = generator.generate_text(str(input.prompt), args=args)
    return Output(output=result.text, loading_time_seconds=(time.time() - start_time))


@app.post('/read_txt_file')
async def upload_file_and_read(file: UploadFile = File(...),):

    print("Loading ...")

    if file.content_type.startswith("text"):
        text_binary = await readTxt(file)
        response = text_binary.decode()
    else:
        response = file.filename

    f = open("train.txt", "w")
    f.write(response)
    f.close()

    args = GENTrainArgs(num_train_epochs=10)
    generator.train("train.txt", args=args)

    return response


def readTxt(file):
    return file.read()

@app.get("/")
async def root():
    return {"message": "Please go to /docs to work with our AI ..."}


uvicorn.run(app, host="0.0.0.0", port=8080)
