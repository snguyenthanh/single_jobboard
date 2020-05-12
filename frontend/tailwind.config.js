/* eslint global-require: 0 */
const defaultTheme = require('tailwindcss/defaultTheme');

module.exports = {
  purge: {
    mode: 'all',
    content: [
      './src/**/*.js',
    ],
  },
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter var', ...defaultTheme.fontFamily.sans],
      },
    },
  },
  variants: {},
  plugins: [require('@tailwindcss/ui')],
};
