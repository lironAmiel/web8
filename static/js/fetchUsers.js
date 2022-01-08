console.log('instide fetch');

function getUsers(){
    fetch('https://reqres.in/api/users/1')
        .then(
        response => response.json()
    ).then(
        responseObj => putUsersInHtml(responseObj.data)
    ).catch(
        err => console.log(err)
    )
}
function putUsersInHtml(data){
    console.log(data);
    const currMain = document.querySelector("main")

    const section = document.createElement('section')
    section.innerHTML=`
    <img src="${data.avatar}" alt="profile pic"/>
    <div>
        <span> ${data.first_name} ${data.last_name}</span>
            <br>
            <a href="mailto:${data.email}">Send email</a>
    </div>
    `;
    currMain.appendChild(section);

}