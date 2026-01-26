import { SignUp } from '@clerk/nextjs';
import Link from 'next/link';
import { Card, CardContent } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Separator } from '@/components/ui/separator';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Create Account | Forumix',
  description:
    'Create a Forumix account to start real-time chats and participate in threaded community discussions.',
  robots: {
    index: false,
    follow: false,
  },
  openGraph: {
    title: 'Create Account | Forumix',
    description:
      'Join Forumix today for fast, organized real-time conversations and community interaction.',
  },
};

export default function SignUpPage() {
  return (
    <main className="flex min-h-[calc(100vh-5rem)] items-center justify-center px-4">
      <div className="w-full max-w-md space-y-8 animate-in fade-in slide-in-from-bottom-4 duration-500">
        <div className="space-y-4 text-center">
          <div className="inline-flex h-16 w-16 items-center justify-center rounded-full bg-primary/10">
            <svg
              className="h-8 w-8 text-primary"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
              strokeWidth={1.5}
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                d="M19 7.5v3m0 0v3m0-3h3m-3 0h-3m-2.25-4.125a3.375 3.375 0 11-6.75 0 3.375 3.375 0 016.75 0zM4 19.235v-.11a6.375 6.375 0 0112.75 0v.109A12.318 12.318 0 0110.374 21c-2.331 0-4.512-.645-6.374-1.766z"
              />
            </svg>
          </div>
          <div className="space-y-2">
            <h1 className="text-3xl font-bold tracking-tight text-foreground">Create Account</h1>
            <p className="text-sm text-muted-foreground">Join us today and start your journey</p>
          </div>
        </div>

        <Card className="border-border/40 bg-card/50 backdrop-blur-sm shadow-lg">
          <CardContent className="p-6">
            <SignUp
              routing="path"
              path="/sign-up"
              signInUrl="/sign-in"
              fallbackRedirectUrl="/"
              appearance={{
                elements: {
                  formButtonPrimary: 'bg-primary hover:bg-primary/90 text-primary-foreground',
                  footerActionLink: 'text-primary hover:text-primary/80',
                  socialButtonsBlockButton: 'border-border hover:bg-accent',
                  formFieldInput: 'border-input focus:border-primary',
                  card: 'shadow-none',
                },
              }}
            />
          </CardContent>
        </Card>

        <div className="space-y-4">
          <div className="relative">
            <Separator className="bg-border/50" />
            <div className="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 bg-background px-3 text-sm text-muted-foreground">
              Already have an account?
            </div>
          </div>

          <Button
            variant="outline"
            className="w-full border-border bg-background hover:bg-accent hover:text-accent-foreground transition-all duration-200"
            asChild
          >
            <Link href="/sign-in">
              Sign In to Your Account
              <svg
                className="ml-2 h-4 w-4"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                strokeWidth={2}
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  d="M15.75 9V5.25A2.25 2.25 0 0013.5 3h-6a2.25 2.25 0 00-2.25 2.25v13.5A2.25 2.25 0 007.5 21h6a2.25 2.25 0 002.25-2.25V15M12 9l-3 3m0 0l3 3m-3-3h12.75"
                />
              </svg>
            </Link>
          </Button>
        </div>

        <div className="text-center">
          <p className="text-xs text-muted-foreground">
            By creating an account, you agree to our{' '}
            <Link href="/terms" className="text-primary hover:text-primary/80 transition-colors">
              Terms of Service
            </Link>{' '}
            and{' '}
            <Link href="/privacy" className="text-primary hover:text-primary/80 transition-colors">
              Privacy Policy
            </Link>
          </p>
        </div>
      </div>
    </main>
  );
}
