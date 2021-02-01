var express = require('express');
var router = express.Router();
var path = require("path");
const PythonShell = require("python-shell");
const spawn = require("child_process").spawn;

//import {PythonShell} from 'python-shell';

/* GET home page. */
router.get('/', function(req, res, next) {
  console.log('get home root')
  res.render('index', { title: 'Express' });
});


router.post('/', function(req, res, next) {
  const script = path.join(__dirname, '../python/led_utils.py');
  console.log('command: ', req.body.command);

  const pythonProcess = spawn('python3',[script, req.body.command], {uid:0});
  pythonProcess.stdout.on('data', (data) => {
    console.log('response from python script: ', data);
  });
  pythonProcess.on('close', (code) => {
    console.log(`child process close all stdio with code ${code}`);
    // send data to browser
    res.json({status: 'success'});
 });

  console.log('POST to root')
  //res.json({status: 'success'});
});


module.exports = router;
