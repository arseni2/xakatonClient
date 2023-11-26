/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
    colors: {
      primary: "#08a652",
      white: "#FFF",
      primaryHovered: '#148F2B',
      gray: "#F5F6F7",
      borderGray: "rgba(38,38,38,.24)",
      errorBg: "#F8CBCB"
    }
  },
  plugins: [],
}

