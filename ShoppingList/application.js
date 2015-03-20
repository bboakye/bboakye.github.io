$(document).ready(function(){
$('button').on('click',function()
{
  var item=$('#placeholder').val();
  console.log("updated1" + item);
  $("#my_shoppinglist").append("<li>" + item + "</li>")
})
  
})
