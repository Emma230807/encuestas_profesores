function comenzarEncuesta(event) {
    event.preventDefault();

    const formulario = document.getElementById("accesoFormulario");

    if (!formulario.checkValidity()) {
        formulario.reportValidity();
        return;
    }

    const grupo = document.getElementById("grupo").value;

    // cveAlumno autoincremental
    const cveAlumno = Number(localStorage.getItem("cveAlumno") || 0) + 1;
    localStorage.setItem("cveAlumno", cveAlumno);

    sessionStorage.setItem("grupo", grupo);
    sessionStorage.setItem("cveAlumno", cveAlumno);

    window.location.href = "encuesta.html";
}