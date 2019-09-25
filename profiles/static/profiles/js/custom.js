 // When the user scrolls down 20px from the top of the document, slide down the navbar
 window.onscroll = function() {scrollFunction()};
                
 function scrollFunction() {
     if (document.body.scrollTop > 30 || document.documentElement.scrollTop > 30) {                        
         $('#navbar').removeClass('bg-t');  
         $('#navbar').addClass('bg-change');        
         $('#navbar-2').removeClass('bg-t');  
         $('#navbar-2').addClass('bg-change');        

     } else {                      
         $('#navbar').removeClass('bg-change');
         $('#navbar').addClass('bg-t');
         $('#navbar-2').removeClass('bg-change');
         $('#navbar-2').addClass('bg-t');
     }
 }


// Gets the csrf token data
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

// Maps
var map, infoWindow;
var marker = false;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: -34.397, lng: 150.644},
        zoom: 8
    });

    infoWindow = new google.maps.InfoWindow;

    // Try HTML5 geolocation.
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
        var pos = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
        };

        // infoWindow.setPosition(pos);
        // infoWindow.setContent('Location found.');
        // infoWindow.open(map);
        map.setCenter(pos);
        }, function() {
        // handleLocationError(true, infoWindow, map.getCenter());
        });
    } else {
        // Browser doesn't support Geolocation
        handleLocationError(false, infoWindow, map.getCenter());
    }

    var input = document.getElementById('pac-input');
    var searchBox = new google.maps.places.SearchBox(input);
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);

    // Bias the SearchBox results towards current map's viewport.
    map.addListener('bounds_changed', function() {
        searchBox.setBounds(map.getBounds());
    });

    
        // Listen for the event fired when the user selects a prediction and retrieve
        // more details for that place.
    searchBox.addListener('places_changed', function() {
        var places = searchBox.getPlaces();

        if (places.length == 0) {
        return;
        }

        // For each place, get the icon, name and location.
        var bounds = new google.maps.LatLngBounds();
        places.forEach(function(place) {
        if (!place.geometry) {
            console.log("Returned place contains no geometry");
            return;
        }

        // Create a marker for each place.
        if(marker === false)
        {
            marker = new google.maps.Marker({
                map: map,
                title: place.name,
                position: place.geometry.location
            });
        }
        else
        {
            marker.setTitle(place.name);
            marker.setPosition(place.geometry.location);
        }
        

        if (place.geometry.viewport) {
            // Only geocodes have viewport.
            bounds.union(place.geometry.viewport);
        } else {
            bounds.extend(place.geometry.location);
        }
        });
        map.fitBounds(bounds);
        markerLocation();
    });


    //Listen for any clicks on the map.
    google.maps.event.addListener(map, 'click', function(event) {                
        //Get the location that the user clicked.
        var clickedLocation = event.latLng;
        //If the marker hasn't been added.
        if(marker === false){
            //Create the marker.
            marker = new google.maps.Marker({
                position: clickedLocation,
                map: map,
                draggable: true //make it draggable
            });
            //Listen for drag events!
            google.maps.event.addListener(marker, 'dragend', function(event){
                markerLocation();
            });
        } else{
            //Marker has already been added, so just change its location.
            marker.setPosition(clickedLocation);
        }
        //Get the marker's location.
        markerLocation();
    });
}

function geocodeLatLng(currentLocation) {

    var latlng = {lat: parseFloat(currentLocation.lat()), lng: parseFloat(currentLocation.lng())};
    console.log(latlng);
    var geocoder = new google.maps.Geocoder;
    geocoder.geocode({'location': latlng}, function(results, status) {
        if (status === 'OK') {
            
        if (results[0]) {
            
            
            var j=0;
            for (var i=0; i<results[j].address_components.length; i++)
            {
                if (results[j].address_components[i].types[0] == "locality") {
                        //this is the object you are looking for City
                        city = results[j].address_components[i];
                        $('#city').val(city.long_name);
                    }
                if (results[j].address_components[i].types[0] == "administrative_area_level_1") {
                        //this is the object you are looking for State
                        region = results[j].address_components[i];
                        $('#state').val(region.long_name);
                    }
                if (results[j].address_components[i].types[0] == "country") {
                        //this is the object you are looking for
                        country = results[j].address_components[i];
                        $('#country').val(country.long_name);
                    }
            }

            //city data
        } 
        }
    });
}


function handleLocationError(browserHasGeolocation, infoWindow, pos) {
    infoWindow.setPosition(pos);
    infoWindow.setContent(browserHasGeolocation ?
                            'Error: The Geolocation service failed.' :
                            'Error: Your browser doesn\'t support geolocation.');
    infoWindow.open(map);
}


function markerLocation(){
    //Get location.
    var currentLocation = marker.getPosition();
    // //Add lat and lng values to a field that we can save.
    document.getElementById('lat').value = currentLocation.lat(); //latitude
    document.getElementById('lng').value = currentLocation.lng(); //longitude
    geocodeLatLng(currentLocation);
    
}


//Cookie Setting

function setCookie(cname, cvalue) {
    var d = new Date();
    var exdays = 100;
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires="+ d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
        c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
        }
    }
    return "";
}

function cookieSettingType() {
    setCookie("type", $('input[name=empire]:checked').attr('title'));
    setCookie("value", $('input[name=empire]:checked').attr('value'));
}
$("input[name='empire']").change(function(){
    cookieSettingType();
});
var type1 = String(getCookie("type"));
var value1 = String(getCookie("value"));

if($('input[name="empire"]').length)
    $('input[name="empire"]').filter("[value="+ value1+ "]").filter("[title=" + type1 + "]").prop('checked', true);

// Cookie Setting Ends