// external modules
const express = require("express");
const path = require("path");

// variables
const app = express();
const port = process.env.PORT || "8000";

// application config
app.set("views", path.join(__dirname, "views"));
app.set("view engine", "pug");
app.use(express.static(path.join(__dirname, "public")));

// routes
app.get("/", (req, res) => {
    res.render("index", { title: "Home"});
});

// server activation
app.listen(port, () => {
    console.log(`Listening on http://localhost:${port}`);
});