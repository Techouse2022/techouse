from flask import Flask, render_template, request
import mysql.connector
from flask_mail import Mail, Message


conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='techousebr',
)

cursor = conexao.cursor()

app = Flask(__name__, static_folder='static')
app.config['MAIL_SERVER'] = 'smtp.office365.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'guiaraujo2007@outlook.com'
app.config['MAIL_PASSWORD'] = 'gui28141528'
mail = Mail(app)




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact_send.php', methods=['POST'])
def processar_formulario():
    nome = request.form.get('nome')
    email = request.form.get('email')
    mensagem = request.form.get('message')

    # Faça o processamento dos dados, se necessário
    # print(nome, email, mensagem)
    # Exemplo: exibir os dados recebidos

    # Envio de dados para o banco de dados
    comando = f'INSERT INTO registros (nome, email) VALUES ("{nome}", "{email}")'
    cursor.execute(comando)
    conexao.commit()


    #Envio
    msg = Message('Assunto do E-mail', sender='guiaraujo2007@outlook.com', recipients=['contato.techouse.br@gmail.com'])
    msg.body = f"Nome: {nome}\nEmail: {email}\nMensagem: {mensagem}"

    with app.app_context():
        mail.send(msg)

    return render_template('index.html')

@app.route('/contato_form')
def contato_form():
    nome = request.form.get('nome')
    email = request.form.get('email')
    mensagem = request.form.get('message')

    # Envio
    msg = Message('Assunto do E-mail', sender='guiaraujo2007@outlook.com', recipients=['contato.techouse.br@gmail.com'])
    msg.body = f"Nome: {nome}\nEmail: {email}\nMensagem: {mensagem}"

    with app.app_context():
        mail.send(msg)

    return render_template('contato.html')
    



@app.route('/outro_index')
def outro_index():
    return render_template('servicos.html')


@app.route('/conexao_page', methods=['GET'])
def conexao_page():
    return render_template('loginpage.html') 

@app.route('/conexao_page', methods=['POST'])
def login_index():
    # Puxa os dados escritos
    user = request.form.get('nome')
    senha = request.form.get('password')

    # Variaveis de senha
    user1 = "teste4321"
    senha1 = "senha4321"

    # Função de conexão
    if user == user1 and senha == senha1:
        return render_template('perfil1/perfil.html')
    else:
        return render_template('loginpageerror.html')
    


@app.route('/conexao_plataform_crud', methods=['GET', 'POST'])
def conexao_plataform_crud():
    if request.method == 'POST':
        # Puxa os dados escritos
        user = request.form.get('nome')
        senha = request.form.get('password')

        # Variaveis de senha
        user1 = "teste4321"
        senha1 = "senha4321"

        # Função de conexão
        if user == user1 and senha == senha1:
            return render_template('perfil1/login-perfil.html')
        else:
            return render_template('perfil1/login-perfil-error.html')
    else:
        return render_template('perfil1/login-perfil.html')


@app.route('/about_nos')
def about_us():
    return render_template('aboutus.html')

if __name__ == '__main__':
    app.run()