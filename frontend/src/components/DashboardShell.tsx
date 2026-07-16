import {ReactNode} from 'react';
export default function DashboardShell({sidebar,header,children}:{sidebar?:ReactNode;header?:ReactNode;children:ReactNode}){
return <div style={{display:'grid',gridTemplateColumns:'240px 1fr',minHeight:'100vh'}}><aside>{sidebar}</aside><main><div>{header}</div><section>{children}</section></main></div>;
}