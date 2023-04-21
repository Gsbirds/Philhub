

import React, { useEffect, useState } from "react";
function File(){
return(

    <div className="row">
    <div className="offset-3 col-6">
      <div className="container">
        <h1>Make a note</h1>
        <form  id="create-presentation-form">
          <div className="form-floating mb-3">
            <input  placeholder="Presenter name" required type="text" id="presenter_name" className="form-control" />
            <label htmlFor="presenter_name">Title</label>
          </div>
          <div className="mb-3">
            <label htmlFor="synopsis">Note</label>
            <textarea  id="synopsis" className="form-control" rows="3" ></textarea>
          </div>

          <button className="btn btn-primary">Create</button>
        </form>
      </div>
    </div>
  </div>

)
}

export default File;