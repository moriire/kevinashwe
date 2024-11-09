<template>
  <div class="card-body">
    <router-link :to="{ name: 'book', params: { pk: props.book.id } }">
      <img
        :src="props.book.cover"
        class=".card-img-top img-fluid"
        :alt="props.book.title"
      />
    </router-link>
    <div class="card-footer text-center">
      <h5 class="card-title">{{ props.book.title }}</h5>
      <p class="card-text">&#8358; {{ props.book.price }}</p>
      <div class="d-flex column">
        <div class="col">
          <button
            class="btn btn-outline-primary btn-sm"
            @click="useBookStore().addToCart(props.book)"
          >
            Add to Cart
          </button>
        </div>
        <div class="col">
          <button
            class="btn btn-outline-primary btn-sm"
            @click="useBookStore().buyNow(props.book)"
          >
            Buy Now
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useBookStore } from '@/stores/book';
import { useRouter } from 'vue-router';
const book = useBookStore()
const router = useRouter()
const props = defineProps({
  book: {
    type: Object,
    required: true
  }
})
</script>
<style scoped>
.card-body,
img {
  width: 100% !important;
  height: 100%;
}

.img-fluid {
  max-width: 100%;
  height: auto;
}

.slide-caption {
  text-align: center;
  margin-top: 10px;
}
</style>
