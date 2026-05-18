import psutil
import time
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Variabel Penyimpanan Counter (Disimpan di Memory/RAM)
click_count = 0
start_time = time.time()

@app.route('/')
def home():
    return render_template('index.html', count=click_count)

@app.route('/add', methods=['POST'])
def add_click():
    global click_count
    click_count += 1
    return jsonify({'count': click_count})

@app.route('/stats')
def stats():
    # Mengambil data system monitoring secara real-time
    cpu = psutil.cpu_percent(interval=0.1)
    ram = psutil.virtual_memory().percent
    uptime = int(time.time() - start_time)
    
    return jsonify({
        'cpu': cpu,
        'ram': ram,
        'uptime': uptime
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)