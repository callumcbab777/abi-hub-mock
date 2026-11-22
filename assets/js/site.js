/* ABI Group hub — MOCK interactions only. No backend, nothing is sent or stored beyond this browser. */
(function(){
const $=(s,r=document)=>r.querySelector(s), $$=(s,r=document)=>[...r.querySelectorAll(s)];
const CAL='https://calendly.com/callum-ambarorlando/30min';
const toast=(t)=>{let el=$('.toast');if(!el){el=document.createElement('div');el.className='toast';document.body.appendChild(el)}el.textContent=t;el.classList.add('show');clearTimeout(el._t);el._t=setTimeout(()=>el.classList.remove('show'),3200)};
window.abiToast=toast;

/* Mobile drawer + More menu */
const burger=$('.burger'),drawer=$('.drawer');
burger&&burger.addEventListener('click',()=>{const o=drawer.classList.toggle('open');burger.setAttribute('aria-expanded',o)});
$$('.nav .more>button').forEach(b=>b.addEventListener('click',()=>b.parentElement.classList.toggle('open')));
document.addEventListener('click',e=>{$$('.nav .more.open').forEach(m=>{if(!m.contains(e.target))m.classList.remove('open')})});

/* Currency toggle — EXAMPLE rates for the mock only (a live feed with a rate date replaces this) */
const RATES={USD:1,GBP:0.79,CAD:1.38}, SYM={USD:'$',GBP:'£',CAD:'C$'};
function setCcy(c){
  try{localStorage.setItem('abi-ccy',c)}catch(e){}
  $$('.ccy button').forEach(b=>b.setAttribute('aria-pressed',b.dataset.c===c));
  $$('[data-usd]').forEach(el=>{el.textContent=SYM[c]+(Math.round(+el.dataset.usd*RATES[c]/1000)*1000).toLocaleString('en-US')});
  $$('.ccy-note').forEach(el=>{el.innerHTML=c==='USD'?'Prices shown in USD. Example conversion rates for this mock only: 1 USD = 0.79 GBP / 1.38 CAD &middot; rate date <span class="placeholder">[live feed date]</span>':'Shown in '+c+' using an <b>example</b> rate (1 USD = '+RATES[c]+' '+c+') for this mock only &middot; rate date <span class="placeholder">[live feed date]</span>. USD is the contract currency.'});
}
$$('.ccy button').forEach(b=>b.addEventListener('click',()=>{setCcy(b.dataset.c);toast('Currency set to '+b.dataset.c+' (example rate — mock)')}));
let saved='USD';try{saved=localStorage.getItem('abi-ccy')||'USD'}catch(e){}
setCcy(saved);

/* Side navigation scrollspy */
const side=$('.sidenav');
if(side){const links=$$('a',side),secs=links.map(a=>$(a.getAttribute('href'))).filter(Boolean);
  const io=new IntersectionObserver(es=>{es.forEach(e=>{if(e.isIntersecting){links.forEach(l=>l.classList.toggle('on',l.getAttribute('href')==='#'+e.target.id))}})},{rootMargin:'-30% 0px -60% 0px'});
  secs.forEach(s=>io.observe(s));}

/* Buyer account modal (mock) */
const modal=$('#account');
$$('[data-open-account]').forEach(b=>b.addEventListener('click',e=>{e.preventDefault();modal.classList.add('open')}));
modal&&modal.addEventListener('click',e=>{if(e.target===modal||e.target.classList.contains('x'))modal.classList.remove('open')});
$$('.tabs').forEach(t=>{$$('button',t).forEach(b=>b.addEventListener('click',()=>{$$('button',t).forEach(x=>x.setAttribute('aria-selected',x===b));const host=t.parentElement;$$('[data-tab]',host).forEach(p=>p.hidden=p.dataset.tab!==b.dataset.t)}))});

/* Forms: visual only */
$$('form[data-mock]').forEach(f=>{const cap=$('.captured',f);if(cap)cap.innerHTML='Captured with enquiry (mock): <b>source</b> = '+(f.dataset.source||'site form')+' &middot; <b>page</b> = '+document.title.split('|')[0].trim();
  f.addEventListener('submit',e=>{e.preventDefault();toast('Mock form — nothing was sent. In the build this creates a CRM record.')})});
$$('[data-save]').forEach(b=>b.addEventListener('click',e=>{e.preventDefault();b.textContent='Saved ✓';toast('Saved to your buyer account (mock)')}));

/* Route chooser chips etc. */
$$('[data-chipgroup]').forEach(g=>{$$('.chip',g).forEach(c=>c.addEventListener('click',()=>{$$('.chip',g).forEach(x=>x.setAttribute('aria-pressed',x===c));const tgt=g.dataset.chipgroup;if(tgt){$$('[data-route]').forEach(p=>p.hidden=p.dataset.route!==c.dataset.v)}}))});

/* Mock notes toggle */
const badge=$('.phase-badge'),notes=$('.mocknotes');
badge&&badge.addEventListener('click',()=>{const o=notes.classList.toggle('open');document.body.classList.toggle('show-notes',o)});
document.addEventListener('keydown',e=>{if(e.key==='n'&&e.altKey){badge&&badge.click()}});

/* Floor plan viewer (sample) */
$$('.fp').forEach(fp=>{const btns=$$('.list button',fp),view=$('.view',fp);
  function draw(b){btns.forEach(x=>x.setAttribute('aria-selected',x===b));const beds=+b.dataset.beds;const W=600,H=380;let rooms='';
    const wall='stroke="#0F1D35" stroke-width="3" fill="none"', thin='stroke="#0F1D35" stroke-width="1.2" fill="none"';
    rooms+=`<rect x="20" y="20" width="${W-40}" height="${H-40}" ${wall}/>`;
    const n=Math.max(1,beds),bw=(W-40)*0.42/n;
    if(beds===0){rooms+=`<line x1="${W*0.62}" y1="20" x2="${W*0.62}" y2="${H*0.55}" ${thin}/><text x="${W*0.3}" y="${H*0.5}" class="rl">Living / sleeping</text><text x="${W*0.78}" y="${H*0.3}" class="rl">Bath</text><text x="${W*0.78}" y="${H*0.78}" class="rl">Kitchen</text>`}
    else{for(let i=0;i<n;i++){const x=20+(W-40)*0.58+i*bw;rooms+=`<rect x="${x}" y="20" width="${bw}" height="${H*0.55}" ${thin}/><text x="${x+bw/2}" y="${H*0.32}" class="rl">Bed ${i+1}</text>`}
      rooms+=`<line x1="20" y1="${H*0.62}" x2="${W*0.55}" y2="${H*0.62}" ${thin}/><text x="${W*0.3}" y="${H*0.36}" class="rl">Living</text><text x="${W*0.3}" y="${H*0.8}" class="rl">Kitchen / dining</text><text x="${W*0.78}" y="${H*0.82}" class="rl">Bath</text>`}
    rooms+=`<rect x="20" y="${H-26}" width="${W*0.4}" height="6" fill="#C4A35A"/><text x="${W-30}" y="${H-28}" text-anchor="end" class="rs">SCHEMATIC — NOT AN ACTUAL PLAN</text>`;
    $('.plan',view).innerHTML=`<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="Schematic plan"><style>.rl{font:600 11px Montserrat,sans-serif;letter-spacing:.14em;text-transform:uppercase;fill:#6B5C4E;text-anchor:middle}.rs{font:500 9px Montserrat,sans-serif;letter-spacing:.18em;fill:#6B5C4E}</style>${rooms}</svg>`;
    $('.pname',view).textContent=b.dataset.name;$('.pmeta',view).innerHTML=b.dataset.meta;}
  btns.forEach(b=>b.addEventListener('click',()=>draw(b)));btns[0]&&draw(btns[0]);});

/* 3D availability viewer (SAMPLE DATA — not live) */
$$('.av').forEach(av=>{const LV=11,PER=12,scene=$('.scene',av),levels=$('.levels',av),panel=$('.unitpanel',av);
  let seed=7;const rnd=()=>(seed=(seed*9301+49297)%233280)/233280;
  const plans=['Studio','Studio','1 bed','1 bed','1 bed','2 bed','2 bed','2 bed','3 bed'];
  const units=[];for(let l=1;l<=LV;l++)for(let u=1;u<=PER;u++)units.push({l,u,st:'s',plan:plans[(u+l)%9],price:0});
  // exactly 35 available, some reserved, rest sold — illustrative only
  const idx=[...units.keys()].sort(()=>rnd()-.5);idx.slice(0,35).forEach(i=>units[i].st='a');idx.slice(35,52).forEach(i=>units[i].st='r');
  units.forEach(x=>{const base={'Studio':300000,'1 bed':380000,'2 bed':480000,'3 bed':600000}[x.plan];x.price=base+x.l*4000});
  scene.innerHTML='';for(let l=LV;l>=1;l--){const f=document.createElement('div');f.className='floor';f.dataset.l=l;f.style.top=((LV-l)*36+10)+'px';
    units.filter(x=>x.l===l).forEach(x=>{const b=document.createElement('button');b.className='unit '+x.st;b.title='Residence '+l+String(x.u).padStart(2,'0');b.onclick=()=>show(x,b);f.appendChild(b)});scene.appendChild(f)}
  levels.innerHTML='<button class="on" data-l="all"><span>ALL LEVELS</span><span>35</span></button>'+Array.from({length:LV},(_,i)=>LV-i).map(l=>`<button data-l="${l}"><span>LEVEL ${l}</span><span>${units.filter(x=>x.l===l&&x.st==='a').length}</span></button>`).join('');
  $$('button',levels).forEach(b=>b.onclick=()=>{$$('button',levels).forEach(x=>x.classList.toggle('on',x===b));$$('.floor',scene).forEach(f=>{const on=b.dataset.l==='all'||f.dataset.l===b.dataset.l;f.classList.toggle('dim',!on);f.classList.toggle('lift',on&&b.dataset.l!=='all')})});
  let ry=-28,rx=8,z=1;const apply=()=>scene.style.transform=`rotateX(${rx}deg) rotateY(${ry}deg) scale(${z})`;apply();
  $$('.ctrl button',av).forEach(b=>b.onclick=()=>{const a=b.dataset.a;if(a==='l')ry-=15;if(a==='r')ry+=15;if(a==='in')z=Math.min(1.6,z+.15);if(a==='out')z=Math.max(.6,z-.15);if(a==='reset'){ry=-28;rx=8;z=1}apply()});
  const ST={a:'Available',r:'Reserved',s:'Sold'};
  function show(x,b){$$('.unit.sel',scene).forEach(u=>u.classList.remove('sel'));b.classList.add('sel');
    panel.innerHTML=`<span class="label" style="color:#C4A35A">Sample data</span><h3 style="margin-top:10px">Residence ${x.l}${String(x.u).padStart(2,'0')}</h3><dl><dt>Status</dt><dd>${ST[x.st]}</dd><dt>Level</dt><dd>${x.l}</dd><dt>Plan type</dt><dd>${x.plan}</dd><dt>Size</dt><dd><span class="placeholder">[sq ft]</span></dd><dt>Price</dt><dd>${x.st==='s'?'—':'<span class="ccy-price" data-usd="'+x.price+'"></span>'}</dd></dl>${x.st==='a'?'<div class="btn-row"><a class="btn light small" href="#" data-save>Save residence</a><a class="btn ghost small" style="color:#F2E8DC;border-color:#F2E8DC55" href="contact.html">Enquire</a></div>':'<p style="font-size:14px;color:#a9b0c0">This residence is not available. Register interest to hear about similar homes.</p>'}<p style="font-size:12px;color:#8f97a8;margin-top:18px;font-family:Inter,sans-serif">Illustrative prices and statuses generated for the mock. Live Building 1 availability will come from ABI's sales system.</p>`;
    let c='USD';try{c=localStorage.getItem('abi-ccy')||'USD'}catch(e){}setCcy(c);
    $$('[data-save]',panel).forEach(s=>s.onclick=e=>{e.preventDefault();s.textContent='Saved ✓';toast('Saved to your buyer account (mock)')});}
});

/* Compare tool (mock) */
$$('[data-compare]').forEach(sel=>sel.addEventListener('change',()=>{const col=sel.dataset.compare;$$('[data-col="'+col+'"]').forEach(td=>td.style.opacity=sel.value?1:.35)}));

/* Isla — ABI's AI concierge; speaks as ABI on every page (scripted sample — no AI connected) */
const isla=$('.isla'),launch=$('.isla-launch');
if(isla){const log=$('.log',isla),quick=$('.quick',isla),ctx=document.body.dataset.context||'the ABI hub';
  const add=(t,who='bot')=>{const m=document.createElement('div');m.className='msg '+who;m.innerHTML=t;log.appendChild(m);log.scrollTop=log.scrollHeight};
  const S={
    start:{bot:`Hello, I'm Isla, ABI's AI concierge. I can help with anything across ABI, its developments and services. I can see you're looking at <b>${ctx}</b>. What would be most useful?`,chips:['buyuk','purpose','ambar','returns','advisor']},
    buyuk:{me:"I'm buying from the UK",bot:'Lovely. UK buyers follow a <a href="buying-from-the-uk.html">six-step journey</a>, with guidance on FIRPTA, ITIN, currency and timelines. Is this mainly an investment, a holiday home, or both?',chips:['invest','holiday','both']},
    purpose:{me:'Investment or holiday home?',bot:'Both are common. Could you tell me which matters most to you?',chips:['invest','holiday','both']},
    invest:{me:'Mainly investment',bot:'Thank you. Roughly what budget, and which currency do you think in?',chips:['b1','b2']},
    holiday:{me:'A holiday home',bot:'Got it. Roughly what budget, and which currency do you think in?',chips:['b1','b2']},
    both:{me:'A bit of both',bot:'That\'s a popular mix. Roughly what budget, and which currency do you think in?',chips:['b1','b2']},
    b1:{me:'Around £300k',bot:'Based on that, you may like <a href="development-ambar.html">AMBAR</a> (studio to three-bed residences) and the guide to <a href="buying-from-the-uk.html">buying from the UK</a>. Shall I connect you with an advisor?',chips:['advisor','ambar']},
    b2:{me:'Around $500k',bot:'Based on that, you could look at <a href="development-ambar.html">AMBAR</a> and our <a href="areas.html">area guides</a>. Shall I connect you with an advisor?',chips:['advisor','areas']},
    ambar:{me:'Show me AMBAR',bot:'AMBAR Building 1 has 132 residences, with 9 floor plans from studio to three bedrooms. <a href="development-ambar.html#availability">See availability</a> (sample data in this mock).',chips:['returns','advisor']},
    areas:{me:'Tell me about areas',bot:'Our <a href="areas.html">area guides</a> cover Orlando and surrounding towns, with drive times to the parks and the airport.',chips:['advisor']},
    returns:{me:'What returns can I expect?',bot:'I can\'t give rental income or return figures. Those need advice specific to you, and ABI doesn\'t promise returns. I can share the <a href="investor-hub.html">ownership cost explainers</a> or arrange a call with an advisor.',chips:['advisor'],guard:true},
    advisor:{me:'Talk to an advisor',bot:`I'll pass a short summary to your ABI advisor, <span class="placeholder">[Advisor name]</span>, so you don't have to repeat yourself. <a href="${CAL}" target="_blank" rel="noopener">Book a 30-minute call</a> at a UK-friendly time.`,chips:['summary'],},
    summary:{me:'What will you send them?',bot:'<b>Lead summary (mock)</b><br>Page: '+ctx+'<br>Purpose: as discussed<br>Budget &amp; currency: as discussed<br>Next step: call booked via Calendly<br><i>Written to the CRM on hand-off (not connected in this mock).</i>',chips:['start']}
  };
  const label={buyuk:"I'm buying from the UK",purpose:'Investment or holiday home?',ambar:'Show me AMBAR',returns:'What returns can I expect?',advisor:'Talk to an advisor',invest:'Investment',holiday:'Holiday home',both:'Both',b1:'~£300k',b2:'~$500k',areas:'Areas',summary:'What will you send?',start:'Start again'};
  function step(k){const s=S[k];if(s.me)add(s.me,'me');setTimeout(()=>{if(s.guard)add('Compliance guard applied: return wording rules','sys');add(s.bot);quick.innerHTML='';(s.chips||[]).forEach(c=>{const b=document.createElement('button');b.className='chip';b.textContent=label[c];b.onclick=()=>step(c);quick.appendChild(b)})},350)}
  let started=false;const open=()=>{isla.classList.add('open');if(!started){started=true;step('start')}};
  launch.addEventListener('click',()=>isla.classList.contains('open')?isla.classList.remove('open'):open());
  $('.x',isla).addEventListener('click',()=>isla.classList.remove('open'));
  $$('[data-open-isla]').forEach(b=>b.addEventListener('click',e=>{e.preventDefault();open()}));
  $('.composer',isla).addEventListener('submit',e=>{e.preventDefault();const i=$('input',isla);if(!i.value.trim())return;add(i.value,'me');i.value='';setTimeout(()=>add('This is a scripted preview, so I can\'t answer free text yet. Try one of the suggestions below.'),350)});
  $('.mic',isla).addEventListener('click',()=>toast('Voice mode is a Phase 2 feature (mock)'));
}
})();
