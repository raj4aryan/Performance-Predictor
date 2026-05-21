const express = require("express");
const cors = require("cors")
const corsOptions = require('./config/corsOptions');
const app = express();
const PORT = process.env.PORT || 3500;
const {logValid, logError} = require("./middleware/logger")

app.use(cors(corsOptions))
app.use(logValid)
app.use(express.urlencoded({extended: false}))
app.use(express.json())
app.use("/", require("./Routes/root"))
app.use("/predict", require("./Routes/api/predict"))

app.use(logError)

app.listen(PORT, (req, res) => console.log(`Server Running on port ${PORT}`))