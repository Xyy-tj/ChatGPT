from flask import Flask, request, render_template, redirect
from gevent import pywsgi
import openai
import logging

app = Flask(__name__)
openai.api_key = "openAi API key"


@app.route('/')
def hello_world():
    return 'Hello World!'


def init_logger():
    fmt = "%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s"
    logging.basicConfig(
        level=logging.INFO,
        format=fmt,
        filename="logs.txt",
        filemode="w",
        datefmt="%a, %d %b %Y %H:%M:%S"
    )


def get_completion(question):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"{question}\n",
            temperature=0.3,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=None
        )
    except Exception as e:

        print(e)
        return e
    return response["choices"][0].text


@app.route('/chat', methods=['GET', 'POST'])
def get_request_json():
    if request.method == 'POST':
        if len(request.form['question']) < 1:
            return render_template(
                'chat.html', question="null", res="问题不能为空")
        question = request.form['question']
        print("======================================")
        print("接到请求:", question)
        res = get_completion(question)
        print("问题：", question)
        print("答案：", res)
        logging.info("问题：{}\n答案：{}".format(str(question), str(res).strip()))
        return render_template('chat.html', question=question, res=str(res))
    return render_template('chat.html', question=0)


if __name__ == '__main__':
    init_logger()
    logging.info("Its a info logger")
    server = pywsgi.WSGIServer(('0.0.0.0', 8081), app)
    server.serve_forever()
