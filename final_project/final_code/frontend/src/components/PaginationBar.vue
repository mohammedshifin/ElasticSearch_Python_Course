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
  </div>
</template>

<script>
import Select from "primevue/select";

export default {
  name: "PaginationBar",
  components: {
    Select,
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
  },
};
</script>

<style scoped>
.pagination-bar-container {
  border: 1px solid rgba(234, 94, 19, 0.2);
  background: rgba(255, 255, 255, 0.05);
  padding: 0.5rem;

  width: 60rem;
  margin-top: 1rem;
}

.page-size-selector {
  margin-left: 1rem;
  border-radius: 0rem;
}
</style>
