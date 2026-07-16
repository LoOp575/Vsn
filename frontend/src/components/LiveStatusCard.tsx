type Props={connected:boolean;lastUpdate?:string};
export default function LiveStatusCard({connected,lastUpdate}:Props){
return (<div><h3>Connection</h3><p>Status: {connected?'Connected':'Disconnected'}</p><p>Last update: {lastUpdate??'-'}</p></div>);
}