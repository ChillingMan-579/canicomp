let hours = document.getElementById("hours");
let minutes = document.getElementById("minutes");
let seconds = document.getElementById("seconds");
let day = document.getElementById("day");
let month = document.getElementById("month");
let year = document.getElementById("year");

const days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", ]
const months= ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

function setTime(){
  let now = new Date();
  hours.innerHTML = (now.getHours() < 10 ? "0" : "") + now.getHours();
  minutes.innerHTML = (now.getMinutes() < 10 ? "0" : "") + now.getMinutes();
  seconds.innerHTML = (now.getSeconds() < 10 ? "0" : "") + now.getSeconds();
  day.innerHTML = days[now.getDay()];
  month.innerHTML = months[now.getMonth()] + " ";
  year.innerHTML = now.getFullYear();
}

function redirectPage(file){
  location.replace(file);
}

setInterval(setTime, 1000);

setTime()