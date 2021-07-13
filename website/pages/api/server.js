// Handler for starboard data
export default function dataHandler(req, res) {
  if (req.method == 'GET') {
    res.status(200).json({ message: 'data' })
  } else if (req.method == 'POST') {
    res.status(200).json({ message: 'Updated data!' })
  } else {
    res.status(400).json({ message: 'Bad request error' })
  }
}
