import Card from './layout/Card';
import {typography} from '../theme/typography';
import {colors} from '../theme/colors';

type Props={label:string;value:string|number;hint?:string};
export default function StatCard({label,value,hint}:Props){return <Card><div style={{fontSize:typography.sizes.sm,color:colors.muted}}>{label}</div><div style={{fontSize:typography.sizes.xl,fontWeight:typography.weights.bold}}>{value}</div>{hint?<div style={{fontSize:typography.sizes.xs,color:colors.muted}}>{hint}</div>:null}</Card>}