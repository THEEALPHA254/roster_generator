<template>
  <div>
    <h2>Generate Roster</h2>
    <form @submit.prevent="generateRoster">
      <label for="sunday_date">Sunday Date:</label>
      <input type="date" v-model="sunday_date" required />

      <label for="members">Select Members:</label>
      <select v-model="selectedMembers" multiple required>
        <option v-for="member in members" :key="member.id" :value="member.id">{{ member.name }}</option>
      </select>

      <button type="submit">Generate Roster</button>
    </form>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';

export default {
  setup() {
    // Reactive state
    const sunday_date = ref('');
    const selectedMembers = ref([]);
    const members = ref([]);

    // Fetch members from the backend
    const fetchMembers = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/members/');
        members.value = response.data;
      } catch (error) {
        console.error('Error fetching members:', error);
      }
    };

    // Generate the roster by posting the data to the backend
    const generateRoster = async () => {
      const rosterData = {
        sunday_date: sunday_date.value,
        members: selectedMembers.value.map(id => ({ id }))
      };

      try {
        await axios.post('http://localhost:8000/api/rosters/', rosterData);
        // Reset form after submission
        sunday_date.value = '';
        selectedMembers.value = [];
      } catch (error) {
        console.error('Error generating roster:', error);
      }
    };

    // Fetch members when component is mounted
    onMounted(() => {
      fetchMembers();
    });

    return {
      sunday_date,
      selectedMembers,
      members,
      generateRoster,
    };
  },
};
</script>
