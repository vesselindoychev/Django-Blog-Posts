console.log('HI DETAILS')
console.log(window.location)


const backBtn = document.getElementById('back-btn');
const editBtn = document.getElementById(`edit-btn`);
const editBtnId = editBtn.getAttribute('itemid');
const spinnerBox = document.getElementById('spinner-box');
const titleInput = document.getElementById('id_title');
const bodyInput = document.getElementById('id_body');
const elTitle = document.getElementById('edit-title').innerText.split(': ')[1];
const elBody = document.getElementById('edit-body').innerText.split(': ')[1];

const url = window.location.href;
const editUrl = `http://127.0.0.1:8000/edit-blog-post-function/${editBtnId}/`;
const deleteUrl = `http://127.0.0.1:8000/delete-blog-post-function/${editBtnId}/`;
const editPostForm = document.getElementById('edit-post-form');
const deletePostForm = document.getElementById('delete-post-form');
const csrf = document.getElementsByName('csrfmiddlewaretoken');
const alertBox = document.getElementById('alert-box');

backBtn.addEventListener('click', (e) => {
    e.preventDefault();
    history.back();
})

$.ajax({
    type: 'GET',
    url: url,
    success: function (response) {
        // console.log(response);
        setTimeout(() => {
            spinnerBox.classList.add('not-visible')
        }, 1000);
        titleInput.value = elTitle;
        bodyInput.value = elBody;
    },
    error: function (error) {
        console.log(error);
    }
})

editPostForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const title = document.getElementById('edit-title');
    const body = document.getElementById('edit-body');

    $.ajax({
        type: 'POST',
        url: editUrl,
        data: {
            'csrfmiddlewaretoken': csrf[0].value,
            'title': titleInput.value,
            'body': bodyInput.value,
        },
        success: function (response) {
            console.log(response);
            $('#editPostModal').modal('hide');
            handleAlerts('success', 'You have successfully edited the blog post!')
            setTimeout(() => {
                alertBox.classList.add('not-visible');
            }, 6000);
            alertBox.classList.remove('not-visible');
            title.textContent = `Title: ${titleInput.value}`;
            body.textContent = `Body: ${bodyInput.value}`;

        },
        error: function (error) {
            console.log(error);
        }
    })
})

deletePostForm.addEventListener('submit', (e) => {
    e.preventDefault();

    $.ajax({
        type: 'POST',
        url: deleteUrl,
        data: {
            'csrfmiddlewaretoken': csrf[0].value,
        },
        success: function (response) {
           window.location.href = 'http://127.0.0.1:8000/blog-posts/'
           localStorage.setItem('title', titleInput.value);
        },
        error: function (error) {
            console.log(error);
        }
    })
})