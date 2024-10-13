document.addEventListener('DOMContentLoaded', function() {
    // Initialize AOS
    AOS.init({
        duration: 1000,
        once: true,
    });

    // Add smooth scrolling to all links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Change navbar background on scroll
    window.addEventListener('scroll', function() {
        const navbar = document.querySelector('.navbar');
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Parallax effect for hero section
    window.addEventListener('scroll', function() {
        const heroSection = document.querySelector('#hero');
        const scrollPosition = window.pageYOffset;
        heroSection.style.backgroundPositionY = scrollPosition * 0.7 + 'px';
    });

    // Animate featured work items on hover
    const featuredItems = document.querySelectorAll('.featured-item');
    featuredItems.forEach(item => {
        item.addEventListener('mouseenter', function() {
            this.querySelector('.featured-overlay').style.transform = 'translateY(0)';
        });
        item.addEventListener('mouseleave', function() {
            this.querySelector('.featured-overlay').style.transform = 'translateY(100%)';
        });
    });
});