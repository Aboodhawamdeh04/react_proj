import CropCard from "./CropCard";

function CropList({ crops }) {
  return (
    <div className="crop-list">
      {crops.map((crop) => (
        <CropCard
          key={crop.id}
          name={crop.name}
          focus={crop.focus}
          soilType={crop.soilType}
          status={crop.status}
        />
      ))}
    </div>
  );
}

export default CropList;