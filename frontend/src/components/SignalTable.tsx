type Signal={symbol:string;action:string;confidence:number};
export default function SignalTable({signals,onSelect}:{signals:Signal[];onSelect?:(signal:Signal)=>void}){
return <table><thead><tr><th>Symbol</th><th>Action</th><th>Confidence</th></tr></thead><tbody>{signals.map(s=><tr key={s.symbol} onClick={()=>onSelect?.(s)} style={{cursor:'pointer'}}><td>{s.symbol}</td><td>{s.action}</td><td>{s.confidence.toFixed?.(2) ?? s.confidence}</td></tr>)}</tbody></table>;
}