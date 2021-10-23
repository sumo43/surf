

const onCreate = (tab) => {

    // TODO add more data to send
    sendMessage(tab.url)

}

const sendMessage = (url) => {

    port = chrome.runtime.connectNative('com.surf.surf_search')

    port.onMessage.addListener(function(msg) {
        console.log("Received: " + msg)
    })

    console.log("the url is " + url)

    port.postMessage({text: url})

}


chrome.runtime.onMessage.addListener((message) => {
    sendMessage(message.parameter)
})



