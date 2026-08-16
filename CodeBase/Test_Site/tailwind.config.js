const Animatedcss = require('animated/lib/Animated')

const Animatecss('animated-tailwindcss')



/** @type {import('tailwindcss').Config} */
module.exports = Animatedcss( {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [],
}

)

