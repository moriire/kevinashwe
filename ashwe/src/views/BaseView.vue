<template>
  <div>
    <Navbar :name="app_conf.config.name" />
    <router-view />
    <Footer />
  </div>
</template>

<script setup>
import Navbar from "@/components/Navbar.vue";
import Footer from "@/components/Footer.vue";

import { RouterView } from "vue-router";
import { useConfigStore } from "@/stores/config";
import { onMounted } from "vue";
const app_conf = useConfigStore()
</script>
