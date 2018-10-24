//window.onload = function(){ initGoogleMap(); }

var map
initGoogleMap = function() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(getLocation);
    } else {
        alert("No geolocation support");
    }
};

function getLocation(position) {
	var latitude = position.coords.latitude;
	var longitude = position.coords.longitude;
	
	showMap(position.coords);
}

function showMap(coords) {
	var googleLatAndLong = new google.maps.LatLng(coords.latitude, coords.longitude);
	var mapOptions = {
		zoom: 10,
		center: googleLatAndLong
	};
	var mapDiv = document.getElementById("map");
	map = new google.maps.Map(mapDiv, mapOptions);
}
