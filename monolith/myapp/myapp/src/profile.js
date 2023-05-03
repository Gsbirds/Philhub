import React, { useState, useEffect } from "react";
import "./App.css";

function Profile() {
  const [files, setFiles] = useState([]);
  const [name, setName] = useState([]);
  const [picture, setPicture] = useState([]);
  const [Faves, setFaves] = useState([]);

  const fetchData = async () => {
    const url = "http://localhost:8001/api/profile/";

    const response = await fetch(url);

    if (response.ok) {
      const data = await response.json();
      setFiles(data.paper);
      setName(data.profile);
      setPicture(data.picture);
      console.log(files);
    }
  };
  useEffect(() => {
    fetchData();
  }, []);

  const fetchWorks = async () => {
    const url = "http://localhost:8000/philhub/searchworks";

    const response = await fetch(url);

    if (response.ok) {
      const data = await response.json();
      setFaves(data.posts);
    }
  };
  useEffect(() => {
    fetchWorks();
  }, []);

  return (
    <div className="profile">
      <div>
        <ul>
          <li>
            <img src={picture} className="profilePic" alt="profile picture" />
          </li>
          <li><h4>{name.name}</h4></li>
          <li>{files}</li>
        </ul>
      </div>
      <ul>
        <h3>Papers you've written:</h3>
        {Faves.map((el) => {
          if (el.author == name.name) {
            return <li>{el.name}</li>;
          }
        })}
      </ul>
      <ul>
        <h3>Your Favorites:</h3>
      </ul>
      <ul>
        <h3>Your Collabs:</h3>
        {Faves.map((el) => {
          if (el.author == name.name) {
            return <li>{el.name}</li>;
          }
        })}
      </ul>
    </div>
  );
}

export default Profile;
