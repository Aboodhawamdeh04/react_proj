import { useState } from 'react';
import './App.css';
import { crops } from "./dataset";
import Header from "./components/Header";
import CropList from "./components/CropList"; // Importing the newly filled component

function App() {
  const [showCrops, setShowCrops] = useState(true);

  return (
    <div className="container">
      <Header />
      
      <button onClick={() => setShowCrops(!showCrops)} style={{ marginBottom: "20px" }}>
        {showCrops ? "Hide Crop Data" : "Show Crop Data"}
      </button>

      {/* Passing the dataset into the CropList component */}
      {showCrops && <CropList crops={crops} />}
    </div>
  );
}

export default App;