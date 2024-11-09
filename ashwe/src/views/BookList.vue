<template>
  <section class="my-5">
    <div class="container">
      <div class="row">
        <div>
          <h2 class="text-center my-4">Books by Kevin Ashwe</h2>
        </div>
        <div
          class="col-lg-3 card mx-2 my-4"
          v-for="book in items"
          :key="book.id"
        >
          <BookSingle :book="book" />
          
        </div>
        <div class="pagination justify-content-center my-4" >
        <!-- Pagination Controls -->
        <nav>
          <ul class="pagination ">
            <li class="page-item p-2" :class="{ disabled: !pagination.previous }">
              <button
                class="btn btn-primary"
                @click="fetchItems(pagination.previous)"
                :disabled="!pagination.previous"
              >
                Previous
              </button>
            </li>
            <li class="page-item p-2" :class="{ disabled: !pagination.next }">
              <button
                class="btn btn-primary"
                @click="fetchItems(pagination.next)"
                :disabled="!pagination.next"
              >
                Next
              </button>
            </li>
          </ul>
        </nav>
        <!-- Pagination Controls -->
      </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useBookStore } from "@/stores/book";
import BookSingle from "@/components/books/BookSingle.vue";
import { useRoute } from "vue-router";
import axios from "axios";
const books = useBookStore()
const route = useRoute()
const loading = ref(true)
const items = ref([])

const pagination = ref({
  count: 0,
  next: null,
  previous: null,
})
const limit = 8 
const offset = ref(0)

onMounted(async () => {
  await fetchItems()
})

const fetchItems = async (url = null) => {
  try {
    const apiUrl = url || `api/books/?limit=${limit}&offset=${offset}`
    const response = await axios.get(apiUrl)
    items.value = response.data.results
    pagination.value.count = response.data.count
    pagination.value.next = response.data.next
    pagination.value.previous = response.data.previous

    // Update offset for the next page
    if (response.data.next) {
      const urlParams = new URLSearchParams(new URL(response.data.next).search)
      offset.value = parseInt(urlParams.get('offset'), 10)
    }
  } catch (error) {
    console.error('Error fetching items:', error)
  }
}
</script>

<style scoped>
.card-body {
  width: 100% !important;
  height: 100%;
}
</style>
