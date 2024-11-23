<template>
  <div class="container">
    <a href="/">
      <img
        src="../assets/galaxy_logo_white.svg"
        class="image_logo"
        alt="My Universe Hub logo"
      />
    </a>

    <div class="search-container">
      <InputText
        class="input_text medium-text"
        type="text"
        v-model="searchQuery"
        placeholder="Andromeda galaxy"
        @keyup.enter="handleSearch"
      />
      <span class="icon-container">
        <Transition name="fade">
          <i
            v-if="searchQuery"
            class="fas fa-times clear-icon"
            @click="clearSearch"
          ></i>
        </Transition>
        <Transition name="fade">
          <i
            v-if="searchQuery"
            class="fas fa-paper-plane search-icon medium-text"
            @click="handleSearch"
          ></i>
        </Transition>
      </span>
    </div>

    <Transition name="fade">
      <PaginationBar v-show="searchQuery" @page-size-change="setPageSize" />
    </Transition>
  </div>
</template>

<script>
import axios from "axios";
import InputText from "primevue/inputtext";
import PaginationBar from "./PaginationBar.vue";

export default {
  name: "SearchSection",
  components: {
    InputText,
    PaginationBar,
  },
  data() {
    return {
      searchQuery: "",
      pageSize: 10,
      pageOffset: 0,
    };
  },
  watch: {
    searchQuery() {
      this.pageOffset = 0;
      this.handleSearch();
    },
    pageSize() {
      this.handleSearch();
    },
  },
  methods: {
    async handleSearch() {
      if (this.searchQuery === "") {
        return;
      }

      const endpoint = `${axios.defaults.baseURL}/api/v1/search?search_query=${this.searchQuery}&skip=${this.pageOffset}&limit=${this.pageSize}`;
      await axios
        .get(endpoint)
        .then((response) => {
          let searchResults = response.data.hits;
          // Add timestamp to force reactivity
          this.$emit("search-results", {
            results: searchResults,
            timestamp: Date.now(),
          });
        })
        .catch((error) => {
          console.error(error);
        });
    },
    clearSearch() {
      this.searchQuery = "";
    },
    setPageSize(pageSize) {
      this.pageSize = pageSize;
    },
  },
};
</script>

<style scoped>
.container {
  margin-top: 10rem;
}

.image_logo {
  display: block;
  width: 100%;
  max-width: 10rem;
}

.search-container {
  position: relative;
  display: inline-block;
  margin-top: 3rem;
}

.icon-container {
  position: absolute;
  right: 0.625rem;
  top: 50%;
  transform: translateY(-50%);
  display: flex;
  gap: 0.75rem;
  align-items: center;
}

.clear-icon,
.search-icon {
  cursor: pointer;
  color: #ea5e13;
  transition: color 0.3s ease;
}

.clear-icon {
  font-size: 1.3rem;
}

.search-icon {
  font-size: 1.1rem;
  position: relative;
  top: -1px;
}

.clear-icon:hover,
.search-icon:hover {
  color: #666;
}

.input_text {
  padding-right: 80px;
  width: 60rem;
  height: 3rem;
  border-radius: 0rem;
}

.input_text:focus {
  border-color: #ea5e13 !important;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(1rem);
}

.fade-enter-to,
.fade-leave-from {
  opacity: 1;
  transform: translateY(0);
}
</style>
