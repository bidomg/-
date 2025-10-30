import React, { useState } from "react";

export default function LottoApp() {
  const [gameCount, setGameCount] = useState(1);
  const [results, setResults] = useState([]);

  // 로또 번호 생성 함수
  const generateLotto = () => {
    const games = [];
    for (let i = 0; i < gameCount; i++) {
      const numbers = [];
      while (numbers.length < 6) {
        const num = Math.floor(Math.random() * 45) + 1;
        if (!numbers.includes(num)) numbers.push(num);
      }
      numbers.sort((a, b) => a - b);
      games.push(numbers);
    }
    setResults(games);
  };

  // 입력값 유효성 제한 (1~10)
  const handleGameCountChange = (e) => {
    let value = parseInt(e.target.value, 10);
    if (isNaN(value)) value = 1;
    if (value < 1) value = 1;
    if (value > 10) value = 10;
    setGameCount(value);
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>🎰 로또 번호 생성기</h1>

      <div style={styles.card}>
        <label style={styles.label}>게임 수 (1~10):</label>
        <input
          type="number"
          min="1"
          max="10"
          value={gameCount}
          onChange={handleGameCountChange}
          style={styles.input}
        />
        <button onClick={generateLotto} style={styles.button}>
          번호 생성하기
        </button>

        <div style={styles.resultBox}>
          {results.map((game, i) => (
            <div key={i} style={styles.resultItem}>
              {i + 1}게임:{" "}
              <span style={styles.numbers}>{game.join(", ")}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

// 💅 간단한 스타일 (CSS-in-JS)
const styles = {
  container: {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "center",
    minHeight: "100vh",
    backgroundColor: "#f5f5f5",
    fontFamily: "sans-serif",
  },
  title: {
    fontSize: "2rem",
    marginBottom: "1rem",
  },
  card: {
    backgroundColor: "white",
    padding: "20px",
    borderRadius: "15px",
    boxShadow: "0 2px 8px rgba(0,0,0,0.1)",
    width: "300px",
    textAlign: "center",
  },
  label: {
    fontSize: "1rem",
  },
  input: {
    width: "80px",
    margin: "10px 0",
    padding: "5px",
    textAlign: "center",
    borderRadius: "5px",
    border: "1px solid #ccc",
  },
  button: {
    backgroundColor: "#007bff",
    color: "white",
    border: "none",
    borderRadius: "10px",
    padding: "10px 20px",
    cursor: "pointer",
  },
  resultBox: {
    marginTop: "15px",
    textAlign: "left",
  },
  resultItem: {
    backgroundColor: "#fff7cc",
    borderRadius: "8px",
    padding: "8px",
    marginTop: "5px",
    fontWeight: "bold",
  },
  numbers: {
    color: "#333",
  },
};
