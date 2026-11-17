function validarAsignacion(event) {
    event.preventDefault();

    const formulario = document.getElementById("asignacionFormulario");

    if (!formulario.checkValidity()) {
        formulario.reportValidity();
        return;
    }

    const profesor = document.getElementById("profesor").value;
    const grupo = document.getElementById("grupo").value;
    const materia = document.getElementById("materia").value;

    if (!profesor || !grupo || !materia) {
        alert("Seleccione un profesor, un grupo y una materia.");
        return;
    }



    alert("Profesor asignado");

    formulario.reset();

}
