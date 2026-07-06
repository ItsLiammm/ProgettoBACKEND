document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('main-search');
    const resultsDropdown = document.getElementById('search-results-dropdown');

    searchInput.addEventListener('input', function() {
        const query = this.value.trim();

        if (query.length < 1) {
            resultsDropdown.style.display = 'none';
            resultsDropdown.innerHTML = '';
            return;
        }

        
        
            fetch('/api/search/?q=' + encodeURIComponent(query))
                .then(response => response.json())
                .then(data => {
                    resultsDropdown.innerHTML = '';
                    
                    if (data.results && data.results.length > 0) {
                        data.results.forEach(song => {
                            const item = document.createElement('div');
                            item.className = 'search-result-item';
                            item.innerHTML = '<strong>' + song.title + '</strong> - ' + song.artist;
                            
                            item.addEventListener('click', () => {
                                searchInput.value = song.title + ' - ' + song.artist;
                                resultsDropdown.style.display = 'none';
                            });

                            resultsDropdown.appendChild(item);
                        });
                        resultsDropdown.style.display = 'block';
                    } else {
                        const noResults = document.createElement('div');
                        noResults.className = 'search-no-results';
                        noResults.innerText = 'No songs found';
                        resultsDropdown.appendChild(noResults);
                        resultsDropdown.style.display = 'block';
                    }
                })
                .catch(err => console.error('Error fetching search results:', err));

    });
    document.addEventListener('click', (e) => {
        if (!searchInput.contains(e.target) && !resultsDropdown.contains(e.target)) {
            resultsDropdown.style.display = 'none';
        }
    });
});