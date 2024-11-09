<template>
  <section class="my-5">
    <div class="container">
      <div class="row" >
        <h2 class="text-center my-4">Books by Kevin Ashwe</h2>
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
          class="mySwiper my-5">
          <swiper-slide v-for="(book, index) in books.latestBooks" :key="index" class="swiper-slide card">
            <BookSingle :book="book" />
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
import BookSingle from "./books/BookSingle.vue";

const books = useBookStore()
onMounted(()=>{
  books.getLatestBooks()
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
