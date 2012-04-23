function Login(user, pass) {
  //Check if user is valid

  //Load the main page
  $.post('textScroller.py', { u: user, p:pass }, function( data ) {
          $( "#mainContent" ).empty().append( data );
    });
}

function UpdateTextScroller(user, msg, time) {
  //Do db work in python
  //post data with js
  //will have to add A LOT MORE logic to this

  $.post('message.py', { u: user, m: msg, t: time }, function( data ) {
          $( "#textScroller" ).append( data );
    });
  
}
