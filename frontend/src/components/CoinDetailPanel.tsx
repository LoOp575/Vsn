import Panel from './layout/Panel';
import Divider from './layout/Divider';
import Badge from './layout/Badge';

type Props={signal?:any};
export default function CoinDetailPanel({signal}:Props){
 if(!signal) return <Panel title='Coin Detail'>Select a coin</Panel>;
 const variant=String(signal.action).match(/BUY|LONG/i)?'success':'warning';
 return <Panel title={signal.symbol}><p>Action: <Badge variant={variant as any}>{signal.action}</Badge></p><Divider/><p>Confidence: {signal.confidence}</p><p>Regime: {signal.regime??'-'}</p><p>Drop Probability: {signal.probability_of_drop??'-'}</p></Panel>;
}