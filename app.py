from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dados fictícios para a página "Sobre Raças"
racas = {
    "buldog": {
        "nome": "Bulldog",
        "descricao": "O Bulldog é conhecido por sua aparência distinta, com um corpo muscular e enrugado, e um rosto achatado. Eles são carinhosos e leais.",
        "imagem": "bulldog_raças.jpg"
    },
    "golden": {
        "nome": "Golden Retriever",
        "descricao": "Os Golden Retrievers são conhecidos por sua natureza amigável e leal. Eles são ótimos com crianças e se destacam como cães de família.",
        "imagem": "golden_raças.jpg"
    },
    "vira_lata": {
        "nome": "Vira Lata",
        "descricao": "O Vira Lata é conhecido por sua adaptabilidade e resistência. Eles são bastante variados em aparência e são cães amigáveis.",
        "imagem": "oreo_home.jpg.jpeg"
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/appointment', methods=['GET', 'POST'])
def appointment():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        data = request.form['data']
        hora = request.form['hora']
        mensagem = request.form['mensagem']
        # Aqui você pode adicionar código para armazenar esses dados no banco de dados ou enviar um e-mail
        return redirect(url_for('home'))
    return render_template('appointment.html')

@app.route('/about')
def about():
    return render_template('about.html', racas=racas)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        mensagem = request.form['mensagem']
        # Aqui você pode adicionar código para armazenar esses dados no banco de dados ou enviar um e-mail
        return redirect(url_for('home'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
