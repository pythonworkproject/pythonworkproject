// Search implementation
$(document).ready(function() {

    $("#search1").on("keyup", function() {

        var value = $(this).val().toLowerCase();
        $("#employee1 tr").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
});