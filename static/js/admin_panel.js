let menu = document.querySelector('.admin_menu');
const navSmall = document.querySelector('.admin_nav_small');

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

    localStorage.setItem('selectedNavItem', contentIndex.toString());
}

window.addEventListener('DOMContentLoaded', (event) => {
    const selectedNavItem = localStorage.getItem('selectedNavItem');
    if (selectedNavItem) {
        const clickedItem = document.querySelector(`.admin_nav_items[data-index="${selectedNavItem}"]`);
        if (clickedItem) {
            showContent(parseInt(selectedNavItem), clickedItem);
        }
    }
});


const isMenuActive = localStorage.getItem('menuActive') === 'true';

if (isMenuActive) {
    menu.classList.add('act');
    navSmall.classList.add('act');
}

menu.addEventListener('click', () => {
    menu.classList.toggle('act');
    navSmall.classList.toggle('act');

    const isActive = menu.classList.contains('act');
    localStorage.setItem('menuActive', isActive);
});