import { Separator } from '@/components/ui/separator';
import { Sparkles } from 'lucide-react';
import Link from 'next/link';

const footerLinks = [
  {
    title: 'Explore Projects',
    href: '/explore',
  },
  {
    title: 'Trending Now',
    href: '/trending',
  },
  {
    title: 'Launch Project',
    href: '/submit',
  },
  {
    title: 'Collections',
    href: '/collections',
  },
  {
    title: 'About Us',
    href: '/about',
  },
  {
    title: 'Careers',
    href: '/careers',
  },
];

const Footer = () => {
  return (
    <footer className="border-t">
      <div className="max-w-screen-2xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="py-8 sm:py-10 md:py-12 flex flex-col justify-start items-center">
          {/* Logo */}
          <div className="flex items-center gap-2 sm:gap-3">
            <div className="size-8 sm:size-9 md:size-10 rounded-lg sm:rounded-xl bg-primary flex items-center justify-center">
              <Sparkles className="size-4 sm:size-5 text-primary-foreground" />
            </div>
            <span className="text-lg sm:text-xl md:text-2xl font-bold tracking-tight">
              <span className="text-primary">Build</span>Board
            </span>
          </div>

          <p className="mt-3 sm:mt-4 text-sm sm:text-base text-muted-foreground max-w-xs sm:max-w-sm md:max-w-md text-center leading-relaxed">
            The premier platform where innovators showcase their creations and discover
            groundbreaking projects from makers worldwide.
          </p>

          <ul className="mt-4 sm:mt-6 flex flex-wrap items-center justify-center gap-2 sm:gap-3 md:gap-4">
            {footerLinks.map(({ title, href }) => (
              <li key={title}>
                <Link
                  href={href}
                  className="text-xs sm:text-sm text-muted-foreground hover:text-foreground transition-colors duration-200 px-1 sm:px-0"
                >
                  {title}
                </Link>
              </li>
            ))}
          </ul>
        </div>
        <Separator />
        <div className="py-6 sm:py-8 flex flex-col sm:flex-row items-center justify-between gap-4 sm:gap-2 px-4 sm:px-6 lg:px-0">
          <span className="text-xs sm:text-sm text-muted-foreground text-center sm:text-left">
            © 2026 BuildBoard. Empowering creators worldwide.
          </span>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
