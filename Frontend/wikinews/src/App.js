import './App.css';
import { Routes, Route } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      {/* Static Route for Testing */}
      <Routes>
        <Route path="/" element={<div>Home</div>} />
      </Routes>
    </div>
  );
}

export default App;
