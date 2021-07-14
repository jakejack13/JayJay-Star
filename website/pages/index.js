import homeStyles from '../styles/Home.module.css';
import axios from 'axios';


export default function Home(props) {
  return (
    <div className={homeStyles.container}>
      <h1 className={homeStyles.title}>JayJay Star</h1>
    </div>
  )
}

export const getStaticProps = async () => {
  var posts;
  await (async () => {
    const allPosts = await axios.get("http://localhost:3000/api/server");
    posts = allPosts.data;
  })();

  return {
    props: {
      posts
    }
  }
}