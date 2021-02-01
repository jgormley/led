var express = require('express');
var router = express.Router();
var path = require("path");
const spawn = require("child_process").spawn;

/* GET home page. */
router.get('/', function(req, res, next) {
  console.log('get home root')
  res.render('index', { title: 'Fun with LEDs and Raspberry Pi' });
});


router.post('/', function(req, res, next) {
  const script = path.join(__dirname, '../python/led_utils.py');
  const pythonProcess = spawn('python3',[script, req.body.command]);

  pythonProcess.stdout.on('data', (data) => {
    console.log('response from python script: ', data);
  });
  pythonProcess.on('close', (code) => {
    console.log(`child process closed all stdio with code ${code}`);
    // send data to browser
    res.json({status: 'success'});
 });
});


module.exports = router;
