let slide = document.getElementsByClassName("dinning_carusel_item");
let counter = document.querySelector('.counter_item')

let currentSlideDin = 0;

function showSlideDin(n) {
  for (let i = 0; i < slide.length; i++) {
    slide[i].style.display = "none";
  }
  if (n < 0) {
    currentSlideDin = slide.length - 1;
  } else if (n >= slide.length) {
    currentSlideDin = 0;
  }
  slide[currentSlideDin].style.display = "flex";
  counter.textContent = currentSlideDin + 1;
}
function plusSlideDin(n) {
  currentSlideDin += n;
  showSlideDin(currentSlideDin);
}
showSlideDin(currentSlideDin);
