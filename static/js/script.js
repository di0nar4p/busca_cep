document.addEventListener("DOMContentLoaded", function() {
    const cepInput = document.getElementById("cep");
    const form = document.getElementById("cep-form");

    cepInput.addEventListener("input", function() {
        this.value = this.value.replace(/\D/g, "");
    });

    form.addEventListener("submit", function(event) {
        cepInput.value = cepInput.value.replace(/\D/g, ""); 
        if (cepInput.value.length < 8) { 
            alert("Por favor, insira um CEP válido.");
            event.preventDefault(); 
        }
    });
});
