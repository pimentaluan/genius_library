function toggleMenu() {
    const aside = document.querySelector('aside');
    const overlay = document.querySelector('.overlay');
    aside.classList.toggle('active');
    overlay.classList.toggle('active');
}

function closeMenu() {
    const aside = document.querySelector('aside');
    const overlay = document.querySelector('.overlay');
    aside.classList.remove('active');
    overlay.classList.remove('active');
}
