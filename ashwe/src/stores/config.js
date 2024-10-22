import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from "axios"
export const useConfigStore = defineStore('config', () => {
  const count = ref(0)
  const config = ref({})
  const doubleCount = computed(() => count.value * 2)
  function increment() {
    count.value++
  }

  const getConfig = async () => {
    try {
      const res = await axios.get("http://127.0.0.1:8000/api/config/1")
      config.value = res.data
      console.log(res)
    } catch (error) {
      window.alert("error", error)
    } finally{

    }
  }
  return { getConfig, config }
})
