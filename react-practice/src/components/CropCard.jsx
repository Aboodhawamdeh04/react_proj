function CropCard({ name, focus, soilType, status }) {
  return (
    <div className="crop-card" style={{ border: "1px solid #ccc", padding: "10px", margin: "10px", borderRadius: "8px" }}>
      <h2>{name}</h2>
      <p><strong>Focus:</strong> {focus}</p>
      <p><strong>Soil Type:</strong> {soilType}</p>
      <p><strong>Status:</strong> {status}</p>
    </div>
  );
}

export default CropCard;