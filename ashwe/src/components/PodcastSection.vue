<template>
    <section class="my-5">
      <div class="container">
        <h2 class="text-center mb-4">Podcasts by Kevin Ashwe</h2>
        <div class="row" style="height:80vh;">
          <div class="col-md-6 mb-4" v-for="podcast in podcasts" :key="podcast.id">
            <div class="card">
              <div class="card-body">
                <h5 class="card-title">{{ podcast.title }}</h5>
                <audio :src="podcast.audio" controls class="w-100"></audio>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </template>
  
  <script>
  export default {
    data() {
      return {
        podcasts: [
          { id: 1, title: 'Episode 1', audio: '/home/baun/Documents/ai-tutor.mp4' },
          { id: 2, title: 'Episode 2', audio: '/home/baun/Documents/ai-tutor.mp4' },
        ],
      };
    },
  };
  </script>
  