//----------------------funcion mostrar tabla de citas
function mostrar_cita_admin_tabla() {
    const divcate = document.getElementById("tabla_prueba");
  
    axios
      .get("/api/mostrar_usuarios", { 
        responseType: "json",
      })

      .then(function (response) {
        let datos = response.data;
        var length = Object.keys(datos).length + 1;
        let mostrar = "";
        i = 0;
        for (let index = 1; index < length; index++) {
          mostrar += ` <tr>   
                  <td>${datos[index].id}</td>  
                  <td>${datos[index].usuario}</td>  
                  <td>${datos[index].Email}</td>  
                  <td>${datos[index].contraseña}</td>
                  <td>${datos[index].sexo}</td>
                  <td>${datos[index].fecha_nacimiento}</td>
                  <td><a class="btn btn-primary btn-edit">Actualizar</a></td>
                  <td><a class="btn btn-danger btn-eliminar"">Eliminar</a></td>
                </tr> `;
        }
        divcate.innerHTML = mostrar;
      })
      .catch(function (error) {
        // Maneja los errores aquí
        console.log(error);
      });
  }
  window.addEventListener("load", function () {
    mostrar_cita_admin_tabla();
  });