import { CalendarIcon, RocketIcon } from 'lucide-react';
import SectionHeader from '@/components/common/section-header';
import ProductCard from '@/components/products/product-card';
import EmptyState from '@/components/common/empty-state';
// import { getRecentlyLaunchedProducts } from '@/lib/products/product-select';

export default async function RecentlyLaunchedProducts() {
  // const recentlyLaunchedProducts = await getRecentlyLaunchedProducts();

  return (
    <section className="py-20">
      <div className="wrapper space-y-12">
        <SectionHeader
          title="Recently Launched"
          icon={RocketIcon}
          description="Discover the latest products from our community"
        />

        {recentlyLaunchedProducts.length > 0 ? (
          <div className="grid-wrapper">
            {recentlyLaunchedProducts.map(product => (
              <ProductCard key={product.id} product={product} />
            ))}
          </div>
        ) : (
          <EmptyState
            message="No products launched in the last week. Check back soon for new launches."
            icon={CalendarIcon}
          />
        )}
      </div>
    </section>
  );
}
export const recentlyLaunchedProducts = [
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
