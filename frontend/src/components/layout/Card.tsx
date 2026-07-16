import {ReactNode} from 'react';
import {colors} from '../../theme/colors';
import {spacing,radius} from '../../theme/spacing';

type Props={children:ReactNode};
export default function Card({children}:Props){return <div style={{background:colors.surface,border:`1px solid ${colors.border}`,borderRadius:radius.lg,padding:spacing.lg}}>{children}</div>}