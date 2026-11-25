from flask import Flask, request
from flask import render_template
app = Flask(__name__)
import mssql_python
from datetime import date, time
cadenaConexion=(
    "Server=localhost;"
    "Database=BD_Encuestas;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)
def get_conexion():
    return mssql_python.connect(cadenaConexion)

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
@app.route("/seap/guardarGrupo",methods=['POST'])
def guardarGrupo():
    cveGru=request.form.get('cveGru')
    numAlumnos=int(request.form.get('numAlu'))
    mensaje=""
    conexion=get_conexion()
    cursor=conexion.cursor()
    cursor.execute('Select * from Grupos where cveGru=?',(cveGru,))
    clave=cursor.fetchone()
    if(clave is None):
     cursor.execute("Insert into Grupos(cveGru,numAlumnos)values(?,?)",(cveGru,numAlumnos))
     conexion.commit()
     mensaje="Grupo agregado exitosamente"
     
    else:
        mensaje="Clave repetida intenta otra" 
    cursor.close()
    conexion.close()     
    return render_template('Grupo/agregarGrupo.html',mensaje=mensaje)       

    

@app.route("/seap/gestionGrupos")
def gestionGrupos():
    conexion=get_conexion()
    cursor=conexion.cursor()
    cursor.execute("Select * from Grupos")
    grupos=cursor.fetchall()
    cursor.close()
    conexion.close()
    return render_template("Grupo/gestionGrupos.html",grupos=grupos)

#---------------Profesor
@app.route("/seap/agregarProfesor")
def agregarProfesor():
    return render_template("Profesor/agregarProfesor.html")
@app.route("/seap/guardarPro",methods=['POST'])
def guardarPro():
    cvePro=request.form.get('clave')
    nomPro=request.form.get('nombre')
    apPaterno=request.form.get('apellidoPaterno')
    apMaterno=request.form.get('apellidoMaterno')
    correo=request.form.get('correo')
    mensaje=""
    conexion=get_conexion()
    cursor=conexion.cursor()
    cursor.execute("Select * from Profesor where cvePro=?",(cvePro,))
    clave=cursor.fetchone()
    if(clave is None):
        cursor.execute("Insert into Profesor(cvePro,nomPro,apPaterno,apMaterno,correo)values(?,?,?,?,?)",(cvePro,nomPro,apPaterno,apMaterno,correo))
        conexion.commit()
        mensaje="Profesor agregado correctamente"
    else:
        mensaje="Clave repetida intenta otra"
    cursor.close()
    conexion.close()     
    return render_template("Profesor/agregarProfesor.html",mensaje=mensaje)    


@app.route("/seap/gestionProfesores")
def gestionProfesores():
    conexion=get_conexion()
    cursor=conexion.cursor()
    cursor.execute("Select cvePro, CONCAT(nomPro, ' ', apPaterno, ' ', apMaterno) AS nombreCompleto, correo from Profesor")
    profesores=cursor.fetchall()
    cursor.close()
    conexion.close()
    return render_template("Profesor/gestionProfesores.html",profesores=profesores)

#---------------Materia
@app.route("/seap/agregarMateria")
def agregarMateria():
    return render_template("Materia/agregarMateria.html")
@app.route("/seap/guardarMat",methods=['POST'])
def guardarMat():
    nomMat=request.form.get('materia')
    conexion=get_conexion()
    cursor=conexion.cursor()
    cursor.execute("Insert into Materia(nomMat) values(?)",(nomMat,))
    conexion.commit()
    mensaje="Materia agregada correctamente"
    cursor.close()
    conexion.close()
    return render_template("Materia/agregarMateria.html",mensaje=mensaje)

@app.route("/seap/gestionMaterias")
def gestionMaterias():
    conexion=get_conexion()
    cursor=conexion.cursor()
    cursor.execute("Select * from Materia")
    materias=cursor.fetchall()
    cursor.close()
    conexion.close()
    return render_template("Materia/gestionMaterias.html",materias=materias)

#---------------Asignacion
@app.route("/seap/agregarAsignacion")
def agregarAsignacion():
    conexion=get_conexion()
    cursor=conexion.cursor()
    cursor.execute("Select cvePro, CONCAT(nomPro, ' ', apPaterno, ' ', apMaterno) AS nombreCompleto from Profesor")
    profesores=cursor.fetchall()
    cursor.execute("Select cveGru from Grupos")
    grupos=cursor.fetchall()
    cursor.execute("Select * from Materia")
    materias=cursor.fetchall()
    cursor.close()
    conexion.close()
    return render_template("Asignacion/agregarAsignacion.html",profesores=profesores,grupos=grupos,materias=materias)
@app.route("/seap/guardarAsig", methods=['POST'])
def guardarAsig():
    cvePro=request.form.get('profesor')
    cveGru=request.form.get('grupo')
    cveMat=request.form.get('materia')
    conexion=get_conexion()
    cursor=conexion.cursor()
    cursor.execute("Select cvePro, CONCAT(nomPro, ' ', apPaterno, ' ', apMaterno) AS nombreCompleto from Profesor")
    profesores=cursor.fetchall()
    cursor.execute("Select cveGru from Grupos")
    grupos=cursor.fetchall()
    cursor.execute("Select * from Materia")
    materias=cursor.fetchall()
    cursor.execute("Insert into Asigna(cveGru,cveMat,cvePro) values(?,?,?)",(cveGru,cveMat,cvePro,))
    conexion.commit()
    mensaje="Datos guardados correctamente"
    cursor.close()
    conexion.close()
    return render_template("Asignacion/agregarAsignacion.html",mensaje=mensaje,profesores=profesores,grupos=grupos,materias=materias)

@app.route("/seap/gestionAsignacion")
def gestionAsignacion():
    conexion=get_conexion()
    cursor=conexion.cursor()
    cursor.execute("select  a.cveAsignacion, CONCAT(p.nomPro,' ',p.apPaterno,' ',p.apMaterno,' ') as nombreCompleto, a.cveGru, m.nomMat from Asigna as a inner join Profesor as p on a.cvePro=p.cvePro inner join Materia as m on a.cveMat=m.cveMat")
    asignasiones=cursor.fetchall()
    cursor.close()
    conexion.close()
    return render_template("Asignacion/gestionAsignacion.html",asignasiones=asignasiones)
#---------------Pregunta
@app.route("/seap/agregarPregunta")
def agregarPregunta():
    return render_template("Pregunta/agregarPregunta.html")
@app.route("/seap/guardarPre", methods=['POST'])
def guardarPre():
    pregunta=request.form.get('pregunta')
    conexion=get_conexion()
    cursor=conexion.cursor()
    cursor.execute("Insert into Pregunta(pregunta) values(?)",(pregunta,))
    conexion.commit()
    mensaje="Pregunta agregada correctamente"
    cursor.close()
    conexion.close()
    return render_template("Pregunta/agregarPregunta.html",mensaje=mensaje)


@app.route("/seap/gestionPreguntas")
def gestionPreguntas():
    conexion=get_conexion()
    cursor=conexion.cursor()
    cursor.execute("Select * from Pregunta")
    preguntas=cursor.fetchall()
    cursor.close()
    conexion.close()
    return render_template("Pregunta/gestionPreguntas.html",preguntas=preguntas)

#---------------Sesion
@app.route("/seap/agregarSesion")
def agregarSesion():
    conexion=get_conexion()
    cursor=conexion.cursor()
    cursor.execute("Select * from Grupos")
    grupos=cursor.fetchall()
    cursor.close()
    conexion.close()
    return render_template("Sesion/agregarSesion.html",grupos=grupos)
@app.route("/seap/guardarSesion", methods=['POST'])
def guardarSesion():
    cveGru=request.form.get('grupo')
    fecha = date.fromisoformat(request.form.get('fecha'))
    horaInicio = time.fromisoformat(request.form.get('horaInicio'))
    horaFin = time.fromisoformat(request.form.get('horaFin'))
    mensaje=""
    conexion=get_conexion()
    cursor=conexion.cursor()   
    cursor.execute("Select * from Grupos")
    grupos=cursor.fetchall()

    if(horaInicio>=horaFin):
        mensaje="ERROR; La hora de inicio no puede ser mayor que la hora fin"
    else:
        
        cursor.execute("Insert into Sesiones(cveGru,fecha,horaInicio,horaFin) values(?,?,?,?)",(cveGru,fecha,horaInicio,horaFin))
        conexion.commit()
        mensaje="Sesion registrada correctamnete"
    cursor.close()
    conexion.close()     
    return render_template("Sesion/agregarSesion.html",mensaje=mensaje,grupos=grupos)
        

@app.route("/seap/gestionSesion")
def gestionSesion():
    conexion=get_conexion()
    cursor=conexion.cursor()
    cursor.execute("SELECT cveSesion,cveGru, CONVERT(VARCHAR(10), fecha, 103) AS fecha, CONVERT(VARCHAR(5), horaInicio, 108) AS horaInicio,CONVERT(VARCHAR(5), horaFin, 108) AS horaFin FROM Sesiones;")
    sesiones=cursor.fetchall()
    cursor.close()
    conexion.close()   
    return render_template("Sesion/gestionSesion.html",sesiones=sesiones)

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