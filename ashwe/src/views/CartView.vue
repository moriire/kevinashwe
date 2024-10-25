<template>
  <div class="container my-5">
    <h2>Your Cart</h2>
    
    <div v-if="carts.length === 0">
      <p>
        Your cart is empty. <router-link to="/books">Browse Books</router-link>
      </p>
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
            <tr v-for="(item, index) in carts" :key="index">
              <td>{{ item.title }}</td>
              <td>{{ item.price  }}</td>
              <td>
                <button
                  class="btn btn-danger btn-sm"
                  @click="removeFromCart(index)"
                >
                  Remove
                </button>
              </td>
            </tr>
          </tbody>
          <tfoot>
            <td><h4>Total: {{ totalPrice | currency }}</h4></td>
            <td colspan="2" class="text-center"><router-link to="/checkout" class="btn btn-primary btn-small"
        >Checkout</router-link
      ></td>
          </tfoot>
        </table>
      </div>
      
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from "vue";
const carts = ref(JSON.parse(localStorage.getItem("carts")) || []);

const totalPrice = computed(() => {
  return carts.value.reduce((total, item) => total + item.price, 0);
});
const removeFromCart = (index) => {
  carts.value.splice(index, 1);
  localStorage.setItem("carts", JSON.stringify(carts.value));
};

</script>

<style scoped>
/* Add cart styles here */
</style>
