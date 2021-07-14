import homeStyles from '../styles/Home.module.css';

export default function Home(props) {
  return (
    <div className={homeStyles.container}>
      <h1 className={homeStyles.title}>JayJay Star</h1>
    </div>
  )
}

export const getStaticProps = async () => {
  
}