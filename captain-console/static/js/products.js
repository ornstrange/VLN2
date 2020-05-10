let per_page = document.getElementById('per-page');
let filter_keywords = document.getElementById('filter-keywords');


per_page.addEventListener('change', (e) => {
    if (parseInt(per_page.value) !== undefined) {
        let url = new URL(document.location.href);
        let params = url.searchParams;
        params.set('per_page', parseInt(per_page.value));
        url.search = params;
        window.location.replace(url.toString());
    }
});

filter_keywords.addEventListener('change', (e) => {
    let url = new URL(document.location.href);
    let params = url.searchParams;
    params.set('keyword', filter_keywords.value);
    url.search = params;
    window.location.replace(url.toString());
});


