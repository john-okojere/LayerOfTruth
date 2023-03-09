// require('dotenv').config();
const emailInputField=  document.querySelector('#subscribe-Email');
const emailBtn = document.querySelector('.subscribe');
const emailSignUp = document.querySelector('.email-Sign-Up');
const nameSignUp = document.querySelector('.nameSignUp')
const phoneSignUp = document.querySelector('.PhoneNumber-signUp')
const LocationSignUP = document.querySelector('.Location-Signup');
const btnRegister = document.querySelector('.regsiter-btn');
var checkYes = document.querySelector('.check-yes');
var checkNo = document.querySelector('.check-No');

var checkYesReservation = document.querySelector('.check-yes-reservation');
var checkNoReservation = document.querySelector('.check-No-reservation');

const msgEmailSubscription = document.querySelector('.msgEmailSubscription');
const msgName = document.querySelector('.msgName');
const msgPhone = document.querySelector('.msgPhone')
const msgemail = document.querySelector('.msgemail');
const  msglocation = document.querySelector('.msglocation')





// check first time attending conference
checkYes.checked = false;
checkYes.value = false;

checkNo.checked = false;
checkNo.value = false;

// check reservation
checkYesReservation.checked = false;
checkYesReservation.value = true;

checkNoReservation.checked = false;
checkNoReservation.value = true;












// email validation

emailBtn.addEventListener('click',function(e){
  if(emailInputField.value ===""){
    e.preventDefault();
    msgEmailSubscription.textContent = "email field cannot be left empty"

  }
  


  else if(emailInputField.value !=""){
    var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    var update = emailPattern.test(emailInputField.value);
    if(update ===  false ){
      msgEmailSubscription.textContent = "invalid Email"


    }
   

    
  }

    
    console.log(emailInputField.value)
})


emailInputField.addEventListener('focus',function(){
  msgEmailSubscription.textContent = ""

})



//  form validation


// vaildation for name
nameSignUp.addEventListener('blur',function(){

  if (nameSignUp.value ===""){
    msgName.textContent = "name cannot be left empty"

    
  }
 else if (nameSignUp.value.length  < 3){

    msgName.textContent = "name cannot be less than 3 characters"
  }
})

nameSignUp.addEventListener('focus',function(){
  
  msgName.textContent = ""
})

// validation for phone number

phoneSignUp.addEventListener('blur',function(){

  if (phoneSignUp.value ===""){
    msgPhone.textContent = "phone number is required"

    
  }
 else if (phoneSignUp.value.length  < 7){

  msgPhone.textContent = "invalid phone number"
  }
})

phoneSignUp.addEventListener('focus',function(){
  
  msgPhone.textContent = ""
})


// email vallidation for sign up

emailSignUp.addEventListener('blur',function(){
 var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  var update = emailPattern.test(emailInputField.value);
  if (emailSignUp.value ===""){
   msgemail.textContent = "email cannot be left empty"

    
  }
 
 else  if(update ===  false ){
    msgemail.textContent = "invalid Email"


  }
})
emailSignUp.addEventListener('focus',function(){
  
  msgemail.textContent = ""
})


// location validation for signUp

LocationSignUP.addEventListener('blur',function(){

  if (LocationSignUP.value ===""){
    msglocation.textContent = "please enter location"

    
  }
 else if (LocationSignUP.value.length  < 6){

    msglocation.textContent = "loccation cannot be less than 5 characters"
  }
})

LocationSignUP.addEventListener('focus',function(){
  
  msglocation.textContent = ""
})










btnRegister.addEventListener('click', function(e){
  if (nameSignUp.value ===""){
    msgName.textContent = "name cannot be left empty"
    e.preventDefault()

    
  }
 if (nameSignUp.value.length  < 3){

    msgName.textContent = "name cannot be less than 3 characters"
    e.preventDefault()
  }

 if (phoneSignUp.value ===""){
    msgPhone.textContent = "phone number is required"
    e.preventDefault()

    
  }
 if (phoneSignUp.value.length  < 7){

  msgPhone.textContent = "invalid phone number"
  e.preventDefault()
  }
 if (emailSignUp.value ===""){
    msgemail.textContent = "email cannot be left empty"
    e.preventDefault()
 
     
   }
   if (LocationSignUP.value ===""){
    msglocation.textContent = "please enter location"
    e.preventDefault()

    
  }
 if (LocationSignUP.value.length  < 6){

    msglocation.textContent = "loccation cannot be less than 5 characters"
    e.preventDefault()
  }
  
  else {
    console.log('details uploaded suscessfuly')
  }


})

// check first time attending conference

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



// check reservation 

checkYesReservation.addEventListener('click',function(){
  if(checkYesReservation.checked){
    console.log('checked')
    checkYesReservation.value = true;
    if(checkNoReservation.checked){
      checkNoReservation.checked = false;
      checkNoReservation.value = false;
    }
  }
  else{
    console.log('un checked')
    checkYesReservation.value = false
    checkNoReservation.value = false 

  }
})

checkNoReservation.addEventListener('click',function(){
  if(checkNoReservation.checked){
      console.log('Checked')
      checkNoReservation.value = true
      if(checkYesReservation.checked){
          checkYesReservation.checked= false;
          checkYesReservation.value = false 
      }
  }
  else{
      console.log('un checked')
      checkNoReservation.value = false    }
  


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



