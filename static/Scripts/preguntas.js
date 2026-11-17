const MAX_PREGUNTAS = 12;

function guardarPregunta(event) {
    event.preventDefault();

    const formulario = document.getElementById("preguntaFormulario");

    if (!formulario.checkValidity()) {
        formulario.reportValidity();
        return;
    }

    const texto = document.getElementById("pregunta").value.trim();
    const tabla = document.getElementById("tablaPreguntas");

    if (texto === "") {
        alert("Ingresa el texto de la pregunta.");
        return;
    }

    if (tabla.rows.length >= MAX_PREGUNTAS) {
        alert("El cuestionario ya tiene las 12 preguntas.");
        return;
    }

    const fila = document.createElement("tr");

    const celdaPregunta = document.createElement("td");
    celdaPregunta.textContent = texto;

    const celdaAcciones = document.createElement("td");

    const botonEditar = document.createElement("button");
    botonEditar.type = "button";
    botonEditar.textContent = "Editar";
    botonEditar.onclick = function () {
        editarPregunta(this);
    };

    const botonEliminar = document.createElement("button");
    botonEliminar.type = "button";
    botonEliminar.textContent = "Eliminar";
    botonEliminar.onclick = function () {
        eliminarPregunta(this);
    };

    celdaAcciones.appendChild(botonEditar);
    celdaAcciones.appendChild(botonEliminar);

    fila.appendChild(celdaPregunta);
    fila.appendChild(celdaAcciones);

    tabla.appendChild(fila);

    formulario.reset();
    alert("Pregunta registrada correctamente.");
}

function editarPregunta(boton) {
    const fila = boton.closest("tr");
    const celda = fila.cells[0];

    const nuevoTexto = prompt("Ingresa el nuevo texto de la pregunta:", celda.textContent);

    if (nuevoTexto === null || nuevoTexto.trim() === "") {
        return;
    }

    if (nuevoTexto.trim().length > 255) {
        alert("La pregunta no puede tener más de 255 caracteres.");
        return;
    }

    celda.textContent = nuevoTexto.trim();
    alert("Pregunta actualizada correctamente.");
}

function eliminarPregunta(boton) {
    const confirmar = confirm("¿Estás seguro de que deseas eliminar esta pregunta?");

    if (confirmar) {
        boton.closest("tr").remove();
        alert("Pregunta eliminada correctamente.");
    }
}