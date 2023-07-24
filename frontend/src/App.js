import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Fabricant from './pages/Fabricant';



function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="*" element={<Home />} />
          
          <Route path="/fabricant" element={<Fabricant />} />
          <Route path="*" element={<Home />} />

        
        </Routes>
      </Router>




    </div>
  );
}

export default App;
