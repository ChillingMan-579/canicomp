const selectMenu = document.querySelectorAll("select");
const currentTime = document.querySelector("h1");
const setAlarmBtn = document.querySelector("button");
const content = document.querySelector(".content")

let alarmTime, isAlarmSet=false;

for(let i = 12; i>0; i--){
  i = i<10 ? "0" + i : i;
  let option = `<option value="${i}">${i}</option>`
  selectMenu[0].firstElementChild.insertAdjacentHTML("afterend", option);
}

for(let i = 59; i>0; i--){
  i = i<10 ? "0" + i : i;
  let option = `<option value="${i}">${i}</option>`
  selectMenu[1].firstElementChild.insertAdjacentHTML("afterend", option);
}

for(let i = 2; i>0; i--){
  let ampm = i == 1 ? "AM" : "PM";
  let option = `<option value="${ampm}">${ampm}</option>`
  selectMenu[2].firstElementChild.insertAdjacentHTML("afterend", option);
}

setInterval(()=>{
  let date = new Date(),
    h = date.getHours(),
    m = date.getMinutes(),
    s = date.getSeconds(),
    ampm = "AM";

  if(h>= 12){
    h = h-12;
    ampm = "PM"
  }

  h = h<10?"0"+h:h;
  m = m<10?"0"+m:m;
  s = s<10?"0"+s:s;

  currentTime.innerText = `${h}:${m}:${s} ${ampm}`
  if(alarmTime == `${h}:${m} ${ampm}`){
    document.body.style.background = "red"
  }
}, 1000);

function setAlarm(){
  if(isAlarmSet){
    alarmTime = ""
    document.body.style.background = "linear-gradient(0deg, rgba(0,0,0,1) 0%, rgba(109,26,226,1) 0%, rgba(25,125,204,1) 69%, rgba(0,212,255,1) 98%);";
    content.classList.remove("disable")
    setAlarm.innerText = "SetAlarm";
    return isAlarmSet = false;
  }
  let time = `${selectMenu[0].value}:${selectMenu[1].value} ${selectMenu[2].value}`
  if(time.includes("Hour")||time.includes("Minute")||time.includes("AM/PM")){
    return alert("Please select a valid time")
  }
  alarmTime = time
  content.classList.add("disable")
  setAlarmBtn.innerText = "Clear Alarm"
}

setAlarmBtn.addEventListener("click", setAlarm)

function redirectPage(file){
  location.replace(file);
}
