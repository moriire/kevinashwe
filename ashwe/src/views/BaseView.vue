<template>
  <Navbar :name="app_conf.config.name" />
  <div class="container min-vh-100 cont">
    <router-view />
  </div>
  <Footer />
</template>

<script setup>
import Navbar from "@/components/Navbar.vue";
import Footer from "@/components/Footer.vue";

import { RouterView } from "vue-router";
import { useConfigStore } from "@/stores/config";
import { onMounted } from "vue";
const app_conf = useConfigStore()
</script>
<style scoped>
.cont{
  min-height: var(100vh - 30%) !important
}
</style>