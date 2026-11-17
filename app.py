from flask import Flask, request
from flask import render_template
app = Flask(__name__)
import mssql_python

@app.route("/seap")
def Inicio():
    return render_template("index.html")

@app.route("/inicioS1")
def inicioS1():
    return render_template("bienvenido.html")

#---------------Grupos
@app.route("/seap/agregarGrupo")
def agregarGrupo():
    return render_template("Grupo/agregarGrupo.html")

@app.route("/seap/gestionGrupos")
def gestionGrupos():
    return render_template("Grupo/gestionGrupos.html")

#---------------Profesor
@app.route("/seap/agregarProfesor")
def agregarProfesor():
    return render_template("Profesor/agregarProfesor.html")

@app.route("/seap/gestionProfesores")
def gestionProfesores():
    return render_template("Profesor/gestionProfesores.html")

#---------------Materia
@app.route("/seap/agregarMateria")
def agregarMateria():
    return render_template("Materia/agregarMateria.html")

@app.route("/seap/gestionMaterias")
def gestionMaterias():
    return render_template("Materia/gestionMaterias.html")

#---------------Asignacion
@app.route("/seap/agregarAsignacion")
def agregarAsignacion():
    return render_template("Asignacion/agregarAsignacion.html")

#---------------Pregunta
@app.route("/seap/agregarPregunta")
def agregarPregunta():
    return render_template("Pregunta/agregarPregunta.html")

@app.route("/seap/gestionPreguntas")
def gestionPreguntas():
    return render_template("Pregunta/gestionPreguntas.html")

#---------------Sesion
@app.route("/seap/agregarSesion")
def agregarSesion():
    return render_template("Sesion/agregarSesion.html")

#---------------Reporte
@app.route("/seap/generarReporte")
def generarReporte():
    return render_template("Reporte/generarReporte.html")

#---------------Encuesta
@app.route("/encuesta")
def encuesta():
    return render_template("Encuesta/acceso.html")

@app.route("/responderEncuesta")
def responderEncuesta():
    return render_template("Encuesta/encuesta.html")