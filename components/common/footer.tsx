import Link from 'next/link';
import { SparkleIcon } from 'lucide-react';

export default function Footer() {
  return (
    <footer className="border-t bg-muted/20">
      <div className="px-4 py-12 sm:px-6 lg:px-8 max-w-7xl mx-auto">
        <div className="grid grid-cols-1 gap-10 md:gap-8 md:grid-cols-2 lg:grid-cols-5">
          {/* Brand Section */}
          <div className="space-y-5 md:col-span-2 lg:col-span-2">
            <div className="flex items-center gap-3">
              <div className="size-10 rounded-xl bg-primary flex items-center justify-center">
                <SparkleIcon className="size-5 text-primary-foreground" />
              </div>
              <span className="text-xl font-bold tracking-tight">
                <span className="text-primary">Build</span>Board
              </span>
            </div>
            <p className="text-muted-foreground max-w-lg leading-relaxed">
              The premier platform where innovators showcase their creations and discover
              groundbreaking projects from makers worldwide.
            </p>
          </div>

          {/* Product Links */}
          <div>
            <h4 className="mb-5 text-base font-semibold tracking-tight">Discover</h4>
            <ul className="space-y-3.5 text-sm text-muted-foreground">
              <li>
                <Link
                  href="/explore"
                  className="hover:text-foreground transition-colors duration-200 block py-1.5 hover:translate-x-1"
                >
                  Explore Projects
                </Link>
              </li>
              <li>
                <Link
                  href="/trending"
                  className="hover:text-foreground transition-colors duration-200 block py-1.5 hover:translate-x-1"
                >
                  Trending Now
                </Link>
              </li>
              <li>
                <Link
                  href="/submit"
                  className="hover:text-foreground transition-colors duration-200 block py-1.5 hover:translate-x-1"
                >
                  Launch Project
                </Link>
              </li>
              <li>
                <Link
                  href="/collections"
                  className="hover:text-foreground transition-colors duration-200 block py-1.5 hover:translate-x-1"
                >
                  Collections
                </Link>
              </li>
            </ul>
          </div>

          {/* Company Links */}
          <div>
            <h4 className="mb-5 text-base font-semibold tracking-tight">Company</h4>
            <ul className="space-y-3.5 text-sm text-muted-foreground">
              <li>
                <Link
                  href="/about"
                  className="hover:text-foreground transition-colors duration-200 block py-1.5 hover:translate-x-1"
                >
                  About Us
                </Link>
              </li>
              <li>
                <Link
                  href="/contact"
                  className="hover:text-foreground transition-colors duration-200 block py-1.5 hover:translate-x-1"
                >
                  Contact
                </Link>
              </li>
              <li>
                <Link
                  href="/careers"
                  className="hover:text-foreground transition-colors duration-200 block py-1.5 hover:translate-x-1"
                >
                  Careers
                </Link>
              </li>
              <li>
                <Link
                  href="/blog"
                  className="hover:text-foreground transition-colors duration-200 block py-1.5 hover:translate-x-1"
                >
                  Blog
                </Link>
              </li>
            </ul>
          </div>

          {/* Resources Links */}
          <div>
            <h4 className="mb-5 text-base font-semibold tracking-tight">Resources</h4>
            <ul className="space-y-3.5 text-sm text-muted-foreground">
              <li>
                <Link
                  href="/help"
                  className="hover:text-foreground transition-colors duration-200 block py-1.5 hover:translate-x-1"
                >
                  Help Center
                </Link>
              </li>
              <li>
                <Link
                  href="/guidelines"
                  className="hover:text-foreground transition-colors duration-200 block py-1.5 hover:translate-x-1"
                >
                  Community Guidelines
                </Link>
              </li>
              <li>
                <Link
                  href="/privacy"
                  className="hover:text-foreground transition-colors duration-200 block py-1.5 hover:translate-x-1"
                >
                  Privacy Policy
                </Link>
              </li>
              <li>
                <Link
                  href="/api"
                  className="hover:text-foreground transition-colors duration-200 block py-1.5 hover:translate-x-1"
                >
                  API
                </Link>
              </li>
            </ul>
          </div>
        </div>

        {/* Bottom Bar */}
        <div className="mt-12 pt-8 border-t sm:mt-14">
          <div className="flex flex-col gap-6 sm:flex-row sm:items-center sm:justify-between">
            <div className="text-center sm:text-left">
              <span className="text-sm text-muted-foreground">
                © 2026 BuildBoard. Empowering creators worldwide.
              </span>
            </div>
            <div className="flex justify-center gap-8 text-sm text-muted-foreground sm:justify-start">
              <Link
                href="/terms"
                className="hover:text-foreground transition-colors duration-200 py-1.5"
              >
                Terms of Service
              </Link>
              <Link
                href="/cookies"
                className="hover:text-foreground transition-colors duration-200 py-1.5"
              >
                Cookie Policy
              </Link>
              <Link
                href="/status"
                className="hover:text-foreground transition-colors duration-200 py-1.5"
              >
                System Status
              </Link>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
}
