const objects = [
  { name: 'telefon', features: { canlı: false, elektronik: true, taşınabilir: true, evde: true, giyilebilir: false, sıvı: false, oyun: false, uçabilir: false, hareket: false, iletişim: true } },
  { name: 'bilgisayar', features: { canlı: false, elektronik: true, taşınabilir: true, evde: true, giyilebilir: false, sıvı: false, oyun: false, uçabilir: false, hareket: false, iletişim: false } },
  { name: 'kitap', features: { canlı: false, elektronik: false, taşınabilir: true, evde: true, giyilebilir: false, sıvı: false, oyun: false, uçabilir: false, hareket: false, iletişim: false } },
  { name: 'kalem', features: { canlı: false, elektronik: false, taşınabilir: true, evde: true, giyilebilir: false, sıvı: false, oyun: false, uçabilir: false, hareket: false, iletişim: false } },
  { name: 'anahtar', features: { canlı: false, elektronik: false, taşınabilir: true, evde: true, giyilebilir: false, sıvı: false, oyun: false, uçabilir: false, hareket: false, iletişim: false } },
  { name: 'kedi', features: { canlı: true, elektronik: false, taşınabilir: false, evde: true, giyilebilir: false, sıvı: false, oyun: false, uçabilir: false, hareket: true, iletişim: false } },
  { name: 'köpek', features: { canlı: true, elektronik: false, taşınabilir: false, evde: true, giyilebilir: false, sıvı: false, oyun: false, uçabilir: false, hareket: true, iletişim: false } },
  { name: 'uçak', features: { canlı: false, elektronik: true, taşınabilir: false, evde: false, giyilebilir: false, sıvı: false, oyun: false, uçabilir: true, hareket: true, iletişim: false } },
  { name: 'araba', features: { canlı: false, elektronik: true, taşınabilir: false, evde: false, giyilebilir: false, sıvı: false, oyun: false, uçabilir: false, hareket: true, iletişim: false } },
  { name: 'top', features: { canlı: false, elektronik: false, taşınabilir: true, evde: true, giyilebilir: false, sıvı: false, oyun: true, uçabilir: false, hareket: false, iletişim: false } },
  { name: 'bardak', features: { canlı: false, elektronik: false, taşınabilir: true, evde: true, giyilebilir: false, sıvı: true, oyun: false, uçabilir: false, hareket: false, iletişim: false } },
  { name: 'elbise', features: { canlı: false, elektronik: false, taşınabilir: true, evde: true, giyilebilir: true, sıvı: false, oyun: false, uçabilir: false, hareket: false, iletişim: false } },
  { name: 'saat', features: { canlı: false, elektronik: true, taşınabilir: true, evde: true, giyilebilir: false, sıvı: false, oyun: false, uçabilir: false, hareket: false, iletişim: false } },
  { name: 'fincan', features: { canlı: false, elektronik: false, taşınabilir: true, evde: true, giyilebilir: false, sıvı: true, oyun: false, uçabilir: false, hareket: false, iletişim: false } },
  { name: 'masa', features: { canlı: false, elektronik: false, taşınabilir: false, evde: true, giyilebilir: false, sıvı: false, oyun: false, uçabilir: false, hareket: false, iletişim: false } }
];

const questionBank = [
  { key: 'canlı', text: 'Bu nesne yaşıyor mu?' },
  { key: 'elektronik', text: 'Bu elektronik bir şey mi?' },
  { key: 'taşınabilir', text: 'Bunu kolayca taşıyabilir misin?' },
  { key: 'evde', text: 'Evde daha çok kullanılan bir şey mi?' },
  { key: 'giyilebilir', text: 'Bu giyilebilir bir şey mi?' },
  { key: 'sıvı', text: 'Bunda sıvı olur mu?' },
  { key: 'oyun', text: 'Bunu oyun için kullanır mısın?' },
  { key: 'uçabilir', text: 'Bu uçabilir mi?' },
  { key: 'hareket', text: 'Bu kendi kendine hareket eder mi?' },
  { key: 'iletişim', text: 'Bu iletişim için kullanılır mı?' }
];

let candidates = [];
let currentQuestion = null;
let currentGuess = null;
let askedQuestions = new Set();

const startScreen = document.getElementById('startScreen');
const gameScreen = document.getElementById('gameScreen');
const guessScreen = document.getElementById('guessScreen');
const customScreen = document.getElementById('customScreen');
const listScreen = document.getElementById('listScreen');
const questionText = document.getElementById('questionText');
const guessText = document.getElementById('guessText');
const roundInfo = document.getElementById('roundInfo');
const objectList = document.getElementById('objectList');

function speakText(message) {
  if (!('speechSynthesis' in window)) return;

  window.speechSynthesis.cancel();
  const utterance = new SpeechSynthesisUtterance(message);
  utterance.lang = 'tr-TR';
  utterance.rate = 0.9;
  utterance.pitch = 1.3;
  utterance.volume = 1;
  window.speechSynthesis.speak(utterance);
}

function showScreen(screen) {
  [startScreen, gameScreen, guessScreen, customScreen, listScreen].forEach((s) => {
    s.classList.toggle('active', s === screen);
  });
}

function startGame() {
  candidates = [...objects];
  currentQuestion = null;
  currentGuess = null;
  askedQuestions = new Set();
  showScreen(gameScreen);
  askNextQuestion();
}

function pickBestQuestion(list) {
  let best = null;
  let bestScore = -1;

  for (const q of questionBank) {
    if (askedQuestions.has(q.key)) continue;

    const yesCount = list.filter((obj) => obj.features[q.key]).length;
    const noCount = list.length - yesCount;
    const score = Math.abs(yesCount - noCount);

    if (score > bestScore) {
      bestScore = score;
      best = q;
    }
  }

  return best;
}

function askNextQuestion() {
  if (candidates.length <= 1) {
    finishGuess();
    return;
  }

  const chosen = pickBestQuestion(candidates);
  if (!chosen) {
    finishGuess();
    return;
  }

  askedQuestions.add(chosen.key);
  currentQuestion = chosen;
  questionText.textContent = chosen.text;
  roundInfo.textContent = `Olasılık sayısı: ${candidates.length}`;
  speakText(chosen.text);
}

function answerQuestion(result) {
  if (!currentQuestion) return;

  candidates = candidates.filter((obj) => obj.features[currentQuestion.key] === result);

  if (candidates.length === 0) {
    showScreen(customScreen);
    return;
  }

  if (candidates.length === 1) {
    finishGuess();
    return;
  }

  askNextQuestion();
}

function finishGuess() {
  if (candidates.length === 1) {
    currentGuess = candidates[0].name;
  } else if (candidates.length > 1) {
    currentGuess = candidates[Math.floor(Math.random() * candidates.length)].name;
  } else {
    currentGuess = 'Bilinmeyen nesne';
  }

  guessText.textContent = `Tahminim: ${currentGuess}!`;
  showScreen(guessScreen);
  speakText(`Tahminim: ${currentGuess}. Doğru mu?`);
}

function restartGame() {
  startGame();
}

function showObjectList() {
  objectList.innerHTML = '';
  objects.forEach((item) => {
    const li = document.createElement('li');
    li.textContent = item.name;
    objectList.appendChild(li);
  });
  showScreen(listScreen);
}

function saveCustomObject() {
  const input = document.getElementById('customInput');
  const value = input.value.trim();

  if (!value) {
    alert('Lütfen bir nesne adı yaz.');
    return;
  }

  const niceName = value.charAt(0).toUpperCase() + value.slice(1).toLowerCase();
  currentGuess = niceName;
  guessText.textContent = `Tahminim: ${niceName}`;
  showScreen(guessScreen);
  input.value = '';
}

document.getElementById('startBtn').addEventListener('click', startGame);
document.getElementById('restartBtn').addEventListener('click', restartGame);
document.getElementById('showListBtn').addEventListener('click', showObjectList);
document.getElementById('backToGameBtn').addEventListener('click', startGame);
document.getElementById('customSaveBtn').addEventListener('click', saveCustomObject);

document.querySelectorAll('.answer-btn[data-answer]').forEach((button) => {
  button.addEventListener('click', () => {
    const result = button.dataset.answer === 'true';
    answerQuestion(result);
  });
});

document.getElementById('guessYesBtn').addEventListener('click', () => {
  const message = 'Harika! Buldum!';
  alert(`${message} 🏆`);
  speakText(message);
  restartGame();
});

document.getElementById('guessNoBtn').addEventListener('click', () => {
  const message = 'Aaa, o zaman başka bir şeydi. Hadi tekrar deneyelim!';
  alert('Tamam, bir dahaki sefere daha da iyi olacağım! 😄');
  speakText(message);
  showScreen(customScreen);
});

showScreen(startScreen);
