/*=============================================
OBJETO CON LAS PROPIEDADES DE LA GALERÍA
=============================================*/

var pg = {

    imgGaleria: document.querySelectorAll("#galeria img"),
    rutaImagen: null,
    cuerpoDom: document.querySelector("body"),
    lightbox: null
 
 }
 
 /*=============================================
 OBJETO CON LOS MÉTODOS DE LA GALERÍA
 =============================================*/
 
 var mg = {
 
     inicioGaleria: function(){
         
        
        for(var i = 0; i < pg.imgGaleria.length; i++){            
             pg.imgGaleria[i].addEventListener("click", mg.capturaImagen) 
        }
 
     },
 
     capturaImagen: function(img){
         pg.rutaImagen = img.target;
         mg.lightbox(pg.rutaImagen)
 
     },
 
     lightbox: function(img){
         img.style.opacity=100;
         pg.cuerpoDom.appendChild(document.createElement("DIV")).setAttribute("id", "lightbox");
         pg.lightbox = document.querySelector("#lightbox");
 
         pg.lightbox.style.width = "100%";
         pg.lightbox.style.height = "100%";
         pg.lightbox.style.position = "fixed";
         pg.lightbox.style.zIndex = "10";
         pg.lightbox.style.background = "rgba(0,0,0,.8)";
         pg.lightbox.style.top = 0;
         pg.lightbox.style.lefts = 0;
         pg.lightbox.addEventListener("click",mg.salirGaleria);

         pg.lightbox.appendChild(document.createElement("DIV")).setAttribute("id","modal");
         pg.modal=document.querySelector("#modal");
                  
         pg.modal.innerHTML= img.outerHTML+"<div> X </div>";
         
         
         pg.modal.style.display="block";
         pg.modal.style.position="absolute";
         if(img.height>=130){
            pg.modal.style.width="20%"
         }
         else{
            pg.modal.style.width="50%"
         }
         
         pg.modal.style.top="50%"
         pg.modal.style.left="50%"         
         pg.modal.style.marginLeft= -pg.modal.childNodes[0].width/2  + "px";
         pg.modal.style.marginTop = -pg.modal.childNodes[0].height/2 + "px";
               
         pg.modal.childNodes[0].style.width="100%"         
         pg.modal.childNodes[0].style.border="15px solid white"


         pg.modal.childNodes[1].style.position="absolute";
         pg.modal.childNodes[1].style.right="5px"
         pg.modal.childNodes[1].style.top="5px"
         pg.modal.childNodes[1].style.color="silver"
         pg.modal.childNodes[1].style.cursor="pointer"
         pg.modal.childNodes[1].style.fontSize="30px"
         pg.modal.childNodes[1].style.width="40px"
         pg.modal.childNodes[1].style.height="40px"
         pg.modal.childNodes[1].style.textAlign="center"
         pg.modal.childNodes[1].style.background="white"
         pg.modal.childNodes[1].style.borderRadius="0px 0px 0px 5px"
         
         pg.modal.childNodes[1].addEventListener("click", mg.salirGaleria)

     },
     salirGaleria:function(){    
         mg.reiniciarImg();         
		pg.lightbox.parentNode.removeChild(pg.lightbox);

    },
    reiniciarImg: function (){
        for(var i = 0; i < pg.imgGaleria.length; i++){            
            pg.imgGaleria[i].style.opacity=0;
       }

    }
 
 }
 
 mg.inicioGaleria();
 