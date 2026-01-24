<h1 align="center">Forumix 🗣️</h1>

<p align="center">
  A real-time chat and threaded discussion platform built for fast, organized conversations and meaningful community interaction.
</p>

<div align="center">
  <img src="./client/public/banner.png" alt="Banner" width="900">
</div>

## 🔋 Features

- 💬 **Real-time chat system** for instant messaging and live discussions
- 🧵 **Threaded conversations** to keep discussions organized and easy to follow
- 🔐 **Secure authentication** using Clerk with protected routes
- 🗄️ **Reliable data storage** with PostgreSQL and structured schemas
- ⚡ **Fast and scalable API** built with Express.js
- 🌐 **Modern Next.js frontend** with optimized routing and SSR support
- 🔄 **Live updates** for messages and threads without page refresh
- 🎨 **Responsive UI** with clean, accessible design
- 🧩 **Modular architecture** with clear separation of frontend and backend
- 🚀 **Production-ready setup** with environment-based configuration

## ⚙️ Tech Stack

- **🎨 Frontend**: Next.js, TypeScript, React
- **🛠 Backend**: Node.js, Express.js, TypeScript
- **🗄 Database**: PostgreSQL
- **🔐 Authentication**: Clerk
- **📦 Package Manager**: pnpm
- **🔄 API Communication**: REST API with Axios / Fetch
- **⚡ Real-time**: WebSockets / polling (as implemented)

## 🤸 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/soumadip-dev/Forumix.git
cd Forumix
```

### 2. Backend Setup

```bash
cd server
pnpm install
```

Create a `.env` file in the `server` directory with the following variables:

```env
PORT=8080
NODE_ENV=development
DB_HOST=localhost
DB_PORT=6450
DB_NAME=forumix
DB_USER=postgres
DB_PASSWORD=postgres
CLERK_PUBLISHABLE_KEY=<YOUR_CLERK_PUBLISHABLE_KEY>
CLERK_SECRET_KEY=<YOUR_CLERK_SECRET_KEY>
CLOUDINARY_CLOUD_NAME=<YOUR_CLOUDINARY_CLOUD_NAME>
CLOUDINARY_API_KEY=<YOUR_CLOUDINARY_API_KEY>
CLOUDINARY_API_SECRET=<YOUR_CLOUDINARY_API_SECRET>
FRONTEND_URL=http://localhost:3000
```

### 3. Frontend Setup

```bash
cd ../client
pnpm install
```

Create a `.env.local` file in the `client` directory with the following variables:

```env
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=<YOUR_CLERK_PUBLISHABLE_KEY>
NEXT_PUBLIC_API_URL=http://localhost:8080/api
```

### 4. Run the Application

- **Backend (Terminal 1)**:

```bash
cd server
pnpm run dev
```

- **Frontend (Terminal 2)**:

```bash
cd ../client
pnpm run dev
```
