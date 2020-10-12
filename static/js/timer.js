function initializeTimer() {
	var endDate = new Date(2018,2,28);
 
	var currentDate = new Date();
	var seconds = (endDate-currentDate) / 1000;
	if (seconds > 0) {
		var minutes = seconds/60; 
		var hours = minutes/60;
		var days = hours / 24;
		minutes = (hours - Math.floor(hours)) * 60; 
		days = Math.floor(days);
		hours =  Math.floor(hours)- days * 24; 
 
		seconds = Math.floor((minutes - Math.floor(minutes)) * 60); 
		minutes = Math.floor(minutes); 
 
		setTimePage(days, hours,minutes,seconds); 
 
		function secOut() {
		  if (seconds == 0) { 
			  if (minutes == 0) { 
				  if (hours == 0) { 
				  	   if(days == 0){
				  			showMessage(timerId); 
				  	    }
				  		else{
				  			days--; 
				  			hours = 24; 
						    minutes = 59; 
						    seconds = 59; 
				  		}
				  }
				  else {
					  hours--; 
					  minutes = 59; 
					  seconds = 59; 
				  }
			  }
			  else {
				  minutes--; 
				  seconds = 59; 
			  }
		  }
		  else {
			  seconds--; 
		  }
		  setTimePage(days, hours,minutes,seconds); 
		}
		timerId = setInterval(secOut, 1000) 
	}
	else {
		alert("������������ ���� ��� ������");
	}
}
window.onload = function()
{
     initializeTimer();
}

function setTimePage(d,h,m,s) {
	var days = document.getElementById("days");
	var hours = document.getElementById("hours");
	var minutes = document.getElementById("minutes");
	var seconds = document.getElementById("seconds");

	days.innerHTML = d;
	hours.innerHTML = h;
	minutes.innerHTML = m;
	seconds.innerHTML = s;

}

