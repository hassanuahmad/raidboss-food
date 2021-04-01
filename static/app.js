// Google Signin to console info
// function onSignIn(googleUser) {
//  var profile = googleUser.getBasicProfile();
//  console.log("Name: " + profile.getName());
//  console.log("Image URL: " + profile.getImageUrl());
//  console.log("Email: " + profile.getEmail()); // This is null if the 'email' scope is not present.
//}
// leaving that in case you want to revert


function attemptSignIn() {
  var provider = new firebase.auth.GoogleAuthProvider;
  firebase.auth().signInWithRedirect(provider);
  login(user);
}

function signOut() {
  firebase.auth().signOut();
  location.reload();
}

function login(user) {
  function newLoginHappened(user) {
    if (user) {
      //user is signed in
      app(user)
    }
  }
}
function app(user) {
  document.getElementById("signinbtn").style.display = "none";
  document.getElementById("userDisplay").innerHTML = "Howdy " + user.displayName + "!";
  document.getElementById('userPhoto').src = user.photoURL;
}
