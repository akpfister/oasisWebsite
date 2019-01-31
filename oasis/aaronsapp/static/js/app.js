

 var files;

// Add events
$(document).ready(function() {
  $('input[type=file]').on('change', prepareUpload);
})


// Grab the files and set them to our variable
function prepareUpload(event) {
    files = event.target.files;
}

function feed_it() {
  var data = new FormData();
  $.each(files, function(key, value) {
    data.append('document', value);
  });
  data.append('creation_year', document.getElementById('creation_year').value);

  data.append('csrfmiddlewaretoken', document.getElementById('csrf').value);
  $.post({
    url: '/push_feed',
    data: data,
    processData: false, // Don't process the files
    contentType: false, // Set content type to false as jQuery will tell the server it's a query string request
    success: function(data) {
        if (data == "ok") {
            alert('done');
            //document.getElementById('creation_year').value = '';
        }
    },
    error: function(error) {
        alert('an error occured, please try again later')
    }
  });
  return false;
}
var pusher = new Pusher('118378e516562069dfa0', {
  encrypted: true,
  cluster: 'us2',
  authTransport: 'jsonp',
  authEndpoint: '/pusher_authentication'
});
var my_channel = pusher.subscribe('private-a_channel');
my_channel.bind("an_event", function(doc) {
  alert("message");
  var new_message = `<span>
              <img  src="` + doc.document + `">
          </span>`;
  $('#feeds').prepend(new_message);
});
// <h2>` + doc.description + `</h2>
