function validar_login(event) {
  event.preventDefault(); // Evitar el comportamiento predeterminado del formulario
  const usuario = document.getElementById('email');
  const contrasena = document.getElementById('contrasena');
  if (usuario.value === '' || contrasena.value === '') {
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
  axios.post('api/validar_login', {
    usuario: usuario.value,
    contrasena: contrasena.value
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
        window.location.href = '/fronted/index_dashboar';  // Reemplaza '/otra_vista' con la URL de la vista deseada
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
document.getElementById('entrar').addEventListener('click', validar_login);




function registrar() {
  const regis_usuario = document.getElementById('regis_usuarios').value;
  const regis_email = document.getElementById('regis_email').value;
  const regis_contrasena = document.getElementById('regis_contrasena').value;
  const regis_sexo = document.getElementById('regis_sexo').value;
  const regis_fecha_nacimiento = document.getElementById('regis_fecha_nacimiento').value;
  if (
    regis_usuario === '' ||
    regis_email === '' ||
    regis_contrasena === '' ||
    regis_sexo === '' ||
    regis_fecha_nacimiento === ''
  ) {
    Swal.fire({
      position: 'top-center',
      icon: 'error',
      title: 'Por favor, complete todos los campos.',
      showConfirmButton: false,
      timer: 2000,
    });
    return;
  }
  axios
    .post(
      "/api/guardaregistros",
      {
        regis_usuarios: regis_usuario,
        email: regis_email,
        contrasena: regis_contrasena,
        sexo: regis_sexo,
        fecha_nacimiento: regis_fecha_nacimiento,
      },
      {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      }
    )
    .then((res) => {
      if (res.data === 'Usuario ya existe') {
        Swal.fire({
          position: 'top-center',
          icon: 'warning',
          title: 'El usuario ya existe',
          showConfirmButton: false,
          timer: 2000,
        });
      } else if (res.data === 'Email ya existe') {
        Swal.fire({
          position: 'top-center',
          icon: 'warning',
          title: 'La direccion de correo electronico existente',
          showConfirmButton: false,
          timer: 2000,
        });
      } else {
        Swal.fire({
          position: 'top-center',
          icon: 'success',
          title: '¡Se ha registrado exitosamente!',
          showConfirmButton: false,
          timer: 2000,
        });
        document.getElementById('regis_usuarios').value = '';
        document.getElementById('regis_email').value = '';
        document.getElementById('regis_contrasena').value = '';
        document.getElementById('regis_sexo').value = '';
        document.getElementById('regis_fecha_nacimiento').value = '';
      }
    })
    .catch((error) => {
      console.error(error);
    });
}
