import {ReactNode} from 'react';
import Card from './Card';
import {typography} from '../../theme/typography';
import {spacing} from '../../theme/spacing';

type Props={title:string;children:ReactNode};
export default function Panel({title,children}:Props){return <Card><div style={{fontFamily:typography.fontFamily,fontSize:typography.sizes.lg,fontWeight:typography.weights.semibold,marginBottom:spacing.md}}>{title}</div>{children}</Card>}