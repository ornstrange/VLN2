function isnum(test) {
    return test.match(/[\d]/)
}

function isalph(test) {
    return test.match(/[a-z]/i)
}

function contains(test, list) {
    if (! list) return true
    for (let i = 0; i < list.length; i++)
        if (test === list[i]) return true;
    return false;
}

function valid(test, num, alph, allow) {
    if (! test) return true;
    let n, a, c = false;
    if (num) n = isnum(test);
    if (alph) a = isalph(test);
    if (allow) c = contains(test, allow);
    return n || a || c;
}

let postcode = document.getElementById('id_postcode');
let city = document.getElementById('id_city');
let address = document.getElementById('id_address');
if (postcode) {
    postcode.addEventListener('input', (ev) => {
        if (! valid(ev.data, true, false))
            postcode.value = postcode.value.slice(0, -1);
    });
} if (city) {
    city.addEventListener('input', (ev) => {
        if (! valid(ev.data, false, true, [' ', '-']))
            city.value = city.value.slice(0, -1);
    });
} if (address) {
    address.addEventListener('input', (ev) => {
        if (! valid(ev.data, true, true, [' ', '-', ',']))
            address.value = address.value.slice(0, -1);
    });
}

let expiration = document.getElementById('id_expiration');
let card_number = document.getElementById('id_card_number');
let ccv = document.getElementById('id_ccv');
if (expiration) {
    expiration.addEventListener('input', (ev) => {
        if (! ev.data) {
            return;
        } if (! valid(ev.data, true, false, ['/'])) {
            expiration.value = expiration.value.slice(0, -1);
        } if (expiration.value.length !== 3 && ev.data === '/') {
            expiration.value = expiration.value.slice(0, -1);
        } if (expiration.value.length === 3 && isnum(ev.data)) {
            let expval = expiration.value;
            expiration.value = expval.slice(0, -1) + '/' + expval.slice(-1);
        } if (expiration.value.length > 7) {
            expiration.value = expiration.value.slice(0, -1);
        }
    });
} if (card_number) {
    card_number.addEventListener('input', (ev) => {
        let vallen = 0;
        if (! ev.data) {
            return;
        } if (! valid(ev.data, true, false, ['-'])) {
            card_number.value = card_number.value.slice(0, -1);
        } if (card_number.value) {
            vallen = card_number.value.length;
        } if ((vallen !== 5 && vallen !== 10 && vallen !== 15) && ev.data === '-') {
            card_number.value = card_number.value.slice(0, -1);
        } if ((vallen === 4 || vallen === 9 || vallen === 14) && isnum(ev.data)) {
            card_number.value += '-';
        } if ((vallen === 5 || vallen === 10 || vallen === 15) && isnum(ev.data)) {
            if (card_number.value.slice(-2) !== '-') {
                let cardval = card_number.value;
                card_number.value = cardval.slice(0, -1) + '-' + cardval.slice(-1);
            }
        }
    });
} if (ccv) {
    ccv.addEventListener('input', (ev) => {
        if (! valid(ev.data, true, false))
            ccv.value = ccv.value.slice(0, -1);
    });
}

