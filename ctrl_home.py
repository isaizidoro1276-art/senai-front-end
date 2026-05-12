"""
Esse arquivo é um exemplo de controller
"""

from flask import Blueprint, request, redirect, url_for, render_template, flash, session
from werkzeug.security import check_password_hash, generate_password_hash

from database import db
from models import User

bp = Blueprint(__name__, "HomeController")

@bp.route("/") # cria uma rota
def index(): # função que gerencia rota
    """ Página inicial"""
    if '_user_id' not in session:
        
        return redirect(url_for("auth.login"))

    return render_template("dashboard/index.html") # Renderiza um template


@bp.route("/dashboard")  # cria uma rota para navegador http://127.0.0.1:5000/dashboard
def dashboard(): # função que gerencia rota
    """ Painel de Vendas """
    # remova o login
    vendas: list =  [
         {"mes": "Janeiro", "valor total": 139519.19},
         {"mes": "Fevereiro", "valor total": 139129.19},
         {"mes": "Março", "valor total": 139519.89},
         {"mes": "Abril", "valor total": 789519.19},
         {"mes": "Maio", "valor total": 139519.32},
         {"mes": "Junho", "valor total": 975319.19},
         {"mes": "Julho", "valor total": 705519.19},
         {"mes": "Agosto", "valor total": 139539.19},
         {"mes": "Setembro", "valor total": 135019.19},
         {"mes": "Outubro", "valor total": 165519.19},
        {"mes": "Novembro", "valor total": 139009.19},
         {"mes": "Dezembro", "valor total": 132219.19},

    ] # fim da lista de vendas
    return render_template("dashboard/index.html", title="Painel de Vendas", vendas=vendas)  # Renderiza um template
    