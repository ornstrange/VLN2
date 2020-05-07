let search_form = document.getElementById('search-form');
let search_field = document.getElementById('search-field');

function check_search(e) {
    if (search_field.value === "" || search_field.value === "Search...") {
        e.preventDefault();
        return false;
    }
}

search_field.addEventListener('focus', (e) => {
    search_field.value = "";
});

search_field.addEventListener('blur', (e) => {
    if (search_field.value === "")
        search_field.value = "Search...";
});

search_form.addEventListener('submit', check_search);

