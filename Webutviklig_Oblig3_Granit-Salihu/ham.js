const menu = document.getElementById("main-menu");

const hamMenu = () =>{
    if(menu.style.display == "block"){
        menu.style.display ="none";
        console.log("Hei det skjer");
    }
    else{
        menu.style.display = "block";
        console.log("hei");
    };
}
