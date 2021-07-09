$(document).ready(function() {
    // SideNav Button Initialization
    $(".button-collapse").sideNav2();
    // SideNav Scrollbar Initialization
    var sideNavScrollbar = document.querySelector('.custom-scrollbar');
    var ps = new PerfectScrollbar(sideNavScrollbar);
    //Activate Toast Messages
    $('.toast').toast('show');
    //Detect client time zone
    const timeZoneName = Intl.DateTimeFormat().resolvedOptions().timeZone;
    document.cookie = 'timezone=' + encodeURIComponent(timeZoneName) + '; path=/';
    // If side menu displaying run function during scrolling
    if($(".side-menu-col").is(':visible')) {
        $(window).on('scroll', function() {
            releaseFixedSidebar();
        });
    }
    /* Based upon "Make a Sidebar Always Visible Regardless of Scroll",
    by Łukasz Nojek, 4-20-20, https://lukasznojek.com/blog/2020/04/make-a-sidebar-always-visible-regardless-of-scroll/ */
    function releaseFixedSidebar() {
        const footer = $("footer");
        const topOfFooter = footer.offset().top;
        const sideMenuColumn = $(".side-menu-col");
        const sideMenu = $(".side-menu")
        const sideMenuHeight = sideMenu.outerHeight(false) + 20;
        const headerHeight = $("header").outerHeight(false);
        const scrollPosition = window.scrollY;
        console.log("height", headerHeight + sideMenuHeight);
        console.log("scrollPosition", scrollPosition);
        const sideMenuCalc = scrollPosition + (headerHeight + sideMenuHeight);
        console.log("sideMenuCalc", sideMenuCalc);
        console.log("topOfFooter", topOfFooter);
        const myWindow = $(window).height();
        // if side menu bottom higher than top of footer
        if(sideMenuCalc < topOfFooter) {
           $(sideMenuColumn).css({"position": "fixed"});
           $(sideMenu).css({"display": "block"});
        // if footer reaching bottom of side menu
        } else if((myWindow < sideMenuHeight) || (sideMenuCalc >= topOfFooter)) {
            //$(sideMenuColumn).css({"position": "static"});
            $(sideMenu).css({"display": "none"});
        }
    }
});
