let menu = document.querySelector('.main_menu_box');
menu.addEventListener('click', () => {
    menu.classList.toggle('act');
    document.querySelector('.menu_logo_main').classList.toggle('act');
});