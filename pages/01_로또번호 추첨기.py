import React, { useState } from "react";

export default function LottoGenerator() {
  const [gameCount, setGameCount] = useState(1);
  const [results, setResults] = useState([]);

  // 로또 번호 생성 함수
  const generateLotto = () => {
    let games = [];
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

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-6">
      <h1 className="text-3xl font-bold mb-6">🎰 로또 번호 생성기</h1>

      <div className="bg-white shadow-md rounded-2xl p-6 w-full max-w-md text-center">
        <label className="block text-lg font-medium mb-2">
          생성할 게임 수 (1~10)
        </label>
        <input
          type="number"
          min="1"
          max="10"
          value={gameCount}
          onChange={(e) => setGameCount(Math.min(10, Math.max(1, e.target.value)))}
          className="border rounded-lg p-2 w-24 text-center mb-4"
        />
        <button
          onClick={generateLotto}
          className="bg-blue-500 text-white px-4 py-2 rounded-xl hover:bg-blue-600 transition-all"
        >
          번호 생성하기
        </button>

        <div className="mt-6 space-y-3">
          {results.map((game, i) => (
            <div
              key={i}
              className="bg-yellow-100 p-3 rounded-lg font-semibold text-lg tracking-wider"
            >
              {i + 1}게임: {game.join(", ")}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
