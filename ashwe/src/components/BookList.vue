<template>
    <div class="container my-5">
      <h2>Our Books</h2>
      <div class="row">
        <div class="col-md-3" v-for="book in books" :key="book.id">
          <div class="card mb-4">
            <img :src="book.image" class="card-img-top" :alt="book.title">
            <div class="card-body">
              <h5 class="card-title">{{ book.title }}</h5>
              <p class="card-text">{{ book.price | currency }}</p>
              <router-link :to="'/book/' + book.id" class="btn btn-primary">View Details</router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        books: [
          { id: 1, title: 'Book 1', image: 'path-to-image.jpg', price: 10 },
          { id: 2, title: 'Book 2', image: 'path-to-image.jpg', price: 12 },
        ],
      };
    },
  };
  </script>  