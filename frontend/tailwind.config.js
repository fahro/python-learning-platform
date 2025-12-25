/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        python: {
          blue: '#3776ab',
          yellow: '#ffd43b',
        }
      }
    },
  },
  plugins: [],
}
