from flask import Flask, request, render_template

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('indice.html')


@app.route('/ola')
@app.route('/ola/<nome>')
def ola_mundo(nome=None):
    if nome:
        print(nome)
        return render_template("ola.html", usuario=nome)
    return render_template("ola.html")


@app.route('/logar', methods=['POST'])
def logar():

    if request.method == 'POST':

        return "Recebeu post! Fazer login!"

    else:
        return "Recebeu get! Exibir FORM de login"


if __name__ == '__main__':
    app.run()
