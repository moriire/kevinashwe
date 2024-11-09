<template>
  <div>
    <!--Navbar /-->
    <router-view />
    <!-- Footer /-->
  </div>
</template>

<script setup>
import { RouterView } from 'vue-router';
import { useConfigStore } from './stores/config';
import { onMounted } from 'vue';

onMounted(()=>{
  useConfigStore().getConfig()
})
</script>

<style>
</style>