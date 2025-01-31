/** @type {import('tailwindcss').Config} */
export default {
    content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
    theme: {
        extend: {
            colors: {
                'old-paper': '#f5f5dc', // Light yellow resembling old paper
            },
            fontFamily: {
                'old-font': ['Times New Roman', 'serif'], // Old-style font
            },
        },
    },
    plugins: [],
};
