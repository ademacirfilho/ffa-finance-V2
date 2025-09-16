tailwind.config = {
    theme: {
        extend: {
            fontFamily: {
                sans: ['Inter', 'sans-serif'],
            },
            colors: {
                'brand-dark': '#0A1432', // Fundo principal mais escuro
                'brand-medium': '#202841', // Fundo dos cards e tabelas
                'brand-light': '#3A3C4A', // Borda e elementos sutis
                'brand-accent': '#3B82F6', // Azul para o item de menu ativo
                'brand-text-primary': '#C5CCE0',
                'brand-text-secondary': '#6B79A3'
            }
        }
    }
}

const btn = document.getElementById('menu-btn')
const menu = document.getElementById('mobile-menu')

btn.addEventListener('click', () => {
    menu.classList.toggle('hidden')
})