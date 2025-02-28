import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:4000"; // Change this to your API URL

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

export const uploadFile = async (file) => {
    const formData = new FormData();
    formData.append('file', file);
  
    try {
      const response = await axios.post(`${API_BASE_URL}/home/upload/`, formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      });
        return response.data;
    } catch (error) {
      console.error("Upload failed:", error.response?.data || error.message);
      throw error;
    }
  };