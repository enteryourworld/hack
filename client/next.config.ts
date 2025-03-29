import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
  env: {
    SERVER_URL: process.env.SERVER_URL
  },
  
};

module.exports = {
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: `${nextConfig.env?.SERVER_URL}/api/:path`,
      },
    ];
  },
};

// 'http://localhost:4000/api/:path*'

export default nextConfig;
