let per_page = document.getElementById('per-page');
per_page.addEventListener('change', (e) => {
    if (parseInt(per_page.value) !== undefined) {
        let url = new URL(document.location.href);
        let params = url.searchParams;
        params.set('per_page', parseInt(per_page.value));
        url.search = params;
        window.location.replace(url.toString());
    }
});

