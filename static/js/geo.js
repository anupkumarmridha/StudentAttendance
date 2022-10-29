

document.addEventListener('DOMContentLoaded', () => {
    pageLoad();
});

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function showPosition(position) {
    //to get student getLocation
    {% if user.user_type == '1' or user.is_superuser %}
    document.getElementById("stu_lang").value = position.coords.latitude;
    document.getElementById("stu_lat").value = position.coords.longitude;
    {% endif %}

    //to get faculty getLocation
    {% if user.user_type == '2' or user.is_superuser %}
    document.getElementById("faculty_lang").value = position.coords.latitude;
    document.getElementById("faculty_lat").value = position.coords.longitude;
    {% endif %}
    // x.innerHTML = "Latitude: " + position.coords.latitude +
    // "<br>Longitude: " + position.coords.longitude;
    document.myFrom.submit();
}

function positionError(error) {
    if (error.PERMISSION_DENIED) alert('Please accept geolocation');
    hideLoadingDiv();
    showError('Geolocation is not enabled. Please enable to use this feature');
}

function pageLoad() {
    getLocation();
}