const texts = [
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
]


let current_text = texts[0].split('')
let cursor = 0
let spanned_text = null;

function init() {
    let text_el = document.querySelector('#text')
    for ( let letter of current_text ) {
        text_el.innerHTML += '<span>' + letter + '</span>'
    }


    spanned_text = document.querySelectorAll('#text span')
    spanned_text[cursor].classList.add('cursor')
}
window.onkeydown = function(e) {
    if (e.key !== 'Shift' && e.key !== 'Alt' ){
      if ( e.key === spanned_text[cursor].innerText) {
        spanned_text[cursor].classList.add('green')
     } else {
        if(spanned_text[cursor].innerText === ' '){
            spanned_text[cursor].classList.add('background-red')
        } else 
        spanned_text[cursor].classList.add('red')
    }

    if( cursor < spanned_text.length -  1) {
        spanned_text[cursor].classList.remove('cursor')
        spanned_text[cursor + 1].classList.add('cursor')
        cursor +=1

    } else {
        console.log('закончили')
    }
    // console.log('cursor')
    // console.log(spanner_text[cursor].innerText)
}}


window.onload = function() {
    init()
}