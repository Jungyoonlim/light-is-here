import { type NextRequest, NextResponse } from 'next/server'
import { pipeline } from '@xenova/transformers';

async function getSentiment(query: string){
    let extractor = await pipeline('feature-extraction', 'Xenova/all-Mi');
    let output = await extractor(query, { pooling: 'mean', normalize: true});

    return Array.from(output.data)
}

export async function GET(request: NextRequest){
    const { searchParams } = new URL(request.url)
    const query = searchParams.get('query') || ''
    const sentiment = await getSentiment(query)
    return NextResponse.json({ query: query, message: sentiment }, { status: 200 });
}