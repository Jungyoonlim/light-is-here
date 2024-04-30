export default function Footer(){
    return (
        <>
            <p className="mb-4">Project by <a className="underline" href="https://limjungyoon.com">Jungyoon Lim</a>; design / project inspired by <a className="underline" href="https://github.com/nqureshi/ev-winners/">Nabeel Quershi&lsquo;s</a> and <a className="underline" href="https://thesephist.com">Linus Lee&lsquo;s</a> project, <a className="underline" href="https://www.evwinners.org/">EV Winners</a> and <a className="underline" href="https://ycvibecheck.com/">YC Vibe Check</a>.</p>
            <p className="mb-4">Written in <a className="underline" href="https://nextjs.org/">next.js</a>, with semantic search thanks to <a className="underline" href="https://huggingface.co/docs/transformers.js/index">transformers.js</a> and <a className="underline" href="https://www.sbert.net/">sentence-transformers</a>. The model is <a href="https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2" className="underline">all-MiniLM-L6-v2</a>.</p>
            <p className="mb-4">Data by Dada from <a className="underline" href="https://cafe.naver.com/herecamelight/5056">Here Came Light Cafe.</a></p>
            <p className="mb-4">Last updated April 2024.</p>
        </>
    )
}