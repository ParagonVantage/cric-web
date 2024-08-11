$(document).ready(function() {
    function initializeDataTable(tableId, filterColumns) {
        var numColumns = $(tableId + ' thead th').length; // Get the number of columns dynamically
        var table = $(tableId).DataTable({
            dom: 'Pfrtip',
            searchPanes: {
                cascadePanes: true,
                columns: filterColumns
            },
            columnDefs: [
                { searchPanes: { show: true }, targets: filterColumns },
                { type: 'num', targets: Array.from({length: numColumns - 2}, (_, i) => i + 2), render: function(data, type) {
                    if (type === 'sort' && data === '#DIV/0!') {
                        return -Infinity;
                    } else if (data === '#DIV/0!' || data === "") {
                        return '-';
                    }
                    return data;
                }}
            ]
        });

        // Apply fade-in effect to each cell after the table is drawn
        $(tableId).on('draw.dt', function() {
            $(tableId + ' tbody td').css('opacity', '0').animate({ opacity: 1 }, 500);
        });
    }
    
    // Initialize all tables
    initializeDataTable('#myTable1', [0, 1]);
    initializeDataTable('#myTable2', [0, 1]);
    initializeDataTable('#myTable3', [0, 1]);
    initializeDataTable('#myTable4', [0, 1]);
});
