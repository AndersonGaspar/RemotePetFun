from flask import Flask
from flask import render_template
from flask import request
from threading import Thread

app = Flask(__name__)

@app.before_first_request
def _run_on_start():
    setup_motor()
    t = Thread(target=roda_medicao)
    t.start()

@app.route('/',methods=['GET'])
def form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def submit():
    comando=request.form['comando']
    if(comando == 'w'):
        move_frente()
    if(comando == 's'):
        move_tras()
    if(comando == 'a'):
        move_esquerda()
    if(comando == 'd'):
        move_direita()
    if(comando == 'q'):
        move_parar()
    return ('',204) 


#export FLASK_DEBUG=1
if __name__ == "__main__":
    app.run(host='0.0.0.0') 