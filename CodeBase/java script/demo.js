const array=[12,1321,1243,-341,41,-314,-1414]
function removeneg(number,callback){
  number.forEach(number=>{if(callback(number)){
    console.log(number)
  }})
  }
removeneg(array,x=>x>0)