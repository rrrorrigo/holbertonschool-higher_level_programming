$(document).ready(function () {
  $('INPUT#language_code').keypress(function (event) {
      if(event.which === 13){
        const lang = $('INPUT#language_code').val();
        $.get("https://www.fourtonfish.com/hellosalut/?lang=" + lang, function (data, status) {
          $('DIV#hello').text(data.hello);
        }); 
      }
  });
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();
    $.get("https://www.fourtonfish.com/hellosalut/?lang=" + lang, function (data, status) {
      $('DIV#hello').text(data.hello);
    });
  });
});
