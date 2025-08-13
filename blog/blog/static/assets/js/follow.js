//
//function getCookie(name) {
//    let cookieValue = null;
//    if (document.cookie && document.cookie !== '') {
//        let cookies = document.cookie.split(';');
//        for (let i = 0; i < cookies.length; i++) {
//            let cookie = cookies[i].trim();
//            if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                break;
//            }
//        }
//    }
//    return cookieValue;
//}
//let csrftoken = getCookie('csrftoken');
//
//$.ajaxSetup({
//    headers: { "X-CSRFToken": csrftoken }
//});
//
//

$(document).ready(function () {
    $(document).on('click', '.follow-button', function (e) {
        e.preventDefault();

        var button = $(this);
        var user_id = button.data('user_id');
        var csrfToken = $("input[name='csrfmiddlewaretoken']").val();

        $.ajax({
            type: 'POST',
            url: "/blog/user-follow/",
            data: {
                'user_id': user_id,
                'csrfmiddlewaretoken': csrfToken
            },
            success: function (data) {
                if (data.follow) {
                    button.removeClass('btn-primary').addClass('btn-outline-danger')
                        .html('<i class="bi bi-person-dash"></i> Unfollow');
                } else {
                    button.removeClass('btn-outline-danger').addClass('btn-primary')
                        .html('<i class="bi bi-person-plus"></i> Follow');
                }

                // پیدا کردن و آپدیت شمارنده‌ها
                button.closest('.user-card, .profile-container')
                    .find('.follower_count').text(data.follower_count);
                button.closest('.user-card, .profile-container')
                    .find('.following_count').text(data.following_count);
            }
        });
    });
});

