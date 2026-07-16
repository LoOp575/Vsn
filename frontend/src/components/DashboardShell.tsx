import {ReactNode} from 'react';

export default function DashboardShell({sidebar,header,children}:{sidebar?:ReactNode;header?:ReactNode;children:ReactNode}){
 return <div style={{display:'grid',gridTemplateColumns:'260px 1fr',minHeight:'100vh',background:'#0b1020',color:'#e5e7eb'}}><aside style={{borderRight:'1px solid #1f2937',padding:16}}>{sidebar}</aside><main style={{padding:16}}><div style={{marginBottom:16}}>{header}</div><section>{children}</section></main></div>;
}