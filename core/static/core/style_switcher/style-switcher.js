const svgTemplate2 = `
<svg width="800px" height="800px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M7 8L3 12L7 16" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M17 8L21 12L17 16" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M14 4L9.8589 19.4548" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>`;

function setFavicon() {
    const skinColor = getComputedStyle(document.documentElement).getPropertyValue('--skin-color').trim();
    const svgContent = svgTemplate2.replace(/{color}/g, skinColor);
    const blob = new Blob([svgContent], { type: 'image/svg+xml' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('link');
    link.rel = 'icon';
    link.href = url;
    link.type = 'image/svg+xml';

    const existingIcons = document.querySelectorAll('link[rel="icon"]');
    existingIcons.forEach(icon => icon.parentNode.removeChild(icon));

    document.head.appendChild(link);
}

// toggle style switcher 
const styleSwitcherToggle = document.querySelector('.style-switcher-toggler');
styleSwitcherToggle.addEventListener('click', () => {
    document.querySelector('.style-switcher').classList.toggle('open');
})
// hide style switcher on scroll 
window.addEventListener('scroll', () => {
    if(document.querySelector('.style-switcher').classList.contains('open')) {
        document.querySelector('.style-switcher').classList.remove('open')
    }
})


// theme colors 
const alternateStyles = document.querySelectorAll('.alternate-style');
function setActiveStyle(color) {
    var r = document.querySelector(':root');
    r.style.setProperty('--skin-color', color);
    // alternateStyles.forEach((style) => {
    //     if (color === style.getAttribute('title')) {
    //         style.removeAttribute('disabled');
    //     } else {
    //         style.setAttribute('disabled', 'true');
    //     }
    // })
    setTimeout(() => {
        setFavicon();
    }, 500)
}

// day-night 
const dayNight = document.querySelector('.day-night');
dayNight.addEventListener('click', () => {
    dayNight.querySelector('i').classList.toggle('fa-sun');
    dayNight.querySelector('i').classList.toggle('fa-moon');
    document.body.classList.toggle('dark');
})

window.addEventListener('load', () => {
    if (document.body.classList.contains('dark')) {
        dayNight.querySelector('i').classList.add('fa-sun');
    } else {
        dayNight.querySelector('i').classList.add('fa-moon');

    }
})

// document.body.addEventListener('click', () => {
//     if(document.querySelector('.style-switcher').classList.contains('open')) {
//         document.querySelector('.style-switcher').classList.remove('open')
//     }
// })
