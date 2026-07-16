import {useMemo,useState} from 'react';
import {useSignalStream} from '../hooks/useSignalStream';
import SignalTable from '../components/SignalTable';
import LiveStatusCard from '../components/LiveStatusCard';
import CoinDetailPanel from '../components/CoinDetailPanel';
import SearchBar from '../components/SearchBar';

export default function Dashboard(){
 const {signals,connected,lastUpdate}=useSignalStream();
 const [selected,setSelected]=useState<any>();
 const [query,setQuery]=useState('');
 const filtered=useMemo(()=>signals.filter(s=>s.symbol?.toLowerCase().includes(query.toLowerCase())),[signals,query]);
 return (<div><h1>VSN Formula Brain</h1><LiveStatusCard connected={connected} lastUpdate={lastUpdate}/><SearchBar value={query} onChange={setQuery}/><SignalTable signals={filtered} onSelect={setSelected}/><CoinDetailPanel signal={selected??filtered[0]}/></div>);
}