from flask import Flask
servidor3 = Flask(__name__)
@servidor3.route('/')
def hola():
    return"Hola desde el servidor3!!"
if __name__=='__main__':
    servidor3.run(host='0.0.0.0')
