var gifload_element = document.getElementById("btn-timkiem");
gifload_element.onclick = function() {
    notifi_func();
};
function notifi_func() {
    var  notifi = document.getElementById("notifi-text");
    notifi.innerHTML+= '<a><img class="img-responsive" height="80" width="80" src="/static/img/loading.gif"></a>';
    notifi.innerHTML+='<p class= "text-danger" sytle="font-size:28px; padding:1%">Dữ liệu đang được lấy khắp nơi trên Internet<br>Việc này sẽ mất vài phút</p>';


}