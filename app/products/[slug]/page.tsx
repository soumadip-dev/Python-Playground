'use cache';

import SectionHeader from '@/components/common/section-header';
import VotingButtons from '@/components/products/voting-buttons';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { getFeaturedProducts } from '@/lib/products/product-select';
import { ArrowLeftIcon, CalendarIcon, ExternalLinkIcon, StarIcon, UserIcon } from 'lucide-react';
import Link from 'next/link';
import { notFound } from 'next/navigation';



export default async function ProductPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  return (
    <div>
      <h1>Product Page {slug}</h1>
    </div>
  );
}
export const generateStaticParams = async () => {
  const products = await getFeaturedProducts();
  return products.map(product => ({
    slug: product.slug.toString(),
  }));
};