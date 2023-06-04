function showContent(contentIndex, clickedItem) {
    const contentElements = document.querySelectorAll('[id^="content-"]');
    contentElements.forEach((element) => {
        element.classList.add('hidden');
    });
    const content = document.getElementById(`content-${contentIndex}`);
    if (content) {
        content.classList.remove('hidden');
    }
    const navItems = document.querySelectorAll('.admin_nav_items');
    navItems.forEach((item) => {
        item.classList.remove('activated');
    });
    clickedItem.classList.add('activated');
}
let menu = document.querySelector('.admin_menu');
menu.addEventListener('click', () => {
    menu.classList.toggle('act');
    document.querySelector('.admin_nav_small').classList.toggle('act');
});