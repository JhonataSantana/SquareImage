import data from '../options.json' assert {type:'json'};

console.log(data);

setTimeout(()=>{
    const loader = document.getElementById('loader');
    loader.remove();
}, 2000);