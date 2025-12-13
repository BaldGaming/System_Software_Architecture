function clear_info()
{
    document.getElementById("fname").value = "";
    document.getElementById("lname").value = "";
    document.getElementById("txt").value = "";

    let exp_radios = document.getElementsByName('experience');
    for (let i = 0; i < exp_radios.length; i++)
        exp_radios[i].checked = false;

    let education = document.getElementsByName('education');
    for (let i = 0; i < education.length; i++)
        education[i].checked = false;

    document.getElementById("language").selectedIndex = 0;
}