import { SignIn } from '@clerk/nextjs';
import Link from 'next/link';
import { Card, CardContent } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Separator } from '@/components/ui/separator';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Sign In | Forumix',
  description:
    'Sign in to Forumix to join real-time conversations and participate in threaded discussions.',
  robots: {
    index: false,
    follow: false,
  },
  openGraph: {
    title: 'Sign In | Forumix',
    description:
      'Access your Forumix account to chat in real time and engage in organized discussions.',
  },
};

export default function SignInPage() {
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
                d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z"
              />
            </svg>
          </div>
          <div className="space-y-2">
            <h1 className="text-3xl font-bold tracking-tight text-foreground">Welcome Back</h1>
            <p className="text-sm text-muted-foreground">
              Enter your credentials to access your account
            </p>
          </div>
        </div>

        <Card className="border-border/40 bg-card/50 backdrop-blur-sm shadow-lg">
          <CardContent className="p-6">
            <SignIn
              routing="path"
              path="/sign-in"
              signUpUrl="/sign-up"
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
              Don't have an account?
            </div>
          </div>

          <Button
            variant="outline"
            className="w-full border-border bg-background hover:bg-accent hover:text-accent-foreground transition-all duration-200"
            asChild
          >
            <Link href="/sign-up">
              Create New Account
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
                  d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z"
                />
              </svg>
            </Link>
          </Button>
        </div>

        <div className="text-center">
          <Link
            href="/help"
            className="text-xs text-muted-foreground hover:text-foreground transition-colors inline-flex items-center gap-1"
          >
            <svg
              className="h-3 w-3"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
              strokeWidth={1.5}
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                d="M9.879 7.519c1.171-1.025 3.071-1.025 4.242 0 1.172 1.025 1.172 2.687 0 3.712-.203.179-.43.326-.67.442-.745.361-1.45.999-1.45 1.827v.75M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-9 5.25h.008v.008H12v-.008z"
              />
            </svg>
            Need help signing in?
          </Link>
        </div>
      </div>
    </main>
  );
}
