import React, { useState, useEffect } from "react";
import { NavLink } from "react-router-dom";
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
      setFiles(data);
      console.log(files);
    }
  };
  useEffect(() => {
    fetchData();
  }, []);

  const filteredData = files.filter((el) => {
    if (inputText === "") {
      return el;
    } else {
      return el.name.toLowerCase().includes(inputText);
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
        </ul>
      </div>
      <Notes />
    </>
  );
}

export default SearchBar;
