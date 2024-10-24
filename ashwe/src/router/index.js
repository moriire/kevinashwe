import { createRouter, createWebHistory } from "vue-router";
import HeroSection from "../components/HeroSection.vue";
import BooksSwiper from "../components/BooksSwiper.vue";
import PodcastSection from "../components/PodcastSection.vue";
import CartPage from "../components/CartPage.vue";
import CheckoutPage from "../components/CheckoutPage.vue";
import BaseView from "../views/BaseView.vue";
import HomeView from "@/views/HomeView.vue";
const routes = [
  { path: "/", component: HeroSection },
  { path: "/home", component: HomeView},
  {
    path: "/",
    component: BaseView,
    children: [
      { path: "/books", component: BooksSwiper },
      { path: "/podcasts", component: PodcastSection },
      { path: "/cart", component: CartPage },
      { path: "/checkout", component: CheckoutPage },
    ],
  },
];

const router = createRouter({
  history: createWebHistory("/kevin-ashwe/"),
  routes,
  activeClass:"active",
  exactActiveClass: "active"
});

export default router;