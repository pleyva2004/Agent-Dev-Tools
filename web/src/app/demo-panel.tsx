"use client";
import { useState } from "react";
export default function DemoPanel() {
 const [count,setCount]=useState(0);
 const [status,setStatus]=useState("Ready to test the live server.");
 const [busy,setBusy]=useState(false);
 async function check() {setBusy(true);try{const response=await fetch("/api/health",{cache:"no-store"});if(!response.ok)throw new Error("Server unavailable");const data=await response.json();if(data.status!=="ok"||data.service!=="web")throw new Error("Unexpected response");setStatus("Server connected · status: ok · service: web");}catch{setStatus("Could not reach the server. Please try again.");}finally{setBusy(false);}}
 return <section className="card" aria-label="Interactive web demo"><span className="label">Interactive starter</span><div className="value" aria-live="polite">{count}</div><div className="actions"><button onClick={()=>setCount(c=>c+1)}>Increment</button><button className="secondary" onClick={()=>setCount(0)}>Reset</button></div><hr style={{border:0,borderTop:"1px solid #d7ded2",margin:"28px 0"}}/><button onClick={check} disabled={busy}>{busy?"Checking…":"Check server API"}</button><p className="status" role="status">{status}</p></section>;
}
