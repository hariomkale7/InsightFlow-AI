import axios from "axios";

const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000";

export const analyzeDataset = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  const response = await axios.post(`${API_BASE_URL}/analyze`, formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });

  return response.data;
};

export const generateAIReport = async (reportId) => {
  const response = await axios.post(
    `${API_BASE_URL}/reports/${reportId}/generate-ai-report`
  );

  return response.data;
};

export const askQuestion = async (reportId, question) => {
  const response = await axios.post(`${API_BASE_URL}/ask`, {
    report_id: reportId,
    question: question,
  });

  return response.data;
};

export const getChatHistory = async (reportId) => {
  const response = await axios.get(`${API_BASE_URL}/reports/${reportId}/chat`);

  return response.data;
};

export const getReports = async () => {
  const response = await axios.get(`${API_BASE_URL}/reports`);
  return response.data;
};