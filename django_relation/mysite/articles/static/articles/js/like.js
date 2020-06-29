const likeButton = document.querySelectorAll('.like-button')
likeButton.forEach(button => { //반복문으로 게시글 갯수따라서 버튼 갯수가 다르기 때문에 
    //console.log(button)
    button.addEventListener('click',function(event){
        //console.log(event)
        const articleId = event.target.dataset.id
        const likeCount = document.querySelector(`#like-count-${articleId}`)

        axios.defaults.xsrfCookieName = 'csrftoken';
        axios.defaults.xsrfHeaderName = 'X-CSRFToken';
        
        axios.post(`/articles/${articleId}/like/`) //urls
        .then(response => {
            //이제 특정한 key, value만으로 값 처리
            console.log(response)
            likeCount.innerHTML =response.data.count
            if(response.data.liked){
                event.target.className = 'fas fa-heart fa-lg like-button'
                event.target.style.color = 'crimson'
            }else{
                event.target.className = 'far fa-heart fa-lg like-button'
                event.target.style.color='black'
            }
        })
    })
})