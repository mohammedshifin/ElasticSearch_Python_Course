<template>
  <div class="search_container">
    <img
      src="../assets/galaxy_logo_white.svg"
      class="image_logo"
      alt="My Universe Hub logo"
    />

    <InputText
      class="input_text"
      type="text"
      v-model="searchQuery"
      placeholder="Andromeda galaxy"
      @keyup.enter="handleSearch"
    />
  </div>
</template>

<script>
import axios from "axios";
import InputText from "primevue/inputtext";

export default {
  name: "SearchSection",
  components: {
    InputText,
  },
  data() {
    return {
      searchQuery: "",
    };
  },
  methods: {
    async handleSearch() {
      if (this.searchQuery === "") {
        return;
      }

      const endpoint = `${axios.defaults.baseURL}/api/v1/search?search_query=${this.searchQuery}`;
      await axios
        .get(endpoint)
        .then((response) => {
          let searchResults = response.data.hits;
          this.$emit("search-results", searchResults);
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>

<style scoped>
.search_container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 10rem;
  margin-left: 5rem;
  margin-right: 5rem;
}

.image_logo {
  display: block;
  width: 100%;
  max-width: 10rem;
}

.input_text {
  margin-top: 3rem;
  width: 60rem;
  height: 3rem;
  border-radius: 0rem;
  font-size: 1.2rem;
  font-family: "Roboto Condensed", sans-serif;
}

.input_text:focus {
  border-color: #ea5e13 !important;
}
</style>
