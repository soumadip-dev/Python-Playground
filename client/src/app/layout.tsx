import type { Metadata } from 'next';
import { Geist, Geist_Mono } from 'next/font/google';
import './globals.css';
import { ClerkProvider } from '@clerk/nextjs';
import Navbar from '@/components/layout/navbar';

const geistSans = Geist({
  variable: '--font-geist-sans',
  subsets: ['latin'],
});

const geistMono = Geist_Mono({
  variable: '--font-geist-mono',
  subsets: ['latin'],
});

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <ClerkProvider>
      <html lang="en" suppressHydrationWarning>
        <body className={`${geistSans.variable} ${geistMono.variable} antialiased`}>
          <div className="flex min-h-screen flex-col bg-background text-foreground">
            <Navbar />
            <main className="flex flex-1 flex-col">
              <div className="mx-auto flex w-full max-w-6xl  flex-1 flex-col px-4 py-8 md:py-10">
                {children}
              </div>
            </main>
          </div>
        </body>
      </html>
    </ClerkProvider>
  );
}

export const metadata: Metadata = {
  title: {
    default: 'Forumix — Real-time Discussions & Community Chat',
    template: '%s | Forumix',
  },
  description:
    'Forumix is a real-time chat and threaded discussion platform designed for fast, organized conversations and meaningful community interaction.',
  applicationName: 'Forumix',
  keywords: [
    'Forumix',
    'real-time chat',
    'threaded discussions',
    'community platform',
    'Next.js forum',
    'discussion board',
    'live chat app',
    'websocket chat',
  ],
  authors: [{ name: 'Soumadip Majila' }],
  creator: 'Soumadip Majila',
  publisher: 'Forumix',
  metadataBase: new URL('http://localhost:3000'), // replace with production URL later
  openGraph: {
    title: 'Forumix — Real-time Discussions & Community Chat',
    description:
      'A modern platform for real-time chat and threaded discussions with secure authentication and a scalable architecture.',
    type: 'website',
    siteName: 'Forumix',
    images: [
      {
        url: '/banner.png',
        width: 1200,
        height: 630,
        alt: 'Forumix Banner',
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Forumix — Real-time Discussions & Community Chat',
    description:
      'Fast, organized real-time discussions built with Next.js, PostgreSQL, and secure authentication.',
    images: ['/banner.png'],
  },
  icons: {
    icon: '/favicon.ico',
  },
};
