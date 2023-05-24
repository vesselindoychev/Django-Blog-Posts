console.log('HI DETAILS')

const backBtn = document.getElementById('back-btn');
const editBtn = document.getElementById(`edit-btn`);
const editBtnId = editBtn.getAttribute('itemid');
const spinnerBox = document.getElementById('spinner-box');

console.log(editBtnId);
console.log(window.location.href + 'data/')

backBtn.addEventListener('click', (e) => {
    e.preventDefault();
    history.back();
})

$.ajax({
    type: 'GET',
    url: `/blog-post-details/${editBtnId}/`,
    success: function (response) {
        // console.log(response);
        setTimeout(() => {
            spinnerBox.classList.add('not-visible')
        }, 1000);
    },
    error: function (error) {
        console.log(error);
    }
})