type Props={title:string;subtitle?:string;status:string;lastUpdate?:string};
export default function Topbar({title,subtitle,status,lastUpdate}:Props){
 return <div><div>{title}</div><div>{subtitle}</div><div>{status}</div><div>{lastUpdate??'-'}</div></div>;
}