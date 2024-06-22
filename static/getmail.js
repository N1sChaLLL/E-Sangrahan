function sendEmail(){
  Email.send({
    Host : "smtp.gmail.com",
    Username : "scammersanju@gmail.com",
    Password : "ec3enD1y",
    To : 'farewell31722@gmail.com',
    From : document.getElementById("email").value,
    Subject : "For registering",
    Body : "Thank you for registering in our website"
}).then(
  message => alert(message)
);

}
