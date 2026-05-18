const path = require("path")
const fsPromise = require("fs").promises
const fs = require("fs")
const {v4: uuid} = require("uuid")
const {format} = require("date-fns")

const logger = async (message, fileName)=>{
    const timestamp = `${format(new Date(), "dd-MM-yyyy\thh:mm:ss")}`
    const logItem = `${timestamp}\t${uuid()}\t${message}\n`
    try {
        if(!fs.existsSync(path.join(__dirname, "..", "logs")))
            await fsPromise.mkdir("./logs")
        await fsPromise.appendFile(path.join(__dirname, "..", "logs", fileName), logItem)
    } catch (error) {
        console.error(`Error At Logger\nErrorName: ${error.name}\nErrorMessage: ${error.message}`)
    }
}

const logValid = (req, res, next)=>{
    logger(`${req.method}\t${req.headers.origin}\t${req.url}`, "validLogs.txt")
    next()
}

const logError = (err, req, res, next)=>{
    logger(`${err.name}: ${err.message}`, "errorLogs.txt")
    req.status(500).send(err.message)
}

module.exports = {logValid, logError}