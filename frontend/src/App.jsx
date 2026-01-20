import { useState } from "react";

function App() {
  const [resume, setResume] = useState("");
  const [interest, setInterest] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    setResult("");

    try {
      const response = await fetch("http://localhost:8000/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: new URLSearchParams({
          resume_text: resume,
          interest: interest,
        }),
      });

      if (!response.ok) {
        throw new Error("Failed to analyze resume");
      }

      const data = await response.json();
      setResult(data.result || data.message);
    } catch (err) {
      setError("Something went wrong. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: "800px", margin: "40px auto", fontFamily: "Arial" }}>
      <h1>AI Career Mentor</h1>

      <form onSubmit={handleSubmit}>
        <label>Resume</label>
        <textarea
          rows="6"
          value={resume}
          onChange={(e) => setResume(e.target.value)}
          required
          style={{ width: "100%", marginBottom: "16px" }}
        />

        <label>Career Interest</label>
        <input
          type="text"
          value={interest}
          onChange={(e) => setInterest(e.target.value)}
          style={{ width: "100%", marginBottom: "16px" }}
        />

        <button type="submit" disabled={loading}>
          {loading ? "Analyzing..." : "Analyze Resume"}
        </button>
      </form>

      {error && <p style={{ color: "red" }}>{error}</p>}
      {result && (
        <pre style={{ marginTop: "24px", whiteSpace: "pre-wrap" }}>
          {result}
        </pre>
      )}
    </div>
  );
}

export default App;

