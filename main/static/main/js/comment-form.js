function CommentReplyToggle(parent_id) {
    const row = document.getElementById(parent_id);
    console.log(parent_id)
    if ($('#' + parent_id).is(':hidden')) {
        $('#' + parent_id).hide()
        show_form()
        $('#' + parent_id).fadeIn(300)
        function show_form(){
            row.classList.remove('d-none')
        }
    } else {
        $('#' + parent_id).fadeOut(300)
        setTimeout(hide_form, 300)
        function hide_form(){
            row.classList.add('d-none')
        }
    }
}