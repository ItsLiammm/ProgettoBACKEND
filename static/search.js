document.addEventListener("DOMContentLoaded", function() {
    const searchInput = document.getElementById('song-search');
    const genreFilter = document.getElementById('genre-filter');
    const allLabels = document.querySelectorAll('#songs-list label');

    function eseguiRicerca() {
        const query = searchInput.value.toLowerCase();
        const genre = genreFilter.value;
        if (!query && !genre) {
            allLabels.forEach(label => {
                const container = label.closest('div') || label.closest('li') || label;
                container.style.display = ""; 
            });
            return;
        }
        const url = `/api/search/?q=${encodeURIComponent(query)}&genre=${encodeURIComponent(genre)}`;

        fetch(url)
            .then(response => response.json())
            .then(data => {
                const matchedIds = data.results.map(song => song.id.toString());

                allLabels.forEach(label => {
                    const checkbox = label.querySelector('input[type="checkbox"]');
                    const container = label.closest('div') || label.closest('li') || label;
                    if (checkbox && matchedIds.includes(checkbox.value)) {
                        container.style.display = "";
                    } else {
                        container.style.display = "none";
                    }
                });
            })
            .catch(error => console.error('Errore durante la ricerca:', error));
    }

    if (searchInput) {
        searchInput.addEventListener('input', eseguiRicerca);
    }
    if (genreFilter) {
        genreFilter.addEventListener('change', eseguiRicerca);
    }
});




