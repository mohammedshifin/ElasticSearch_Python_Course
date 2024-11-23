<template>
  <div class="pagination-bar-container">
    <div class="page-size">
      <span class="medium-text">Items per page</span>
      <Select
        checkmark
        class="page-size-selector medium-text"
        v-model="selectedPageSize"
        :options="pageSizes"
        :placeholder="selectedPageSize"
        :highlightOnSelect="false"
        :modelValue="selectedPageSize"
        @update:modelValue="handlePageSizeChange"
        size="large"
      />
    </div>

    <div class="pagination-buttons">
      <button
        :disabled="currentPage === 1"
        @click="goToFirstPage"
        class="pagination-btn medium-text"
      >
        <i class="fas fa-angle-double-left"></i> First
      </button>
      <button
        :disabled="currentPage === 1"
        @click="goToPreviousPage"
        class="pagination-btn medium-text"
      >
        <i class="fas fa-chevron-left"></i> Previous
      </button>

      <span class="current-page medium-text">
        {{ currentPage }} / {{ maxPages }}
      </span>

      <button
        :disabled="currentPage === maxPages"
        @click="goToNextPage"
        class="pagination-btn medium-text"
      >
        Next <i class="fas fa-chevron-right"></i>
      </button>
      <button
        :disabled="currentPage === maxPages"
        @click="goToLastPage"
        class="pagination-btn medium-text"
      >
        Last <i class="fas fa-angle-double-right"></i>
      </button>
    </div>
  </div>
</template>

<script>
import Select from "primevue/select";

export default {
  name: "PaginationBar",
  components: {
    Select,
  },
  props: {
    currentPage: {
      type: Number,
      required: true,
    },
    maxPages: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      selectedPageSize: 10,
      pageSizes: [10, 20, 50],
    };
  },
  methods: {
    handlePageSizeChange() {
      this.$emit("page-size-change", this.selectedPageSize);
    },
    goToFirstPage() {
      this.$emit("go-to-page", 1);
    },
    goToPreviousPage() {
      if (this.currentPage > 1) {
        this.$emit("go-to-page", this.currentPage - 1);
      }
    },
    goToNextPage() {
      if (this.currentPage < this.maxPages) {
        this.$emit("go-to-page", this.currentPage + 1);
      }
    },
    goToLastPage() {
      this.$emit("go-to-page", this.maxPages);
    },
  },
};
</script>

<style scoped>
.pagination-bar-container {
  display: flex;
  justify-content: space-between;
  border: 1px solid rgba(234, 94, 19, 0.2);
  background: rgba(255, 255, 255, 0.05);
  padding: 0.5rem;
  width: 60rem;
  margin-top: 1rem;
}

.page-size-selector {
  margin-left: 1rem;
  border-radius: 0rem;
  height: 3rem;
  background: transparent;
}

.pagination-buttons {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.pagination-btn {
  background: transparent;
  height: 3rem;
  border: 1px solid rgba(234, 94, 19, 0.2);
  padding: 0.5rem;
  border-radius: 0rem;
  cursor: pointer;
  transition: background-color 0.3s ease, color 0.3s ease;
}

.pagination-btn:disabled {
  cursor: not-allowed;
  color: #666;
}

.pagination-btn:hover {
  background-color: rgba(234, 94, 19, 0.1);
}

.current-page {
  margin: 0 1rem;
}
</style>
