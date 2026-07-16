import Panel from './layout/Panel';
import Badge from './layout/Badge';

type Props={connected:boolean;lastUpdate?:string};
export default function LiveStatusCard({connected,lastUpdate}:Props){
return (<Panel title='Connection'><p>Status: <Badge variant={connected?'success':'danger'}>{connected?'Connected':'Disconnected'}</Badge></p><p>Last update: {lastUpdate??'-'}</p></Panel>);
}