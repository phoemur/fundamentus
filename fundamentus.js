var dataInput = {'pl_min':'',
            'pl_max':'',
            'pvp_min':'',
            'pvp_max' :'',
            'psr_min':'',
            'psr_max':'',
            'divy_min':'',
            'divy_max':'',
            'pativos_min':'',
            'pativos_max':'',
            'pcapgiro_min':'',
            'pcapgiro_max':'',
            'pebit_min':'',
            'pebit_max':'',
            'fgrah_min':'',
            'fgrah_max':'',
            'firma_ebit_min':'',
            'firma_ebit_max':'',
            'margemebit_min':'',
            'margemebit_max':'',
            'margemliq_min':'',
            'margemliq_max':'',
            'liqcorr_min':'',
            'liqcorr_max':'',
            'roic_min':'',
            'roic_max':'',
            'roe_min':'',
            'roe_max':'',
            'liq_min':'',
            'liq_max':'',
            'patrim_min':'',
            'patrim_max':'',
            'divbruta_min':'',
            'divbruta_max':'',
            'tx_cresc_rec_min':'',
            'tx_cresc_rec_max':'',
            'setor':'',
            'negociada':'ON',
            'ordem':'1',
            'x':'28',
            'y':'16'
};

var htmlTable = '';

$.ajax({
   type: 'POST',
   url:'http://www.fundamentus.com.br/resultado.php',
   headers: {
   		'Accept': 'text/html, text/plain, text/css, text/sgml, */*;q=0.01'
   },
   data: dataInput,
   success: function(data, textStatus, request){
        var dataOutput = data;
        // console.log(dataOutput);

        var htmlData = $.parseHTML(data);
        // console.log(htmlData);

        htmlTable = htmlData[23].children[1];
        console.log(htmlTable);

        $('#info').append(htmlTable);
   },
   error: function (request, textStatus, errorThrown) {
        console.log(errorThrown);
   }
});