const fs = require('fs');

// Handler for starboard data
export default function dataHandler(req, res) {
  switch(req.method) {
    case 'GET':
      res.status(200).json({ message: 'data' });
      break;

    case 'POST':
      res.status(200).json({ message: 'Updated data!' });
      const newData = JSON.stringify(req.body);
      fs.writeFileSync("data.json", newData, 'utf-8', function (err) {
        if (err) {
          console.log("error writing to json file");
          return console.log(err);
        }
      });
      break;
      
    default: 
      res.status(400).json({ message: 'Bad request error' });
      break;
  }
}
