
function generarReporte(event) {
    event.preventDefault();

    const formulario = document.getElementById("reporteFormulario");

    if (!formulario.checkValidity()) {
        formulario.reportValidity();
        return;
    }

    const grupo = document.getElementById("grupo");
    const profesor = document.getElementById("profesor");
    const materia = document.getElementById("materia");

    const resultado = document.getElementById("resultado");

    resultado.replaceChildren();

    const titulo = document.createElement("h2");
    titulo.textContent = "Resultados de la evaluación";

    const datos = document.createElement("p");
    datos.textContent =
        "Grupo: " + grupo.options[grupo.selectedIndex].text +
        " | Profesor: " + profesor.options[profesor.selectedIndex].text +
        " | Materia: " + materia.options[materia.selectedIndex].text;

    const mensaje = document.createElement("p");
    mensaje.textContent =
        "Todavía no hay resultados disponibles. " +
        "Se necesita conectar la información de las encuestas.";

    const botonPDF = document.createElement("button");
    botonPDF.type = "button";
    botonPDF.textContent = "Imprimir o guardar como PDF";

    botonPDF.onclick = function () {
        window.print();
    };

    resultado.appendChild(titulo);
    resultado.appendChild(datos);
    resultado.appendChild(mensaje);
    resultado.appendChild(botonPDF);
}
