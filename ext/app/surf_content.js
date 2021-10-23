const sendMessage = (url) => {

    chrome.extension.sendMessage({parameter: url}, () => {
        console.log("url sent " + url)
    })
}

sendMessage(location.href)