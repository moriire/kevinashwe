<template>
    <div class="container mt-5">
      <h2>Your Cart</h2>
      <ul class="list-group">
        <li v-for="item in cart" :key="item.id" class="list-group-item d-flex justify-content-between align-items-center">
          {{ item.title }} - ${{ item.price }} x {{ item.quantity }}
          <span class="badge bg-primary rounded-pill" @click="removeFromCart(item)">Remove</span>
        </li>
      </ul>
      <div class="mt-3">
        <h4>Total: ${{ totalPrice }}</h4>
        <button class="btn btn-success" @click="proceedToCheckout">Proceed to Checkout</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: ['cart'],
    computed: {
      totalPrice() {
        return this.cart.reduce((total, item) => total + item.price * item.quantity, 0);
      }
    },
    methods: {
      removeFromCart(item) {
        this.$emit('remove-from-cart', item);
      },
      proceedToCheckout() {
        this.$router.push('/checkout');
      }
    }
  };
  </script>  