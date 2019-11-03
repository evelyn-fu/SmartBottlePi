let Gpio = require('onoff').Gpio; //require onoff to control GPIO
let LEDPin = new Gpio(4, 'out');

data = 1;

buttonState = data;
if (buttonState != LEDPin.readSync()) { //Change LED state if button state is changed
    LEDPin.writeSync(buttonState); 
}