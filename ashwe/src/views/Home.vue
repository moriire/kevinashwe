<template>
    <div>
      <!-- Hero Section -->
      <section class="hero bg-primary text-white text-center p-5">
        <h1>Welcome to Kevin Ashwe's Book Store</h1>
        <p>Explore a collection of Christian books to inspire and uplift you.</p>
        <router-link to="/books" class="btn btn-light btn-lg">Browse Books</router-link>
      </section>
  
      <!-- About Section -->
      <section class="about p-5">
        <div class="container">
          <h2>About Kevin Ashwe</h2>
          <p>Kevin Ashwe is a Christian author with many insightful books that are crafted to deepen your faith and understanding of God’s Word.</p>
        </div>
      </section>
  
      <!-- Books Showcase -->
      <section class="books-showcase bg-light p-5">
        <div class="container">
          <h2>Popular Books</h2>
          <div class="row">
            <!-- Sample Book -->
            <div class="col-md-4">
              <div class="card">
                <img src="" class="card-img-top" alt="Book Title">
                <div class="card-body">
                  <h5 class="card-title">Book Title</h5>
                  <p class="card-text">A brief description of the book.</p>
                  <router-link to="/book/1" class="btn btn-primary">Buy Now</router-link>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </template>
  
  <script>
  export default {
    name: "Home",
  };
  </script>
  
  <style scoped>
  .hero {
    background-image: url('path-to-hero-background.jpg');
    background-size: cover;
    background-position: center;
    height: 400px;
  }
  </style>  