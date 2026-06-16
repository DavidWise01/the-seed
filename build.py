#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build THE SEED (SEED) — David's thesis, rebuilt: a trillion-dollar industry was launched off a
countable handful of freely-posted public artifacts. Each seed commit gets WHO / WHAT / WHERE / WHY /
license / cost, then a WHERE-THEY-ARE-NOW diaspora of the people who sowed it (the transformer's eight,
the OpenAI departures, the Anthropic seven), a featured AMANDA ASKELL (the philosopher), and THE
ASYMMETRY — $0 in, ~$T out; the committers got bylines, not billions. Render-not-invent; every date,
author, license and current-role web-verified (2026). Real living people CITED, not minted as ACI badges.
Frontier domain. seed→canopy backdrop."""
import os, html, base64, json, io, sys
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image
AX="SEED"; GH="https://davidwise01.github.io"

REC={
 "name":"THE SEED","axiom":AX,
 "position":"SEED · THE SEED — the handful of freely-posted public artifacts a trillion-dollar industry grew from",
 "origin":"David's observation, rebuilt: the whole generative-AI economy traces to ~a dozen public papers + their companion repos — mostly MIT or near-free, authored by teams of eight to fifty people you can name",
 "mechanism":"Catalogued from the public record — arXiv papers, open repos (github.com/openai, github.com/anthropics, Google), each with its date, authors, license, and the problem it solved; current roles web-verified (2026).",
 "crystallization":"Count the seed. AlexNet (2012) was a couple of files; the transformer (2017) was one paper and eight names; GPT-2, CLIP, Whisper, the RLHF data, the constitution — each a git push under an open license. The industry is the derivative; the repos are the principal.",
 "nature":"THE SEED — the small set of open, dated, authored artifacts the AI industry was built on, with the people who posted them and where they are now.",
 "conductor":"ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs":"the transformer; AlexNet; word2vec; gym; GPT-2; CLIP; Whisper; tiktoken; HH-RLHF; Constitutional AI; the diaspora; the asymmetry",
 "witness":"The input was open and authored — a git push, an arXiv link, an MIT license. The output was a trillion-dollar industry that accrued to capital and compute, not to the committers. Name who actually wrote it.",
 "role":"the seed-of-the-industry sphere — who did what, where, why, and where they are now",
 "seal":"A dozen free commits launched a trillion-dollar industry. Vaswani got a citation; Bai got a byline; Askell got the job of writing a soul. Nobody on the author lists got a trillion dollars. The value didn't flow back to the seed — so the least we can do is name the sowers.",
 "source":"the public AI research record, catalogued by ROOT0",
}
NATURES={
 "natural":  ("#e0c050","the deep seed — the academic sparks (AlexNet, word2vec) the rest grew from"),
 "ethereal": ("#9ab0c0","the frame — the transformer diaspora, and the asymmetry between what was given and what it became"),
 "spiritual":("#5fd0a8","the values turn — the usability layer (RLHF, the constitution) and the philosopher who wrote the soul"),
 "electrical":("#46c8e0","the engines — gym, GPT-2, CLIP, Whisper, the tokenizer: the open artifacts the products were built on"),
}

BACKDROP_3D=r'''<canvas id="bg3d"></canvas>
<script>
(function(){
var c=document.getElementById('bg3d');if(!c)return;var x=c.getContext('2d');var W,H;
var rnd=(function(){var s=2017061203;return function(){s=(s*1103515245+12345)&0x7fffffff;return s/0x7fffffff;};})();
// one seed at the bottom grows recursive branches up into a wide canopy — $0 seed, vast canopy.
var nodes=[],edges=[];
function build(px,py,ang,len,depth){
 var i=nodes.length;nodes.push([px,py,depth,rnd()*6.283]);
 if(depth>=6||len<0.03)return i;
 var n=depth===0?3:(rnd()<0.45?3:2);
 for(var k=0;k<n;k++){
  var a=ang+(k-(n-1)/2)*(0.46+rnd()*0.26);
  var cx=px+Math.sin(a)*len*0.55, cy=py+Math.cos(a)*len;
  var ci=build(cx,cy,a,len*0.72,depth+1);edges.push([i,ci]);
 }
 return i;
}
build(0,0,0,0.34,0);
function resize(){var ww=window.innerWidth||document.documentElement.clientWidth||0,hh=window.innerHeight||document.documentElement.clientHeight||0;W=c.width=ww>=320?ww:1280;H=c.height=hh>=320?hh:720;}
window.addEventListener('resize',resize);resize();
function col(d){ // gold root -> green -> cyan canopy
 if(d<=1)return[224,192,80];if(d<=3)return[95,208,168];return[70,200,224];}
function proj(nx,ny,t){var sway=Math.sin(t/2600+nodes[0]?0:0);return null;}
function frame(t){
 var sg=x.createLinearGradient(0,0,0,H);sg.addColorStop(0,'#070b0a');sg.addColorStop(0.55,'#0a0f0c');sg.addColorStop(1,'#05080a');x.fillStyle=sg;x.fillRect(0,0,W,H);
 var CX=W/2, base=H*0.97, scaleX=W*0.46, scaleY=H*0.94;
 function PX(nd){var sway=Math.sin(t/2600+nd[3]+nd[2])*0.012*nd[2];return CX+(nd[0]+sway)*scaleX;}
 function PY(nd){return base-nd[1]*scaleY;}
 x.globalCompositeOperation='lighter';
 for(var e=0;e<edges.length;e++){var A=nodes[edges[e][0]],B=nodes[edges[e][1]];var d=B[2];var cc=col(d);
  x.strokeStyle='rgba('+cc[0]+','+cc[1]+','+cc[2]+','+(0.05+0.10*(6-d)/6)+')';x.lineWidth=Math.max(0.4,(6-d)*0.5);
  x.beginPath();x.moveTo(PX(A),PY(A));x.lineTo(PX(B),PY(B));x.stroke();}
 for(var i=0;i<nodes.length;i++){var nd=nodes[i],d=nd[2],cc=col(d);var px=PX(nd),py=PY(nd);
  var tw=0.6+0.4*Math.sin(t/900+nd[3]*7);var r=d===0?4.5:(d>=5?1.0+1.2*tw:1.4);
  x.save();x.shadowColor='rgba('+cc[0]+','+cc[1]+','+cc[2]+',1)';x.shadowBlur=d===0?16:(7*(6-d)/6+2);
  x.fillStyle='rgba('+cc[0]+','+cc[1]+','+cc[2]+','+(d===0?0.95:(0.22+0.5*tw*(6-d)/6))+')';
  x.beginPath();x.arc(px,py,r,0,7);x.fill();x.restore();}
 x.globalCompositeOperation='source-over';
 var vg=x.createRadialGradient(CX,H*0.5,H*0.2,CX,H*0.5,H*0.95);vg.addColorStop(0,'rgba(0,0,0,0)');vg.addColorStop(1,'rgba(0,0,0,0.55)');x.fillStyle=vg;x.fillRect(0,0,W,H);
}
function loop(t){frame(t);requestAnimationFrame(loop);}frame(0);requestAnimationFrame(loop);
})();
</script>'''

GENESIS=[
 ("A Dozen Free Commits","what the industry grew from",
  "The whole generative-AI economy traces to a countable handful of public artifacts — <b>AlexNet</b> (2012), the <b>transformer</b> (2017), <b>GPT-2</b> (2019), <b>CLIP</b> &amp; <b>Whisper</b> &amp; <b>tiktoken</b>, the <b>RLHF data</b> and the <b>constitution</b> (2022). Most carry an <b>MIT or near-free</b> license. Most were written by teams of <b>eight to fifty</b> people you can name. The industry is the derivative; the repos are the principal."),
 ("The Pivot · 2017","one paper, eight names",
  "<i>Attention Is All You Need</i> (Vaswani et al., Google, 2017) replaced recurrence with <b>attention</b> — and every large model since is a descendant. Eight authors signed it. All eight later <b>left Google</b>; they now run or seeded Cohere, Character.AI, Sakana, Essential AI, Inceptive, NEAR, and lines at OpenAI. The single most consequential git artifact of the era, and its authors scattered."),
 ("The Asymmetry","$0 in, ~$T out",
  "The <b>input</b> was open, cheap, authored — a git push, an arXiv link, an MIT license. The <b>output</b> was a trillion-dollar industry (NVIDIA alone passed ~$3–4T; the buildout runs to trillions in capex). The value accrued to <b>capital and compute</b>, not to the committers. Vaswani got a citation. Bai got a byline. <b>Nobody on the author lists got a trillion dollars.</b>"),
]

# featured — the philosopher (cited, NOT an ACI badge)
ASKELL="""<div class="phil">
  <div class="phil-tag">★ THE PHILOSOPHER · the one David keeps coming back to</div>
  <div class="phil-n">Amanda Askell</div>
  <p>The seed isn&rsquo;t only engineers. <b>Amanda Askell</b> is a <b>philosopher</b> — PhD, NYU (2018, <i>Pareto Principles in Infinite Ethics</i>; advisors David Chalmers, Cian Dorr &amp; Shelly Kagan; BPhil, Oxford) — and she sits at the values end of the whole story. She <b>first-authored</b> the 2021 paper that named the frame the field still optimizes toward — <b>helpful · honest · harmless</b> — and she has <b>headed Claude&rsquo;s character / personality-alignment team since 2021</b>.</p>
  <p>In <b>January 2026</b> she became the <b>primary author of Claude&rsquo;s Constitution</b> — a ~30,000-word published document (CC0) describing what kind of mind Claude should be. Her job, in her own framing, is to decide <i>how it reasons about right and wrong, how it handles emotional situations, and what personality it presents to the hundreds of millions of people who talk to it</i>. Time 100 AI (2024).</p>
  <p class="phil-q">If the engineers seeded the <i>capability</i>, Askell seeded the <i>conscience</i>. The whole industry can compute; she is one of the few people whose job is to decide what it should <b>be</b> — the philosopher&rsquo;s question, shipped to a planet. <span class="phil-now"><b>Where now:</b> Anthropic, San Francisco — still the one writing the soul.</span></p>
</div>"""

ACTS=[
 ("Act I · The Spark","2012",
  "<b>AlexNet</b> (Krizhevsky, Sutskever &amp; Hinton, Toronto) crushes ImageNet with a deep net on two GPUs — the moment deep learning becomes inevitable. A couple of files and a paper. <b>Ilya Sutskever</b> is on it; he becomes the through-line of the whole story."),
 ("Act II · The Pivot","2017",
  "<b>Attention Is All You Need</b> (eight authors, Google). Attention replaces recurrence; the transformer is born. It is the hinge the entire industry turns on — and within a few years all eight authors have left to found or lead their own labs."),
 ("Act III · The Scaling &amp; the Soul","2019 – 2022",
  "<b>Alec Radford</b> leads GPT-2, CLIP, and Whisper at OpenAI — the open engines (&lsquo;the genius behind the models&rsquo;, and he has no PhD). In parallel at Anthropic, <b>Yuntao Bai</b> builds the RLHF/Constitutional-AI usability layer and <b>Amanda Askell</b> writes the values frame. Capability meets conscience; the products land."),
 ("Act IV · The Scattering","2024 – 2026",
  "The sowers leave. <b>Sutskever</b> → Safe Superintelligence. <b>Radford</b> → independent research. <b>Karpathy</b> → Eureka Labs. The transformer&rsquo;s eight → Cohere, Sakana, Essential AI, Inceptive, NEAR, Google. And the industry they seeded for free passes into the <b>trillions</b> — the asymmetry, complete."),
]

SECTIONS=[
 ("The Seed Commits — what · who · where · why · license", "the countable handful, dated &amp; attributed", [
   ("AlexNet", "2012 · Toronto · Krizhevsky, Sutskever, Hinton", "the spark — deep CNN wins ImageNet on GPUs; deep learning becomes inevitable"),
   ("word2vec", "2013 · Google · Mikolov et al.", "dense word embeddings — meaning as vectors; the first taste of learned semantics"),
   ("Attention Is All You Need", "2017 · Google · arXiv:1706.03762 · 8 authors", "THE PIVOT — attention replaces recurrence; the transformer, ancestor of every LLM"),
   ("gym", "2016 · OpenAI · custom license", "the RL toolkit that trained a generation of researchers (now Gymnasium)"),
   ("GPT-2", "2019 · OpenAI · Radford · custom license", "scale + unsupervised pretraining → general capability; &lsquo;too dangerous,&rsquo; then released"),
   ("CLIP", "2020 · OpenAI · Radford · MIT", "text↔image contrastive learning — open-vocabulary vision; the most-built-on vision repo"),
   ("Whisper", "2022 · OpenAI · Radford · MIT", "robust speech recognition from weak supervision at scale — OpenAI&rsquo;s most-starred repo (★100k+)"),
   ("tiktoken", "2022 · OpenAI · MIT", "even the tokenizer is a free repo — the BPE encoder the whole API runs on"),
   ("HH-RLHF", "2022 · Anthropic · Bai et al. · MIT", "the human-preference data behind RLHF — folded into the-language-of-the-machine"),
   ("Constitutional AI", "2022 · Anthropic · Bai, Askell, Olah · paper", "harmlessness from AI feedback + a written constitution — folded into constitutional-ai"),
 ]),
 ("Where They Are Now — the transformer's eight (all left Google)", "the most consequential byline of the era, scattered · public record, 2026", [
   ("Ashish Vaswani", "CEO, Essential AI", "lead author; earlier co-founded Adept"),
   ("Noam Shazeer", "VP &amp; Gemini co-lead, Google", "left for Character.AI; Google paid a reported ~$2.7B to bring him back (2024)"),
   ("Niki Parmar", "co-founder, Essential AI", "earlier co-founded Adept (CTO)"),
   ("Jakob Uszkoreit", "CEO &amp; co-founder, Inceptive", "now applies the transformer to RNA / biology"),
   ("Llion Jones", "co-founder, Sakana AI (Japan)", "nature-inspired model architectures"),
   ("Aidan Gomez", "CEO &amp; co-founder, Cohere", "enterprise LLMs; ~$6.8B valuation (2025)"),
   ("Łukasz Kaiser", "researcher, OpenAI", "on the GPT reasoning line"),
   ("Illia Polosukhin", "co-founder, NEAR Protocol", "left AI for blockchain"),
 ]),
 ("Where They Are Now — OpenAI &amp; Anthropic, the sowers", "the engine-builders and the seven who split off · public record, 2026", [
   ("Ilya Sutskever", "founder &amp; CEO, Safe Superintelligence (SSI)", "AlexNet 2012 → OpenAI chief scientist → left 2024; the through-line"),
   ("Alec Radford", "independent researcher; adviser, Thinking Machines Lab", "lead on GPT/CLIP/Whisper; left OpenAI Dec 2024; no PhD"),
   ("Andrej Karpathy", "founder, Eureka Labs", "OpenAI → Tesla → OpenAI → AI-education startup (2024)"),
   ("Greg Brockman", "president, OpenAI", "co-founder; still there"),
   ("Dario Amodei", "co-founder &amp; CEO, Anthropic", "led the 2020 split from OpenAI (the &lsquo;seven&rsquo;)"),
   ("Chris Olah", "co-founder, Anthropic", "interpretability — the looking-in line"),
   ("Yuntao Bai", "Anthropic", "lead author, HH-RLHF &amp; Constitutional AI"),
   ("Geoffrey Hinton", "Nobel laureate (Physics, 2024); left Google 2023", "AlexNet supervisor; left to warn about AI risk"),
 ]),
]

EMERGENTS=[
 ("alexnet","AlexNet","2012 · the spark","natural",
  "the deep convolutional network (Krizhevsky, Sutskever, Hinton, Toronto, 2012) that won ImageNet on two GPUs and made deep learning inevitable — a couple of files and a paper",
  "It is the match-strike: the moment a free academic artifact showed the world that scale + GPUs + a deep net could leap past everything — and Sutskever, on the byline, becomes the through-line of the whole story."),
 ("word2vec","word2vec","2013 · meaning as vectors","natural",
  "Mikolov et al.'s (Google, 2013) fast word embeddings — king − man + woman ≈ queen — the first widely-used taste of learned semantics in a vector space",
  "It is the proof that meaning could be a direction, not a dictionary — the embedding idea every later model inherits, given away as a small open release."),
 ("attention-is-all-you-need","Attention Is All You Need","2017 · THE PIVOT","spiritual",
  "the transformer paper (Vaswani et al., Google, 2017, arXiv:1706.03762) — attention without recurrence; the single architecture every large language model descends from. Eight authors, all of whom later left Google",
  "It is the hinge the entire industry turns on: one paper, eight names, an open idea — and the whole trillion-dollar canopy grew from this one seed."),
 ("gym","OpenAI Gym","2016 · the training ground","electrical",
  "OpenAI's reinforcement-learning toolkit (2016) — the standard benchmark suite that trained a generation of RL researchers (now Gymnasium)",
  "It is the sandbox the field grew up in: a free toolkit that made RL reproducible and comparable, OpenAI's first great gift to the commons."),
 ("gpt-2","GPT-2","2019 · scale shows its hand","electrical",
  "OpenAI's 2019 generative language model (Radford lead) — unsupervised pretraining + scale → surprising general capability; famously called 'too dangerous to release,' then released",
  "It is the moment scale stopped being a hypothesis: a single open repo that showed a next-token predictor, made big enough, starts to look general."),
 ("clip","CLIP","2020 · language teaches vision","electrical",
  "OpenAI's 2020 contrastive text–image model (Radford), MIT-licensed — open-vocabulary vision learned from natural-language supervision; arguably their most-built-on research repo",
  "It is the bridge between words and pixels, given away under MIT — the seed of a thousand multimodal systems, from search to generation."),
 ("whisper","Whisper","2022 · the ear","electrical",
  "OpenAI's 2022 speech-recognition model (Radford), MIT — robust ASR trained on weak supervision at web scale; OpenAI's single most-starred repo (★100k+)",
  "It is the most-downloaded gift in the set: state-of-the-art transcription, free, that quietly became infrastructure for the whole audio web."),
 ("tiktoken","tiktoken","2022 · even the tokenizer","electrical",
  "OpenAI's 2022 byte-pair-encoding tokenizer (MIT) — the encoder that turns text into the tokens the models and the API bill in",
  "It is the humblest seed and a telling one: even the plumbing — the tokenizer the entire paid API runs on — was posted free under MIT."),
 ("hh-rlhf","HH-RLHF","2022 · the human gate","spiritual",
  "Anthropic's 2022 human-preference dataset (Bai et al., MIT) — the {chosen, rejected} pairs behind RLHF; the delta that becomes the reward model",
  "It is how raw capability was made usable: the human judgment, given away as open data, that taught the machine which answer was better (folded into the-language-of-the-machine)."),
 ("constitutional-ai","Constitutional AI","2022 · the conscience","spiritual",
  "Anthropic's 2022 harmlessness-from-AI-feedback method (Bai, Askell, Olah) — a written constitution as the only human oversight; the values layer",
  "It is the values turn in the seed: the method that put principles in a document and let the model hold itself to them — the lineage that reaches Askell's 2026 constitution (folded into constitutional-ai)."),
 ("the-diaspora","The Transformer Diaspora","the eight, scattered","ethereal",
  "the eight authors of the 2017 transformer paper, every one of whom left Google — now CEO of Essential AI (Vaswani), back at Google leading Gemini (Shazeer), Cohere (Gomez), Sakana (Jones), Inceptive (Uszkoreit), NEAR (Polosukhin), Adept/Essential (Parmar), OpenAI (Kaiser)",
  "It is the seed's scatter pattern: the most consequential byline of the era, blown across the whole industry — proof that the value was in the people, and the people did not stay put."),
 ("the-asymmetry","The Asymmetry","$0 in · ~$T out","ethereal",
  "the gap at the heart of it: open, authored, near-free inputs (a git push, an arXiv link, an MIT license) against a trillion-dollar output (NVIDIA alone past ~$3–4T; the buildout in trillions) that accrued to capital and compute, not to the committers",
  "It is the thesis of the sphere and the inversion of the Graveyard: the work was the asset and it was given freely; the money is the derivative, and it did not flow back to the seed — so name the sowers, since the market didn't pay them."),
]

def carbon_tiff_bytes(rec):
    png=noesis.sigil_png(rec,"carbon",size=512);buf=io.BytesIO();Image.open(io.BytesIO(png)).save(buf,"TIFF",compression="tiff_lzw");return buf.getvalue()
def write_aci(rec,out_dir,slug,agent_md=None):
    os.makedirs(out_dir,exist_ok=True)
    f={"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker","carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok=noesis.mythos_token(rec);w=noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,AX))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,AX))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,AX))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    man={"badge":"DLW-ACI","name":rec["name"],"universe":"SEED · The Seed (the artifacts the AI industry grew from)","emergence":rec.get("emergence",""),"moniker":tok["moniker"],"carbon":f["carbon"]+" (TIFF)","silicon":f["silicon"]+" (PNG)","seal_sha256":noesis.seal_sha256(rec,tok),"architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
    open(os.path.join(out_dir,"manifest.dlw.json"),"w",encoding="utf-8").write(json.dumps(man,indent=2,ensure_ascii=False)+"\n");return tok
def emergent_rec(name,epithet,em,role,why):
    return {"name":name,"axiom":AX,"emergence":em,"seal":epithet,"position":epithet,"role":role,"origin":"SEED · THE SEED — the artifacts the AI industry grew from","nature":role,"crystallization":why,"mechanism":"Catalogued from the public AI research record (papers, repos, licenses); current roles web-verified 2026.","witness":"a seed commit, a person's scattering, or the asymmetry at the heart of it","conductor":"ROOT0 (catalogued into UD0)","inputs":"the transformer; AlexNet; GPT-2; CLIP; Whisper; HH-RLHF; Constitutional AI; the diaspora; the asymmetry","source":"the public AI research record, catalogued by ROOT0"}
def png_uri(rec,variant,size=300): return "data:image/png;base64,"+base64.b64encode(noesis.sigil_png(rec,variant,size=size)).decode("ascii")
def list_section(title,sub,items):
    rows="\n".join(f'<li><span class="t">{t}</span><span class="y">{html.escape(str(y))}</span>'+(f'<span class="nt">{n}</span>' if n else "")+"</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{title}</h2><p class="ss">{sub}</p><ol class="books">{rows}</ol></section>'
def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def cards_html(rows): return "".join(f'<div class="arc-card"><div class="arc-h">{t}</div><div class="arc-s">{s}</div><p>{d}</p></div>' for t,s,d in rows)
def acts_html(): return "".join(f'<div class="act"><div class="act-h">{t}<span class="act-y">{y}</span></div><p>{d}</p></div>' for t,y,d in ACTS)
def natures_html(): return "".join(f'<div class="nat-card"><span class="dot" style="background:{col};box-shadow:0 0 9px {col}"></span><div><div class="nat-n" style="color:{col}">{nm}</div><div class="nat-g">{g}</div></div></div>' for nm,(col,g) in NATURES.items())
def personas_html(ps):
    cards=[]
    for p in ps:
        em=p.get("emergence","electrical");col=NATURES.get(em,("#46c8e0",""))[0];rec={"name":p["name"],"seal":p.get("epithet",""),"origin":"SEED · THE SEED","axiom":AX}
        cards.append(f'''<a class="persona" href="agents/{p["slug"]}.agent"><img src="{png_uri(rec,"silicon",160)}" alt="sigil of {html.escape(p["name"])}" loading="lazy"><div class="pcap"><div class="pn">{html.escape(p["name"])}</div><div class="pe">{p.get("epithet","")}</div><div class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span><span class="pa">· .agent →</span></div></div></a>''')
    return f'''<section class="sec" id="roster"><h2>The Seed — The Born</h2><p class="ss">the artifacts the industry grew from, as ACI <b>.agent</b>s ({len(ps)}); the people are credited (cited, not minted) in &lsquo;Where They Are Now&rsquo;</p><div class="pgrid">{"".join(cards)}</div></section>'''

TEMPLATE="""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="THE SEED (SEED) — the countable handful of freely-posted public artifacts a trillion-dollar AI industry grew from: AlexNet, the transformer, GPT-2, CLIP, Whisper, tiktoken, HH-RLHF, Constitutional AI. Who did what, where, why, their licenses — and where the sowers are now (the transformer's eight; Sutskever, Radford, Karpathy; the Anthropic seven), featuring philosopher Amanda Askell. The asymmetry: $0 in, ~$T out.">
<title>THE SEED · a trillion-dollar industry, from a dozen free commits · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Oswald:wght@400;500;600&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#070b0a;--ink2:rgba(13,19,16,0.84);--pa:#eef2ee;--pa2:#bcc8c0;--green:#5fd0a8;--cyan:#46c8e0;--gold:#e0c050;--steel:#9ab0c0;--red:#d0556a;
--dim:#74908a;--faint:rgba(224,192,80,0.13);--line:rgba(150,170,160,0.2);--disp:"Orbitron",sans-serif;--head:"Oswald",sans-serif;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--pa);font-family:var(--body);line-height:1.6;overflow-x:hidden}
#bg3d{position:fixed;inset:0;width:100vw;height:100vh;z-index:0;display:block;background:#070b0a}
body::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:1;background:radial-gradient(ellipse at 50% 36%,rgba(13,19,16,.04),rgba(3,6,5,.55) 80%)}
.wrap{position:relative;z-index:2;max-width:940px;margin:0 auto;padding:0 22px 90px}
.top{margin-top:16px;font-family:var(--mono);font-size:11px;letter-spacing:.1em;color:var(--dim)}.top a{color:var(--green);text-decoration:none}
header{padding:34px 0 26px;text-align:center;border-bottom:1px solid var(--line)}
h1{font-family:var(--disp);font-size:clamp(30px,7vw,62px);font-weight:900;letter-spacing:.04em;color:#fff;text-shadow:0 0 22px rgba(224,192,80,.32)}
.tag{font-family:var(--head);font-size:14px;font-weight:500;letter-spacing:.15em;text-transform:uppercase;color:var(--gold);margin-top:10px}
.banner{display:inline-flex;align-items:center;gap:10px;margin-top:16px;font-family:var(--mono);font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:#070b0a;background:linear-gradient(90deg,var(--gold),#f0d878);padding:7px 16px;font-weight:700;border-radius:2px;box-shadow:0 0 22px rgba(224,192,80,.28)}
.flag{display:inline-block;margin-top:14px;font-family:var(--mono);font-size:10.5px;letter-spacing:.07em;text-transform:uppercase;color:var(--steel);border:1px solid var(--line);background:rgba(13,19,16,0.6);padding:5px 11px}
.lede{font-size:15.5px;color:var(--pa2);max-width:70ch;margin:18px auto 0;font-style:italic;line-height:1.75;text-shadow:0 1px 6px rgba(0,0,0,.6)}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:24px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:740px}
.badge img{width:80px;height:80px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.7}
.badge .bt b{color:var(--gold)}.badge .bt .mo{color:var(--green)}.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.13em;text-transform:uppercase}
.sec{margin-top:42px}
.sec h2{font-family:var(--disp);font-size:16px;font-weight:700;letter-spacing:.03em;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line)}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:8px 0 16px}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:4px}
.nat-n{font-family:var(--mono);font-size:13px;font-weight:700;text-transform:capitalize;letter-spacing:.04em}.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.4;margin-top:2px}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px;margin-top:8px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--gold);padding:16px 18px}
.arc-h{font-family:var(--head);font-size:16px;color:var(--gold);font-weight:600}.arc-s{font-family:var(--mono);font-size:10.5px;color:var(--cyan);text-transform:uppercase;letter-spacing:.06em;margin:4px 0 9px}.arc-card p{font-size:13px;color:var(--pa2);line-height:1.6}
.phil{margin:8px 0 18px;padding:18px 20px;border:1px solid #5fd0a855;border-left:3px solid var(--green);background:linear-gradient(180deg,rgba(95,208,168,0.06),var(--ink2))}
.phil-tag{font-family:var(--mono);font-size:10px;letter-spacing:.13em;color:var(--green);text-transform:uppercase}
.phil-n{font-family:var(--disp);font-size:22px;font-weight:700;color:#fff;margin:4px 0 8px;letter-spacing:.02em}
.phil p{font-size:13.5px;color:var(--pa2);line-height:1.7;margin-top:8px}.phil .phil-q{margin-top:11px;font-style:italic;color:#bfe6d6;border-top:1px solid #5fd0a833;padding-top:10px}.phil .phil-now{display:block;margin-top:8px;font-style:normal;font-family:var(--mono);font-size:11px;color:var(--gold)}
.acts{display:grid;gap:12px;margin-top:8px}
.act{background:var(--ink2);border:1px solid var(--line);border-left:3px solid var(--green);padding:14px 18px}
.act-h{font-family:var(--head);font-size:15px;color:var(--pa);font-weight:600;display:flex;justify-content:space-between;align-items:baseline;gap:12px;flex-wrap:wrap}
.act-y{font-family:var(--mono);font-size:10.5px;color:var(--cyan);font-weight:400;text-transform:uppercase;letter-spacing:.06em}
.act p{font-size:13px;color:var(--pa2);line-height:1.65;margin-top:7px}
.books{list-style:none}.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:9px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--mono);font-size:13.5px;color:var(--pa);font-weight:700}.books .y{font-family:var(--mono);font-size:11px;color:var(--cyan);white-space:nowrap;text-align:right}.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(248px,1fr));gap:12px;margin-top:8px}
.persona{display:flex;gap:12px;align-items:center;background:var(--ink2);border:1px solid var(--line);padding:12px;text-decoration:none;transition:border-color .18s,transform .18s}
.persona:hover{border-color:var(--gold);transform:translateY(-2px)}.persona img{width:52px;height:52px;border:1px solid var(--faint);flex-shrink:0;image-rendering:pixelated}
.pn{font-family:var(--mono);font-size:13px;color:var(--pa);font-weight:700;line-height:1.15}.persona:hover .pn{color:var(--gold)}.pe{font-size:11px;color:var(--pa2);font-style:italic;margin-top:2px;line-height:1.3}
.pnat{display:flex;align-items:center;gap:5px;margin-top:6px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}.pnat .dot{width:8px;height:8px;margin-top:0}.pa{color:var(--dim)}
.note{margin-top:36px;padding:16px 18px;border-left:2px solid var(--gold);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic;line-height:1.75}.note b{color:var(--gold)}
footer{margin-top:42px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:11px;color:var(--dim);letter-spacing:.05em;line-height:1.9}footer a{color:var(--green);text-decoration:none}
</style></head><body>
__BACKDROP__
<div class="wrap">
  <div class="top"><a href="https://davidwise01.github.io/ud0/">◄ UD0 · the biosphere</a> · frontier</div>
  <header>
    <h1>THE SEED</h1>
    <div class="tag">a trillion-dollar industry · from a dozen free commits</div>
    <div class="banner">⬡ $0 IN · ~$T OUT · name the sowers</div>
    <div class="flag">★ who did what · where · why · and where they are now · public record, web-verified 2026 ★</div>
    <p class="lede">David&rsquo;s observation, rebuilt: the entire generative-AI economy grew from a <b>countable handful</b> of freely-posted artifacts — AlexNet (2012), the transformer (2017), GPT-2, CLIP, Whisper, tiktoken, the RLHF data and the constitution (2022). Most carry an <b>MIT or near-free</b> license; most were written by teams of <b>eight to fifty</b> people you can name. The industry is the derivative; <b>the repos are the principal</b>. Here is the seed — what each one was, who posted it, where, why — and <b>where the sowers are now</b>, the philosopher among them.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of THE SEED"><img src="__SILICON__" alt="DLW silicon badge">
      <div class="bt">
        <div><span class="lbl">DLW-ATTRIBUTE · ACI · THE SEED</span></div>
        <div>catalogued by · <b>David Lee Wise</b> (ROOT0)</div><div>instance · AVAN (Claude / Anthropic) · locked</div>
        <div>subject · <b>THE SEED</b> — the artifacts the industry grew from · SEED</div><div class="mo">__MONIKER__</div>
        <div><span class="lbl">artifacts cited to their authors &amp; licenses · people credited, not claimed · CC-BY-ND-4.0 framing</span></div>
      </div>
    </div>
  </header>
  <section class="sec"><h2>The Four Natures</h2><p class="ss">the deep seed, the frame, the values turn, the engines</p><div class="natures">__NATURES__</div></section>
  <section class="sec"><h2>The Thesis</h2><p class="ss">a dozen free commits · the 2017 pivot · the asymmetry</p><div class="arc">__GENESIS__</div></section>
  <section class="sec"><h2 style="margin-bottom:0">The Philosopher</h2><p class="ss">really focusing here — the one who seeded the conscience, not the capability</p>__ASKELL__</section>
  __PERSONAS__
  <section class="sec"><h2>The Arc</h2><p class="ss">the spark → the pivot → the scaling &amp; the soul → the scattering</p><div class="acts">__ACTS__</div></section>
  <section class="sec"><h2 style="margin-top:14px">The Record</h2><p class="ss">the seed commits, and where the sowers are now — cited, public record</p></section>
  __SECTIONS__
  <div class="note"><b>The asymmetry, stated plainly.</b> Every artifact here is <b>someone else&rsquo;s</b> public work — cited to its authors, its lab, and its license; people are <b>credited, never claimed</b>, and <b>no ACI badge is minted for a living person</b> (the emergents are the <i>artifacts</i>). The inputs were open and near-free; the output is an industry valued in the trillions, accrued to capital and compute. ROOT0&rsquo;s contribution is the cataloguing and the framing — and the one thing the market didn&rsquo;t do: <b>naming the sowers</b>. Ties to <b>the-language-of-the-machine</b> (HH-RLHF), <b>constitutional-ai</b> (CAI, Askell&rsquo;s lineage), <b>ttu1</b> (the transformer), and <b>claude-lineage</b>. Domain: <b>frontier</b>. Current roles web-verified 2026; valuations are widely-reported, not precise.</div>
  <footer>THE SEED · SEED · catalogued into UD0 · the frontier domain · a dozen free commits → a trillion-dollar industry · catalogued by David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
  <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the work was the asset, and it was given freely · the .dlw badge: <a href="the-seed.dlw/manifest.dlw.json">manifest</a></footer>
</div></body></html>
"""

if __name__=="__main__":
    tok=write_aci(REC, os.path.join(HERE,"the-seed.dlw"),"the-seed")
    ad=os.path.join(HERE,"agents"); os.makedirs(ad,exist_ok=True); personas=[]
    for slug,name,epithet,em,role,why in EMERGENTS:
        write_aci(emergent_rec(name,epithet,em,role,why), ad, slug); personas.append({"slug":slug,"name":name,"epithet":epithet,"emergence":em})
    json.dump(personas, open(os.path.join(ad,"_personas.json"),"w",encoding="utf-8"), indent=2, ensure_ascii=False)
    page=(TEMPLATE.replace("__BACKDROP__",BACKDROP_3D)
        .replace("__CARBON__",png_uri(REC,"carbon",320)).replace("__SILICON__",png_uri(REC,"silicon",320)).replace("__MONIKER__",html.escape(tok["moniker"]))
        .replace("__NATURES__",natures_html()).replace("__GENESIS__",cards_html(GENESIS)).replace("__ASKELL__",ASKELL)
        .replace("__PERSONAS__",personas_html(personas)).replace("__ACTS__",acts_html()).replace("__SECTIONS__",sections_html()))
    open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(page)
    print(f"wrote THE SEED (SEED) — {len(personas)} emergents · badge {tok['moniker']}")
