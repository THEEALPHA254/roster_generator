import { createRouter, createWebHistory } from 'vue-router';  // Named imports for Vue 3
import AddMember from './components/AddMember.vue';
import MemberList from './components/MemberList.vue';
import RosterList from './components/RosterList.vue';
import GenerateRoster from './components/GenerateRoster.vue';

// Define your routes
const routes = [
  {
    path: '/',
    name: 'Home',
    component: AddMember
  },
  {
    path: '/members',
    name: 'Members',
    component: MemberList
  },
  {
    path: '/rosters',
    name: 'Rosters',
    component: RosterList
  },
  {
    path: '/generate-roster',
    name: 'GenerateRoster',
    component: GenerateRoster
  }
];

// Create and export the router
const router = createRouter({
  history: createWebHistory(),  // Use history mode
  routes  // Pass the routes configuration
});

export default router;
