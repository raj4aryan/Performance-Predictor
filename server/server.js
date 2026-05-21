const express = require("express");
const app = express();
const PORT = process.env.PORT || 3500;
const {logValid, logError} = require("./middleware/logger")

app.use(logValid)
app.use(express.urlencoded({extended: false}))
app.use(express.json())
app.use("/", require("./Routes/root"))
app.use("/predict", require("./Routes/api/predict"))

app.use(logError)

app.listen(PORT, (req, res) => console.log(`Server Running on port ${PORT}`))