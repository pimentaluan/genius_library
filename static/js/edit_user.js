function openModal() {
    document.getElementById('passwordModal').style.display = 'flex';
}

function closeModal() {
    document.getElementById('passwordModal').style.display = 'none';
}

window.onclick = function(event) {
    const modal = document.getElementById('passwordModal');
    if (event.target == modal) {
        closeModal();
    }
}
