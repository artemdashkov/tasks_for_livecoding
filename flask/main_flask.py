from flask import Flask, Response, render_template
import time

app = Flask(__name__)

def generate_data():
    for i in range(10):
        yield f"data: {i}\n\n"  # Отправляем данные в формате Server-Sent Events (SSE)
        time.sleep(1)  # Симуляция долгого процесса

@app.route('/stream')
def stream():
    return Response(generate_data(), mimetype='text/event-stream')

@app.route('/')
def index():
    return render_template('index.html')  # Страница с HTML-шаблоном

if __name__ == '__main__':
    app.run(debug=True)