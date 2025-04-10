import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// Export configuration
export default defineConfig({
  plugins: [react()],
  server: {
    // Set up the proxy to forward API requests to your Flask backend
    proxy: {
      // Assuming your Flask app is running on http://localhost:5000
      '/api': {
        target: 'http://localhost:5000', // Your Flask server's URL
        changeOrigin: true,              // Prevents issues with cross-origin requests
        rewrite: (path) => path.replace(/^\/api/, ''), // Strips `/api` from the request path
      },
    },
    // Configure the dev server port and host (optional)
    port: 5173, // Vite default port (you can change this if needed)
    host: '0.0.0.0', // This ensures Vite can be accessed externally if needed
  },
  build: {
    // This sets the output directory where the production build will be stored
    outDir: 'dist',
    // Customize other build options if needed
  },
});
