$(document).ready(function(){
$('button').on('click',function()
{
  var item=$('#placeholder').val();
  console.log(item);
$("#my_shopinglist").append(item)
})
  
})
