from flask import Flask, request
import time

app = Flask(__name__)

@app.route('/')
def get_user_ip():
    # Lấy IP thực từ Cloudflare hoặc fallback về request.remote_addr
    user_ip = request.headers.get('CF-Connecting-IP', request.remote_addr)
    # save ip and time 
    with open('log.txt', 'a') as f:
        f.write(f'IP: {user_ip} - {time.ctime()}')
    print(user_ip)
    return f'Địa chỉ IP của bạn là: {user_ip}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
