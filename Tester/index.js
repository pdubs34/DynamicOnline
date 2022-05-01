const express = require('express')
const mysql = require('mysql')

const db = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "Wendis112!"
  })

db.connect(err => {
    if(err){
        throw err
    }
    console.log('MySQL Connected')
})

const app = express()

app.get('/createdb', (req,res) => {
    let sql = 'create database nodemysql'
    db.query(sql, err => {
        if(err){
            throw err
        }
        res.send('Database Created')
    })
})

app.listen('3000')