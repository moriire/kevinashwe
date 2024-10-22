import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from "axios"
export const useBookStore = defineStore('book', () => {
  const count = ref(0)
  const books = ref([])
  
  const getBooks = async () => {
    try {
      const res = await axios.get("http://127.0.0.1:8000/api/books/")
      books.value = res.data
      console.log(res)
    } catch (error) {
      window.alert("error", error)
    } finally{

    }
  }
  return { getBooks, books }
})
