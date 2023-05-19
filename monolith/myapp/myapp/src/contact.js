import React, { useState } from "react";
function Contact() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [message, setMessage] = useState("");

  const handleNameChange = (event) => {
    const value = event.target.value;
    setName(value);
  };
  const handleEmailChange = (event) => {
    const value = event.target.value;
    setEmail(value);
  };
  const handleMessageChange = (event) => {
    const value = event.target.value;
    setMessage(value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    // create an empty JSON object
    const data = {};

    data.first_name = name
    data.email_address = email;
    data.message = message;

    const hatsUrl = "http://localhost:8000/philhub/api/contact/";
    const fetchConfig = {
      method: "post",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json",
      },
    };

    const response = await fetch(hatsUrl, fetchConfig);
    if (response.ok) {
      const newEmail = await response.json();
      setName("");
      setEmail("");
      setMessage("");
    }
  };

  return (
    <div className="row">
      <div className="offset-3 col-6">
          <h1>Send a Message</h1>
          <form onSubmit={handleSubmit} id="create-presentation-form">
            <div className="form-floating mb-3">
              <input
                onChange={handleNameChange}
                value={name}
                placeholder="name"
                required
                type="text"
                id="name"
                className="form-control"
              />
              <label htmlFor="presenter_name">Name</label>
            </div>
            <div className="form-floating mb-3">
              <input
                type="text"
                onChange={handleEmailChange}
                value={email}
                placeholder="Picture"
                id="text"
                className="form-control"
              />
              <label htmlFor="presenter_name">E-mail</label>
            </div>
            <div className="form-floating mb-3">
              <input
                type="text-area"
                onChange={handleMessageChange}
                value={message}
                placeholder="Picture"
                id="text"
                className="form-control"
              />
              <label htmlFor="presenter_name">Message</label>
            </div>

            <button className="upload">Send</button>
          </form>
        </div>
      </div>
  );
}

export default Contact;

// `"href":${manufact}, "id":${manufact.id}, "name":${manufact.name}`
