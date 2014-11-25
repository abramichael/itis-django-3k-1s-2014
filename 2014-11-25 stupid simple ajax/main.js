function showusers() {
    jQuery.ajax({
        url: '/get_users/',
        type: "GET",
        dataType: "html",
        success: function (response) { //Если все нормально
            document.getElementById("showUsers").innerHTML = response;
        },
        error: function (response) { //Если ошибка
            document.getElementById("showUsers").innerHTML = "Ошибк";
        }
    });
    return false;
}