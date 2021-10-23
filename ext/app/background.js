

const onCreate = (tab) => {

    // TODO add more data to send
    sendMessage(tab.url)

}

const sendMessage = (url) => {


    let text_string = "this is a test, the url is " + url

    port = chrome.runtime.connectNative('com.surf.surf_search')

    port.onMessage.addListener(function(msg) {
    console.log("Received: " + msg)
    })

    console.log("the url is " + url)

    port.postMessage({text: text_string})

}


chrome.runtime.onMessage.addListener((message) => {
    sendMessage(message.parameter)
})



