import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Home | Forumix',
  description:
    'Forumix is a real-time chat and threaded discussion platform built for fast, organized community conversations.',
  openGraph: {
    title: 'Forumix — Real-time Discussions & Community Chat',
    description:
      'A modern platform for real-time chat and threaded discussions with secure authentication.',
  },
};

export default function HomePage() {
  return <div className="flex w-full flex-1 flex-col">Home</div>;
}
