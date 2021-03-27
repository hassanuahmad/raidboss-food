// Google Signin to console info
function onSignIn(googleUser) {
    var profile = googleUser.getBasicProfile();
    console.log("ID: " + profile.getId()); // Do not send to your backend! Use an ID token instead.
    console.log("Name: " + profile.getName());
    console.log("Image URL: " + profile.getImageUrl());
    console.log("Email: " + profile.getEmail()); // This is null if the 'email' scope is not present.
  }
  
  function handleSubmit() {
    const getPostalCode = document.getElementById("postal-code").value;
    const getDistance = document.getElementById("distance").value;
  
    localStorage.setItem("POSTALCODE", getPostalCode);
    localStorage.setItem("DISTANCE", getDistance);
  }
  
  // Taking the postal code and displaying it on the search.html page to see the entire sentence at the top
  window.addEventListener("load", () => {
    const postalCode = localStorage.getItem("POSTALCODE");
    const distance = localStorage.getItem("DISTANCE");
  
    document.getElementById("result-postalCode").innerHTML = postalCode;
    document.getElementById("result-distance").innerHTML = distance;
  });
  