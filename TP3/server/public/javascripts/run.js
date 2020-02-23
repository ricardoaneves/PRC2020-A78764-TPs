var prefixes = `
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX noInferences: <http://www.ontotext.com/explicit>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
`;

var genLink = 'http://localhost:7200/repositories/';

$(document).ready(function(){

    $("#run").click(function(){

        var query = $("#query").val();
        var repository = $("#repository").val();
        var link = genLink + repository + '?query=';
        var encoded = encodeURIComponent(prefixes + query);

        axios.get('http://localhost:3012/query?query=' + link + encoded)
            .then(function(dados){

                d = JSON.stringify(dados.data);
                $("#results").val(d);

            })
            .catch(function(error){

                $("#results").val(error);

            })
    });
});

$(document).ready(function(){

    $("#clean").click(function(){

        $("#results").val('');

    });
});