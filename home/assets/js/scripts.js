const tab1 = document.getElementById('tab1');
const tab2 = document.getElementById('tab2');
const content1 = document.getElementById('content1');
const content2 = document.getElementById('content2');

content2.style.display = "none";
tab1.classList.add('active')

function opentab1() {
    content1.style.display = "contents"
    content2.style.display = "none"
    tab1.classList.add('active')
    tab2.classList.remove('active')

}

function opentab2() {
    content1.style.display = "none"
    content2.style.display = "contents"
    tab2.classList.add('active')
    tab1.classList.remove('active')
}