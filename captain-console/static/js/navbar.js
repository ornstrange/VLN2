let search_form = document.getElementById('search-form');
let search_field = document.getElementById('search-field');
let search_form_res = document.getElementById('search-form-responsive');
let search_field_res = document.getElementById('search-field-responsive');

function prevent_search(e) {
    if (e.srcElement.value === "" ||
        e.srcElement.value === "Search...") {
        e.preventDefault();
        return false;
    }
}
function clear_focus(e) {
    e.srcElement.value = "";
}
function search_blur(e) {
    if (e.target.value === "")
        e.target.value = "Search...";
}

if (search_field) {
    search_field.addEventListener('focus', clear_focus);
    search_field.addEventListener('blur', search_blur);
} if (search_field_res) {
    search_field_res.addEventListener('focus', clear_focus);
    search_field_res.addEventListener('blur', search_blur);
} if (search_form) {
    search_form.addEventListener('submit', prevent_search);
} if (search_form_res) {
    search_form_res.addEventListener('submit', prevent_search);
}

let nav_collapse = document.getElementById('nav-collapse');
let collapse_btn = document.getElementById('collapse-btn');

collapse_btn.addEventListener('click', (e) => {
    if (nav_collapse.classList.contains('hide')) {
        nav_collapse.classList.remove('hide');
    } else {
        nav_collapse.classList.add('hide');
    }
});

