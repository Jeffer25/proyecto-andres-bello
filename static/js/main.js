let mensaje = document.querySelector('.alert');
let boton_ocultar_mensaje = document.querySelector('.close');

boton_ocultar_mensaje.addEventListener('click', () => {
    mensaje.style.display  = 'none';
})

// mostrar formulario de representante en la vista de estudiante
function mostrar(){
    document.getElementById('representante').style.display='grid';
}