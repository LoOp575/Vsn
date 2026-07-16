import {useEffect,useState} from 'react';
export function useSignalStream(){
 const [signals,setSignals]=useState<any[]>([]);
 const [connected,setConnected]=useState(false);
 useEffect(()=>{
  const ws=new WebSocket(`ws://${location.host}/ws/signal`);
  ws.onopen=()=>setConnected(true);
  ws.onclose=()=>setConnected(false);
  ws.onmessage=(e)=>{const data=JSON.parse(e.data);setSignals(data.signals??[])};
  return ()=>ws.close();
 },[]);
 return {signals,connected};
}