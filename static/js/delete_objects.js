const deleteReservation = document.querySelectorAll('.delete_button_res');
const deleteJet = document.querySelectorAll('.delete_button_jet');
const deleteContact = document.querySelectorAll('.delete_button_con');
const deleteRates = document.querySelectorAll('.delete_button_rate');

// Функция для удаления объекта и обновления отображения
async function deleteObject(url, objectType, objectContainer) {
    try {
        const response = await fetch(url, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': csrfToken
            }
        });

        if (response.ok) {
            console.log(`${objectType} deleted successfully.`);
            objectContainer.remove();
        } else {
            console.error(`Failed to delete ${objectType}.`);
        }
    } catch (error) {
        console.error('An error occurred:', error);
    }
}

deleteReservation.forEach(button => {
    button.addEventListener('click', (e) => {
        e.preventDefault();
        const url = e.currentTarget.getAttribute('href');
        const objectType = e.currentTarget.getAttribute('data-object-type');
        const objectContainer = e.currentTarget.closest('.appeal_box');

        deleteObject(url, objectType, objectContainer);
    });
});

deleteJet.forEach(button => {
    button.addEventListener('click', (e) => {
        e.preventDefault();
        const url = e.currentTarget.getAttribute('href');
        const objectType = e.currentTarget.getAttribute('data-object-type');
        const objectContainer = e.currentTarget.closest('.appeal_box_jet');

        deleteObject(url, objectType, objectContainer);
    });
});

deleteContact.forEach(button => {
    button.addEventListener('click', (e) => {
        e.preventDefault();
        const url = e.currentTarget.getAttribute('href');
        const objectType = e.currentTarget.getAttribute('data-object-type');
        const objectContainer = e.currentTarget.closest('.appeal_box_contact');

        deleteObject(url, objectType, objectContainer);
    });
});

deleteRates.forEach(button => {
    button.addEventListener('click', (e) => {
        e.preventDefault();
        const url = e.currentTarget.getAttribute('href');
        const objectType = e.currentTarget.getAttribute('data-object-type');
        const objectContainer = e.currentTarget.closest('.appeal_box_reservation');

        deleteObject(url, objectType, objectContainer);
    });
});
