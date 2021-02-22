document.addEventListener("DOMContentLoaded", function() {
    (function () {
        const start_time = (new Date()).getTime();
        const num_milliseconds_until_email_lightbox = 10000;
        const close_button = document.getElementById('lightbox_content_email_signup_close_button');


        const email_display_interval = setInterval(function () {
            let do_not_show_email_lightbox_until = null;
            if (((new Date()).getTime() - start_time) > num_milliseconds_until_email_lightbox) {
                do_not_show_email_lightbox_until = window.localStorage.getItem("do_not_show_email_lightbox_until");

                if (
                    -1 !== do_not_show_email_lightbox_until &&
                    (
                        null === do_not_show_email_lightbox_until ||
                        (new Date()).getTime() >= do_not_show_email_lightbox_until
                    )
                ) {
                    document.body.classList.add("active_lightbox");
                    document.body.classList.add("email_signup");
                    document.body.classList.add("blurry_face");

                    clearInterval(email_display_interval);
                }
            }
        }, 10000);

        /* Close email signup lightbox without submission. */
        close_button.addEventListener("click", function (e) {
            document.body.classList.remove("active_lightbox");
            document.body.classList.remove("email_signup");
            document.body.classList.remove("blurry_face");

            // Add a record to local storage to prevent displaying popup for one day.
            // window.localStorage.setItem("do_not_show_email_lightbox_until", (new Date).getTime() + (1000 * 60)); // DEBUG: Display again after one minute.
            window.localStorage.setItem("do_not_show_email_lightbox_until", (new Date).getTime() + (1000 * 60 * 60 * 24));

            e.stopPropagation();
        });
    })();
});

