import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { Loading } from './loading'

export const Upload = () => {

  const [url, setUrl] = useState("")
  const [files,setFile]=useState()
  const [loading, setLoading] = useState(false)

  const navigate = useNavigate();

  const handleSubmit = () => {
    // console.log({url});
    const uploadData = new FormData();
    // uploadData.append('url',url);
    uploadData.append('files',files,files.name);
    setLoading(true)
    fetch("http://localhost:8000/api/", {
      method: "POST",
      body: uploadData
    }).then((res) => {
      setLoading(false)
      alert('Uploaded successfully.')
      console.log(res)
      navigate('/prev_uploads')
    }).catch((err => {
      console.log(err.message)
    }))
  }

  return (
    <>
      {loading ? (<Loading/>): (<div className="container disp">
        <div className="card">
          <div className='card-title'>
            <h2>Upload</h2>
              {/* <label>
                URL:
                <input type="url" name="name" onChange={e => setUrl(e.target.value)} />
              </label> */}
              <label>
                Choose a video file:
                <input type="file" onChange={e=> setFile(e.target.files[0])} />
              </label>
              <button onClick={()=>{handleSubmit()}}>Submit</button>
          </div>
        </div>
      </div>)}
    </>
  )
}