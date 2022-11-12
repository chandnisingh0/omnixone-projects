//Open Dialog
const openDialogBtns = document.querySelectorAll('[data-toggle="modal"]');
const openDialog = ($event) => {
  const dialog = document.querySelector($event.target.dataset.target);
  if(!dialog){
    console.error(`cannot find dialog called ${$event.target.dataset.target}`);
    return;
  }
  dialog.showModal();
};
openDialogBtns.forEach((e)=>{e.addEventListener("click", openDialog);});

//Close Dialog
const closeDialogBtns = document.querySelectorAll('[data-dismiss="modal"]');
const closeDialog = ($event) => {
  const dialog = $event.target.parentElement.closest('dialog');
  if(!dialog){
    console.error(`no parent dialog fond`);
    return;
  }
  dialog.classList.add('hide');
  dialog.addEventListener('animationend',animeEnd = ($event)=>{
    if($event.pseudoElement == '::backdrop'){   
      dialog.classList.remove('hide');
      dialog.close();
      dialog.removeEventListener('animationend',animeEnd);    
    }
  }); 

  const openDialogBtn = document.querySelector(`[data-target="#${dialog.id}"]`);
  if(openDialogBtn)openDialogBtn.focus();
};
closeDialogBtns.forEach((e)=>{e.addEventListener("click", closeDialog);});

//document.getElementById('Modal').showModal();