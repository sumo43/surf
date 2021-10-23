
chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
    let url = tabs[0].url

    let text_string = "this is a test, the url is " + url

    port = chrome.runtime.connectNative('com.surf.surf_search')


    port.onMessage.addListener(function(msg) {
      console.log("Received: " + msg)
    })

    console.log("the url is " + url)

    port.postMessage({text: "This Works!"})
})

/**
let headers = new Headers()
let params = new URLSearchParams()

var init = { method: 'POST'}
        
let req = new Request(ADDRESS, init)

fetch(req).then(function(response) {
    console.log('request sent')
    console.log(response)
})
.catch(function(error) {
    console.log(error)
}
) 

var port = chrome.runtime.connectNative('com.my_company.my_application');
port.onMessage.addListener(function(msg) {
  console.log("Received" + msg);
});
port.onDisconnect.addListener(function() {
  console.log("Disconnected");
});
port.postMessage({ text: "Hello, my_application" });
*/
