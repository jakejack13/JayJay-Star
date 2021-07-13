// Handler for starboard data
export default function dataHandler(req, res) {
  switch(req.method) {
    case 'GET':
      res.status(200).json({ message: 'data' });
      break;
    case 'POST':
      res.status(200).json({ message: 'Updated data!' });
      console.log(req.body.query)
      break;
    default: 
      res.status(400).json({ message: 'Bad request error' });
      break;
  }
}
