<template>
  <div>
    <h2>Add New Member</h2>
    <form @submit.prevent="addMember">
      <input type="text" v-model="name" placeholder="Member Name" />
      
      <select v-model="selectedRoles" multiple>
        <option v-for="role in roles" :key="role.id" :value="role.id">{{ role.name }}</option>
      </select>
      
      <button type="submit">Add Member</button>
    </form>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';

export default {
  setup() {
    const name = ref('');
    const selectedRoles = ref([]);
    const roles = ref([]);

    // Fetch roles from the backend
    const fetchRoles = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/roles/');
        roles.value = response.data;
      } catch (error) {
        console.error('Error fetching roles:', error);
      }
    };

    // Add new member to the backend
    const addMember = async () => {
      try {
        await axios.post('http://localhost:8000/api/members/', {
          name: name.value,
          roles: selectedRoles.value,
        });
        name.value = ''; // Clear the name field
        selectedRoles.value = []; // Clear the selected roles
      } catch (error) {
        console.error('Error adding member:', error);
      }
    };

    // Fetch roles on mount
    onMounted(fetchRoles);

    return {
      name,
      selectedRoles,
      roles,
      addMember,
    };
  },
};
</script>
