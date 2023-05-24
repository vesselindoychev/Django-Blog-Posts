const blogPostBox = document.getElementById('blog-posts-box');
const spinnerBox = document.querySelector('#spinner-box');
const loadBtn = document.querySelector('#load-btn');
const endBox = document.querySelector('#end-box');

const createPostForm = document.getElementById('create-post-form');
const title = document.getElementById('id_title');
const body = document.getElementById('id_body');
const csrf = document.getElementsByName('csrfmiddlewaretoken');

const alertBox = document.getElementById('alert-box');
console.log('csrf', csrf[0].value)
const buttonsList = [];

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

// const likeUnlikePost = () => {
//     const likeUnlikeForm = [...document.getElementsByClassName('like-unlike-form')]
//     likeUnlikeForm.forEach(form => form.addEventListener('submit', e => {
//         e.preventDefault();
//         const clickedId = e.target.getAttribute('data-form-id');
//         const clickedBtn = document.getElementById(`like-unlike-${clickedId}`);
//
//         $.ajax({
//             type: 'POST',
//             url: "/like-unlike-post/",
//             data: {
//                 'csrfmiddlewaretoken': csrftoken,
//                 'pk': clickedId,
//             },
//             success: function (response) {
//                 console.log(response);
//                 clickedBtn.textContent = response.liked ? `Unlike (${response.likes_count})` : `Like (${response.likes_count})`
//             },
//             error: function (error) {
//                 console.log(error)
//             }
//
//         })
//     }))
// }

let visible = 3

const getBlogData = () => {
    $.ajax({
        type: 'GET',
        url: `/blog-data/${visible}/`,
        success: function (response) {
            console.log(response);
            const data = response.data;
            setTimeout(() => {
                spinnerBox.classList.add('not-visible');
                console.log(data);
                data.forEach(el => {
                    blogPostBox.innerHTML += `
                    <div class="card mb-2">
                        <div class="card-body">
                            <h5 class="card-title">${el.title}</h5>
                            <p class="card-text">${el.body}</p>
                        </div>
                        <div class="card-footer">
                            <div class="row">
                                <div class="col-2">
                                    ${el.is_creator ? `<a href="/blog-post-details/${el.id}" class="btn btn-primary">Details</a>` :
                        `<a href="#" class="btn btn-primary">Comment</a>`}
                                </div>
                                <div class="col-2">
                                    <form class="like-unlike-form" data-form-id="${el.id}">
                                        ${el.is_creator ? `<p>${el.likes_count} likes</p>` :
                        `<button id="like-unlike-${el.id}" class="btn btn-primary">${el.liked ? `Unlike (${el.likes_count})` :
                            `Like (${el.likes_count})`}</button>`}
                                    </form>
                                 
                                </div>
                                <div class="col-2">
                                    <button id="extend-details-btn-${el.id}" type="submit" class="btn btn-primary">Show Blog Details</button>
                                    
                                </div>
                            </div>
                            
                            <div class="card-footer-extended-details-${el.id}" hidden="hidden">
                                <p>Details</p>
                            </div>
                        </div>
                    </div>
                `
                });

                <!-- Hide and Show a DIV Box but it's not working properly -->
                // blogPostBox.addEventListener('click', (e) => {
                //     e.preventDefault();
                //     const isButton = e.target.nodeName === 'BUTTON';
                //     if (isButton) {
                //
                //         let btnId = e.target.id.split('-').slice(-1);
                //         const div = document.getElementsByClassName(`card-footer-extended-details-${btnId}`)
                //         let divArray = [...div];
                //         let realDiv;
                //         divArray.forEach(el => {
                //             realDiv = el;
                //         })
                //
                //         if (realDiv.hidden) {
                //             realDiv.removeAttribute('hidden');
                //             // realDiv.style.hidden = ''
                //             e.target.textContent = 'Hide Blog Details';
                //
                //         } else {
                //             realDiv.setAttribute('hidden', true);
                //             e.target.textContent = 'Show Blog Details';
                //         }
                //
                //
                //     }
                // });
                <!-- End of Hide and Show DIV Box -->


                // likeUnlikePost();
            }, 1000);
            console.log(response.size);
            if (response.size === 0) {
                endBox.textContent = 'No posts added...';
                loadBtn.classList.add('not-visible');
            } else if (response.size <= visible) {
                setTimeout(() => {
                    loadBtn.classList.add('not-visible');
                    endBox.textContent = 'No more posts to load...';
                }, 1000);

            }
        },
        error: function (error) {
            console.log(error);
        }
    })
};


getBlogData();

loadBtn.addEventListener('click', () => {
    spinnerBox.classList.remove('not-visible');
    visible += 3;
    getBlogData();
})

createPostForm.addEventListener('submit', e => {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '/blog-posts/',
        data: {
            'csrfmiddlewaretoken': csrf[0].value,
            'title': title.value,
            'body': body.value,
            // 'action': 'post',
        },
        success: function (response) {
            console.log(response)
            blogPostBox.insertAdjacentHTML('afterbegin', `
                    <div class="card mb-2">
                        <div class="card-body">
                            <h5 class="card-title">${response.title}</h5>
                            <p class="card-text">${response.body}</p>
                        </div>
                        <div class="card-footer">
                            <div class="row">
                                <div class="col-2"><a href="/post-details/${response.id}" class="btn btn-primary">Details</a></div>
                                <div class="col-2">
                                    <form class="like-unlike-form" data-form-id="${response.id}">
                                        <p>0 likes</p>
                                    </form>
                                </div>
                            </div>
                            
                        </div>
                    </div>
            `
            );
            $('#addPostModal').modal('hide');
            handleAlerts('success', 'You have successfully created a blog post!');
            createPostForm.reset();
        },
        error: function (error) {
            console.log(error);
            handleAlerts('danger', 'Opps.. Something went wrong')
        }
    })
});