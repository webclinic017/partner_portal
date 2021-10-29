
// Buscar titulos em aberto do cliente
function getReceivableTitles(contract_id) {
    $('#id_title_list div').remove();
    var myModal = new bootstrap.Modal(document.getElementById('modalReceivableTitles'), {
        keyboard: false
    });
    myModal.show();
    
    fetch(`${contract_id}/titulos-em-aberto/`, {method: 'GET'})
        .then(response => response.json())
        .then(data => {
            
            var date = new Date();
            var now = new Date(date.getFullYear(), date.getMonth(), date.getDay());
            let row = '';
            
            for (const obj of data.title_list) { 
                
                var border = "border-0";
                var textColor = "text-dark";
                var date = new Date(obj.expiration_date);
                
                if( now >= date ) {
                    border = "border-danger border-1 shadow-lg";
                    textColor = "text-danger";
                }
                
                row += `
                <div class="col-md-4 col-12 mb-15">
                    <div class="card shadow p-2 ${border}">
                        
                        <div class="card-body pb-30">

                            <div class="row">

                                <div class="col-12 pt-10">
                                    
                                    <h5 class="text-primary">
                                        ${ obj.title }
                                    </h5>
                                    
                                </div>


                                <div class="col-12 pt-10">
                                    
                                    <h1 style="font-size: 32px;">
                                        <b>R$ ${ obj.balance }</b>
                                    </h1>
                                    
                                </div>

                                <div class="col-12 text-left">
                                    
                                    <span class="${textColor}">
                                        Vencimento: ${obj.expiration_date.replace(/(\d*)-(\d*)-(\d*).*/, '$3/$2/$1') }
                                    </span>
                                    
                                    
                                </div>

                                <div class="col-12 pt-30">
                                    
                                    <button onclick="createPix(${obj.id});" class="btn btn-outline-primary" data-bs-target="#modalReceivableTitles2" data-bs-toggle="modal" data-bs-dismiss="modal">
                                        Pagar <i class="lni lni-arrow-right"></i>
                                    </button>
                                    
                                </div>
                                

                            </div>

                        </div>
                        
                    </div>
                </div>
                `;
                
            };

            $('#id_title_list').append(row);
            
        })
        .catch(console.error);
}


function createPix(receivable_title_id) {
    $('#id_frt_modal_body_2 div').remove();
    var spinner = `
        <div class="row p-1 align-items-center min-vh-75">
            <div class="col-12">
                <div class="d-flex justify-content-center">
                <div class="spinner-border" style="width: 3rem; height: 3rem;" role="status">
                    <span class="visually-hidden">Loading...</span>
                </div>
                </div>
            </div>
        </div>
    `;

    $('#id_frt_modal_body_2').append(spinner);

    fetch(`${receivable_title_id}/cobranca/`, {method: 'GET'})
        .then(response => response.json())
        .then(data => {
            
            // console.log(data.data.valor.original);
            // $('#id_pix_value').html(data.data.valor.original);
            // $('#id_pix_code').val(data.data.txid);

            $('#id_frt_modal_body_2 div').remove();

            var modal = `
            <div class="row p-1 align-items-center min-vh-40">
                                
                <div class="col-md-12 text-center text-light " style="padding-bottom: 50px;">

                    <p class="" style="font-size: 24px;">
                        Falta pouco! Copie e cole o código a seguir em seu app de pagamentos.
                    </p>
                    
                </div>
            
            </div>

            <div class="row p-1 min-vh-40">

                <div class="col-md-12">

                    <div class="card border-0 p-2 shadow" style="margin-top: -50px;">

                        <div class="card-body pb-25">
                            
                            <div class="mb-3">
                                <b>Valor do PIX a pagar: R$ ${data.data.valor.original}</b>
                            </div>

                            <div class="mb-3">
                                <input id="id_pix_code" type="text" class="form-control bg-white" value="${data.data.textoImagemQRcode}" readonly>
                            </div>

                            <div class="mb-3">
                                <small>
                                    Código válido por 30 minutos. 
                                </small>
                            </div>
                            
                            <div class="d-grid gap-2">
                                <button onclick="copyPixCode();" class="btn btn-primary" type="button" >Copiar código</button>
                            </div>

                        </div>

                    </div>

                </div>
            
            </div>
            
            `;

            $('#id_frt_modal_body_2').append(modal);
            
        })
        .catch(console.error);

}


function copyPixCode() {
    var copyText = document.getElementById("id_pix_code");
    copyText.select();
    copyText.setSelectionRange(0, 99999)
    document.execCommand("copy");
    snackbar();
}

function snackbar() {
    var x = document.getElementById("snackbar");
    x.className = "show";
    setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
}

