function show(){ 
    var message = "<li>Simple Fruits</li>"
         message += "<li>Aggregate Fruits</li>"
         message += "<li>Multiple Fruits</li>"
         message += "<li>Dry Fruits</li>"
         message += "<li>Fleshy Fruits</li>"
    document.getElementById("test").innerHTML = message;
    }
    function unshow(){
       document.getElementById('test').innerHTML = '';
    }
    var elem = document.getElementById('test');
    elem.onmouseout = unshow;
   function reset(e)
   { 
       var target = e.target;
       target.textContent = "show cat";
   }
   function apple(){alert("Fleshy Fruits");}
   function cheeries(){alert("Simple Fruits");}   
   function drybeans(){alert("Dry Fruits");}
   function grains(){alert("Dry Fruits");}
   function nuts(){alert("Dry Fruits");}
   function peaches(){alert("Citrus Fruits");}
   function pear(){alert("Simple Fruits");}
   function pineapple(){alert("Multiple Fruits");}
   function pumpkin(){alert("Simple Fruits");}
   function strawberries(){alert("Aggregate Fruits");}
   function watermelon(){alert("Simple Fruits");}
   function oranges(){alert("Citrus Fruits");}
   function mango(){alert("Citrus Fruits");}
   function pawpaw(){alert("Simple Fruits");}
   function grape(){alert("Fleshy Fruits");}
   function coconut(){alert("Dry Fruits");}
   function banana(){alert("Citrus Fruits");}
   