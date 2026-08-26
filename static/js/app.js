const form = document.getElementById("prediction-form");
const input = document.getElementById("image-input");
const preview = document.getElementById("preview");
const loading = document.getElementById("loading");
const result = document.getElementById("result");
const error = document.getElementById("error");
const button = document.getElementById("predict-button");

input.addEventListener("change", () => {
  const file = input.files[0];
  if (!file) return;
  preview.src = URL.createObjectURL(file);
  preview.classList.remove("hidden");
  result.classList.add("hidden");
  error.classList.add("hidden");
});

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  if (!input.files[0]) return;

  loading.classList.remove("hidden");
  result.classList.add("hidden");
  error.classList.add("hidden");
  button.disabled = true;

  try {
    const data = new FormData();
    data.append("image", input.files[0]);

    const response = await fetch("/predict", { method: "POST", body: data });
    const payload = await response.json();

    if (!response.ok) throw new Error(payload.error || "Prediction failed.");

    const rows = payload.top_predictions.map(
      item => `<div class="prediction"><span>${item.label}</span><strong>${item.confidence}%</strong></div>`
    ).join("");

    result.innerHTML = `
      <h2>Prediction: ${payload.label}</h2>
      <p>Confidence: <strong>${payload.confidence}%</strong></p>
      <h3>Top predictions</h3>
      ${rows}
    `;
    result.classList.remove("hidden");
  } catch (err) {
    error.textContent = err.message;
    error.classList.remove("hidden");
  } finally {
    loading.classList.add("hidden");
    button.disabled = false;
  }
});
