let search = document.querySelector('.user_search');

search.oninput = (e) => {
    let val = e.target.value.trim();
    let searchItems = document.querySelectorAll('.user_data')
    let searchRow = document.querySelectorAll('.user_data_row')
    if (val !== ''){
        searchItems.forEach((e) =>{
            let row = e.closest('.user_data_row');
            if (e.textContent.search(val) === -1){
                row.classList.add('hidden')
            }
            else {
                row.classList.remove('hidden');
            }
        })
    }
    else{
        searchItems.forEach((e) =>{
            let row = e.closest('.user_data_row');
            row.classList.remove('hidden');
        })
    }
};
