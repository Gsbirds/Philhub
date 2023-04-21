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


function App(props) {

  return (
    <>
    <BrowserRouter>
      <Nav />
      <Routes>
      <Route path="/">
    <Route index element={< HomePage/>} />
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
      </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
