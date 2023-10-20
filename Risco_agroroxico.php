<!DOCTYPE html>


<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
   
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
    

<?php
    require '/solo_local.php';
    require '/solo_carc.php';
    require '/agrotoxico.php';
    require '/resultado.php';

?>


<h1> 1 - Caracterizaçõ   de estudos </h1>

<div class="mb-3">
<form id="">
    <h2> Informações da área </h2>
    <label> precipitacao mm/ano</label>
    <input type='text' placeholder='mm/ano'> </input><br>

    <label> tx irrrigação mm/ano</label>
    <input type='text' placeholder='mm/ano'> </input><br>
    <label> evapotranspiracao mm/ano</label>
    <input type='text' placeholder='mm/ano'> </input><br>
</form>
</div>
<div class="mb-3">
<form id="aquifero">
<h2> Dados do aqífero </h2>
    <label> porosidade v/v</label>
    <input type='text' placeholder='v/v'> </input><br>
    <label> profundidade mm/ano</label>
    <input type='text' placeholder='mm/ano'> </input><br>
</form> 
</div>



<br>
<br>
<br>
<br>
<div class="mb-3">
<h2> Solo </h2>
<form>   
<h2> Dados do aqífero </h2><br>
    <label> Camadas</label>
    <br>
    <br><label> Camadas 1</label> <input type='number' placeholder='cm'> </input><input type='number' placeholder='cm'> </input>
   <br> <label> Camadas 2</label> <input type='number' placeholder='cm'> </input><input type='number' placeholder='cm'> </input>
    <br><label> Camadas 3</label> <input type='number' placeholder='cm'> </input><input type='number' placeholder='cm'> </input>
    
    
   

</form>
</div>

<form>
<label> evapotranspiracao mm/ano</label>
<br>
<br><label>Capacidade de Campo</label>
<input type='number' placeholder='cm'> </input>
<br><label>Densidade</label><br>
<input type='number' placeholder='cm'> </input>
<br>    <label>Carbono Organico</label><br>
<input type='number' placeholder='cm'> </input><br>
</form>

<form>
    <label> Carreamento Superfícial</label><br>
    <label> Pedra solo kg/ha</label>
    <input type='number' placeholder='cm'> </input><br>
    <label> Pedra água m³/ha</label>
    <input type='number' placeholder='cm'> </input><br>

</form>




<h1>Agoróxico</h1>

