import {ReactNode} from 'react';
import {spacing} from '../../theme/spacing';

type Props={children:ReactNode};
export default function Section({children}:Props){return <section style={{display:'flex',flexDirection:'column',gap:spacing.lg,marginBottom:spacing.xl}}>{children}</section>}