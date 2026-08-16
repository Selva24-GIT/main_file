
import Header from './Header'
import Footer from './Footer'
import Content from './Content'
import './index.css'
import { useState } from 'react'


function App() {
 const [show,setshow]=useState(false)
const [number,setnumber]=useState([1,2,3])


  return (
    <div>
      <Header />
      <Footer string="Respect" />
      <Content />
    
      
      <button onClick={()=>setshow(!show)}>
        {show?"hide":"show"}
      </button>
      {show&&<h1>Hello</h1>}
    
      {...number.map(num=>num===2?num*10:num)}
  </div>
  );

}

export default App;
