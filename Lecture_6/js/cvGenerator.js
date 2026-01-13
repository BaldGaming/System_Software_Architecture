function send_info()
{
    // Defines variables for elements in the html file.
    let first_name = document.getElementById("fname").value;
    let last_name = document.getElementById("lname").value;
    let message = document.getElementById("txt").value;
    let education = document.getElementsByName('education');
    let language = document.getElementById("language").value;

    let selected_items = [];

    let i;

    // These loops check if education and or experience have been selected.
    for (i = 0; i < education.length; i++) {
        if (education[i].checked)
            selected_items.push(education[i].value);
    }

    let exp_radios = document.getElementsByName('experience');
    let selected_exp = "";
    let exp_text = "";

    for (let i = 0; i < exp_radios.length; i++) {
        if (exp_radios[i].checked)
        {
            selected_exp = exp_radios[i].value;

            if (selected_exp === "0-3") exp_text = "low experience";
            else if (selected_exp === "4-7") exp_text = "medium experience";
            else if (selected_exp === "7+") exp_text = "high experience";
            break;
        }
    }

    // These if statements check if the user had filled the requiered fields.
    let error_msg = "";

    if (first_name == "")
        error_msg += "Please enter your first name.\n";

    if (last_name === "")
        error_msg += "Please enter your last name.\n";

    if (message === "")
        error_msg += "Please enter your message.\n";

    if (selected_items.length === 0)
        error_msg += "Please enter your education.\n";

    if (selected_exp === "")
        error_msg += "Please select your experience.\n";

    let output = document.getElementById("output_message");

    // This makes a message popout.
    if (error_msg !== "")
    {
        alert(error_msg);
        output.innerText = "";
        return 0;
    }

    // Prints out a message if the user filled every field.
    else
    {
        output.innerText = 
            "\nHello " + first_name + " " + last_name + "!\n" +
            "Your message is:\n" + message + "\n" +
            "It is important to know " + language + " and you have " + exp_text + " with it.\n" +
            "You are an educated person, having: " + selected_items.join(", ") + ",";
        return 1;
    }
}