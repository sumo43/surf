const parse = (website) => {

    if(!website.includes('https://') && !website.includes('http://')) {
        if(!website.includes('www.')) {
            website = 'www.' + website
        }
        website = 'https://' + website
    }
    return website
}

const display_results = (results) => {
    const div_element = document.getElementById("search_list")

    results = JSON.parse(results)

    for(let i = 0; i < 100; i++) {
        const new_li = document.createElement('li')
        const new_link = document.createElement('a')
        const parsed_text = parse(results[i])
        const text_node = document.createTextNode(parsed_text)
        new_link.appendChild(text_node)
        new_link.href = parsed_text
        new_li.appendChild(new_link)
        div_element.appendChild(new_li)
    }
}

fetch('data/ranks.json').then(
response => response.text()).then(
text => 
    display_results(text)
)
