<template>
  <div class="row my-5">
    <div class="col-lg-8  col-sm-10 col-xs-12">
      <h2 class="text-center mb-4">Checkout</h2>
      <form @submit.prevent="submitCheckout">
        <div class="mb-3">
          <label for="name" class="form-label">Full Name</label>
          <input
            type="text"
            id="name"
            class="form-control"
            v-model="form.customer.name"
            required
          />
        </div>
        <div class="mb-3">
          <label for="phone" class="form-label">Mobile Phone </label>
          <input
            id="phone"
            class="form-control"
            v-model="form.customer.phonenumber"
            required
          />
        </div>
        <div class="mb-3">
          <label for="email" class="form-label">Email</label>
          <input
            type="email"
            id="email"
            class="form-control"
            v-model="form.customer.email"
            required
          />
        </div>
      
        <button type="submit" class="btn btn-primary">Complete Purchase {{ books.totalPrice }}</button>
      </form>
    </div>
    <div class="col-lg-4 col-sm-10 col-xs-12 table-responsive responsive overflow">
      <table class="table">
        <tr v-for="cart in carts">
          <td>
            <img
              :src="cart.cover"
              :alt="cart.title"
              class="img img-thumbnail"
            />
          </td>
          <td>
            <h4>{{ cart.title }}</h4>
            <p>{{ cart.subtitle }}</p>
            <h2>{{ cart.price }}</h2>
          </td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script setup>
import { useBookStore } from "@/stores/book";
import axios from "axios";
import { ref } from "vue";
const books = useBookStore();
const form = ref({
  tx_ref: "UNIQUE_TRANSACTION_REFERENCE",
  amount: books.totalPrice,
  paymentMethod: "credit_card",
  redirect_url: "",
  max_retry_attempt: 5,
  customer: {
    email: "",
    name: "",
    phonenumber: "",
  },
  customizations: {
    title: "Kevin Ashwe Books",
    description: "",
  },
});

const submitCheckout = async () => {
  try {
    const response = await axios.post(
      "https://api.flutterwave.com/v3/payments",
      form.value,
      {
        headers: {
          Authorization: `Bearer ${process.env.FLW_SECRET_KEY}`,
          "Content-Type": "application/json",
        },
      }
    );
  } catch (err) {
    console.error(err.code);
    console.error(err);
  }
};
</script>
