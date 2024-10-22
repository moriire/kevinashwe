<template>
    <div class="container my-5">
      <div class="row">
        <div class="col-md-6">
          <img :src="book.image" class="img-fluid" :alt="book.title">
        </div>
        <div class="col-md-6">
          <h2>{{ book.title }}</h2>
          <p>{{ book.description }}</p>
          <h4>{{ book.price | currency }}</h4>
          <button class="btn btn-primary" @click="addToCart(book)">Add to Cart</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        book: null,
      };
    },
    methods: {
      addToCart(book) {
        let cart = JSON.parse(localStorage.getItem('cart')) || [];
        cart.push(book);
        localStorage.setItem('cart', JSON.stringify(cart));
        alert(`${book.title} has been added to the cart!`);
      },
    },
    mounted() {
      const bookId = this.$route.params.id;
      // Simulate fetching book details
      const books = [
        { id: 1, title: 'Book 1', description: 'This is book 1 description', price: 10, image: '' },
        { id: 2, title: 'Book 2', description: 'This is book 2 description', price: 12, image: '' },
      ];
      this.book = books.find(b => b.id === parseInt(bookId));
    },
  };
  </script>
  
  <style scoped>
  /* Add styles for book details page */
  </style>  