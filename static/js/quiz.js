$(document).ready(function(){
    $("#but1").click(function(){
        $(".rb").show();
        $(".rb").attr("disabled",true);
    });
});
function getAnswers(){
    document.getElementById('corans');
    var e=document.getElementByTagName(input);
    for(i=0;i<=e.length;i++){
        if(e[i].type=="radio"){
            if(e[i].checked){
                document.getElementById('corans').style.display="block";
            }
        }
    }
}