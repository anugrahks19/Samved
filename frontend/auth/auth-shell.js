/* Updated portal artwork around the existing login and registration forms. */
(() => {
  function decorate() {
    const box=document.querySelector('.login-box');
    if (!box) return;
    document.body.classList.add('samved-auth');
    const isRegister=Boolean(document.getElementById('registerForm'));
    const art=document.createElement('div'); art.className='samved-auth-art';
    const picture=document.createElement('img');
    picture.src=`/assets/illustrations/${isRegister ? 'REGISTER' : 'LOGIN'}.jpeg`;
    picture.alt=isRegister ? 'Student beginning a learning journey' : 'Student ready to learn';
    art.appendChild(picture);
    const caption=document.createElement('p');
    caption.textContent=isRegister ? 'Learn, Grow, Achieve ♡' : 'Better Than Yesterday ♡';
    art.appendChild(caption);
    const content=document.createElement('div'); content.className='samved-auth-content';
    const logo=document.createElement('img'); logo.className='samved-auth-logo';
    logo.src='/assets/samved-portal-logo.png'; logo.alt='SAMVED Portal';
    content.appendChild(logo);
    while(box.firstChild) content.appendChild(box.firstChild);
    box.append(art,content);
  }
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',decorate,{once:true});
  else decorate();
})();
