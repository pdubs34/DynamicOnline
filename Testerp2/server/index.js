const express = require('express')
const app = express()
const mysql = require('mysql')
const cors = require("cors");

app.use(cors());
app.use(express.json());

const db = mysql.createConnection({
    user: 'root',
    host: 'localhost',
    password: 'Wendis112!',
    database: 'sys',
});

app.post('/checkUser', (req,res) => {
    const username = req.body.username;
    const password = req.body.password
    db.query("Select * from Login where userName = ? and userPassword = ?",[username,password],
    (err,result) => {
        if(err){
            console.log(err)
        }else{
            res.send(result);
        }
    }
    )
});
app.listen(3001, ()=>{
    console.log("Worked")
});