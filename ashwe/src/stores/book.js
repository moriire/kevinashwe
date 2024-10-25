import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from "axios"
import router from '@/router'
export const useBookStore = defineStore('book', () => {
  const count = ref(0)
  const books = ref([])
  const carts = ref(JSON.parse(localStorage.getItem("carts"))||[])
  const addToCart = async (book)=>{
    carts.value.push(book)
    localStorage.setItem("carts", JSON.stringify(carts.value))
    console.log(book)
  };
  const buyNow = async (book)=>{
    carts.value.push(book)
    localStorage.setItem("carts", JSON.stringify(carts.value))
    console.log(carts.value)
    router.push("/buy")
  };
  const getBooks = async () => {
    try {
      const res = await axios.get("api/books/")
      books.value = res.data
      console.log(res)
    } catch (error) {
      window.alert("error", error)
    } finally{

    }
  }
  return { getBooks, books, addToCart, buyNow }
})
