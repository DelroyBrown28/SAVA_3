const showServices = document.querySelector('.services-btn');
const showServices2 = document.querySelector('.btn-to-services');
const closeServices = document.querySelector('.close-btn');
const navOpen = document.querySelector('nav-open');


// Stops animation from playing unless refreshed
const tl = new TimelineLite({
    paused: true,
    reversed: true
});

tl.to('.remove-me', 0.3, {
        autoAlpha: 0,
        stagger: 0.1,
    })
    .to('.services-section', 0.3, {
        autoAlpha: 1,
    })


// Button to toggle animation
showServices.addEventListener('click', () => {

    if (tl.isActive()) {
        e.preventDefault();
        e.stopImmediatePropagation();
        return false;
    }
    toggleTween(tl)
})
showServices2.addEventListener('click', () => {

    if (tl.isActive()) {
        e.preventDefault();
        e.stopImmediatePropagation();
        return false;
    }
    toggleTween(tl)
})


closeServices.addEventListener('click', () => {

    if (tl.isActive()) {
        e.preventDefault();
        e.stopImmediatePropagation();
        return false;
    }
    toggleTween(tl)
})

function toggleTween(tween) {
    tween.reversed() ? tween.play() : tween.reverse();
}