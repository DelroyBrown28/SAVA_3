$(document).ready(function () {
    $('.sidenav').sidenav();
    $('.tooltipped').tooltip();
})

AOS.init();


const showHelpInfo = document.querySelector('.show-contact-help-btn');
const closeHelpInfo = document.querySelector('.help-modal-close-btn');


// Stops animation from playing unless refreshed
const newtl = new TimelineLite({
    paused: true,
    reversed: true
});

newtl.to('.contact-help-info-modal', 0.3, {
        autoAlpha: 1,
        height: '100%',
        width: '65%',
        top: '0px',
    })
    .to('.content-info-blurb, .contact-info-help-list, .question-mark', 0.3, {
        delay: 0.3,
        autoAlpha: 1,
    })
    .to('.help-modal-close-btn', 0.3, {
        // delay: 0.2,
        autoAlpha: 1,

    })


// Button to close services sectio
showHelpInfo.addEventListener('click', () => {

    if (newtl.isActive()) {
        e.preventDefault();
        e.stopImmediatePropagation();
        return false;
    }
    toggleTween(newtl)
})



closeHelpInfo.addEventListener('click', () => {

    if (newtl.isActive()) {
        e.preventDefault();
        e.stopImmediatePropagation();
        return false;
    }
    toggleTween(newtl)
})


function toggleTween(tween) {
    tween.reversed() ? tween.play() : tween.reverse();
}