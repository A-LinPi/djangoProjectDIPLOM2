const menu = document.getElementById('menu');
const active = document.getElementById('active');
const sections = document.querySelectorAll('.section');

let activeSize = menu.querySelector('a').offsetWidth;
active.style.width = `${activeSize}px`;

let indexActiveSection;

// Observer
const observer = new IntersectionObserver(
  (items) => {
    items.forEach((item) => {
      if (item.isIntersecting) {
        indexActiveSection = [...sections].indexOf(item.target);
        active.style.transform = `translateX(${activeSize * indexActiveSection}px)`;
      }
    });
  },
  {
    rootMargin: '-80px 0px 0px 0px',
    threshold: 0.2,
  }
);

// observer.observe(document.getElementById('hero'));
//
// sections.forEach((section) => observer.observe(section));

const onResize = () => {
  activeSize = menu.querySelector('a').offsetWidth;

  active.style.width = `${activeSize}px`;

  active.style.transform = `translateX(${activeSize * indexActiveSection}px)`;
};

window.addEventListener('resize', onResize);
