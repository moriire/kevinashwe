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
          <swiper-slide v-for="book in books.books" :key="book.id" class="swiper-slide card">
            <div class="card-body">
              <router-link :to="{name: 'book', params: {pk: book.id}}">
              <img :src="book.cover" class=".card-img-top img-fluid" :alt="book.title" />
            </router-link>
              <div class="card-footer text-center">
                <h5 class="card-title">{{ book.title }}</h5>
                <p class="card-text">&#8358; {{ book.price }}</p>
               <div class="d-flex column">
               <div class="col">
                <button class="btn btn-outline-primary btn-sm" @click="books.addToCart(book)">
                  Add to Cart
                </button>
               </div>
               <div class="col">
                <button class="btn btn-outline-primary btn-sm" @click="books.buyNow(book)">
                  Buy Now
                </button>
               </div>
               </div>
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
.mySwiper, .card-body, img{
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
