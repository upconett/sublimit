$(document).ready(function () {
    $('#edit_field').on('input', function() {
        $('.preview').html(
            marked.parse($(this).val())
        );
    })
})