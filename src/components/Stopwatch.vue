<template>
  
      <v-card
  elevation="2"
  loading
  style="height:50px">
    <p class="pt-4">Time:{{ time | secondsInMinutes }}</p>
</v-card>

  
</template>

<script>
import moment from "moment";
export default {
  name: "Stopwatch",
  props: {
    running: {
      type: Boolean,
      default: false
    },
    resetWhenStart: {
      type: Boolean,
      default: false
    },
    restWhenStop: {
      type: Boolean,
      default: false
    }
  },
  watch: {
    running: function(newVal) {
      if (newVal) this.startT();
      else this.stopT();
    }
  },
  mounted() {
    if (this.running) this.startT();
  },
  data() {
    return { time: 0, timer: null };
  },
  methods: {
    stopT: function() {
      clearInterval(this.timer);
      if (this.restWhenStop) this.resetT();
    },
    startT: function() {
      if (this.resetWhenStart) this.resetT();
      this.timer = setInterval(() => {
        this.time++;
      }, 1000);
    },
    resetT: function() {
      this.time = 0;
    }
  },
  filters: {
    secondsInMinutes: function(seconds) {
      return moment("2015-01-01")
        .startOf("day")
        .seconds(seconds)
        .format("HH:mm:ss");
    }
  }
};
</script>

<style scoped>
p {
  font-weight: bold;
  font-size: x-large;
}
</style>
