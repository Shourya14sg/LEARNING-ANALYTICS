import React,{useRef} from 'react'
import { instruction, promo1 } from '../Utils/Constants'
//import { Button } from 'flowbite-react'
import { useNavigate } from 'react-router-dom'
import * as XLSX from 'xlsx'
import { uploadFile } from '../Utils/api'

const HomePage = () => {
  const navigate= useNavigate();
  const fileInputRef = useRef(null);
  
  const handleFileUpload=(event)=>{  
    const file = event.target.files[0];
    if (!file){ 
      alert('upload file with suitable format')
      return;
    }

    const reader = new FileReader();  //as array buffer
   
    reader.onload =async (e) => {
      const data = new Uint8Array(e.target.result);
      const workbook = XLSX.read(data, { type: 'array' });
  
      // Get sheet names
      const sheetNames = workbook.SheetNames;
      console.log("Sheet Names:", sheetNames);
  
       // Check if "Sheet1" and "Sheet2" exist
      if (sheetNames.includes("Sheet1") && sheetNames.includes("Sheet2")) {
        console.log("Valid file. Sending to backend...");
        try {
          const response = await uploadFile(file);
          console.log("Server Response:", response);
          navigate('/analysis',{state:{response:response}});
          //if(response.status)

        } catch (error) {
          console.error("Upload Failed:", error);
        }
      } else {
        console.log("Invalid file: Missing Sheet1 or Sheet2.");
      }
    };

    if (file.name.endsWith('.xlsx')) {
      reader.readAsArrayBuffer(file);
    } else {
      console.log("Invalid file type. Please upload an .xlsx file.");
    }
  };
  return (
    
    <div className='flex flex-col gap-y-8 w-full h-[100vh] p-16'>
      <h1>{promo1}</h1>
      <h5 >{instruction}</h5>
      <label className='bg-black text-white mx-auto p-4 rounded-lg'>
      <h3>Get Started!!</h3>
      <input
        type='file'
        className='hidden'
        onChange={handleFileUpload} 
        accept=".csv,.xlsx" 
        ref={fileInputRef}
      />
      </label>
    </div>
    
  )
}
export {HomePage};