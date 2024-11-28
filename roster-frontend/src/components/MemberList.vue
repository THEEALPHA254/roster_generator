<template>
  <div>
    <h2>Members</h2>
    <ul>
      <li v-for="member in members" :key="member.id">
        {{ member.name }} - Roles: {{ member.roles.map(role => role.name).join(', ') }}
      </li>
    </ul>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';

export default {
  setup() {
    // Reactive state
    const members = ref([]);

    // Fetch members from the API
    const fetchMembers = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/members/');
        members.value = response.data;
      } catch (error) {
        console.error('Error fetching members:', error);
      }
    };

    // Fetch members when component is mounted
    onMounted(() => {
      fetchMembers();
    });

    return {
      members
    };
  }
};
</script>
