// require('dotenv').config();
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













// emailBtn.addEventListener('click',function(){
    
//     console.log(emailInputField.value)
// })

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







// import { initializeApp } from "https://www.gstatic.com/firebasejs/9.16.0/firebase-app.js";
// import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.16.0/firebase-analytics.js";
// import firebaseConfig from "./variable.js"

// const app = initializeApp(firebaseConfig);
// const analytics = getAnalytics(app);
// console.log(firebaseConfig)

// import{getDatabase,set,get,update,remove,ref,child}
// from "https://www.gstatic.com/firebasejs/9.16.0/firebase-database.js";


// const db = getDatabase(); 

// function insertData(){
//     set(ref(db,"newsLetters/"),{
//       EmailSuscribe:emailInputField.value
//     }).then(function(){
//       alert("data uploaded successfully")
//     })
//     .catch(function(err){
//       alert(err.message);
//     })
//   }

//   function findData (){
//     insertData();
//     const dbref = ref(db);
//     get(dbref,"newsLetters/").then(function(response){
//       if(response.exists()){
//         console.log(response.val().EmailSuscribe)

//       }
//     })
//   }

//   emailBtn.addEventListener('click',findData);





