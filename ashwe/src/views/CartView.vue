<template>
    <div class="container my-5">
      <h2>Your Cart</h2>
      <div v-if="cart.length === 0">
        <p>Your cart is empty. <router-link to="/books">Browse Books</router-link></p>
      </div>
      <div v-else>
        <div class="table-responsive">
          <table class="table">
            <thead>
              <tr>
                <th>Title</th>
                <th>Price</th>
                <th>Remove</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(item, index) in cart" :key="index">
                <td>{{ item.title }}</td>
                <td>{{ item.price | currency }}</td>
                <td>
                  <button class="btn btn-danger btn-sm" @click="removeFromCart(index)">Remove</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <h4>Total: {{ totalPrice | currency }}</h4>
        <router-link to="/checkout" class="btn btn-primary">Proceed to Checkout</router-link>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        cart: [],
      };
    },
    computed: {
      totalPrice() {
        return this.cart.reduce((total, item) => total + item.price, 0);
      },
    },
    methods: {
      removeFromCart(index) {
        this.cart.splice(index, 1);
        localStorage.setItem('cart', JSON.stringify(this.cart));
      },
    },
    mounted() {
      this.cart = JSON.parse(localStorage.getItem('cart')) || [];
    },
  };
  </script>
  
  <style scoped>
  /* Add cart styles here */
  </style>
  