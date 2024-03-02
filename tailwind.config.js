/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        'primary-dark': '#121113',
        'primary-light': '#FAF7EF',
        'primary': '#4BB3FD',
        'secondary': '#246A73',
        'tertiary': '#E55934',
      },
    },
  },
  plugins: [],
}

