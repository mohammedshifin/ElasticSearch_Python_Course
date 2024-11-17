<template>
  <div class="search_container">
    <SearchSection />
  </div>
</template>

<script>
import SearchSection from "@/components/SearchSection.vue";

export default {
  name: "HomeView",
  components: {
    SearchSection,
  },
};
</script>

<style scoped>
.search_container {
  display: flex;
  justify-content: center;
  margin-top: 10rem;
  margin-left: 5rem;
  margin-right: 5rem;
}
</style>
