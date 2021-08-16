function verifyPassword() {  
    let pw1 = document.getElementById("pass1").value;
    let pw2 = document.getElementById("pass2").value;
    console.log(pw1)
    console.log(pw1)
    if(pw1 != pw2){
      document.getElementById("message").innerHTML = "**Passwords didn't match!";
      return false;
    }
    else
      return true;
  }