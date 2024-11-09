import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from "axios"
import router from '@/router'
export const useBookStore = defineStore('book', () => {
  const count = ref(0)
  const books = ref([])
  const latestBooks = ref([])
  const book = ref({})
  const carts = ref(JSON.parse(localStorage.getItem("carts"))||[])

const totalPrice = computed(() => {
  return carts.value.reduce((total, item) => total + item.price, 0);
});
const removeFromCart = (index) => {
  carts.value.splice(index, 1);
  localStorage.setItem("carts", JSON.stringify(carts.value));
};
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
  const getBook = async (pk)=>{
    try {
      const res = await axios.get(`api/books/${pk}/`)
      book.value = res.data
      console.log(res.data)
    } catch (error) {
      window.alert("error", error)
    } finally{

    }
  }
  const getLatestBooks = async () => {
    try {
      const res = await axios.get("api/books/latest/")
      latestBooks.value = res.data
      console.log(res.data)
    } catch (error) {
      window.alert("error", error)
    } finally{

    }
  }
  const getBooks = async () => {
    try {
      const res = await axios.get("api/books/")
      books.value = res.data
      console.log(res.data)
    } catch (error) {
      window.alert("error", error)
    } finally{

    }
  }
  return {getLatestBooks, getBook, getBooks, latestBooks, book,  books, addToCart, buyNow, totalPrice, removeFromCart, carts }
})
