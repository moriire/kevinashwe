<template>
  <div class="container my-5">
    <h2>Your Cart</h2>

    <div v-if="books.carts.length === 0">
      <p>
        Your cart is empty. <router-link to="/books">Browse Books</router-link>
      </p>
    </div>
    <div v-else>
      <div class="table-responsive responsive">
        <table class="table table-hovered">
          <tbody>
            <tr v-for="(item, index) in books.carts" :key="index">
              <td>
                <img :src="item.cover" :alt="item.title" class="img-thumbnail img-responsive">
              </td>
              <td>{{ item.title }}</td>
              <td>{{ item.price }}</td>
              <td>
                <button
                  class="btn btn-danger btn-sm"
                  @click="books.removeFromCart(index)"
                >
                  Remove
                </button>
              </td>
            </tr>
          </tbody>
          <tfoot>
            <tr>
              <td>
                <h4>Total: {{ books.totalPrice | currency }}</h4>
              </td>
              <td colspan="3" class="text-end">
                <router-link to="/checkout" class="btn btn-outline-primary btn-small"
                  >Checkout</router-link
                >
              </td>
            </tr>
          </tfoot>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useBookStore } from "@/stores/book";
const books = useBookStore()
</script>

<style scoped>
/* Add cart styles here */
</style>
