const homeDiv = Array.from(document.getElementsByClassName('home-wrapper'))[0];
const viewBtn = document.getElementById('view-picture');

const backToHomeDivBtn = Array.from(document.getElementsByClassName('back-to-home-view-btn'))[0];
const backToHomeDiv = document.getElementById('back-to-home-view-div');
const footer = Array.from(document.getElementsByTagName('footer'))[0];

const isHidden = () => homeDiv.classList.contains('home-wrapper--hidden');

homeDiv.addEventListener('transitioned', function () {
    if (isHidden()) {
        // homeDiv.style.display = 'none';
        homeDiv.classList.add('not-visible');
        footer.classList.add('not-visible')
    }
})


viewBtn.addEventListener('click', e => {
    e.preventDefault();
    if (isHidden()) {
        homeDiv.classList.remove('not-visible');
        footer.classList.remove('not-visible')
        setTimeout(() => homeDiv.classList.remove('home-wrapper--hidden'), 0);
        setTimeout(() => footer.classList.remove('home-wrapper--hidden'), 0);
    } else {
        homeDiv.classList.add('home-wrapper--hidden');
        homeDiv.classList.add('not-visible');
        footer.classList.add('home-wrapper--hidden');
        footer.classList.add('not-visible');
        setTimeout(() => backToHomeDiv.hidden = false, 800)
    }
})

backToHomeDivBtn.addEventListener('click', e => {
    e.preventDefault();

    if (isHidden()) {
        homeDiv.classList.remove('not-visible');
        footer.classList.remove('not-visible');
        setTimeout(() => homeDiv.classList.remove('home-wrapper--hidden'), 0);
        setTimeout(() => footer.classList.remove('home-wrapper--hidden'), 0);
    } else {
        homeDiv.classList.add('home-wrapper--hidden');
        homeDiv.classList.add('not-visible');
        footer.classList.add('home-wrapper--hidden');
        footer.classList.add('not-visible');
    }
    backToHomeDiv.hidden = true;

})

