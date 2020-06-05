
 let fetchBtn = document.getElementById('fetch-btn2');
 let baiLam = document.getElementById("ajax-lab2");

 let data = null;

 const url = "https://vuggg.github.io/files.html";
 let xhr = new XMLHttpRequest();

 
 xhr.onerror = ()=>{
     alert("Error")
 }
 function createTable(data, node){
     let table = document.createElement("table");
     
     table.insertAdjacentHTML("afterbegin",`<thead><tr> 
         <th>Name </th><th>Age</th><th>Number of Cars </th>
         <th>Name of Cars </th></tr><thead>`)
     
     node.prepend(table);
     let tableData = null;
     let rows = "";
     for(let i = 0;i <data.length;i++){
         let row = "<tr><td>" +data[i].name+ "</td>" + 
             "<td>" +data[i].age+"</td>" +
             "<td>" +data[i].cars.length + "</td></tr>";
        
         
         rows = rows + row;
     }
     tableData = "<tbody>" + rows + "<tbody>";
     
     table.insertAdjacentHTML("afterbegin",tableData);
     node.append(table);
     console.log(tableData)
 }
 xhr.onreadystatechange = ()=>{
     if(xhr.readyState == 4){
         console.log(xhr.responseText);
         const response = xhr.responseText;
         
         data = JSON.parse(response);
         console.log(data)
         baiLam.innerHTML = "";
         createTable(data, baiLam);
         
     }
 }
 
 fetchBtn.onclick = ()=>{
     xhr.open("GET",url,true);
     xhr.send();
 }
}