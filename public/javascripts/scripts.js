// global variable (I know, not cool) for managing state of the python script
// if you call the python script too many times before it completes, it locks up
// and requires killing the process
var scriptRunning = false;

// barebones XMLHttpRequest
function doPost(){
  var formData = new FormData();
  formData.append("name", "Murdock");
  var req = new XMLHttpRequest();
  req.open("POST", "http://dataserver/update");
  req.send(formData);
}

// Fetch
function fetchPost(c){
  if (scriptRunning){
    console.log('unable to start a new command, a script is running');
    return;
  }
  scriptRunning = true;
  console.log("fetchPost()");
  fetch('/', {
    headers: { "Content-Type": "application/json; charset=utf-8" },
    method: 'POST',
    body: JSON.stringify({command: c})
  })
  .then(response => response.json())
  .then(data => {
    console.log(data);
    scriptRunning = false;
    console.log('reset scriptRunning');
  })
}