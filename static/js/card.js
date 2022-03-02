function make_data_array(raw_data_array, day) {
	var array_length = (raw_data_array.length / (day + 2));
	var data_array = new Array(array_length);
	for (var i = 0; i < array_length; i++) {
		data_array[i] = new Array(day + 2);
		for (var j = 0; j < day + 2; j++) {
			data_array[i][j] = raw_data_array[i * (day + 2) + j]
		}
	}
    return data_array;
}

function make_card(data_array, year, month, day) {
	var today = new Date();
	var user_day = today.getDate();
	
	if((day - user_day) > 0){
		month--;
	}
	
	var html = "<div class=\"d-sm-flex align-items-center justify-content-between mb-4\"><h1 class=\"h3 mb-0 text-gray-800\">";
	if (data_array[0][1].indexOf("1060") != -1) {
		html += "Nvidia Geforce GTX 1060</h1></div>";
	} else if (data_array[0][1].indexOf("1070") != -1) {
		html += "Nvidia Geforce GTX 1070</h1></div>";
	} else if (data_array[0][1].indexOf("1660") != -1) {
		html += "Nvidia Geforce GTX 1660</h1></div>";
	} else if (data_array[0][1].indexOf("2060") != -1) {
		html += "Nvidia Geforce RTX 2060</h1></div>";
	} else if (data_array[0][1].indexOf("2070") != -1) {
		html += "Nvidia Geforce RTX 2070</h1></div>";
	} else if (data_array[0][1].indexOf("2080") != -1) {
		html += "Nvidia Geforce RTX 2080</h1></div>";
	} else if (data_array[0][1].indexOf("3060") != -1) {
		html += "Nvidia Geforce RTX 3060</h1></div>";
	} else if (data_array[0][1].indexOf("3070") != -1) {
		html += "Nvidia Geforce RTX 3070</h1></div>";
	} else if (data_array[0][1].indexOf("3080") != -1) {
		html += "Nvidia Geforce RTX 3080</h1></div>";
	} else if (data_array[0][1].indexOf("3090") != -1) {
		html += "Nvidia Geforce RTX 3090</h1></div>";
	} else if (data_array[0][1].indexOf("470") != -1) {
		html += "AMD Radeon RX 470</h1></div>";
	} else if (data_array[0][1].indexOf("480") != -1) {
		html += "AMD Radeon RX 480</h1></div>";
	} else if (data_array[0][1].indexOf("570") != -1) {
		html += "AMD Radeon RX 570</h1></div>";
	} else if (data_array[0][1].indexOf("580") != -1) {
		html += "AMD Radeon RX 580</h1></div>";
	} else if (data_array[0][1].indexOf("5600") != -1) {
		html += "AMD Radeon RX 5600</h1></div>";
	} else if (data_array[0][1].indexOf("5700") != -1) {
		html += "AMD Radeon RX 5700</h1></div>";
	} else if (data_array[0][1].indexOf("6500") != -1) {
		html += "AMD Radeon RX 6500</h1></div>";
	} else if (data_array[0][1].indexOf("6600") != -1) {
		html += "AMD Radeon RX 6600</h1></div>";
	} else if (data_array[0][1].indexOf("6700") != -1) {
		html += "AMD Radeon RX 6700</h1></div>";
	} else if (data_array[0][1].indexOf("6800") != -1) {
		html += "AMD Radeon RX 6800</h1></div>";
	} else if (data_array[0][1].indexOf("6900") != -1) {
		html += "AMD Radeon RX 6900</h1></div>";
	}
	for (var i = 0; i < data_array.length; i++) {
		var temp = "";
		temp = "<a href=\"/specific/" + data_array[i][0] + "/" + year + "/" + month + "\"><div class=\"col-xl-10 col-md-10 mb-4\"><div class=\"card border-left-primary shadow h-100 py-2\"><div class=\"card-body\"><div class=\"row no-gutters align-items-center\"><div class=\"col mr-2\"><div class=\"text-xs font-weight-bold text-primary text-uppercase mb-1\">";
		temp += data_array[i][1];
		temp += "</div><div class=\"h5 mb-0 font-weight-bold text-gray-800\"><small>KRW</small>";
		temp += data_array[i][day + 1] + "<br>";
		temp += "</div></div><div class=\"col-auto\"><ruby>";
		if (data_array[i].length < 4) {
			temp += "<i class=\"fas fa-sort-down fa-2x text-primary\">집계중</i><rp><rt class=\"text-right\"></rt></rp></ruby></div></div></div></div></div></a>";
		} else if (data_array[i][day + 1] - data_array[i][day] > 0) {
			temp += "<i class=\"fas fa-sort-up fa-2x text-danger\">" + (data_array[i][day + 1] - data_array[i][day]) + "</i><rp><rt class=\"text-right\">전일대비</rt></rp></ruby></div></div></div></div></div></a>";
		} else if (data_array[i][day + 1] - data_array[i][day] < 0) {
			temp += "<i class=\"fas fa-sort-down fa-2x text-primary\">" + (data_array[i][day] - data_array[i][day + 1]) + "</i><rp><rt class=\"text-right\">전일대비</rt></rp></ruby></div></div></div></div></div></a>";
		} else {
			temp += "<i class=\"fas fa-2x text-secondary\">0</i><rp><rt class=\"text-right\"></rt></rp></ruby></div></div></div></div></div></a>";
		}
		html += temp;
	}
	
    document.getElementById("card_container").innerHTML = html;
	
    return;
}