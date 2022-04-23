// Onclick of the button
document.querySelector("button").onclick = function () {
// Call python's random_python function
eel.multiply(intj, intj)(function(number){
	// Update the div with a random number returned by python
	document.querySelector(".addition").innerHTML = number;
})
}
