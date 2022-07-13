'hello'.length // always has length of O(1) because .length is a built in js method so we aren't have to count each character from scratch. make sure to check operation complexity for different languages


//----- SPACE COMPLEXITY -----//

function booooo(n) {
	for (let i = 0; i < n.length; i++) {
		console.log('boooooo!')
	}
}

booooo([1, 2, 3, 4, 5])

// time complexity is O(n), because number of steps will increase linear to size of input
// space complexity is O(1), because the function doesn't take up more space given the size of input. it only ever creates one variable (i)


function arrayOfHiNTimes(n) {
	let hiArray = [];
	for (let i = 0; i < n; i++) {
		hiArray[i] = 'hi';
	}
	return hiArray;
}

arrayOfHiNTimes(6)

// space complexity - O(n). we are adding a new array, which grows in memory linear to size of input
// time complexity - also O(n)







//----- TIME COMPLEXITY -----//


// What is the Big O of the below function? (Hint, you may want to go line by line)
function funChallenge(input) {
	let a = 10; // o(1)
	a = 50 + 3; // o(1)

	for (let i = 0; i < input.length; i++) { // o(n)
		anotherFunction(); // o(n)
		let stranger = true; // o(n)
		a++; // o(n)
	}
	return a; // o(1)
}
// BIG O - O(n)



function anotherFunChallenge(input) {
	let a = 5; // o(1)
	let b = 10; // o(1)
	let c = 50; // o(1)
	for (let i = 0; i < input; i++) { // o(n), number of loops will increase depending on input
		let x = i + 1; // o(n)
		let y = i + 2; // o(n)
		let z = i + 3; // o(n)

	}
	for (let j = 0; j < input; j++) { // o(n), number of loops will increase depending on input
		let p = j * 2; // o(n)
		let q = j * 2; // o(n)
	}
	let whoAmI = "I don't know"; // o(1)
}

// BIG O - O(n)