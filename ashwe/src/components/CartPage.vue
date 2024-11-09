<template>
  <section class="container my-5">
    <h2 class="text-center mb-4">Your Cart</h2>
    <div v-if="cart.length > 0">
      <div class="list-group">
        <div class="list-group-item" v-for="item in carts" :key="item.id">
          {{ item }} - {{ item.price }}
        </div>
      </div>
      <button class="btn btn-success mt-3" @click="checkout">
        Proceed to Checkout
      </button>
    </div>
    <div v-else>
      <p>Your cart is empty.</p>
    </div>
  </section>
</template>

<script setup>
import { ref } from "vue";
const carts = ref(JSON.parse(localStorage.getItem("kevinBooks")) | []);
const checkout = () => {
  router.push("/checkout");
};
</script>
