import Badge from './layout/Badge';
import EmptyState from './empty/EmptyState';
type Signal={symbol:string;action:string;confidence:number};
export default function SignalTable({signals,onSelect}:{signals:Signal[];onSelect?:(signal:Signal)=>void}){
 if(!signals.length) return <EmptyState title='No Signals' message='No live signals are available right now.'/>;
 return <table><thead><tr><th>Symbol</th><th>Action</th><th>Confidence</th></tr></thead><tbody>{signals.map(s=>{const buy=/BUY|LONG/i.test(s.action);return <tr key={s.symbol} onClick={()=>onSelect?.(s)} style={{cursor:'pointer'}}><td>{s.symbol}</td><td><Badge variant={buy?'success':'warning'}>{s.action}</Badge></td><td>{s.confidence.toFixed?.(2)??s.confidence}</td></tr>})}</tbody></table>;
}