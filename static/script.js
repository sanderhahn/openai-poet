const generatePoem = async () => {
  // Create JSON payload from form fields
  var payload = {
    recipient_name: document.getElementById("recipient_name").value,
    occasion: document.getElementById("occasion").value,
    memory: document.getElementById("memory").value,
  };

  // Make POST request with JSON payload
  const response = await fetch("/generate_poem", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });
  const poemResponse = await response.json();
  // Render the poem response in the current page
  const poemContainer = document.getElementById("poemContainer");
  poemContainer.innerHTML = poemResponse.poem.replaceAll("\n", "<br>");
};

document.addEventListener("DOMContentLoaded", function () {
  // Get the select element and the heading element
  const selectPersona = document.getElementById('persona');
  const poemHeading = document.getElementById('poemHeading');

  const onChangePersona = () => {
    // Get the selected poet's nickname and update the heading
    const poetNickname = selectPersona.options[selectPersona.selectedIndex].text;
    poemHeading.innerText = `A Poem by ${poetNickname}`;
    const poetCode = selectPersona.options[selectPersona.selectedIndex].value;
    document.body.classList = [poetCode];
  };

  // Add an event listener to the select element
  selectPersona.addEventListener('change', onChangePersona);
  onChangePersona();

  const poemForm = document.getElementById("poemForm");
  const submitButton = document.getElementById("submitButton");
  const loadingIndicator = document.getElementById("loadingIndicator");

  poemForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    submitButton.disabled = true;
    loadingIndicator.style.display = "block";
    poemForm.classList.add("form-disabled");

    // Perform poem generation API request
    // Wait for the response
    await generatePoem();

    submitButton.disabled = false;
    loadingIndicator.style.display = "none";
    poemForm.classList.remove("form-disabled");
  });
});