const menuButton = document.querySelector(".menu-toggle");
const nav = document.querySelector(".nav");

if (menuButton && nav) {
  menuButton.addEventListener("click", () => {
    const isOpen = nav.classList.toggle("is-open");
    menuButton.setAttribute("aria-expanded", String(isOpen));
  });
}

const form = document.querySelector("#diagnosis-form");
const panel = document.querySelector("#result-panel");
const title = document.querySelector("#result-title");
const copy = document.querySelector("#result-copy");

const results = {
  organize: {
    title: "まず整理タイプ",
    copy:
      "AIツールを増やす前に、業務の棚卸しから始めるのがおすすめです。繰り返し作業、判断が必要な作業、機密情報を扱う作業を分けると、最初の一歩が見えます。",
  },
  template: {
    title: "テンプレート活用タイプ",
    copy:
      "すでにAIを少し使えているため、メール、投稿、資料作成などをテンプレート化すると進めやすい状態です。業務別の下書きテンプレートから整えるのがおすすめです。",
  },
  team: {
    title: "チーム導入タイプ",
    copy:
      "社員や外注先にもAIを使わせる前に、利用ルール、チェック体制、入力してはいけない情報を整理しましょう。安全な運用設計から始めるのがおすすめです。",
  },
};

if (form && panel && title && copy) {
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    const data = new FormData(form);
    const aiLevel = Number(data.get("aiLevel") || 0);
    const goal = data.get("goal");
    const risks = data.getAll("risk");

    let key = "organize";
    if (aiLevel >= 2 || goal === "prompt" || goal === "content") {
      key = "template";
    }
    if (aiLevel >= 4 || goal === "rule" || risks.includes("team") || risks.includes("security")) {
      key = "team";
    }

    title.textContent = results[key].title;
    copy.textContent = results[key].copy;
    panel.hidden = false;
    panel.scrollIntoView({ behavior: "smooth", block: "start" });
  });
}
