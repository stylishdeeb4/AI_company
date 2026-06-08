const form = document.querySelector(".form");
const status = document.querySelector(".status");

if (form && status) {
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    status.textContent = "送信ありがとうございます。正式公開時にフォーム送信先を設定してください。";
    form.reset();
  });
}

