const postBox = document.querySelector('#posts-box');
const spinnerBox = document.querySelector('#spinner-box');
const loadBtn = document.querySelector('#load-btn');
const endBox = document.querySelector('#end-box');
// $.ajax({
//     type: 'GET',
//     url: '/hello-world/',
//     success: function (response) {
//         console.log('success', response);
//         helloWorldBox.textContent = response.text;
//     },
//     error: function (error) {
//         console.log('error', error)
//     }
// })

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
                                <div class="col-2"><a href="/post-details/${el.id}" class="btn btn-primary">${el.liked ? `Unlike (${el.likes_count})` : 
                        `Like (${el.likes_count})`}</a>
                                </div>
                            </div>
                            
                        </div>
                    </div>
                `
                });
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