// static/js/password-toggle.js

document.addEventListener('DOMContentLoaded', function() {
    const hesloField = document.getElementById('id_heslo');
    const togglePassword = document.getElementById('togglePassword');

    if (hesloField && togglePassword) {
        togglePassword.addEventListener('click', function() {
            if (hesloField.type === 'password') {
                hesloField.type = 'text';
            } else {
                hesloField.type = 'password';
            }
        });
    }
});
