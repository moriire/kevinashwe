<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light shadow-sm py-3 sticky-top">
    <div class="container">
      <router-link class="navbar-brand fw-bold text-primary" to="/">{{ props.name }}</router-link>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item">
            <router-link class="nav-link" to="/">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/books">Books</router-link>
          </li>
          <!--li class="nav-item">
            <router-link class="nav-link" to="/podcasts">Podcasts</router-link>
          </li-->
          <li class="nav-item">
            <router-link class="nav-link" to="/cart">Cart</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/about">About</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/about">Support</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script setup>
const props = defineProps({
  name:{
    type: String,
    default: "kevin"
  }
})
</script>

<style>
/* Add navbar styles */
</style>
