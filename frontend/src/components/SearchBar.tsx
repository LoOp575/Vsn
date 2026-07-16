type Props={value:string;onChange:(v:string)=>void};
export default function SearchBar({value,onChange}:Props){
 return <input type='text' placeholder='Search symbol...' value={value} onChange={e=>onChange(e.target.value)} style={{padding:8,width:'100%',maxWidth:320}}/>;
}