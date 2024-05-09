function follow_user(username, token) {
    let follow_btn = $("#follow")
    $.ajax({
        type: "post",
        url: `/user/${username}/follow/`,
        data: { csrfmiddlewaretoken: token },
        success: function (response) {
            let data = JSON.parse(response)
            follow_btn.attr('class', `btn ${data.followed}`);
            if (data.followed == 'True') { follow_btn.text('unfollow') }
            else { follow_btn.text('follow') }
        }
    });
}