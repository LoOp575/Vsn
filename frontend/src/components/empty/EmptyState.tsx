import Panel from '../layout/Panel';
import {colors} from '../../theme/colors';

type Props={title:string;message:string};
export default function EmptyState({title,message}:Props){return <Panel title={title}><p style={{color:colors.muted}}>{message}</p></Panel>}