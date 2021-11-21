
const sendMessage = (url) => {
    chrome.extension.sendMessage({parameter: url}, () => {
        if(chrome.runtime.lastError) {
            console.log("error, check client")
        }
        else {
            console.log("url sent " + url)
        }
    })
}

try {
    sendMessage(location.href)
}
catch(error) {
    console.log("erorr")
    console.log(error)
}
