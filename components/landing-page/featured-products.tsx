import { ArrowUpRightIcon, StarIcon } from 'lucide-react';
import SectionHeader from '../common/section-header';
import { Button } from '../ui/button';
import Link from 'next/link';
import ProductCard from '../products/product-card';

export default async function FeaturedProducts() {
  return (
    <section className="py-20 bg-muted/40">
      <div className="wrapper">
        <div className="flex items-center justify-between mb-8">
          <SectionHeader
            title="Featured Today"
            icon={StarIcon}
            description="Top picks from our community this week"
          />
          <Button variant="outline" asChild className="hidden sm:flex">
            <Link href="/explore">
              View All <ArrowUpRightIcon className="size-4" />
            </Link>
          </Button>
        </div>
        <div className="grid-wrapper">
          {featuredProducts.map(product => (
            <ProductCard key={product.id} product={product} />
          ))}
        </div>
      </div>
    </section>
  );
}

export const featuredProducts = [
  {
    id: 'prod_001',
    name: 'DevTool Pro',
    slug: 'devtool-pro',
    description: 'A simple tool to boost developer productivity.',
    voteCount: 42,
    tags: ['developer', 'productivity', 'tool'],
  },
  {
    id: 'prod_002',
    name: 'UI Kit X',
    slug: 'ui-kit-x',
    description: 'Reusable UI components for modern web apps.',
    voteCount: 156,
    tags: ['ui', 'design', 'react'],
  },
  {
    id: 'prod_003',
    name: 'API Monitor',
    slug: 'api-monitor',
    description: 'Monitor and track API uptime and performance.',
    voteCount: 18,
    tags: ['api', 'monitoring'],
  },
];
