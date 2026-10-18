
function validarProfesor(event) {
    event.preventDefault();

    const formulario = document.getElementById("profesorFormulario");

    if (!formulario.checkValidity()) {
        formulario.reportValidity();
        return;
    }

    const clave = document.getElementById("clave").value.trim();
    const nombre = document.getElementById("nombre").value.trim();
    const apellidoPaterno = document.getElementById("apellidoPaterno").value.trim();
    const apellidoMaterno = document.getElementById("apellidoMaterno").value.trim();
    const correo = document.getElementById("correo").value.trim();

    const patronNombre = /^[A-Za-zÁÉÍÓÚáéíóúÑñÜü]+([ '-][A-Za-zÁÉÍÓÚáéíóúÑñÜü]+)*$/;

    if (!/^[A-Za-z0-9-]{1,20}$/.test(clave)) {
        alert("La clave solo puede contener letras, números y guiones.");
        return;
    }

    if (!patronNombre.test(nombre)) {
        alert("Ingrese un nombre válido.");
        return;
    }

    if (!patronNombre.test(apellidoPaterno)) {
        alert("Ingrese un apellido paterno válido.");
        return;
    }

    if (!patronNombre.test(apellidoMaterno)) {
        alert("Ingrese un apellido materno válido.");
        return;
    }

    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(correo)) {
        alert("Ingrese un correo electrónico válido.");
        return;
    }

    alert("Datos validados correctamente.");

    formulario.reset();
}
