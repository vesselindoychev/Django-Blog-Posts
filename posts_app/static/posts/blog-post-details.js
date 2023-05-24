console.log('HI DETAILS')

const backBtn = document.getElementById('back-btn');
backBtn.addEventListener('click', (e) => {
    e.preventDefault();
    history.back();
})