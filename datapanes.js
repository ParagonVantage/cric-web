$(document).ready(function() {
    function initializeDataTable(tableId, filterColumns, numColumns) {
        $(tableId).DataTable({
            dom: 'Pfrtip',
            searchPanes: {
                cascadePanes: true,
                columns: filterColumns
            },
            columnDefs: [
                { searchPanes: { show: true }, targets: filterColumns },
                { type: 'num', targets: Array.from({length: numColumns}, (_, i) => i + 2), render: function(data, type) {
                    if (type === 'sort' && data === '#DIV/0!') {
                        return -Infinity;
                    } else if (data === '#DIV/0!' || data === "") {
                        return '-';
                    }
                    return data;
                }}
            ]
        });
    }
    initializeDataTable('#myTable1', [0, 1], 15);
    initializeDataTable('#myTable2', [0, 1], 13);
    initializeDataTable('#myTable3', [0, 1], 13); // Adjusted number of columns for myTable3
    initializeDataTable('#myTable4', [0, 1], 13);
});