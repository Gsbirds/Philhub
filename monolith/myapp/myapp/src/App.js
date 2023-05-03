import "./App.css";
import * as React from "react";
import Nav from "./Nav";
import SearchBar from "./searchbar";
import HomePage from "./homepage";
import Notes from "./notes";
import NotesList from "./notesList";
import File from "./show-file";
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Upload from "./upload-works";
import Contact from "./contact";
import Profile from "./profile";
import { Login } from "./login";
import Footer from "./footer";

function App(props) {

  return (
    <>
    <BrowserRouter>
      <Nav />
      <Routes>
      <Route path="/">
    <Route index element={< HomePage/>} />
    </Route>
    <Route>
    <Route path="/contact" element={<Contact />}></Route>
    </Route>
    <Route>
    <Route path="/profile" element={<Profile />}></Route>
    </Route>
      <Route path="/searchworks">
      <Route index element={<SearchBar />} />
      <Route path="new" element={<Upload />}></Route>
      </Route>
      <Route path="/notes">
      <Route index element={<Notes />} />
      </Route>
      <Route path="/noteslist">
      <Route index element={<NotesList />} />
      </Route>
      <Route>
      <Route path="/login" element={<Login/>}/>
      </Route>
      </Routes>
      <Footer/>
      </BrowserRouter>
    </>
  );
}

export default App;
