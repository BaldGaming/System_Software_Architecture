function colorChange()
{
    var currentColor = document.getElementById('h3').innerHTML;
    
    if(currentColor == 'Black')
        {
        document.getElementById('HelloWorld').src = "photos\\colorYellow.jpg";
        document.getElementById('h3').innerHTML = 'Yellow';
        document.getElementById('h3').style.color = 'yellow';
        }

    else if(currentColor == 'Yellow')
        {
        document.getElementById('HelloWorld').src = "photos\\colorRed.jpg";
        document.getElementById('h3').innerHTML = 'Red';
        document.getElementById('h3').style.color = 'red';
        }

    else if(currentColor == 'Red')
        {
        document.getElementById('HelloWorld').src = "photos\\colorGreen.jpg";
        document.getElementById('h3').innerHTML = 'Green';
        document.getElementById('h3').style.color = 'green';
        }

    else if(currentColor == 'Green')
        {
        document.getElementById('HelloWorld').src = "photos\\colorBlack.jpg";
        document.getElementById('h3').innerHTML = 'Black';
        document.getElementById('h3').style.color = 'black';
        }
}