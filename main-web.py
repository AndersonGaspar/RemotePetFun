from flask import Flask
from flask import render_template
from flask import request
from controle import posicao_inicial, move_cima, move_direita, move_esquerda, move_baixo, auto

app = Flask(__name__)

@app.before_first_request
def _run_on_start():
    posicao_inicial()

@app.route('/',methods=['GET'])
def form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def submit():
    comando=request.form['comando']
    if(comando == 'w'):
        move_cima()
    if(comando == 's'):
        move_baixo()
    if(comando == 'a'):
        move_esquerda()
    if(comando == 'd'):
        move_direita()
    if(comando == 'g'):
        print('\n Modo automatico')
        posicao_inicial()
        auto()
    if(comando == 'h'):
        print('\n Posicao inicial')
        posicao_inicial()
    return ('',204) 

#export FLASK_DEBUG=1
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5001') 
