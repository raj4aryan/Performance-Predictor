const {predict} = require("../../controllers/mlServiceController")
const express = require("express")
const router = express.Router()

router.post("/", predict)

module.exports = router
