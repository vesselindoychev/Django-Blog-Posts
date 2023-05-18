const postBox = document.querySelector('#posts-box');
const spinnerBox = document.querySelector('#spinner-box');
const loadBtn = document.querySelector('#load-btn');
const endBox = document.querySelector('#end-box');

const createPostForm = document.getElementById('create-post-form');
const title = document.getElementById('id_title')
const body = document.getElementById('id_body')
const csrf = document.getElementsByName('csrfmiddlewaretoken');
console.log('csrf', csrf[0].value)
console.log(createPostForm)

const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

const likeUnlikePost = () => {
    const likeUnlikeForm = [...document.getElementsByClassName('like-unlike-form')]
    likeUnlikeForm.forEach(form => form.addEventListener('submit', e => {
        e.preventDefault();
        const clickedId = e.target.getAttribute('data-form-id');
        const clickedBtn = document.getElementById(`like-unlike-${clickedId}`);

        $.ajax({
            type: 'POST',
            url: "/like-unlike-post/",
            data: {
                'csrfmiddlewaretoken': csrftoken,
                'pk': clickedId,
            },
            success: function (response) {
                console.log(response);
                clickedBtn.textContent = response.liked ? `Unlike (${response.likes_count})` : `Like (${response.likes_count})`
            },
            error: function (error) {
                console.log(error)
            }

        })
    }))
}

let visible = 3

const getData = () => {
    $.ajax({
        type: 'GET',
        url: `/data/${visible}/`,
        success: function (response) {
            console.log(response);
            const data = response.data;
            setTimeout(() => {
                spinnerBox.classList.add('not-visible');
                console.log(data);
                data.forEach(el => {
                    postBox.innerHTML += `
                    <div class="card mb-2">
                        <div class="card-body">
                            <h5 class="card-title">${el.title}</h5>
                            <p class="card-text">${el.body}</p>
                        </div>
                        <div class="card-footer">
                            <div class="row">
                                <div class="col-2"><a href="/post-details/${el.id}" class="btn btn-primary">Details</a></div>
                                <div class="col-2">
                                    <form class="like-unlike-form" data-form-id="${el.id}">
                                        ${el.is_creator ? `<p>${el.likes_count} likes</p>` : 
                                        `<button id="like-unlike-${el.id}" class="btn btn-primary">${el.liked ? `Unlike (${el.likes_count})` : 
                                        `Like (${el.likes_count})`}</button>`}
                                    </form>
                                    
                                </div>
                            </div>
                            
                        </div>
                    </div>
                `
                });
                likeUnlikePost();
            }, 1000);
            console.log(response.size);
            if (response.size === 0) {
                endBox.textContent = 'No posts added...';
                loadBtn.classList.add('not-visible');
            } else if (response.size <= visible) {
                setTimeout(() => {
                    loadBtn.classList.add('not-visible');
                    endBox.textContent = 'No more posts to load...' ;
                }, 1000);

            }
        },
        error: function (error) {
            console.log(error);
        }
    })
};


getData();

loadBtn.addEventListener('click', () => {
    spinnerBox.classList.remove('not-visible');
    visible += 3;
    getData();
})

createPostForm.addEventListener('submit', e => {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '',
        data: {
            'csrfmiddlewaretoken': csrf[0].value,
            'title': title.value,
            'body': body.value,
            // 'action': 'post',
        },
        success: function (response) {
            console.log(response)
        },
        error: function (error) {
            console.log(error)
        }
    })
});