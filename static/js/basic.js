function func(){
    var button = document.createElement("a")
    button.innerHTML = "Download(double-click)"
    button.id = "download"
    var btn = document.getElementById("download-btn")
    btn.appendChild(button)
    button.onclick = function(){
        var element = document.getElementById('output')

        html2canvas(element, {
            onrendered: function(canvas){
                var imageData = canvas.toDataURL("image/png")
                var newData = imageData.replace(/^data:image\/png/, "data:application/octet-stream")
                $("#download").attr("download", "Qr-Code.png").attr("href", newData)
            }
        })
    }
}