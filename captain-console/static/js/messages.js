let body = document.getElementsByTagName('body')[0];
let msg_container = document.getElementById('messages_container');
let msg = document.getElementById('messages');

function kill_modal(e) {
    msg.style.display = 'none';
    msg_container.style.display = 'none';
    body.classList = "";
}

msg_container.addEventListener('click', kill_modal);
msg.addEventListener('click', kill_modal);

