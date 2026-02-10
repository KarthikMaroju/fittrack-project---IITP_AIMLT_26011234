function addWorkout() {
  let workout = document.getElementById("workout").value;

  if (workout === "") {
    alert("Please enter a workout");
    return;
  }

  let li = document.createElement("li");
  li.textContent = workout;

  document.getElementById("workoutList").appendChild(li);
  document.getElementById("workout").value = "";
}

