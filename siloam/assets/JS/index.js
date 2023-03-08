const emailInputField=  document.querySelector('#subscribe-Email');
const emailBtn = document.querySelector('.subscribe');

emailBtn.addEventListener('click',function(){
    console.log(emailInputField.value)
})