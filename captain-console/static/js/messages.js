let body = document.getElementsByTagName('body')[0];
let msg_container = document.getElementById('messages_container');
let msg = document.getElementById('messages');

function kill_modal(e) {
    msg.style.display = 'none';
    msg_container.style.display = 'none';
    body.classList = "";
}

if (msg_container !== null) {
    msg_container.addEventListener('click', kill_modal);
}
if (msg !== null) {
    msg.addEventListener('click', kill_modal);
}

