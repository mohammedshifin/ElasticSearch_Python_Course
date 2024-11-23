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
/* Customize PrimeVue's default color */
:root {
  --primary-color: #ea5e13;
  --p-primary-color: var(--primary-color) !important;
  --p-select-placeholder-color: #fff !important;
  --p-select-dropdown-color: #fff !important;
}

body {
  font-family: "Roboto Condensed", sans-serif;
}

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-left: 5rem;
  margin-right: 5rem;
}

.action-button {
  width: 2.5rem;
  height: 2.5rem;
  border: none;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
  backdrop-filter: blur(5px);
}

.action-button i {
  font-size: 1rem;
  color: white;
}

.medium-text {
  font-size: 1.2rem !important;
}
</style>
