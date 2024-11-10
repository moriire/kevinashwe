<script setup>
import { onMounted } from 'vue';
import { RouterLink } from 'vue-router';
onMounted(()=>localStorage.removeItem("carts"))
</script>
<template>
  <div class="container d-flex flex-column align-items-center text-center py-5">
    <!-- Success GIF Animation -->
    <img src="@/assets/success.gif" alt="Success" class="success-gif mb-4" />

    <!-- Success Message -->
    <h2 class="text-success mb-3">Order Placed Successfully!</h2>
    <p class="text-muted">
      Thank you for your purchase! Your order has been successfully placed and is now being processed.
    </p>

    <!-- Action Buttons -->
    <div class="d-flex gap-3 mt-4">
      <RouterLink to="/shop" class="btn btn-primary btn-lg">
        Continue Shopping
      </RouterLink>
     
    </div>
    </div>
</template>

<style scoped>
.success-gif {
  max-width: 250px;
  height: auto;
  border-radius: 10px;
}

.container {
  max-width: 600px;
}

h2 {
  font-family: "Arial", sans-serif;
}

.btn {
  min-width: 150px;
}
</style>
