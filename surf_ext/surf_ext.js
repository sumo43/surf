

// make this settable later
var ADDRESS = 'http://0.0.0.0:5001'
ADDRESS += '/urls'
ADDRESS += '?url='

let url = window.location.href

ADDRESS += url

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

