import { React, useState } from 'react'

function List(props) {

    return(
<div className="container">
<h2>Published Works</h2>

{props.files.map((file) => {
  return (
    <ul>
      <li>{file.name}</li>
      <li>{file.filepath}</li>
    </ul>
  );
})}
</div>
    );
}

export default List;