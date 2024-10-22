<template>
    <section class="container my-5">
      <h2 class="text-center mb-4">Checkout</h2>
      <form @submit.prevent="submitCheckout">
        <div class="mb-3">
          <label for="name" class="form-label">Name</label>
          <input type="text" id="name" class="form-control" v-model="form.name" required>
        </div>
        <div class="mb-3">
          <label for="email" class="form-label">Email</label>
          <input type="email" id="email" class="form-control" v-model="form.email" required>
        </div>
        <div class="mb-3">
          <label for="payment" class="form-label">Payment Method</label>
          <select id="payment" class="form-select" v-model="form.paymentMethod" required>
            <option value="credit_card">Credit Card</option>
            <option value="paypal">PayPal</option>
          </select>
        </div>
        <button type="submit" class="btn btn-primary">Complete Purchase</button>
      </form>
    </section>
  </template>
  
  <script>
  export default {
    data() {
      return {
        form: {
          name: '',
          email: '',
          paymentMethod: 'credit_card',
        },
      };
    },
    methods: {
      submitCheckout() {
        // Handle the payment process here
        alert('Order placed successfully!');
      },
    },
  };
  </script>
  