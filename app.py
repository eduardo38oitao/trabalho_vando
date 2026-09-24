from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

perguntas = [
    {
        "id": 1,
        "titulo": "Como resolver uma equação de segundo grau?",
        "materia": "Matemática",
        "autor": "Lucas",
        "respostas": 3
    },
    {
        "id": 2,
        "titulo": "Qual a diferença entre mitose e meiose?",
        "materia": "Biologia",
        "autor": "Ana",
        "respostas": 5
    },
    {
        "id": 3,
        "titulo": "Como funciona a Revolução Industrial?",
        "materia": "História",
        "autor": "Pedro",
        "respostas": 2
    }
]

materiais = [
    {
        "titulo": "Resumo de Matemática",
        "materia": "Matemática",
        "autor": "Mariana",
        "descricao": "Resumo com fórmulas importantes para provas."
    },
    {
        "titulo": "Revisão de Biologia",
        "materia": "Biologia",
        "autor": "João",
        "descricao": "Material para revisar células e genética."
    },
    {
        "titulo": "História do Brasil",
        "materia": "História",
        "autor": "Gabriel",
        "descricao": "Resumo dos principais acontecimentos históricos."
    }
]

ranking = [
    {"nome": "Mariana", "pontos": 950},
    {"nome": "Lucas", "pontos": 820},
    {"nome": "Ana", "pontos": 760},
    {"nome": "Pedro", "pontos": 690},
    {"nome": "Gabriel", "pontos": 610}
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        perguntas=perguntas[:3],
        materiais=materiais[:3]
    )


@app.route("/perguntas")
def listar_perguntas():
    busca = request.args.get("busca", "").lower()
    
    if busca:
        resultado = [
            p for p in perguntas
            if busca in p["titulo"].lower()
            or busca in p["materia"].lower()
        ]
    else:
        resultado = perguntas

    return render_template(
        "perguntas.html",
        perguntas=resultado
    )


@app.route("/nova-pergunta", methods=["GET", "POST"])
def nova_pergunta():
    if request.method == "POST":
        titulo = request.form.get("titulo")
        materia = request.form.get("materia")
        autor = request.form.get("autor")

        if titulo and materia and autor:
            nova = {
                "id": len(perguntas) + 1,
                "titulo": titulo,
                "materia": materia,
                "autor": autor,
                "respostas": 0
            }

            perguntas.append(nova)

        return redirect(url_for("listar_perguntas"))

    return render_template("nova_pergunta.html")


@app.route("/materiais")
def listar_materiais():
    return render_template(
        "materiais.html",
        materiais=materiais
    )


@app.route("/ranking")
def listar_ranking():
    return render_template(
        "ranking.html",
        ranking=ranking
    )


if __name__ == "__main__":
    app.run(debug=True)
