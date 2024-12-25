function deletePenyewa(id) {
    var confirmation = confirm("Apakah Anda yakin ingin menghapus penyewa ini?");
    if (confirmation) {
        var form = document.createElement('form');
        form.method = 'POST';  
        form.action = '/deletepenyewa/' + id;  
        document.body.appendChild(form);
        form.submit();
    }
}

function downloadPDF() {
    const paymentContainer = document.querySelector('.payment-container');
    const button = document.querySelector('.btn');

    if (!paymentContainer) {
        alert("Payment container tidak ditemukan!");
        return;
    }

    button.style.display = 'none';

    const options = {
        margin: 10,
        filename: 'Payment_Details.pdf',
        html2canvas: { scale: 2 },
        jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' }
    };

    html2pdf()
        .set(options)
        .from(paymentContainer)
        .save()
        .finally(() => {
            button.style.display = 'block';
        });
}

const today = new Date().toISOString().split('T')[0];
document.getElementById('tanggal_penyewaan').setAttribute('min', today);


