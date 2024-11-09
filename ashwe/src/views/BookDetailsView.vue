<template>
  <div class="container my-5">
    <div class="row">{{ book }}
      <div class="col-md-6">
        <img :src="books.book.cover" class="img-fluid img-thumbnail" :alt="books.book.title" />
      </div>
      <div class="col-md-6">
        <h2>{{ books.book.title }}</h2>
        <h4>{{ books.book.subtitle }}</h4>
        <p class="my-3">{{ books.book.description }}</p>
        <h4>{{ books.book.price | currency }}</h4>
        <div class="my-4 d-flex">
          <button class="btn btn-outline-primary btn-small me-4" @click="books.addToCart(book)">
          Add to Cart
        </button>
        <button class="btn btn-outline-secondary btn-small" @click="books.buyNow(book)">
         Buy Now
        </button>
        </div>
        
      </div>
    </div>
  </div>
</template>

<script setup>
import { useBookStore } from "@/stores/book";
import { onMounted, ref, watch } from "vue";
import { useRoute } from "vue-router";
const route = useRoute()
const books = useBookStore()
watch(()=> route.params.pk)
onMounted(() => {
  books.getBook(route.params.pk)
});
</script>
<style scoped>
.img-fluid{
  height: 100vh;
  width: 100%;
}
</style>