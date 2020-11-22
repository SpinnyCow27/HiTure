function validarFormulario(){
    $('.alert').remove();
    
    //hacemos una declaración de variables
    var rut=$('#Rut').val(),
        nombre=$('#Nombre').val(),
        apellidos=$('#Apellidos').val(),
        fecnac=$('#FecNac').val(),
        correo=$('#Correo').val(),
        contrasena=$('#Contraseña').val(),

    //Vamos a validar campo nombre:
    if(nombre=="" || nombre==null){
        cambiarColor("nombre");
        mostrarAlerta("Campo obligatorio");
        return false;
    }
    // console.Log(nombre);
}


// Función de cambio de color de los input
function cambiarColor(dato){
    $('#' + dato).css({
        border: "1px solid #dd5144"
    });
}

function mostrarAlerta(){
    $('#Nombre').before('<div class="alert" >Error: '+ texto +'</div>')
}
