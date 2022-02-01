let img;
let ledStatus = false;
let buttonStatus = true;

function preload() {
  img = loadImage("rpi_led_mockup.png");
}

function setup() {
  createCanvas(500, 500);
  background('white');
  drawButton();
}

function draw(){
  // RPi image refeshes each frame
  image(img, 0,0);
  
  getData();
  drawLed();
}

// Draw LED when ledStatus is true
let drawLed = () => {
  if(ledStatus) {
    fill('red');
    ellipse(278,98, 21, 21);
  }
}

// Get the output data from GPIO
function getData() {
  httpGet("/gpio", "json", false, (data) => {
    console.log(data);
    ledStatus = data["1"];
  }, (error) => {
    console.log(error);
  })
}

// Set input data on GPIO
let postData = () => {
  let data = httpPost("/gpio", "json", {"6": buttonStatus}, (result) => {
    console.log(result)
  });
}

function drawButton() {
  button = createButton('Input Button');
  button.position(10, 350);
  button.mousePressed(buttonPress);
}

function buttonPress() {
  buttonStatus = false;
  postData();
}

function mouseReleased() {
  if(buttonStatus === false) {
    buttonStatus = true;
    postData()
  }
}

