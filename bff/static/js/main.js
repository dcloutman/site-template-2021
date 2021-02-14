document.addEventListener("DOMContentLoaded", function() {
    (function () {
        const start_time = (new Date()).getSeconds();
        const num_seconds_to_email_display = 5;
        const close_button = document.getElementById('overlay_content_email_signup_close_button');

        console.log(close_button);

        const email_display_interval = setInterval(function () {
            if (((new Date()).getSeconds() - num_seconds_to_email_display) > num_seconds_to_email_display) {
                document.body.classList.add("active_overlay");
                document.body.classList.add("email_signup");
                document.body.classList.add("blurry_face");


                clearInterval(email_display_interval);
            }
        }, 1000);

        close_button.addEventListener('click', function (e) {
            document.body.classList.remove("active_overlay");
            document.body.classList.remove("email_signup");
            document.body.classList.remove("blurry_face");


            e.stopPropagation();
        });
    })();
});

