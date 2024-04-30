"use client"

import { useSearchParams, usePathname, useRouter } from 'next/navigation';
import { Badge, badgeVariants } from "@/components/ui/badge"
import { Input } from "../../components/ui/input"
import { Button } from "../../components/ui/button"
import { useState } from "react"

export const BADGES = [
    // Add appropriate badges here
]

interface SearchBarProps {
    setLoadingTrue: () => void;
}

export default function SearchBar({ setLoadingTrue }: SearchBarProps) {

    const searchParams = useSearchParams();
    const pathname = usePathname();
    const { push } = useRouter();
    const params = new URLSearchParams(searchParams);

    const [searchTerm, setSearchTerm] = useState(searchParams.get('query') || '');

    // handles search function, takes in a term and updates the URL, doesn't return anything 
    function handleSearch(term: string) {
        if (term) {
            params.set('query', term);
        } else {
            params.delete('query');
        }
        push(`${pathname}?${params.toString()}`);
        setSearchTerm(term);
        setLoadingTrue();
    }

    return (
        <>
            <h2 className="font-semibold mb-2">Semantic search over every Emergent Ventures winner</h2>
            <p className="mb-4 text-sm">
                <a className="underline" href="https://www.mercatus.org/emergent-ventures">Emergent Ventures</a> is 
            </p>
            <p className="mb-4 text-sm">
                이 사이트는 다다님의 텍스트를 한 곳에 모았습니다. 오른쪽 상단의 Github 링크를 클릭하면 CSV도 찾을 수 있습니다.
            </p>
            <p className="mb-4 text-sm">
                이 검색창은 정확한 키워드를 입력할 필요가 없습니다. 머신러닝 기법인 임베딩을 사용하여 충분히 가까운 매치를 찾습니다.
                여기 몇 가지 시작 제안이 있습니다:
            </p>
            <div className="flex flex-wrap gap-2 mb-4">
                {BADGES.map((badgeText) => (
                    <button
                        key={badgeText}
                        className={`badge ${badgeVariants({ variant: "secondary" })}`}
                        onClick={() => handleSearch(badgeText)}
                    >
                        {badgeText}
                    </button>
                ))}
            </div >
            <div>
                <form onSubmit={(event) => {
                    event.preventDefault;
                    handleSearch(searchTerm);
                }} className="flex">
                    <Input
                        className="flex-1 mr-2"
                        placeholder="Search project descriptions..."
                        name="query"
                        value={searchTerm}
                        onChange={(event: React.ChangeEvent<HTMLInputElement>) => setSearchTerm(event.target.value)}
                    />
                    <Button type="submit">Search</Button>
                </form>
            </div>
        </>
    )
}