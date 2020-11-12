function confirmarEliminacionCupon(id) {
  Swal.fire({
    title: '¿Estas seguro?',
    text: "No podras deshacer esta acción!",
    icon: 'ALERTA',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Si, Borrar esto!',
    cancelButtonText: 'Cancelar',
  }).then((result) => {
    if (result.value) {
      window.location.href = "/eliminar_cupon/" + id + "/";

    }
  });
}

function confirmarEliminacionCliente(id) {
   
  Swal.fire({
    title: '¿Estas seguro?',
    text: "No podras deshacer esta acción!",
    icon: 'ALERTA',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Si, Borrar esto!',
    cancelButtonText: 'Cancelar',
  }).then((result) => {
    if (result.value) {
      window.location.href = "/eliminar_cliente/" + id + "/";

    }
  });
}

function confirmarEliminacionPlanes(id) {
  Swal.fire({
    title: '¿Estas seguro?',
    text: "No podras deshacer esta acción!",
    icon: 'ALERTA',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Si, Borrar esto!',
    cancelButtonText: 'Cancelar',
  }).then((result) => {
    if (result.value) {
      window.location.href = "/eliminar_planes/" + id + "/";

    }
  });
}

function confirmarEliminacionContrato(id) {
  Swal.fire({
    title: '¿Estas seguro?',
    text: "No podras deshacer esta acción!",
    icon: 'ALERTA',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Si, Borrar esto!',
    cancelButtonText: 'Cancelar',
  }).then((result) => {
    if (result.value) {
      window.location.href = "/eliminar_contrato/" + id + "/";

    }
  });
}

