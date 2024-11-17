<template>
  <img
    src="../assets/galaxy_logo_white.svg"
    class="image_logo"
    alt="My Universe Hub logo"
  />
</template>

<script>

export default {
  name: "SearchSection",
  components: {
  },
  data() {
    return {
      searchQuery: "",
    };
  },
};
</script>

<style scoped>
.image_logo {
  width: 100%;
  max-width: 10rem;
}
</style>
