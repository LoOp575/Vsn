type Props={signal?:any};
export default function CoinDetailPanel({signal}:Props){
if(!signal)return <div>Select a coin</div>;
return <div><h2>{signal.symbol}</h2><p>Action: {signal.action}</p><p>Confidence: {signal.confidence}</p><p>Regime: {signal.regime}</p><p>Drop Probability: {signal.probability_of_drop}</p></div>;
}