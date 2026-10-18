
function Validacion(event) {
    event.preventDefault();

    const input = document.getElementById("materia");
    const materia = input.value.trim();

    const patron = /^[A-ZÁÉÍÓÚÜÑa-záéíóúüñ]+(?:[ '-][A-ZÁÉÍÓÚÜÑa-záéíóúüñ]+)*$/;

    if (materia === "") {
        alert("Ingrese el nombre de la materia.");
        input.focus();
        return;
    }

    if (!patron.test(materia)) {
        alert("El nombre solo puede contener letras, espacios, apóstrofes y guiones.");
        input.focus();
        return;
    }

    alert("Datos validados correctamente.");
    document.getElementById("materiaFormulario").reset();
}
