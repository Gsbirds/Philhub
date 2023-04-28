import React, { useEffect, useState } from "react";
function Notes(){
    const [title, setTitle] = useState("");
    const [note, setNote] = useState("");

    const handleTitleChange = (event) => {
      const value = event.target.value;
      setTitle(value);
    };
    const handleNoteChange = (event) => {
      const value = event.target.value;
      setNote(value);
    };
  
    const handleSubmit = async (event) => {
      event.preventDefault();
      // create an empty JSON object
      const data = {};
  
      data.title = title;
      data.text_area = note;
      console.log(data);
  
      const locationUrl = "http://localhost:8000/philhub/noteslist";
      const fetchConfig = {
        method: "post",
        body: JSON.stringify(data),
        headers: {
          "Content-Type": "application/json",
        },
      };
     
      const response = await fetch(locationUrl, fetchConfig);
      if (response.ok) {
        const newLocation = await response.json();
        console.log(newLocation);
        setTitle("");
        setNote("");
      }
    };
    const fetchData = async () => {
      const url = "http://localhost:8000/philhub/noteslist";
  
      const response = await fetch(url);
  
      if (response.ok) {
        const data = await response.json();
        console.log(data);
        
      }
    };
  
    useEffect(() => {
      fetchData();
    }, []);


return(

    <div className="row">
    <div className="offset-1 col-6">
      <div className="makeNote">
        <h1>Make a note</h1>
        <form onSubmit={handleSubmit} id="create-presentation-form">
          <div className="form-floating mb-3">
            <input onChange={handleTitleChange} placeholder="Presenter name" required type="text" id="presenter_name" className="form-control" />
            <label htmlFor="presenter_name">Title</label>
          </div>
          <div className="mb-3">
            <label htmlFor="synopsis">Note</label>
            <textarea onChange={handleNoteChange} id="synopsis" className="form-control" rows="3" ></textarea>
          </div>

          <button className="create">Create</button>
        </form>
      </div>
    </div>
    </div>

)
}

export default Notes;