let banana = 0;

function firstJsFunction()
{

    if (!banana)
    {
        document.getElementById('h1Text').innerHTML = 'Have a nice day!';
    }

    else
        document.getElementById('h1Text').innerHTML = 'Hello World!';

    banana =!banana;
}