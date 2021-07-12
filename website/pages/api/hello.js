// Saving latest starbaord data to json file
export default function updateData(req, res) {
  if (req.method == 'POST') {
    res.status(200).json({ message: 'Updated data!' })
  } else {
    res.status(400).json({ message: 'Bad request error' })
  }
}

// Get latest starboard data to load into website
export default function getData(req, res) {
  if (req.method == 'GET') {
    res.status(200).json({ message: 'data' })
  } else {
    res.status(400).json({ message: 'Bad request error' })
  }
}