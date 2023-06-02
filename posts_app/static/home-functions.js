const homeDiv = Array.from(document.getElementsByClassName('home-wrapper'))[0];
const viewBtn = document.getElementById('view-picture');

backToHomeDivBtn = Array.from(document.getElementsByClassName('back-to-home-view-btn'))[0];
backToHomeDiv = document.getElementById('back-to-home-view-div');

viewBtn.addEventListener('click', e => {
    e.preventDefault();
    homeDiv.classList.add('not-visible');
    homeDiv.classList.remove('home-wrapper')
    backToHomeDiv.hidden = false
})

backToHomeDivBtn.addEventListener('click', e => {
    e.preventDefault();
    backToHomeDiv.hidden = true;
    homeDiv.classList.remove('not-visible');
    homeDiv.classList.add('home-wrapper');
})

