$(document).ready(function(){
$('button').on('click',function()
{
  var item=$('#placeholder').val();
  console.log("updated" + item);
  $("#my_shopinglist").append("<li>" + item + "</li>")
})
  
})
