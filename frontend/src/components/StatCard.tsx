type Props={label:string;value:string|number;hint?:string};
export default function StatCard({label,value,hint}:Props){
 return <div><div>{label}</div><div>{value}</div>{hint?<div>{hint}</div>:null}</div>;
}