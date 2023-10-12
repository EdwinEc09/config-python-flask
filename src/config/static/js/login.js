
function ingreso_login() {
  const usuario = document.getElementById('correo_login');
  const contrasena = document.getElementById('contraseña_login');

  if (
    usuario.value === '' ||
    contrasena.value === ''

  ) {
    // Mostrar la alerta de error
    Swal.fire({
      position: 'top-center',
      icon: 'error',
      title: 'Por favor, complete todos los campos.',
      showConfirmButton: false,
      timer: 2000,
    });
    return; // Salir de la función si no hay datos en todos los campos
  }
  axios.post('fronted/login_chat', {
    usuario: usuario.value,
    contraseña: contrasena.value
  })
    .then(function (response) {
      console.log(response);

      if (response.data.status === "Correcto") { 
        // Alerta de inicio de sesión exitoso
        Swal.fire({
          position: 'top-center',
          icon: 'success',
          title: '¡Inicio de sesión exitoso!',
          showConfirmButton: false,
          timer: 2000
        });

        // Redirigir a otra vista
        window.location.href = 'fronted/principal';  // Reemplaza '/otra_vista' con la URL de la vista deseada
      } else if (response.data.status === "Error") {
        // Alerta de error con mensaje específico
        Swal.fire({
          position: 'top-center',
          icon: 'error',
          title: 'Error',
          text: response.data.message,
          showConfirmButton: false,
          timer: 2000
        });
      }
    })
    .catch(function (error) {
      console.log(error);
    });
}






//esta es la funcion de guardar paciente(registro) como admin utilizando la ruta de "admin_tabla_paciente.py"
function registrar() {

  const usuario = document.getElementById('usuario');
  const Correo = document.getElementById('Correo');
  const contraseña = document.getElementById('contraseña');
  const sexo = document.getElementById('sexo');
  const fecha = document.getElementById('fecha');


  // Validar si hay datos en todos los campos
  if (
    usuario.value === '' ||
    Correo.value === '' ||
    contraseña.value === '' ||
    sexo.value === '' ||
    fecha.value === '' 
  ) {
    // Mostrar la alerta de error
    Swal.fire({
      position: 'top-center',
      icon: 'error',
      title: 'Por favor, complete todos los campos.',
      showConfirmButton: false,
      timer: 2000,
    });
    return; // Salir de la función si no hay datos en todos los campos
  }

  axios
    .post('guardar_usuario', {
      usuario: usuario.value,
      Correo: Correo.value,
      contraseña: contraseña.value,
      sexo: sexo.value,
      fecha: fecha.value,
   
    }, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    })
    .then((res) => {
      console.log(res.data);
      if (res.data === 'Paciente already exists in the database') {
        // Mostrar la alerta de paciente existente
        Swal.fire({
          position: 'top-center',
          icon: 'warning',
          title: 'El paciente ya existe en la base de datos.',
          showConfirmButton: false,
          timer: 2000,
        });
      } else {
        // Mostrar la alerta de éxito
        Swal.fire({
          position: 'top-center',
          icon: 'success',
          title: '¡Paciente Registrado Exitosamente!',
          showConfirmButton: false,
          timer: 2000,
        });
        setTimeout(function () {
          window.location.href = '/fronted/principal';
        }, 2000);


        // Restablecer los valores de los campos

      }
    })
    .catch((error) => {
      console.error(error);
    });
}

