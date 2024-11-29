<template>
  <div class="container">
    <a href="/">
      <img
        src="../assets/galaxy_logo_white.svg"
        class="image_logo"
        alt="My Universe Hub logo"
      />
    </a>

    <Transition name="fade">
      <div v-if="errorExists" class="error-message">{{ errorMessage }}</div>
    </Transition>

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
            v-tooltip.top="'Clear search'"
          ></i>
        </Transition>
      </span>
    </div>

    <Transition name="fade">
      <PaginationBar
        v-show="canPerformSearch"
        :currentPage="currentPage"
        :maxPages="max_pages"
        :yearOptions="yearOptions"
        @page-size-change="handlePageSizeChange"
        @year-change="handleYearChange"
        @go-to-page="handlePageChange"
        @search-method-change="handleSearchMethodChange"
      />
    </Transition>

    <Transition name="fade">
      <div v-if="noResultsFound" class="no-results-message">
        <i class="fas fa-search"></i> No results found.
      </div>
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
      currentPage: 1,
      max_pages: null,
      errorExists: false,
      errorMessage: "",
      noResultsFound: false,
      yearOptions: {},
      selectedYear: null,
      selectedSearchMethod: null,
    };
  },
  watch: {
    searchQuery() {
      this.pageOffset = 0;
      if (this.searchQuery !== "") {
        this.getYearOptions();
        this.handleSearch();
      }
    },
    pageSize() {
      this.handleSearch();
    },
    pageOffset() {
      this.handleSearch();
    },
    selectedYear() {
      this.handleSearch();
    },
    selectedSearchMethod() {
      this.handleSearch();
    },
  },
  computed: {
    canPerformSearch() {
      return this.searchQuery && !this.errorExists;
    },
  },
  methods: {
    async handleSearch() {
      if (this.searchQuery === "") {
        this.errorMessage = "Please enter a search query.";
        this.errorExists = true;
        return;
      }

      const year = this.selectedYear ? this.selectedYear.slice(0, 4) : ''
      let endpoint = ""

      if (this.selectedSearchMethod === "Semantic search") {
        endpoint = `${axios.defaults.baseURL}/api/v1/semantic_search?search_query=${this.searchQuery}&skip=${this.pageOffset}&limit=${this.pageSize}&year=${year}`;
      } else {
        endpoint = `${axios.defaults.baseURL}/api/v1/regular_search?search_query=${this.searchQuery}&skip=${this.pageOffset}&limit=${this.pageSize}&year=${year}`;
      }
      
      await axios
        .get(endpoint)
        .then((response) => {
          let searchResults = response.data.hits;
          this.noResultsFound = searchResults.length === 0;
          this.max_pages = response.data.max_pages;

          // Add timestamp to force reactivity
          this.$emit("search-results", {
            results: searchResults,
            timestamp: Date.now(),
          });
          this.errorExists = false;
        })
        .catch((error) => {
          console.error(error);
          this.errorMessage = error.response.data;
          this.errorExists = true;
        });
    },
    async getYearOptions() {
      const endpoint = `${axios.defaults.baseURL}/api/v1/get_docs_per_year_count?search_query=${this.searchQuery}`;
      await axios
        .get(endpoint)
        .then((response) => {
          this.yearOptions = Object.entries(response.data.docs_per_year).map(
            ([year, count]) => `${year} (${count})`
          );
        })
        .catch((error) => {
          console.error(error);
        });
    },
    clearSearch() {
      this.searchQuery = "";
    },
    handlePageSizeChange(pageSize) {
      this.pageOffset = 0;
      this.currentPage = 1;
      this.pageSize = pageSize;
    },
    handleYearChange(year) {
      this.pageOffset = 0;
      this.currentPage = 1;
      this.selectedYear = year;
    },
    handlePageChange(page) {
      this.pageOffset = (page - 1) * this.pageSize;
      this.currentPage = page;
    },
    handleSearchMethodChange(searchMethod) {
      this.selectedSearchMethod = searchMethod;
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
  margin-bottom: 5rem;
}

.search-container {
  position: relative;
  display: inline-block;
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

.clear-icon {
  cursor: pointer;
  color: var(--primary-color);
  transition: color 0.3s ease;
  font-size: 1.5rem;
}

.clear-icon:hover {
  color: #666;
}

.input_text {
  width: 60rem;
  height: 3rem;
  border-radius: 0rem;
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

.error-message {
  margin-bottom: 0.3rem;
  color: rgb(255, 58, 58);
  width: 60rem;
  padding-left: 0.75rem;
}

.no-results-message {
  margin-top: 2rem;
  text-align: center;
  font-size: 1.5rem;
  color: #666;
}

.no-results-message i {
  margin-right: 0.5rem;
}
</style>
