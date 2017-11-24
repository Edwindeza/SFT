$(function(){
    $('.select2').select2({
        placeholder: 'Seleccione sus instrumentos',
        width: '100%'
    });

    var cliente = $('input[name="es_cliente"]');

    cliente.change(function(){
        // Si no es cliente
        if (parseInt($(this).val()) === 0) {
            $('.no-es-cliente').show();
        } else {
            $('.no-es-cliente').hide();
            $('.es-cliente').show();
        }
    });

    $('#hora_inicio').timepicker({
        timeFormat: 'HH:mm:ss',
        interval: 60,
        minTime: '10',
        maxTime: '6:00pm',
        defaultTime: '11',
        startTime: '10:00',
        dynamic: false,
        dropdown: true,
        scrollbar: true
    });

    $('#hora_fin').timepicker({
        timeFormat: 'HH:mm:ss',
        interval: 60,
        minTime: '10',
        maxTime: '6:00pm',
        defaultTime: '11',
        startTime: '10:00',
        dynamic: false,
        dropdown: true,
        scrollbar: true
    });

    $('.datepicker').datepicker({
        altFormat: "yy-mm-dd",
        altField: "#fecha_reserva"
    });
});
