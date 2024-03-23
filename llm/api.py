from zhipuai import ZhipuAI
from http import HTTPStatus
import dashscope
import openai
from llm.api_config import *


def get_glm4_response(prompt):
    client = ZhipuAI(api_key=glm4_api_key)
    try:
        response = client.chat.completions.create(
            model=glm4_model_name,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return str(e)


def get_gpt3_response(prompt):
    openai.api_base = base_url
    openai.api_key = gpt3_api_key
    try:
        response = openai.ChatCompletion.create(
            model=gpt3_model_name,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        return str(e)


def get_gpt4_response(prompt):
    openai.api_base = base_url
    openai.api_key = gpt4_api_key
    try:
        response = openai.ChatCompletion.create(
            model=gpt4_model_name,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        return str(e)



def get_qwen_response(prompt):
    dashscope.api_key = qwen_api_key
    response = dashscope.Generation.call(
        dashscope.Generation.Models.qwen_max,
        messages=[
            {"role": "user", "content": prompt}
        ],
        result_format='message',
    )
    if response.status_code != HTTPStatus.OK:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))
    return response.output.choices[0].message.content



def get_claude3_response(prompt):
    openai.api_base = base_url
    openai.api_key = claude3_api_key
    try:
        response = openai.ChatCompletion.create(
            model=claude3_model_name,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        return str(e)


model_list = {
    "glm4": get_glm4_response,
    "gpt3": get_gpt3_response,
    "gpt4": get_gpt4_response,
    "qwen": get_qwen_response,
    "claude3": get_claude3_response
}


def generate(name, prompt):
    return model_list[name](prompt)

