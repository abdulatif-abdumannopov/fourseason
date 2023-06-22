let form = document.querySelector('#edit_form');
let button = document.querySelector('#edit_button');
let userPk = form.dataset.userPk

button.addEventListener('click', (e) => {
    e.preventDefault();

    let formData = new FormData(form);
    formData.append('custom_field', 'custom_value');

    let url = `/edit/${userPk}`
    console.log(url)

    fetch(url, {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': '{{ csrf_token }}'
        }
    })
    .then(response => {
        if (response.ok) {
            console.log('User data updated successfully.');
        } else {
            console.error('Failed to update user data.');
        }
    })
    .catch(error => {
        console.error('An error occurred:', error);
    });
});
