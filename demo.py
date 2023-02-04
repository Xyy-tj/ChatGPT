import openai

openai.api_key = "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"


# openai.Model.list()


def completion_request(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.2,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )
    print(response['choices'][0]['text'])
    return response


def image_request(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.2,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )
    print(response['choices'][0]['text'])
    return response


if __name__ == '__main__':
    prompt = "你好\n\nA:"
    completion_request(prompt)
    image_request(prompt)
