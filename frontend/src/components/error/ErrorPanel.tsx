import Panel from '../layout/Panel';
import Badge from '../layout/Badge';
import {colors} from '../../theme/colors';

type Props={title?:string;message:string;onReconnect?:()=>void};
export default function ErrorPanel({title='Error',message,onReconnect}:Props){return <Panel title={title}><p style={{color:colors.danger,marginBottom:12}}>{message}</p><Badge variant='danger'>Disconnected</Badge>{onReconnect?<div style={{marginTop:12}}><button onClick={onReconnect}>Reconnect</button></div>:null}</Panel>}