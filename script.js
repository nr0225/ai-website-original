function toggleMenu(){
  const m=document.getElementById('menu');
  m.style.display = (m.style.display==='block') ? 'none' : 'block';
}
const y=document.getElementById('year');
if(y){ y.textContent=new Date().getFullYear(); }
