import { useEffect, useState } from "react";

function About(){
    const [version,setVersion] = useState(22)
    const [score,setScore] =useState(0)
    useEffect(
        ()=>{console.log("Hellow world")},[score]
    )
    // let version =22
    function add(){
        setVersion(version+1)
        console.log(version+1)
    }
    return (<>
        <p>Hello REact World {version}</p>
        <button type="submit" onClick={add}>Add</button>
        <p>Score:{score}</p>
        <button type="submit" onClick={()=>{setScore(score+1);console.log(score)}}>Add</button>
    </>)
}

export default About;