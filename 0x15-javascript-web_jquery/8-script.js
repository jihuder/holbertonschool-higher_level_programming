$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    for (const i of data.results) {
        $('ul#list_movies').append('<li>' + i.title + '</li>');
    }
});
