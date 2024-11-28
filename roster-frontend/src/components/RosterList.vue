<template>
  <div>
    <h2>Generated Rosters</h2>
    <table>
      <thead>
        <tr>
          <th>Sunday Date</th>
          <th>Members</th>
          <th>Roles</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="roster in rosters" :key="roster.id">
          <td>{{ roster.sunday_date }}</td>
          <td>{{ roster.members.map(member => member.name).join(', ') }}</td>
          <td>{{ roster.roles.map(role => role.name).join(', ') }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';

export default {
  setup() {
    // Reactive state
    const rosters = ref([]);

    // Fetch rosters from the API
    const fetchRosters = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/rosters/');
        rosters.value = response.data;
      } catch (error) {
        console.error('Error fetching rosters:', error);
      }
    };

    // Fetch rosters when component is mounted
    onMounted(() => {
      fetchRosters();
    });

    return {
      rosters
    };
  }
};
</script>
