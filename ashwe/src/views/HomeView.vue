<template>
  <div>
    <Navbar />
    <HeroSection />
    <BooksSwiper />
    <!--section class="container my-5">
  <h2 class="text-center mb-5">Latest Podcasts</h2>
  <div class="row justify-content-center">
    <div class="col-md-4">
      <div class="card shadow-sm">
        <img src="/src/assets/file.png" class="card-img-top" alt="Podcast Cover">
        <div class="card-body">
          <h5 class="card-title">Episode 1: The Journey of Faith</h5>
          <p class="card-text text-muted">Join Pastor Kevin Ashwe as he explores the journey of faith in this inspiring podcast episode.</p>
          <audio controls class="w-100">
            <source src="/src/assets/mixkit-tech-house-vibes-130.mp3" type="audio/mpeg">
            Your browser does not support the audio element.
          </audio>
          <div class="progress mt-3" style="height: 5px;">
            <div class="progress-bar bg-primary" role="progressbar" style="width: 30%;" aria-valuenow="30" aria-valuemin="0" aria-valuemax="100"></div>
          </div>
          <div class="d-flex justify-content-between align-items-center mt-3">
            <button class="btn btn-outline-primary">Download</button>
            <span class="text-muted">30:15</span>
          </div>
        </div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="card shadow-sm">
        <img src="/src/assets/file.png" class="card-img-top" alt="Podcast Cover">
        <div class="card-body">
          <h5 class="card-title">Episode 1: The Journey of Faith</h5>
          <p class="card-text text-muted">Join Pastor Kevin Ashwe as he explores the journey of faith in this inspiring podcast episode.</p>
          <audio controls class="w-100">
            <source src="/src/assets/mixkit-tech-house-vibes-130.mp3" type="audio/mpeg">
            Your browser does not support the audio element.
          </audio>
          <div class="progress mt-3" style="height: 5px;">
            <div class="progress-bar bg-primary" role="progressbar" style="width: 30%;" aria-valuenow="30" aria-valuemin="0" aria-valuemax="100"></div>
          </div>
          <div class="d-flex justify-content-between align-items-center mt-3">
            <button class="btn btn-outline-primary">Download</button>
            <span class="text-muted">30:15</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section-->

    <Footer />
  </div>
</template>
<script setup>
import Navbar from "@/components/Navbar.vue";
import Footer from "@/components/Footer.vue";
import BooksSwiper from "@/components/BooksSwiper.vue";
import HeroSection from "@/components/HeroSection.vue";

import { RouterView } from 'vue-router';
import { useConfigStore } from '@/stores/config';
import { onMounted } from 'vue';

onMounted(()=>{
  useConfigStore().getConfig()
})
</script>

<style>
/* Add any global styles here */
</style>