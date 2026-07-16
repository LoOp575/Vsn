import {ReactNode} from 'react';
import {colors} from '../../theme/colors';
import {spacing,radius} from '../../theme/spacing';

type Variant='default'|'success'|'warning'|'danger';
type Props={children:ReactNode;variant?:Variant};
const bg={default:colors.surfaceAlt,success:colors.success,warning:colors.warning,danger:colors.danger};
export default function Badge({children,variant='default'}:Props){return <span style={{display:'inline-block',background:bg[variant],color:colors.text,padding:`${spacing.xs}px ${spacing.sm}px`,borderRadius:radius.md,fontSize:12}}>{children}</span>}