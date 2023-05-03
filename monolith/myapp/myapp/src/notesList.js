import React, { useState, useEffect } from "react";
import "./App.css";
import Notes from "./notes";

function NotesList() {
  const [files, setFiles] = useState([]);
  const [input, setInput]= useState("")

  const fetchData = async () => {
    const url = "http://localhost:8000/philhub/noteslist";

    const response = await fetch(url);

    if (response.ok) {
      const data = await response.json();
      setFiles(data.notes);
      console.log(files);
    }
  };
  useEffect(() => {
    fetchData();
  }, []);

  let inputHandler = (e) => {
    //convert input text to lower case
    var lowerCase = e.target.value.toLowerCase();
    setInput(lowerCase);
  };

  const handleDeleteButton = async (e) => {
    const { id } = e.target;
    const locationUrl = `http://localhost:8000/philhub/note/${id}`;
    const fetchConfig = {
      method: "delete",
      headers: {
        "Content-Type": "application/json",
      },
    };

    const response = await fetch(locationUrl, fetchConfig);
    if (response.ok) {
      const data = await response.json();
      console.log(data);
      setFiles(files.filter((item) => item.id !== parseInt(id)));
    }
  };
  const filteredData = files.filter((el) => {
    if (input === "") {
      return el;
    } else {
      return el.title.toLowerCase().includes(input);
    }
  });

  return (
    <>
          <div className="container">
      <div className="input-group mb-3">
      <div className="input-group-prepend">
             <label className="label">Search Notes</label>
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
        <div className="grid">
      <div classname="grid-item-2">
      <ul className="list">
        {filteredData.map((item) => (
          // <div className="container">
          <div className= "note">
            <li key={item.id}>
              <a href={item.title}> {item.title}</a>
            </li>
            <li>
              {item.text_area}
              <button
                className="delete"
                id={item.id}
                onClick={handleDeleteButton}
              >
                {" "}
                Delete
              </button>
            </li>
           </div>
        ))}
      </ul>
      </div>
      <div classname="grid-item-1">
        <Notes />
      </div>
      </div>
    </>
  );
}

export default NotesList;
