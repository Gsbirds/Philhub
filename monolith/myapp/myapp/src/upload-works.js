import React, { useEffect, useState } from "react";

function Upload(){
    const [name, setName] = useState("");
    const [author, setAuthor] = useState("");
    const [topic, setTopic] = useState("");
    const [file, setFile] = useState("");

    const handleNameChange = (event) => {
      const value = event.target.value;
      setName(value);
    };
    const handleAuthorChange = (event) => {
      const value = event.target.value;
      setAuthor(value);
    };
    const handleTopicChange = (event) => {
      const value = event.target.value;
      setTopic(value);
    };
    const handleFileChange = (event) => {
      const value = event.target.value;
      setFile(value);
    };

    const handleSubmit = async (event) => {
      event.preventDefault();
      // create an empty JSON object
      const data = {};
    const newfile=file.replace('C:\\fakepath\\', "files/")
      data.name = name;
      data.filepath = newfile;
      data.author=author;
      data.topic=topic;
      console.log(data);
  
      const locationUrl = "http://localhost:8000/philhub/api/searchworks/";
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
        setName("");
        setFile("");
        setTopic("");
        setAuthor("");
      }
    };

return(
<>
    <div className="row">
    <div className="offset-3 col-6">
        <h1>Upload a Paper</h1>
        <form onSubmit={handleSubmit} id="create-presentation-form">
          <div className="form-floating mb-3">
            <input onChange={handleNameChange} value={name} placeholder="Presenter name" required type="text" id="presenter_name" className="form-control" />
            <label htmlFor="presenter_name">Title</label>
          </div>
          <div className="form-floating mb-3">
            <input onChange={handleAuthorChange} value={author} placeholder="Presenter name" required type="text" id="presenter_name" className="form-control" />
            <label htmlFor="presenter_name">Author</label>
          </div>
          <div className="form-floating mb-3">
            <input onChange={handleTopicChange} value={topic} placeholder="Presenter name" required type="text" id="presenter_name" className="form-control" />
            <label htmlFor="presenter_name">Topic</label>
          </div>

          <div className="mb-3">
            <label htmlFor="formFile" className="form-label">File</label>
            <input onChange={handleFileChange} value={file} className="form-control" type="file" id="formFile"/>
            </div>

          <button className="upload">Upload</button>
        </form>
      </div>
    </div>
</>
)
}

export default Upload;