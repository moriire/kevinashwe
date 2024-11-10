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
  { path: "/", component: HomeView, meta:{ title: 'Welcome'}},
  {
    path: "/",
    component: BaseView,
    children: [
      { path: "/books", component: BookList, meta:{ title: 'All Books'} },
      { path: "/book/:pk", name:"book", component: BookDetailsView, meta:{ title: "book"} },
      { path: "/podcasts", component: PodcastSection, meta:{ title: 'Coming Soon'} },
      { path: "/cart", component: CartView, meta:{ title: 'Your Cart'} },
      { path: "/checkout", component: CheckoutPage, meta:{ title: 'Pay Securely'} },
      {
        path: '/payment-success',
        name: 'payment-success',
        component: SuccessView,
        meta: { title: "Payment Success" }
      },
      {
        path: '/about',
        name: 'about',
        component: PodcastSection,
        meta: { title: "About" }
      },
    ],
  },
];

const router = createRouter({
  history:  createWebHashHistory("/kevin-ashwe/"),
  linkActiveClass: 'active',
  linkExactActiveClass: 'active',
  routes,
  activeClass:"active",
  exactActiveClass: "active"
});


router.afterEach((to) => {
  document.title = `${to.meta.title}|Kevin Ashwe`
  console.log(router.value)
  setTimeout(() => hideLoader(), 500); 
})

export default router;