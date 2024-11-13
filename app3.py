from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Usuários e lista de artigos (apenas para simulação; em produção, usaria um banco de dados)
usuarios = {'usuario@example.com': {'senha': '12345'}}
artigos = []

@app.route('/')
def index():
    if 'user' in session:
        return render_template('index.html', usuario=session['user'], artigos=artigos)
    return redirect(url_for('login'))



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        
        # Verificar se o usuário existe e se a senha está correta
        if email in usuarios and usuarios[email]['senha'] == senha:
            session['user'] = email
            return redirect(url_for('index'))
        else:
            return "Credenciais inválidas. Tente novamente."
    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        
        # Adiciona o novo usuário (não há verificação de duplicidade neste exemplo)
        usuarios[email] = {'senha': senha}
        return redirect(url_for('login'))
    return render_template('cadastro.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))






@app.route('/adicionar_artigo', methods=['GET', 'POST'])
def adicionar_artigo():
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        titulo = request.form['titulo']
        conteudo = request.form['conteudo']
        autor = session['user']

        # Adiciona o artigo à lista (pode ser modificado para salvar em um banco de dados)
        artigos.append({'titulo': titulo, 'conteudo': conteudo, 'autor': autor})
        return redirect(url_for('index'))

    return render_template('adicionar_artigo.html')






#teste
@app.route('/editar_artigo/<int:artigo_id>', methods=['GET', 'POST'])
def editar_artigo(artigo_id):
    artigo = artigos.get(artigo_id)
    if not artigo:
        return "Artigo não encontrado.", 404
    if request.method == 'POST':
        artigo['titulo'] = request.form['titulo']
        artigo['conteudo'] = request.form['conteudo']
        return redirect(url_for('index'))
    return render_template('editar_artigo.html', artigo=artigo, artigo_id=artigo_id)

if __name__ == '__main__':
    app.run(debug=True)
