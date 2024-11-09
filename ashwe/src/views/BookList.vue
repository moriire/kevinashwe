<template>
  <section class="my-5">
    <div class="container">
      <div class="row">
        <h2 class="text-center my-4">Books by Kevin Ashwe</h2>
        <div
          class="col-lg-3 card mx-2"
          v-for="book in books.books"
          :key="book.id"
        >
          <BookSingle :book="book" />
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { onMounted } from "vue";
import { useBookStore } from "@/stores/book";
import BookSingle from "@/components/books/BookSingle.vue";

const books = useBookStore();
onMounted(() => {
  books.getBooks();
});
</script>

<style scoped>
.card-body {
  width: 100% !important;
  height: 100%;
}
</style>
