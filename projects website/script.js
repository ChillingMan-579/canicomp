function startTypeWriter(elementId, text) {
  const title = document.getElementById(elementId);
  let i = 0;

  function typeWriter() {
      if (i < text.length) {
          title.innerHTML += text[i];
          i++;
          setTimeout(typeWriter, 250);
      }
  }

  window.onload = function () {
      typeWriter();
  };
}
