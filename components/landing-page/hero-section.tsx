import { ArrowRightIcon, EyeIcon, RocketIcon, SparklesIcon, UsersIcon } from 'lucide-react';
import { Badge } from '../ui/badge';
import { Button } from '../ui/button';
import Link from 'next/link';
import StatsCard from './stats-card';

export default function HeroSection() {
  return (
    <section className="relative overflow-hidden bg-gradient-to-b from-background via-background to-muted/20">
      <div className="wrapper">
        <div className="flex flex-col items-center justify-center lg:py-28 py-12 md:py-20 text-center">
          <LiveBadge />

          <div className="space-y-4 sm:space-y-6 md:space-y-8 max-w-5xl mx-auto px-4">
            <h1 className="text-3xl sm:text-4xl md:text-5xl lg:text-6xl xl:text-7xl font-bold tracking-tight leading-tight md:leading-tighter">
              Launch, Showcase & <span className="text-primary">Grow Together</span>
            </h1>

            <p className="text-base sm:text-lg md:text-xl text-muted-foreground max-w-2xl mx-auto leading-relaxed px-4">
              Where builders share projects, get meaningful feedback, and find their next
              collaboration. Start growing with a community that supports real progress.
            </p>
          </div>

          <div className="flex flex-col sm:flex-row gap-3 sm:gap-4 mt-8 sm:mt-12 mb-16 sm:mb-20 px-4">
            <Button
              asChild
              size="lg"
              className="text-base px-6 sm:px-8 shadow-lg hover:shadow-xl transition-all duration-300 hover:scale-[1.02] active:scale-[0.98]"
            >
              <Link href="/submit" className="flex items-center justify-center gap-2">
                <SparklesIcon className="size-4 sm:size-5" />
                Launch Your Project
              </Link>
            </Button>
            <Button
              asChild
              size="lg"
              variant="secondary"
              className="text-base px-6 sm:px-8 shadow-lg hover:shadow-xl transition-all duration-300 hover:scale-[1.02] active:scale-[0.98] group"
            >
              <Link href="/explore" className="flex items-center justify-center gap-2">
                Explore Projects
                <ArrowRightIcon className="size-4 sm:size-5 transition-transform duration-300 group-hover:translate-x-1" />
              </Link>
            </Button>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 sm:gap-6 md:gap-8 max-w-4xl w-full px-4">
            {statsData.map((stat, index) => (
              <div
                key={stat.label}
                className="animate-in fade-in slide-in-from-bottom-4"
                style={{ animationDelay: `${index * 100}ms` }}
              >
                <StatsCard {...stat} />
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}

const LiveBadge = () => {
  return (
    <Badge
      variant="outline"
      className="px-3 py-1.5 sm:px-4 sm:py-2 mb-6 sm:mb-8 md:mb-10 text-xs sm:text-sm backdrop-blur-sm border-muted hover:border-primary/50 transition-colors duration-300 group"
    >
      <span className="relative flex h-2 w-2 mr-2">
        <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-primary opacity-75" />
        <span className="relative inline-flex rounded-full h-2 w-2 bg-primary" />
      </span>
      <span className="text-muted-foreground group-hover:text-foreground transition-colors">
        Live Community of Builders & Creators
      </span>
    </Badge>
  );
};

const statsData = [
  {
    icon: RocketIcon,
    value: '2.5K+',
    label: 'Projects Launched',
    description: 'And actively growing',
  },
  {
    icon: UsersIcon,
    value: '10K+',
    label: 'Active Builders',
    hasBorder: true,
    description: 'Collaborating daily',
  },
  {
    icon: EyeIcon,
    value: '50K+',
    label: 'Monthly Reach',
    description: 'Across the community',
  },
];
