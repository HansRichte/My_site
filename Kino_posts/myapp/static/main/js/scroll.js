const scrollLeftBtn = document.querySelector('.scroll-left');
const scrollRightBtn = document.querySelector('.scroll-right');
const postsContainer = document.querySelector('.posts-container');

scrollLeftBtn.addEventListener('click', scrollLeft);
scrollRightBtn.addEventListener('click', scrollRight);

function scrollLeft() {
    postsContainer.scrollLeft -= 250; // Прокрутка влево на ширину блока posts + отступы
}

function scrollRight() {
    postsContainer.scrollLeft += 250; // Прокрутка вправо на ширину блока posts + отступы
}
