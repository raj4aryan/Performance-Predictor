const allowedOrigins = require('./allowedOrigins')

const corsOptions = {
    origin: (origin, callback)=>{
        if(allowedOrigins.indexOf(origin) !== -1 || !origin){
            return callback(null, true)
        }
        else return callback(new Error("cors not allowed")) 
    },
    optionsSuccessStatus: 200
}
module.exports = corsOptions