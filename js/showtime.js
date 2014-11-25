showDate();
t = setInterval("showDate()", 500);

function showDate() {
    //document.write(new Date());
    document.getElementById("time").innerHTML = new Date();
}