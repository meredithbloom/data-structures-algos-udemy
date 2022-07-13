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