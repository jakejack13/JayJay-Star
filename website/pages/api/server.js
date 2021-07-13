const fs = require('fs');

// Handler for starboard data
export default function dataHandler(req, res) {
  switch(req.method) {
    case 'GET': // Read data.json and return recent starboard data
      const data = fs.readFileSync("data.json", {
        encoding: "utf-8"
      });
      res.status(200).json(data);
      break;

    case 'POST': // Update data.json and save recent starboard data
      const newData = JSON.stringify(req.body);
      fs.writeFileSync("data.json", newData, 'utf-8', function (err) {
        if (err) {
          console.log("error writing to json file");
          return console.log(err);
        }
        console.log("Succesfully stored data");
      });
      res.status(200).json({ message: 'Updated data!' });
      break;

    default: 
      res.status(400).json({ message: 'Bad request error' });
      break;
  }
}
