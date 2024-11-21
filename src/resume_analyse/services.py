import os
import json
import jsbeautifier
from langchain.schema import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import Docx2txtLoader, PyPDFLoader
from src.resume_analyse.config import resume_analyse_config
from src.resume_analyse.prompts import system_prompt_strength, fn_strength_analysis, system_prompt_weakness, fn_weakness_detection


def output2json(output):
    """GPT Output Object >>> json"""
    opts = jsbeautifier.default_options()
    return json.loads(jsbeautifier.beautify(output["function_call"]["arguments"], opts))


def generate_content(content, weakness):
    content = "\nContent:" + str(content) + "\Identified weakness:" + str(weakness)
    return content


async def save_cv_candidate(file):
    # Prepend the current datetime to the filename
    file_name = file.filename

    # Construct the full image path based on the settings
    image_path = resume_analyse_config.CV_UPLOAD_DIR + file_name

    # Read the contents of the uploaded file asynchronously
    contents = await file.read()

    # Write the uploaded contents to the specified image path
    with open(image_path, "wb") as f:
        f.write(contents)

    return file_name


def load_pdf_docx(file_path):
    # Determine the file type and choose the appropriate loader
    if os.path.basename(file_path).lower().endswith((".pdf", ".docx")):
        loader = (
            PyPDFLoader(file_path)
            if file_path.lower().endswith(".pdf")
            else Docx2txtLoader(file_path)
        )

    # Load and split the document using the selected loader
    documents = loader.load_and_split()

    return documents


def read_cv_candidate(file_name):
    file_path = resume_analyse_config.CV_UPLOAD_DIR + file_name

    documents = load_pdf_docx(file_path=file_path)
    content = ""
    for page in documents:
        content += page.page_content
    return content


def calculate_gpt_cost(input_tokens, output_tokens, cached_input_tokens=0, cached_output_tokens=0):
    input_cost_per_million = 2.50
    cached_input_cost_per_million = 1.25
    output_cost_per_million = 10.00
    cached_output_cost_per_million = 5.00

    input_cost = (input_tokens / 1_000_000) * input_cost_per_million
    cached_input_cost = (cached_input_tokens / 1_000_000) * cached_input_cost_per_million

    output_cost = (output_tokens / 1_000_000) * output_cost_per_million
    cached_output_cost = (cached_output_tokens / 1_000_000) * cached_output_cost_per_million

    total_cost = input_cost + cached_input_cost + output_cost + cached_output_cost

    return total_cost 


def analysing_strength(cv_content):
    llm = ChatOpenAI(model=resume_analyse_config.MODEL_NAME, temperature=0.5, openai_api_key=os.getenv("OPENAI_API_KEY_PRO"))

    input_tokens = len(cv_content.split()) 
    
    completion = llm.predict_messages(
        [
            SystemMessage(content=system_prompt_strength),
            HumanMessage(content=cv_content),
        ],
        functions=fn_strength_analysis,
    )

    output_analysis = completion.additional_kwargs

    # Assume output token count from the completion (rough estimate, depends on actual output)
    output_tokens = len(json.dumps(output_analysis).split())  # Estimation based on output length

    # Calculate and print the cost
    cost = calculate_gpt_cost(input_tokens, output_tokens)
    # print(f"Total GPT cost for this analysis: ${cost}")

    json_output = output2json(output=output_analysis)
    return json_output



        
        
def analysing_weakness(cv_content):
    llm = ChatOpenAI(model=resume_analyse_config.MODEL_NAME, temperature=0.5, openai_api_key=os.getenv("OPENAI_API_KEY_PRO"))
    completion = llm.predict_messages(
        [
            SystemMessage(content=system_prompt_weakness),
            HumanMessage(content=cv_content),
        ],
        functions=fn_weakness_detection,
    )

    output_analysis = completion.additional_kwargs
    json_output = output2json(output=output_analysis)

    return json_output