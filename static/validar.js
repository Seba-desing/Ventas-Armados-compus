$(function()
{
  $("#form-despacho").validate
  ({
    rules:
    {
      nom:
      {
        required:true
      },
      apellido:
      {
        required:true
      },
      tel:
      {
        required:true
      },
      direc:
      {
        required:true
      },
      mail:
      {
        required:true
      },
      ciudad:
      {
        required:true
      },
      tipore:
      {
        required:true
      },
      zip:
      {
        required:true
      }
    },
    messages:
    {
      nom:
      {
        required:'Este campo es requerido',
        minlength:'Por favor ingresa al menos 5 carácteres'
      },
      apellido:
      {
        required:'Este campo es requerido',
        minlength:'Por favor ingresa al menos 5 carácteres'
      },
      tel:
      {
        required:'Este campo es requerido',
        minlength:'Por favor ingresa 9 carácteres',
        maxlength:'Por favor ingresa 9 carácteres'
      },
      direc:
      {
        required:'Este campo es requerido'

      },
      mail:
      {
        required:'Este campo es requerido'

      },
      ciudad:
      {
        required:'Este campo es requerido'

      },
      tipore:
      {
        required:'Este campo es requerido',
        minlength:'Por favor Ingrese un minimo de 4 caracteres',
        maxlength:'Ingrese un maximo de 13 caracteres'
      },
      zip:
      {
        required:'Este campo es requerido',
        minlength:'Por favor ingrese su zip minimo y maximo de 3 digitos',
        maxlength:'Por favor ingrese su zip minimo y maximo de 3 digitos'
      }
    }
  });
});

/*const expresiones =  {
	usuario : / ^ [ a-zA-Z0-9 \ _ \ - ] { 4,16 } $ / ,  // Letras, numeros, guion y guion_bajo
	nombre : / ^ [ a-zA-ZÀ-ÿ \ s ] { 1,40 } $ / ,  // Letras y espacios, pueden llevar acentos.
	contraseña : / ^ . { 4,12 } $ / ,  // 4 a 12 dígitos.
	correo : / ^ [ a-zA-Z0-9 _. + - ] + @ [ a-zA-Z0-9- ] + \. [ a-zA-Z0-9-. ] + $ / ,
	telefono : / ^ \ d { 7,14 } $ /  // 7 a 14 numeros.
}*/

/*const  formulario  =  documento . getElementById ( 'form-despacho' ) ;
const inputs =  documento . querySelectorAll ( '#form-despacho input' ) ;
const validarFormulario = (e) =>{
  switch (e.target.name) {
    case "nom":
      if (expresiones.nombre.test(e.target.value)) {

      }else {
        document.getElementById('form-group col-md-6').classlist.add('formulario_label_incorrecto');

      }

    break;
    case "apellido":

    break;
    case "mail":

    break;
    case "nummber":

    break;
    case "direc":

    break;
    case "tipore":

    break;
    case "ciudad":

    break;

  }
}

inputs.forEach((input) => {
  input.addEventListener('Keyup', validarFormulario);
  input.addEventListener('blur', validarFormulario);
});

form-despacho.addEventListener('submit',(e)=>{
  e.preventDefault();
});*/
