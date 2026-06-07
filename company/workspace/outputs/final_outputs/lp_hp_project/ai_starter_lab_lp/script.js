const form = document.querySelector(".contact-form");
const status = document.querySelector(".form-status");

if (form && status) {
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    status.textContent = "送信ありがとうございます。現在は仮フォームのため、正式公開時に送信先を設定してください。";
    form.reset();
  });
}

