<template>
  <section class="my-5">
    <div class="container">
      <div class="row" >
        <h2 class="text-center mb-4">Books by Kevin Ashwe</h2>
        <swiper
          :slides-per-view="1"
          space-between="10"
          navigation
          pagination
          loop
          :breakpoints="{
            640: { slidesPerView: 1, spaceBetween: 10 },
            768: { slidesPerView: 2, spaceBetween: 20 },
            1024: { slidesPerView: 4, spaceBetween: 30 },
          }"
          class="mySwiper"
        >
          <swiper-slide v-for="book in books.books" :key="book.id">
            <div class="card">
              <img :src="book.cover" class="card-img-top img-fluid" :alt="book.title" />
              <div class="card-body text-center">
                <h5 class="card-title">{{ book.title }}</h5>
                <p class="card-text">&#8358; {{ book.price }}</p>
                <button class="btn btn-primary" @click="addToCart(book)">
                  Add to Cart
                </button>
              </div>
            </div>
          </swiper-slide>
        </swiper>
      </div>
    </div>
  </section>
</template>

<script setup>
import { Swiper, SwiperSlide } from "swiper/vue";
import "swiper/swiper-bundle.min.css"; 
import { onMounted } from "vue";
import { useBookStore } from "@/stores/book";
const books = useBookStore()
onMounted(()=>{
  books.getBooks()
})
</script>

<style scoped>
.mySwiper {
  width: 100%;
  height: 100%;
}

.swiper-slide {
  display: flex;
  flex-direction: column;
  align-items: center;
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
