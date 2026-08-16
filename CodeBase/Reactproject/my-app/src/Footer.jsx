import { useState } from "react";

function Footer(props) {
    const [name, setName] = useState("Earn")
    const [count,setConut]=useState(100)

    function handlenamechange() {
        const namelist = ["like ", "share ", "comment",props.string]
        const int = Math.floor(Math.random() * 4)
        setName(namelist[int])
    }

    function increase() {
        setConut(count+1)

    }
    
    function decrease() {
        setConut(count-1)

    }
    function reset(){
        setConut(100)
    }

    return (
        <footer>
            <h1>
                Let's Do {name}
            </h1>
            <button onClick={()=>{return handlenamechange()}} >subscribe</button>
            <h1>
                <button onClick={()=>{increase()}}>+</button>
                {count}
                <button onClick={()=>{decrease()}}>-</button>
            </h1>
            <button onClick={()=>{ reset()}}>reset</button>
        </footer>




    );

}
export default Footer;