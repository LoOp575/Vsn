import {useState} from 'react';
import {useSignalStream} from '../hooks/useSignalStream';
import SignalTable from '../components/SignalTable';
import LiveStatusCard from '../components/LiveStatusCard';
import CoinDetailPanel from '../components/CoinDetailPanel';

export default function Dashboard(){
 const {signals,connected}=useSignalStream();
 const [selected,setSelected]=useState<any>();
 return (<div><h1>VSN Formula Brain</h1><LiveStatusCard connected={connected} lastUpdate={new Date().toLocaleTimeString()}/><SignalTable signals={signals}/><button onClick={()=>setSelected(signals[0])}>Show First</button><CoinDetailPanel signal={selected}/></div>);
}