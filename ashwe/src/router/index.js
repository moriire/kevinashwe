import { createRouter,  createWebHashHistory } from "vue-router";
import HeroSection from "../components/HeroSection.vue";
import PodcastSection from "../components/PodcastSection.vue";
import CartView from "@/views/CartView.vue";
import CheckoutPage from "../components/CheckoutPage.vue";
import BaseView from "../views/BaseView.vue";
import HomeView from "@/views/HomeView.vue";
import BookDetailsView from "@/views/BookDetailsView.vue";
import BookList from "@/views/BookList.vue";
import SuccessView from '@/views/SuccessView.vue'

const routes = [
  { path: "/home", component: HeroSection },
  { path: "/", component: HomeView},
  {
    path: "/",
    component: BaseView,
    children: [
      { path: "/books", component: BookList },
      { path: "/book/:pk", name:"book", component: BookDetailsView },
      { path: "/podcasts", component: PodcastSection },
      { path: "/cart", component: CartView },
      { path: "/checkout", component: CheckoutPage },
      {
        path: '/payment-success',
        name: 'payment-success',
        component: SuccessView,
        meta: { title: "Payment Success" }
      },
    ],
  },
];

const router = createRouter({
  history:  createWebHashHistory("/kevin-ashwe/"),
  routes,
  activeClass:"active",
  exactActiveClass: "active"
});

export default router;