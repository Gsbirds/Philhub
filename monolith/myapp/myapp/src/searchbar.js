
 

import React, { useState, useEffect } from "react";
import "./App.css";
import Notes from "./notes";

function SearchBar() {
  const [inputText, setInputText] = useState("");
  const [files, setFiles] = useState([]);


  let inputHandler = (e) => {
    //convert input text to lower case
    var lowerCase = e.target.value.toLowerCase();
    setInputText(lowerCase);
  };

  const fetchData = async () => {
    const url = "http://localhost:8000/philhub/searchworks";

    const response = await fetch(url);

    if (response.ok) {
      const data = await response.json();
      setFiles(data.posts);
      console.log(files);
    }
  };
  useEffect(() => {
    fetchData();
  }, []);

  const filteredData = files.filter((el) => {
    if (inputText === "") {
      return "";
    } else {
      return el.name.toLowerCase().includes(inputText);
    }
  });
  const filteredAuthor = files.filter((el) => {
    if (inputText === "") {
      return "";
    } else {
      return el.author.toLowerCase().includes(inputText);
    }
  });
  const filteredTopic = files.filter((el) => {
    if (inputText === "") {
      return "";
    } else {
      return el.topic.toLowerCase().includes(inputText);
    }
  });


  return (
    <>
      <div className="container">
        <div className="main">
          <h1>Published Works</h1>
          <div className="input-group mb-3">
            <div className="input-group-prepend">
              <button className="btn btn-outline-secondary" type="button">
                Search Papers
              </button>
            </div>
            <input
              id="outlined-basic"
              onChange={inputHandler}
              type="text"
              className="form-control"
              placeholder=""
              aria-label="search"
              aria-describedby="basic-addon1"
            />
             <div className="input-group-prepend">
              <button className="btn btn-outline-secondary" type="button">
                Search Author
              </button>
            </div>
            <input
              id="outlined-basic"
              onChange={inputHandler}
              type="text"
              className="form-control"
              placeholder=""
              aria-label="search"
              aria-describedby="basic-addon1"
            />
                 <div className="input-group-prepend">
              <button className="btn btn-outline-secondary" type="button">
                Search Topic
              </button>
            </div>
            <input
              id="outlined-basic"
              onChange={inputHandler}
              type="text"
              className="form-control"
              placeholder=""
              aria-label="search"
              aria-describedby="basic-addon1"
            />
          </div>
        </div>

        <ul className="list">
          {filteredData.map((item) => (
            <li key={item.href}>
              <a
                className="headerProfile-menu-list"
                onClick={() => window.open(item.filepath)}
              >
                {item.name}
              </a>
            </li>
          ))}
                    {filteredAuthor.map((item) => (
            <li key={item.href}>
              <a
                className="headerProfile-menu-list"
                onClick={() => window.open(item.filepath)}
              >
                {item.name}
              </a>
            </li>
          ))}
                    {filteredTopic.map((item) => (
            <li key={item.href}>
              <a
                className="headerProfile-menu-list"
                onClick={() => window.open(item.filepath)}
              >
                {item.name}
              </a>
            </li>
          ))}

        </ul>
      </div>
      <div className="grid">
      <ul className="topics">
        <h1>Topics</h1>
        {files.map((item) => (
            <li key={item.href}>
                {item.topic}
            </li>
          ))}


        </ul>
      <ul className="recent">
        <h1>Recently Published:</h1>
        {files.map((item) => (
            <li key={item.href}>
                {item.topic}
            </li>
          ))}
        </ul>
        <ul className="popular">
        <h1>Most popular:</h1>
        {files.map((item) => (
            <li key={item.href}>
                {item.topic}
            </li>
          ))}
          
        </ul>

        </div>

        {/* <div className="note1"> */}
        <Notes />
        {/* </div> */}
    
    </>
  );
}

export default SearchBar;