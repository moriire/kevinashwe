<template>
  <div class="row my-5">
    <div class="col-lg-8  col-sm-10 col-xs-12 my-4">
      <h2 class="text-center mb-4">Checkout</h2>
      <form @submit.prevent="submitCheckout">
        <div class="mb-3">
          <label for="name" class="form-label">Full Name</label>
          <input
            type="text"
            id="name"
            class="form-control"
            v-model="form.metadata.full_name"
            required
          />
        </div>
        <div class="mb-3">
          <label for="phone" class="form-label">Mobile Phone </label>
          <input
            id="phone"
            class="form-control"
            v-model="form.metadata.phone"
            required
          />
        </div>
        <div class="mb-3">
          <label for="email" class="form-label">Email</label>
          <input
            type="email"
            id="email"
            class="form-control"
            v-model="form.email"
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
import { v4 as uuid4 } from 'uuid'
import axios from "axios";
import { onMounted, ref } from "vue";

const books = useBookStore();
const tx_ref = ref(null)
const paymetApi = import.meta.env.VITE_PAYSTACK_API

const form = ref({
  reference: tx_ref.value,
  email: "",
  amount: books.totalPrice * 100,
  metadata: {
    email: "",
    full_name: "",
    phone: "",
    custom_fields: books.carts
  }
});

const submitCheckout = async () => {
  form.value.metadata.email = form.value.email
  try {
    const response = await axios.post(
      'https://api.paystack.co/transaction/initialize',
      form.value,
      {
        headers: {
          Authorization: `Bearer ${paymetApi}`,
          'Content-Type': 'application/json',
        },
      })
    //console.log(response.data.data.authorization_url)
    location.href = response.data.data.authorization_url
  } catch (err) {
    console.error(err.code)
    console.error(err)
  }
};
onMounted(()=>{
  tx_ref.value = uuid4()
})
</script>
