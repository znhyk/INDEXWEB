function search_engine(keyword) {
    if (keyword.indexOf("1060") != -1) {
        window.location.href = "/gpu_index_500/series/1060";
    } else if (keyword.indexOf("1070") != -1) {
        window.location.href = "/gpu_index_500/series/1070";
    } else if (keyword.indexOf("1660") != -1) {
        window.location.href = "/gpu_index_500/series/1660";
    } else if (keyword.indexOf("2060") != -1) {
        window.location.href = "/gpu_index_500/series/2060";
    } else if (keyword.indexOf("2070") != -1) {
        window.location.href = "/gpu_index_500/series/2070";
    } else if (keyword.indexOf("2080") != -1) {
        window.location.href = "/gpu_index_500/series/2080";
    } else if (keyword.indexOf("3060") != -1) {
        window.location.href = "/gpu_index_500/series/3060";
    } else if (keyword.indexOf("3070") != -1) {
        window.location.href = "/gpu_index_500/series/3070";
    } else if (keyword.indexOf("3080") != -1) {
        window.location.href = "/gpu_index_500/series/3080";
    } else if (keyword.indexOf("3090") != -1) {
        window.location.href = "/gpu_index_500/series/3090";
    } else if (keyword.indexOf("470") != -1) {
        window.location.href = "/gpu_index_500/series/470";
    } else if (keyword.indexOf("480") != -1) {
        window.location.href = "/gpu_index_500/series/480";
    } else if (keyword.indexOf("570") != -1) {
        window.location.href = "/gpu_index_500/series/570";
    } else if (keyword.indexOf("580") != -1) {
        window.location.href = "/gpu_index_500/series/580";
    } else if (keyword.indexOf("5600") != -1) {
        window.location.href = "/gpu_index_500/series/5600";
    } else if (keyword.indexOf("5700") != -1) {
        window.location.href = "/gpu_index_500/series/5700";
    } else if (keyword.indexOf("6500") != -1) {
        window.location.href = "/gpu_index_500/series/6500";
    } else if (keyword.indexOf("6600") != -1) {
        window.location.href = "/gpu_index_500/series/6600";
    } else if (keyword.indexOf("6700") != -1) {
        window.location.href = "/gpu_index_500/series/6700";
    } else if (keyword.indexOf("6800") != -1) {
        window.location.href = "/gpu_index_500/series/6800";
    } else if (keyword.indexOf("6900") != -1) {
        window.location.href = "/gpu_index_500/series/6900";
    } else {
        alert("검색 결과가 없거나 검색어가 잘못되었습니다.");
    }
}

function get_year() {
    return 22;
}

function get_month() {
    var today = new Date();
    return today.getMonth() + 1;
}