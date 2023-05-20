let minus_child = document.querySelector('.rates_minus_child')
let plus_child = document.querySelector('.rates_plus_child')
let plus = document.querySelector('.rates_plus')
let minus = document.querySelector('.rates_minus')
let adult = document.querySelector('.rates_count')
let child = document.querySelector('.rates_count_child')
let num = Number(adult.textContent)
let child_num = Number(child.textContent)
let button = document.querySelector('.rates_button')
let adult_input = document.querySelector('.rates_count_input')
let children_input = document.querySelector('.rates_count_input_children')

plus.addEventListener('click', () => {
    num += 1
    adult.textContent = num.toString()
})
minus.addEventListener('click', () => {
    if (num > 1){
        num -= 1
        adult.textContent = num.toString()
    }
})
plus_child.addEventListener('click', () => {
    child_num += 1
    child.textContent = child_num.toString()
})
minus_child.addEventListener('click', () => {
    if (child_num > 0){
        child_num -= 1
        child.textContent = child_num.toString()
    }
})

button.addEventListener('click', () => {
    adult_input.value = adult.textContent
    children_input.value = child.textContent
    console.log(adult_input.value, children_input.value)
})