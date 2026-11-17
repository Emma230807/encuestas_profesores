
function validarSesion(event) {
    event.preventDefault();

    const formulario = document.getElementById("sesionFormulario");

    if (!formulario.checkValidity()) {
        formulario.reportValidity();
        return;
    }

    const grupo = document.getElementById("grupo").value;
    const fecha = document.getElementById("fecha").value;
    const horaInicio = document.getElementById("horaInicio").value;
    const horaFin = document.getElementById("horaFin").value;

    const hoy = new Date();
    const anio = hoy.getFullYear();
    const mes = String(hoy.getMonth() + 1).padStart(2, "0");
    const dia = String(hoy.getDate()).padStart(2, "0");
    const fechaActual = `${anio}-${mes}-${dia}`;

    if (!grupo) {
        alert("Seleccione un grupo.");
        return;
    }

    if (fecha < fechaActual) {
        alert("La fecha no puede ser anterior a la fecha actual.");
        return;
    }

    if (horaFin <= horaInicio) {
        alert("La hora de fin debe ser posterior a la hora de inicio.");
        return;
    }

    alert("Datos validados correctamente.");

    formulario.reset();
}
