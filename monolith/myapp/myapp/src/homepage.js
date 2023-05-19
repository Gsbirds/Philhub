import React, { useState, useEffect } from "react";
import "./App.css";

function HomePage() {
  const [files, setFiles]=useState([]);

  const fetchData = async () => {
    const url = "http://localhost:8000/api/philhub/";

    const response = await fetch(url);

    if (response.ok) {
      const data = await response.json();
      setFiles(data.news)
      console.log(files);
    }
  };
  useEffect(() => {
    fetchData();
  }, []);


  return (
<>
        <h1>News</h1>



      <ul className="list">
        {files.map((item) => (
            <div className= "container">
          <li key={item.href}>
            <a href={item.href}> {item.title}</a>
          </li>
          <li>
          <p>{item.description}</p>
          </li>
          </div>
        ))}
      </ul>
      </>
  );

}

export default HomePage;
