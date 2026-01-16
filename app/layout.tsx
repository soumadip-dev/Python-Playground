import type { Metadata } from 'next';
import { Outfit } from 'next/font/google';
import './globals.css';
import Footer from '@/components/common/footer';
import Header from '@/components/common/header';
const outfit = Outfit({
  subsets: ['latin'],
});

export const metadata: Metadata = {
  title: 'BuildBoard',
  description:
    'A community platform for creators to showcase their apps, AI tools, SaaS products, and creative projects. Authentic launches, real builders, genuine feedback.',
  keywords: [
    'BuildBoard',
    'product launch platform',
    'startup community',
    'indie hackers',
    'AI tools',
    'SaaS products',
    'apps showcase',
    'creator platform',
    'tech startups',
    'software projects',
  ],
  authors: [{ name: 'Soumadip Majila' }],
  creator: 'Soumadip Majila',
  publisher: 'Soumadip Majila',
  category: 'Technology',

  alternates: {
    canonical: '/',
  },

  openGraph: {
    title: 'BuildBoard – Discover & Launch Apps, AI Tools, and SaaS',
    description:
      'A community platform for creators to launch and showcase apps, AI tools, SaaS products, and creative projects. Built by real builders, for real feedback.',
    url: '/',
    siteName: 'BuildBoard',
    type: 'website',
    locale: 'en_US',
    images: [
      {
        url: '/og-image.png',
        width: 1200,
        height: 630,
        alt: 'BuildBoard – Launch and Discover Tech Products',
      },
    ],
  },

  twitter: {
    card: 'summary_large_image',
    title: 'BuildBoard – Discover & Launch Apps, AI Tools, and SaaS',
    description:
      'Launch and discover apps, AI tools, SaaS products, and creative projects on BuildBoard. A community for authentic builders and honest feedback.',
    images: ['/og-image.png'],
    creator: '@buildboard',
  },

  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      'max-image-preview': 'large',
      'max-snippet': -1,
      'max-video-preview': -1,
    },
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={`${outfit.className} antialiased`}>
        <Header />
        {children}
        <Footer />
      </body>
    </html>
  );
}
