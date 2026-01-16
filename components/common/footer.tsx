import Link from 'next/link';
import { SparkleIcon } from 'lucide-react';

export default function Footer() {
  return (
    <footer className="border-t bg-muted/20">
      <div className="px-4 py-8 sm:px-6 lg:px-8 max-w-7xl mx-auto">
        <div className="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-4">
          <div className="space-y-4 md:col-span-1 lg:col-span-2">
            <div className="flex items-center gap-2">
              <div className="size-8 rounded-lg bg-primary flex items-center justify-center">
                <SparkleIcon className="size-4 text-primary-foreground" />
              </div>
              <span className="text-lg font-bold">
                <span className="text-primary">Build</span>Board
              </span>
            </div>
            <p className="text-sm text-muted-foreground max-w-md">
              A community platform where creators share what they&apos;ve built and discover new
              launches.
            </p>
          </div>

          <div className="mt-4 md:mt-0">
            <h4 className="mb-4 text-sm font-semibold">Product</h4>
            <ul className="space-y-3 text-sm text-muted-foreground">
              <li>
                <Link
                  href="/explore"
                  className="hover:text-foreground transition-colors block py-1"
                >
                  Explore
                </Link>
              </li>
              <li>
                <Link
                  href="/trending"
                  className="hover:text-foreground transition-colors block py-1"
                >
                  Trending
                </Link>
              </li>
              <li>
                <Link href="/submit" className="hover:text-foreground transition-colors block py-1">
                  Submit Project
                </Link>
              </li>
            </ul>
          </div>

          <div className="mt-4 md:mt-0">
            <h4 className="mb-4 text-sm font-semibold">Company</h4>
            <ul className="space-y-3 text-sm text-muted-foreground">
              <li>
                <Link href="/about" className="hover:text-foreground transition-colors block py-1">
                  About
                </Link>
              </li>
              <li>
                <Link
                  href="/contact"
                  className="hover:text-foreground transition-colors block py-1"
                >
                  Contact
                </Link>
              </li>
              <li>
                <Link
                  href="/privacy"
                  className="hover:text-foreground transition-colors block py-1"
                >
                  Privacy
                </Link>
              </li>
            </ul>
          </div>
        </div>

        <div className="mt-8 pt-6 border-t sm:mt-10">
          <div className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
            <span className="text-sm text-muted-foreground text-center sm:text-left">
              © 2026 BuildBoard. All rights reserved.
            </span>
            <div className="flex justify-center gap-6 text-sm text-muted-foreground sm:justify-start">
              <Link href="/terms" className="hover:text-foreground transition-colors py-1">
                Terms
              </Link>
              <Link href="/cookies" className="hover:text-foreground transition-colors py-1">
                Cookies
              </Link>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
}
