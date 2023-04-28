import React, { useState, useEffect } from "react";
import "./App.css";
import Notes from "./notes";

function NotesList() {
  const [files, setFiles] = useState([]);

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

  return (
    <>
      <div>
        <Notes />
      </div>

      <ul className="list">
        {files.map((item) => (
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
    </>
  );
}

export default NotesList;
