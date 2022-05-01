// import "../DatabaseConnection"
export default class LoginAccessor {
  constructor(username, password) {
    this.username = username;
    this.password = password;
  }

  getUsername() {
    return this.username;
  }

  getPassword() {
    return this.password;
  }


  createNewAccount() {
    /*
            1. Add new username to the database
            2. Add new password to the database
            3. Maybe add a new email and phonenumber to the database
            
        */
    return 1;
  }

  validateLogin(username,password) {
    /* 
            1. Check if the given username is in the database
                1a) Show username is incorrect
                1b) Maybe suggest creating an account
            2. Check if the password is correct given the username is correct
                2a) Show password is incorrect
            3. Successful login
        
        */
      // con.connect(function(err) {
      //   if (err) throw err;
      //   console.log("Connected!");
      //   var sql = "insert into Login(username,userPassword,loginId) values ('frenchdog34','chickennugget',1)";
      //   con.query(sql, function (err, result) {
      //   if (err) throw err;
      //   console.log("Result: " + result);
      //         });
      //       });
      console.log(username);
      console.log(password);
      alert("You clicked submit");
    return;
  }
}
