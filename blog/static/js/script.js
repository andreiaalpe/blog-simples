// Fecha os alerts após 10 segundos

document.querySelectorAll('.alert').forEach(alert => {

    setTimeout(() => { bootstrap.Alert.getOrCreateInstance(alert).close(); }, 10000);

});