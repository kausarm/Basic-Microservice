const express = require("express");
const app = express();
const port = 3000;

app.get("/kausar/getTingkatPrevalensiStunting", (req, res) => {
  var req = require("request");

  var options = {
    method: "GET",
    url: "https://api.bireuendigital.id/tingkat-prevalensi/prov",
    headers: {
      "x-access-token":
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTUyNTEsImlhdCI6MTY1MzU0MDYwNCwiZXhwIjoxNjUzNjI3MDA0fQ.il2Ax5SOVaE5EbUK52hboWD6rS1BJ-OLfe8A318mdyE",
      "content-type": "application/x-www-form-urlencoded",
    },
  };

  req(options, function (error, response, body) {
    if (error) throw new Error(error);
    res.send(body);
    const data = response.data
    return JSON.stringify(data);

  });
});

app.listen(port, () => {
  console.log(`listening at http://94.74.127.32:${port}`);
});
