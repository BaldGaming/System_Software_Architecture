// Variable definitions for later functions.
let counter = 0;

const GOOD = "photos\\allah.jpeg";
const BAD = "photos\\allah's_wrath.jpeg";
const COLOR = 15;

let decreasing_channel;

// This function increments "counter", changes "img" and shifts backround color. 
function add()
{
    counter++; 
    document.getElementById('counter').textContent = counter;
            
    if (counter != 0)
        document.getElementById('img').src = BAD;

    decreasing_channel = Math.max(0, 255 - (counter * (255 / COLOR)));
    document.body.style.backgroundColor = `rgb(255, ${decreasing_channel}, ${decreasing_channel})`;
}

// Reset function
function reset()
{
    counter = 0; 
    document.getElementById('counter').textContent = counter;
    document.getElementById('img').src = GOOD;
    document.body.style.backgroundColor = 'white';
}