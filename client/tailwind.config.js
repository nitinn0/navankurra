export default {
  content: ['./index.html', './src/**/*.{js,jsx}'],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#4f46e5',
          light: '#818cf8',
          dark: '#3730a3'
        },
        secondary: {
          DEFAULT: '#ec4899',
          light: '#f472b6',
          dark: '#be185d'
        }
      },
      boxShadow: {
        soft: '0 20px 60px rgba(15, 23, 42, 0.08)'
      },
      backgroundImage: {
        'hero-gradient': "radial-gradient(circle at top right, rgba(79, 70, 229, 0.2), transparent 36%), radial-gradient(circle at bottom left, rgba(236, 72, 153, 0.16), transparent 28%)"
      }
    }
  },
  plugins: []
};
