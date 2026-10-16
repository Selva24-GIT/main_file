const cells = Array.from(document.querySelectorAll("[data-cell]"));
const turnLabel = document.getElementById("turn");
const statusText = document.getElementById("status-text");
const scores = { X: 0, O: 0, draws: 0 };
const scoreLabels = {
  X: document.getElementById("score-x"),
  O: document.getElementById("score-o"),
  draws: document.getElementById("score-draws"),
};
const winningLines = [
  [0, 1, 2], [3, 4, 5], [6, 7, 8],
  [0, 3, 6], [1, 4, 7], [2, 5, 8],
  [0, 4, 8], [2, 4, 6],
];

let board = Array(9).fill("");
let currentPlayer = "X";
let roundOver = false;

function updateScores() {
  scoreLabels.X.textContent = scores.X;
  scoreLabels.O.textContent = scores.O;
  scoreLabels.draws.textContent = scores.draws;
}

function setStatus(mark, message) {
  turnLabel.textContent = mark;
  turnLabel.classList.toggle("mark-o", mark === "O");
  statusText.textContent = message;
}

function findWinner() {
  return winningLines.find(([a, b, c]) =>
    board[a] && board[a] === board[b] && board[a] === board[c]
  );
}

function finishRound() {
  roundOver = true;
  cells.forEach((cell) => { cell.disabled = true; });
}

document.getElementById("board").addEventListener("click", (event) => {
  const cell = event.target.closest("[data-cell]");
  if (!cell || roundOver) return;

  const index = Number(cell.dataset.cell);
  if (board[index]) return;

  board[index] = currentPlayer;
  cell.textContent = currentPlayer;
  cell.classList.add("mark-" + currentPlayer.toLowerCase());
  cell.setAttribute("aria-label", "Square " + (index + 1) + ": " + currentPlayer);

  const line = findWinner();
  if (line) {
    scores[currentPlayer] += 1;
    updateScores();
    line.forEach((winningIndex) => cells[winningIndex].classList.add("winner"));
    finishRound();
    setStatus(currentPlayer, "wins this round!");
    return;
  }

  if (board.every(Boolean)) {
    scores.draws += 1;
    updateScores();
    finishRound();
    setStatus("—", "It's a draw.");
    return;
  }

  currentPlayer = currentPlayer === "X" ? "O" : "X";
  setStatus(currentPlayer, "to move");
});

function startNewRound() {
  board = Array(9).fill("");
  currentPlayer = "X";
  roundOver = false;
  cells.forEach((cell, index) => {
    cell.textContent = "";
    cell.disabled = false;
    cell.classList.remove("mark-x", "mark-o", "winner");
    cell.setAttribute("aria-label", "Empty square " + (index + 1));
  });
  setStatus("X", "starts first");
}

document.getElementById("new-round").addEventListener("click", startNewRound);
document.getElementById("reset-score").addEventListener("click", () => {
  scores.X = 0;
  scores.O = 0;
  scores.draws = 0;
  updateScores();
  startNewRound();
});

setStatus("X", "starts first");
