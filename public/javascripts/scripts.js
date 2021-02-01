// global variable (I know, not cool) for managing state of the python script
// if you call the python script too many times before it completes, it locks up
// and requires killing the process
var scriptRunning = false;

function docReady(fn) {
    // see if DOM is already available
    if (document.readyState === "complete" || document.readyState === "interactive") {
        // call on next available tick
        setTimeout(fn, 1);
    } else {
        document.addEventListener("DOMContentLoaded", fn);
    }
}

docReady(function() {
    // set up the event handlers
  document.getElementById("clear").addEventListener("click", function() {
    fetchPost('clear');
  });

  document.getElementById("flag").addEventListener("click", function() {
    fetchPost('flag');
  });

  document.getElementById("spiral").addEventListener("click", function() {
    fetchPost('spiral');
  });

  document.getElementById("diagonal").addEventListener("click", function() {
    fetchPost('diagonal');
  });
});


function showMessage(m){
  var o = document.getElementById("output");
  o.value = m + '\n' + o.value;
}


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
    showMessage('script running, please wait');
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
    showMessage('script complete');
  })
}