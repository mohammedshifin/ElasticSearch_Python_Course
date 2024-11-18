<template>
  <StarsBackground />
  <router-view />
</template>

<script>
import StarsBackground from "@/components/StarsBackground.vue";

export default {
  name: "App",
  components: {
    StarsBackground,
  },
};
</script>

<style>
body {
  font-family: "Roboto Condensed", sans-serif;
}

.search_container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-left: 5rem;
  margin-right: 5rem;
}
</style>
