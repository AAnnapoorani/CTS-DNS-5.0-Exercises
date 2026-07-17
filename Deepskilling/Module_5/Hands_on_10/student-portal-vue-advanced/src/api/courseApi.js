import apiClient from "./apiClient";
export const getAllCourses = () => apiClient.get("/posts");
export const getCourseById = (id) => apiClient.get(`/posts/${id}`);
export const enrollStudent = ( studentId, courseId ) => Promise.resolve({ success: true, studentId, courseId });