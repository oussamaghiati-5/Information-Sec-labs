(function () {
    function getCookie(name) {
        const match = document.cookie.match(new RegExp('(?:^|; )' + name + '=([^;]*)'));
        return match ? match[1] : null;
    }

    function randomId() {
        return Math.random().toString(16).slice(2) + Date.now().toString(16);
    }

    let id = getCookie("analytics_id");
    if (!id) {
        id = randomId();
        // no Domain attribute set -> defaults to the current document's host,
        // i.e. whichever publisher is executing this script
        document.cookie = "analytics_id=" + id + "; path=/; max-age=31536000";
    }

    console.log("analytics_id:", id);
})();