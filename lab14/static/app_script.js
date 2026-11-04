console.log('Jiaxi Pang')
const itemform = document.querySelector('#itemform')

itemform.addEventListener("submit", async function(event){
    event.preventDefault()
    const name = document.querySelector('#name').value
    const price = document.querySelector('#price').value

    try{
        //await to pause a request until the request finishes
        //fetch() sends an HTTP request to a server
        const res = await fetch("http://127.0.0.1:5000/items", {method: "POST", headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ name: name, price: Number(price) })
        }
        )
        const data = await res.json()
        document.querySelector('#response').innerText = 'Response: ' + JSON.stringify(data)
    }
    catch(error){
        document.querySelector('#response').innerText = 'Error: ' + error
    }
})

async function loaditems() {
    const res = await fetch("http://127.0.0.1:5000/items")
    const data = await res.json()
    // collect the element to print all items
    const list = document.querySelector(".itemslist")

// use a loop to place each item in the json data to a list
    for (const id in data) {
        const item = data[id]
        const li = document.createElement("li")
        li.innerHTML = `ID = ${id} | Name = ${item.name} | Price = ${item.price} 
        <button onclick = "showupdateform('${id}', '${item.name}', '${item.price}')">Update</button> 
        <button onclick = "deleteitem('${id}')"> Delete </button> `
        list.appendChild(li)
    }
}

function showupdateform(id, name, price) {
    document.querySelector("#updatesection").style.display = "block"
    document.querySelector("#updateID").value = id
    document.querySelector("#updateName").value = name
    document.querySelector("#updatePrice").value = price
}

async function updateItem() {
    const id = document.querySelector("#updateID").value
    const name = document.querySelector("#updateName").value
    const price = document.querySelector("#updatePrice").value
// update the json data in the localhost
    const res = await fetch(`http://127.0.0.1:5000/items/${id}`, {
        method: "PUT",
        headers: { "Content-type": "application/json" },
        body: JSON.stringify({ name: name, price: Number(price) })
    })
    const html = await res.text()
    document.body.innerHTML = html
}
