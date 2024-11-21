import json
import jsbeautifier
from langchain.schema import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from src.jobs.config import job_config
from src.jobs.prompts import fn_job_analysis, system_prompt_job


def output2json(output):
    opts = jsbeautifier.default_options()
    return json.loads(jsbeautifier.beautify(output["function_call"]["arguments"], opts))


def analyse_job(job_data):

    llm = ChatOpenAI(model=job_config.MODEL_NAME, temperature=0.5)
    completion = llm.predict_messages(
        [
            SystemMessage(content=system_prompt_job),
            HumanMessage(content=job_data.job_description),
        ],
        functions=fn_job_analysis,
    )
    output_analysis = completion.additional_kwargs

    json_output = output2json(output=output_analysis)

    return json_output