import { React, useState } from 'react'


function SearchList(props) {
    //create a new array by filtering the original array
    const filteredData = props.files.filter((el) => {
        //if no input the return the original
        if (props.input === '') {
            return el;
        }
        //return the item which contains the user input
        else {
            return el.text.toLowerCase().includes(props.input)
        }
    })
    return (
        <ul>
            {filteredData.map((item) => (
                <li key={item.filepath}>{item.name}</li>
            ))}
        </ul>
    )
}

export default SearchList