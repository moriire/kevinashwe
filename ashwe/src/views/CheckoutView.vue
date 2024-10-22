<template>
    <div class="container my-5">
      <h2>Checkout</h2>
      <form @submit.prevent="processPayment">
        <div class="mb-3">
          <label for="name" class="form-label">Full Name</label>
          <input type="text" v-model="name" class="form-control" id="name" required>
        </div>
        <div class="mb-3">
          <label for="email" class="form-label">Email</label>
          <input type="email" v-model="email" class="form-control" id="email" required>
        </div>
        <div class="mb-3">
          <label for="address" class="form-label">Shipping Address</label>
          <input type="text" v-model="address" class="form-control" id="address" required>
        </div>
        <h4>Total: {{ totalPrice | currency }}</h4>
        <button type="submit" class="btn btn-success">Pay Now</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        name: '',
        email: '',
        address: '',
        cart: [],
      };
    },
    computed: {
      totalPrice() {
        return this.cart.reduce((total, item) => total + item.price, 0);
      },
    },
    methods: {
      processPayment() {
        // Payment gateway integration (Stripe, PayPal, etc.)
        alert('Payment processing...');
        // Clear the cart after payment
        localStorage.removeItem('cart');
        this.$router.push('/');
      },
    },
    mounted() {
      this.cart = JSON.parse(localStorage.getItem('cart')) || [];
    },
  };
  </script>
  
  <style scoped>
  /* Add checkout page styles */
  </style>
  