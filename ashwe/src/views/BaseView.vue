<template>
  <Navbar :name="app_conf.config.name" />
  <div class="container cont">
    <router-view />
  </div>
  <Footer />
</template>

<script setup>
import Navbar from "@/components/Navbar.vue";
import Footer from "@/components/Footer.vue";

import { RouterView } from "vue-router";
import { useConfigStore } from "@/stores/config";
const app_conf = useConfigStore()
</script>
<style scoped>
.cont{
  height: var(100vh - 30%) !important
}
</style>