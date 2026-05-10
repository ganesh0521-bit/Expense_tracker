document.addEventListener('DOMContentLoaded', () => {
    const themeSwitch = document.getElementById('theme-switch');
    const htmlElement = document.documentElement;
    const icon = themeSwitch ? themeSwitch.querySelector('i') : null;
    
    // Check saved theme
    const savedTheme = localStorage.getItem('theme') || 'dark';
    setTheme(savedTheme);

    if (themeSwitch) {
        themeSwitch.addEventListener('click', () => {
            const currentTheme = htmlElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            setTheme(newTheme);
        });
    }

    function setTheme(theme) {
        htmlElement.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
        
        if (icon) {
            if (theme === 'dark') {
                icon.className = 'fa-solid fa-sun';
            } else {
                icon.className = 'fa-solid fa-moon';
            }
        }

        // Trigger chart update if chart exists
        if (typeof Chart !== 'undefined') {
            Chart.instances.forEach(chart => {
                if (chart.options.plugins.legend) {
                    chart.options.plugins.legend.labels.color = theme === 'dark' ? '#f8fafc' : '#0f172a';
                }
                chart.update();
            });
        }
    }

    // Auto-dismiss flashes
    const flashes = document.querySelectorAll('.alert');
    flashes.forEach(flash => {
        setTimeout(() => {
            flash.style.opacity = '0';
            flash.style.transform = 'translateY(-10px)';
            setTimeout(() => flash.remove(), 300);
        }, 3000);
    });
});
