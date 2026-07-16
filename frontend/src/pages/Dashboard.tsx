import {useMemo,useState} from 'react';
import {useSignalStream} from '../hooks/useSignalStream';
import SignalTable from '../components/SignalTable';
import LiveStatusCard from '../components/LiveStatusCard';
import CoinDetailPanel from '../components/CoinDetailPanel';
import SearchBar from '../components/SearchBar';
import StatCard from '../components/StatCard';

export default function Dashboard(){
 const {signals,connected,lastUpdate}=useSignalStream();
 const [selected,setSelected]=useState<any>();
 const [query,setQuery]=useState('');
 const filtered=useMemo(()=>signals.filter(s=>s.symbol?.toLowerCase().includes(query.toLowerCase())),[signals,query]);
 const bullish=filtered.filter(s=>String(s.action).toUpperCase()==='LONG' || String(s.action).toUpperCase()==='BUY').length;
 const bearish=filtered.filter(s=>String(s.action).toUpperCase()==='SHORT' || String(s.action).toUpperCase()==='SELL').length;
 const top=filtered[0];
 return (<div><header><h1>VSN Formula Brain</h1><p>Live market intelligence for MEXC gainers.</p></header><section><StatCard label='Signals' value={filtered.length} hint='Live scan results'/><StatCard label='Bullish' value={bullish} hint='Long / Buy setups'/><StatCard label='Bearish' value={bearish} hint='Short / Sell setups'/><StatCard label='Top Symbol' value={top?.symbol ?? '-'} hint='Highest ranked result'/></section><LiveStatusCard connected={connected} lastUpdate={lastUpdate}/><SearchBar value={query} onChange={setQuery}/><div><SignalTable signals={filtered} onSelect={setSelected}/><CoinDetailPanel signal={selected??filtered[0]}/></div></div>);
}