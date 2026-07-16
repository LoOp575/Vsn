import {useEffect,useState} from 'react';

export function useSignalStream(){
 const [signals,setSignals]=useState<any[]>([]);
 const [connected,setConnected]=useState(false);
 const [lastUpdate,setLastUpdate]=useState<string>('');
 useEffect(()=>{
  const ws=new WebSocket(`ws://${location.host}/ws/signal`);
  ws.onopen=()=>setConnected(true);
  ws.onclose=()=>setConnected(false);
  ws.onmessage=(e)=>{
   const data=JSON.parse(e.data);
   setSignals(data.signals??[]);
   setLastUpdate(new Date().toLocaleTimeString());
  };
  return ()=>ws.close();
 },[]);
 return {signals,connected,lastUpdate};
}