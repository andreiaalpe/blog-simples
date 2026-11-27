// Fecha os alerts após 10 segundos
document.querySelectorAll('.alert').forEach(alert => {
    setTimeout(() => { bootstrap.Alert.getOrCreateInstance(alert).close(); }, 10000);
});

// Mostra o modal de login quando redirecionando sem estar logado
document.addEventListener('DOMContentLoaded', function () {
    const showLoginModal = document.body.dataset.showLogin === 'true';
    if (showLoginModal) {
        const modalElement = document.getElementById('loginModal');
        if (modalElement) {
            const loginModal = new bootstrap.Modal(modalElement);
            loginModal.show();
        }
    }
});