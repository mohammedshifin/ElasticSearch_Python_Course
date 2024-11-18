<template>
  <SearchSection @search-results="handleSearchResults" />
</template>

<script>
import SearchSection from "@/components/SearchSection.vue";

export default {
  name: "HomeView",
  components: {
    SearchSection,
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
