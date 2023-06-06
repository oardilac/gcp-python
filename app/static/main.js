$(document).ready(function() {
    $('#doReplicar').click(function() {
        if ($('#destino').val() == "") {
            $('.console-text').append("---------------------------------------\r\n");
            $('.console-text').append("Replicating\r\n");
            $('.console-text').append("No target table\r\n");
            return;
        }

        $('.console-text').append("---------------------------------------\r\n");
        $('.console-text').append("Replicating\r\n");
        $('.console-text').append("Source: " + $('#source').val() + "\r\n");
        $('.console-text').append("Target: raw." + $('#destino').val() + "\r\n");
        
        var api_url = 'https://copy-table-mysql-to-bigquery-ywtk7siozq-wn.a.run.app/?table_source=' + $('#source').val() + '&table_destination=' + $('#destino').val();
        console.debug('api call: ' + api_url);

        $.ajax({
            url: api_url,
            method: 'GET',
            async: false, 
            success: function(response) {
                if (response.result == "ok") {
                    $('.console-text').append("Result: OK\r\n");
                } else {
                    $('.console-text').append("Error: " + response.description + "\r\n");
                }
            },
            error: function(xhr, status, error) {
                $('.console-text').append("Error: Unknown\r\n");
            }
        });

        var url_api = 'https://get-rows-from-bigquery-ywtk7siozq-wn.a.run.app/?table_name=' + $('#destino').val();

        $.ajax(url_api).done(function(response) {
            if (response.result == "ok") {
                $('.console-text').append("Testing: " + $('#destino').val() + " ~ " + response.rows + " rows in target\r\n");
            } else {
                $('.console-text').append("Testing Error: " + response.description + "\r\n");
            }
        });
    });

    $('#source').change(function() {
        var table = $('#source').val();
        $('#destino').val(table);
    });       
});
