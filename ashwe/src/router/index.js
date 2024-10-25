import { createRouter,  createWebHashHistory } from "vue-router";
import HeroSection from "../components/HeroSection.vue";
import BooksSwiper from "../components/BooksSwiper.vue";
import PodcastSection from "../components/PodcastSection.vue";
import CartView from "@/views/CartView.vue";
import CheckoutPage from "../components/CheckoutPage.vue";
import BaseView from "../views/BaseView.vue";
import HomeView from "@/views/HomeView.vue";
import BookDetailsView from "@/views/BookDetailsView.vue";

const routes = [
  { path: "/", component: HeroSection },
  { path: "/home", component: HomeView},
  {
    path: "/",
    component: BaseView,
    children: [
      { path: "/books", component: BooksSwiper },
      { path: "/book/:pk", name:"book", component: BookDetailsView },
      { path: "/podcasts", component: PodcastSection },
      { path: "/cart", component: CartView },
      { path: "/checkout", component: CheckoutPage },
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