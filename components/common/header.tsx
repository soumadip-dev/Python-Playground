import {
  CompassIcon,
  HomeIcon,
  LoaderIcon,
  SparkleIcon,
  SparklesIcon,
  UserIcon,
} from 'lucide-react';
import Link from 'next/link';
import { Suspense } from 'react';
import { Button } from '../ui/button';
import { ThemeToggle } from './theme-toggle';

const Logo = () => {
  return (
    <Link href="/" className="flex items-center gap-2 group">
      <div className="size-8 rounded-lg bg-primary flex items-center justify-center">
        <SparkleIcon className="size-4 text-primary-foreground" />
      </div>
      <span className="text-xl font-bold hidden sm:inline">
        <span className="text-primary">Build</span>Board
      </span>
    </Link>
  );
};

export default function Header() {
  const isSignedIn = false;

  return (
    <header className="sticky top-0 z-50 border-b bg-background/95 backdrop-blur supports-backdrop-filter:bg-background/60">
      <div className="wrapper px-4 sm:px-6 md:px-12">
        <div className="flex h-16 items-center justify-between">
          <Logo />

          <nav className="flex items-center gap-1 absolute left-1/2 transform -translate-x-1/2">
            <Link
              href="/"
              className="flex items-center gap-2 px-2 sm:px-3 py-2 text-sm font-medium text-muted-foreground hover:text-foreground transition-colors hover:bg-muted/50"
            >
              <HomeIcon className="size-4" />
              <span className="hidden sm:inline">Home</span>
            </Link>
            <Link
              href="/explore"
              className="flex items-center gap-2 px-2 sm:px-3 py-2 text-sm font-medium text-muted-foreground hover:text-foreground transition-colors hover:bg-muted/50"
            >
              <CompassIcon className="size-4" />
              <span className="hidden sm:inline">Explore</span>
            </Link>
          </nav>

          <div className="flex items-center gap-2 sm:gap-3">
            <Suspense
              fallback={
                <div>
                  <LoaderIcon className="size-4 animate-spin" />
                </div>
              }
            >
              {isSignedIn ? (
                <>
                  <Button asChild size="sm" className="hidden sm:inline-flex">
                    <Link href="/submit">
                      <SparklesIcon className="size-4" />
                      <span className="hidden sm:inline ml-2">Submit Project</span>
                    </Link>
                  </Button>
                  <Button variant="ghost" size="sm">
                    <UserIcon className="size-4" />
                  </Button>
                </>
              ) : (
                <>
                  <Button variant="ghost" size="sm" className="hidden sm:inline-flex">
                    Sign In
                  </Button>
                  <Button size="sm">Sign Up</Button>
                </>
              )}
            </Suspense>
            <ThemeToggle />
          </div>
        </div>
      </div>
    </header>
  );
}
