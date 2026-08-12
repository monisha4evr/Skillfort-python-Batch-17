import Home from "./pages/Home";
import About from "./pages/About";
import { BrowserRouter,Route,Routes} from "react-router-dom"
import Header from "./components/Header";
import Registration from "./pages/Registration";

function App(){
    return (
            <BrowserRouter>
              <Header/>
              <Routes>
                <Route path="/home" element={<Home/>}/>
                <Route path="/about" element={<About/>}/>
                <Route path="/Registration" element={<Registration/>}/>

              </Routes>
            </BrowserRouter>
            )
}
export default App;



