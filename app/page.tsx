import HeroSection from '@/components/landing-page/hero-section';
import FeaturedProducts from '@/components/landing-page/featured-products';
import { Suspense } from 'react';
import RecentlyLaunchedProducts from '@/components/landing-page/recently-launched-products';
import ProductSkeleton from '@/components/products/product-skeleton';
export default function Home() {
  return (
    <div>
      <HeroSection />
      <FeaturedProducts />
      <Suspense fallback={<ProductSkeleton />}>
        <RecentlyLaunchedProducts />
      </Suspense>
    </div>
  );
}
