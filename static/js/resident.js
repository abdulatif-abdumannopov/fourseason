let slides = document.getElementsByClassName("resident_slide");
let current = 0;
function showSlideRes(n) {
  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  if (n < 0) {
    current = slides.length - 1;
  } else if (n >= slides.length) {
    current = 0;
  }
  slides[current].style.display = "block";
}
function plusSlideRes(n) {
  current += n;
  showSlideRes(current);
}
showSlideRes(current);
