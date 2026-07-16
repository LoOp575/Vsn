import { useEffect, useState } from 'react';

export default function Dashboard(){
 const [signals,setSignals]=useState<any[]>([]);
 useEffect(()=>{
  fetch('/signal/scan',{method:'POST'})
   .then(r=>r.json())
   .then(d=>setSignals(d.signals||[]));
 },[]);
 return (<div><h1>VSN Formula Brain</h1><table><thead><tr><th>Symbol</th><th>Action</th><th>Confidence</th></tr></thead><tbody>{signals.map((s,i)=><tr key={i}><td>{s.symbol}</td><td>{s.action}</td><td>{s.confidence}</td></tr>)}</tbody></table></div>);
}