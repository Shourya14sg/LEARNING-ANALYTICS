import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'
import tailwindcss from '@tailwindcss/vite'
//const flowbite = import("flowbite-react/tailwind");


// https://vite.dev/config/
export default defineConfig({
  plugins: [
    react(),
    tailwindcss({
      
    }),
  ],
})
