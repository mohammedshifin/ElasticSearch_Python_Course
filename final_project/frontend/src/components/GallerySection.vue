<template>
  <div class="search_container">
    {{ searchResults.length }}
  </div>
</template>

<script>
export default {
  name: "GallerySection",
  props: {
    searchResults: {
      type: Array,
      required: true,
    },
  },
}
</script>

<style scoped>
.search_container {
  margin-top: 5rem;
}
</style>