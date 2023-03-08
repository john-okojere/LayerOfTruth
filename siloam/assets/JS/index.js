const emailInputField=  document.querySelector('#subscribe-Email');
const emailBtn = document.querySelector('.subscribe');
const emailSignUp = document.querySelector('.email-Sign-Up');
const phoneSignUp = document.querySelector('.PhoneNumber-signUp')
const LocationSignUP = document.querySelector('.Location-Signup');
const btnRegister = document.querySelector('.regsiter-btn');
var checkYes = document.querySelector('.check-yes');
var checkNo = document.querySelector('.check-No');

checkYes.checked = false;
checkYes.value = false;
checkNo.checked = false;
checkNo.value = false;













emailBtn.addEventListener('click',function(){
    
    console.log(emailInputField.value)
})

btnRegister.addEventListener('click', function(){

     console.log(checkYes.value, checkNo.value)
     console.log(emailSignUp.value,phoneSignUp.value,LocationSignUP.value)

})

checkYes.addEventListener('click',function(){
    if(checkYes.checked){
        console.log('Checked')
        checkYes.value = true
        if(checkNo.checked){
            checkNo.checked= false;
            checkNo.value = false
        }
    }
    else{
        console.log('un checked')
        checkYes.value = false
        checkNo.value = false 
    }
    


})

checkNo.addEventListener('click',function(){
    if(checkNo.checked){
        console.log('Checked')
        checkNo.value = true
        if(checkYes.checked){
            checkYes.checked= false;
            checkYes.value = false 
        }
    }
    else{
        console.log('un checked')
        checkNo.value = false    }
    


})

