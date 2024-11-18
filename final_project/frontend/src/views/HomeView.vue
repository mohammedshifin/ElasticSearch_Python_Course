<template>
  <SearchSection @search-results="handleSearchResults" />
  <GallerySection :searchResults="searchResults" />
</template>

<script>
import SearchSection from "@/components/SearchSection.vue";
import GallerySection from "@/components/GallerySection.vue";

export default {
  name: "HomeView",
  components: {
    SearchSection,
    GallerySection,
  },
  data() {
    return {
      searchResults: [],
    };
  },
  methods: {
    handleSearchResults(results) {
      this.searchResults = results;
    },
  },
};
</script>
