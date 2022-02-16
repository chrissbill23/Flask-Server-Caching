serverurl = 'http://localhost:80/';

document.addEventListener('DOMContentLoaded', function() {
                  
	$.post( serverurl+"/countries", { query: ``}, function( data ) {
	  let select = $("#country_select");
	  data.forEach(element => select.append($('<option>', {
			value: element,
			text: element
		})));
		
	}, "json");
	
	$('#search_form').on('submit', function(e){
        e.preventDefault();
        let uni = $('#university').val();
		let country = $('#country_select').val();
		
		$.post( serverurl+"/", { query: `query {
            university(name: "${uni}", country: "${country}"){
				name
				country}
			}`}, function( data ) {
						res = $("#result");
						res.empty();
						data.university.forEach(element => res.append(`<li>
						<strong class="uni_name">${element.name}</strong>
						<em class="uni_country">${element.country}</em>
												</li>`));
				}
		, "json");
        
    });
}
);