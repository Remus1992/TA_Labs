

unirest.post("https://imdb.p.mashape.com/movie")
    .header("X-Mashape-Key", "ZliAnc0uCwmshuMsPWnOWwzGsv2gp1qEQmWjsnHGD1a08O8QA0")
    .header("X-Mashape-Host", "imdb.p.mashape.com")
    .header("Content-Type", "application/x-www-form-urlencoded")
    .send("searchTerm=Inception")
    .end(function (result) {
        console.log(result.status, result.headers, result.body);
    });