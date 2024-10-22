<template>
  <section
    class="hero-section text-center text-white"
    style="
      background-image: url('/src/assets/hero1.jpeg');
      background-size: cover;
      padding: 100px 0;
    "
  >
    <div class="container">
      <img
        :src="kevinImage"
        alt="Kevin Ashwe"
        class="rounded-circle mb-3"
        style="width: 150px; height: 150px"
      />
      <h1 class="display-4">{{ app_conf.config.name || "Local Church" }}</h1>
      <p class="lead">{{ app_conf.config.title || "Christian Author & Pastor" }}</p>
      <div class="row justify-content-center mt-3">
        <div class="col-lg-3 col-md-4 col-sm-6 col-xs-10 my-2">
          <RouterLink to="/books" class="btn btn-primary btn-lg w-100"
            >View Books</RouterLink
          >
        </div>
        <div class="col-lg-3 col-md-4 col-sm-6 col-xs-10 my-2">
          <RouterLink to="/podcasts" class="btn btn-secondary btn-lg w-100"
            >Listen to Podcasts</RouterLink
          >
        </div>
      </div>
    </div>
  </section>
</template>
<script setup>
import { useConfigStore } from "@/stores/config";
import { RouterLink } from "vue-router";
const kevinImage = "/src/assets/file.enc";
const app_conf = useConfigStore()
</script>

<style scoped>
.hero-section {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background-position: center;
}
</style>
