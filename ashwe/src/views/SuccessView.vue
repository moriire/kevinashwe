<script setup>
import { onMounted } from 'vue';
import { RouterLink, useRouter } from 'vue-router';
const router = useRouter()

async function downloadPDF(url, filename) {
  try {
	const response = await fetch(url);
	const blob = await response.blob();
	const link = document.createElement('a');
	link.href = URL.createObjectURL(blob);
	link.download = filename;
	document.body.appendChild(link);
	link.click();
	document.body.removeChild(link);
  } catch (error) {
	console.error('Error while downloading PDF:', error);
  }
}
const toHome = () =>{
  localStorage.removeItem("carts");
  router.push("/books")
}
</script>
<template>
  <div class="container d-flex flex-column align-items-center text-center py-5">
    <img src="@/assets/success.gif" alt="Success" class="success-gif mb-4" />

    <!-- Success Message -->
    <h2 class="text-success mb-3">Order Placed Successfully!</h2>
    <p class="text-muted">
      Thank you for your purchase! Your order has been successfully placed and is now being processed.
    </p>

    <!-- Action Buttons -->
    <div class="d-flex gap-3 mt-4">
      <button @click="downloadPDF('/file.enc', 'kevin-ashwe.enc')" class="btn btn-primary btn-lg">
        Click to Download
    </button>
      <button @click="toHome" class="btn btn-primary btn-lg">
        Continue Shopping
      </button>
    </div>
    </div>
</template>

<style scoped>
.success-gif {
  max-width: 250px;
  height: auto;
  border-radius: 10px;
}

h2 {
  font-family: "Arial", sans-serif;
}

.btn {
  min-width: 150px;
}
</style>
