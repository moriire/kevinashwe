<template>
    <div class="container mt-5">
      <h2>Checkout</h2>
      <form @submit.prevent="processPayment">
        <!-- Add form fields like name, address, and payment info -->
        <div class="mb-3">
          <label for="name" class="form-label">Full Name</label>
          <input type="text" class="form-control" id="name" v-model="name" required>
        </div>
        <button type="submit" class="btn btn-primary">Pay Now</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        name: ''
      };
    },
    methods: {
      processPayment() {
        // Process payment via a payment gateway
        alert('Payment processed successfully!');
        this.$router.push('/');
      }
    }
  };
  </script>
  