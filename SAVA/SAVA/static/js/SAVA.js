AOS.init();

const showHelpInfo = document.querySelector('.show-contact-help-btn');
const closeHelpInfo = document.querySelector('.help-info-close-btn');


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
        borderRadius: '0px',
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