


const menu = document.getElementById('menu');
const sidebar = document.getElementById('sidebar')
const menuItemsDropdown = document.querySelectorAll('.menu-item-dropdown')


//desplegar menu lateral presionando "menu de hamburguesa"

menu.addEventListener('click',()=>{
    sidebar.classList.toggle('menu-toggle');
    menu.classList.toggle('menu-toggle')
});


//desplegar subcategorias

menuItemsDropdown.forEach((menuItem)=>{
    menuItem.addEventListener('click',()=>{
        const subMenu = menuItem.querySelector('.sub-menu');
        const isActive = menuItem.classList.toggle('sub-menu-toggle')
        if(subMenu){
            if(isActive){
                subMenu.style.height = `${subMenu.scrollHeight + 6}px`;
                subMenu.style.padding = '0.2rem 0';
            }else{
                subMenu.style.height = '0';
                subMenu.style.padding = '0';
            }
        }
        menuItemsDropdown.forEach((item)=>{
            if(item !== menuItem){
                const otherSubmenu = item.querySelector('.sub-menu')
                if(otherSubmenu){
                    item.classList.remove('sub-menu-toggle');
                    otherSubmenu.style.height = '0';
                    otherSubmenu.style.padding = '0';
                }
            }
        })
    })
});