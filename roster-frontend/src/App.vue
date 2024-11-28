<template>
  <div id="app">
    <AddMember />
    <MemberList />
    <RosterList />
  </div>
</template>

<script>
import AddMember from './components/AddMember.vue'
import MemberList from './components/MemberList.vue'
import RosterList from './components/RosterList.vue'

export default {
  name: 'App',
  components: {
    AddMember,
    MemberList,
    RosterList
  }
}
</script>
