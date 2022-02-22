import Header from "./layout/Header";
import {Route, Routes} from "react-router-dom";
import Home from "./views/Home";

export default () => {
    return (
        <div className="app">
            <Header/>
            <Routes>
                <Route path="/" element={<Home/>}/>
            </Routes>
        </div>
    )
}