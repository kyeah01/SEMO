<script>
import {Bar} from 'vue-chartjs'

export default {
  name: 'BarChart',
  extends: Bar,
  props: {
    chartData: {
      type: Object,
      required: true,
    }
  },
  data() {
    return {
      datacollection: {
        labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        datasets: [
          {
            label: 'request',
            backgroundColor: '#f87979',
            pointBackgroundColor: 'white',
            borderWidth: 1,
            pointBorderColor: '#249EBF',
            data: [40, 20, 30, 50, 90, 10, 20]
          }
        ]
      },
      options: {
        scales: {
          yAxes: [{
            ticks: {
              beginAtZero: true
            },
            gridLines: {
              display: true
            }
          }],
          xAxes: [ {
            gridLines: {
              display: false
            }
          }]
        },
        legend: {
            display: false
          },
        responsive: true,
        maintainAspectRatio: false
      }
    }
  },
  mounted() {
    this.renderChart(this.datacollection, this.options)
  },
  watch: {
    chartData: {
      deep: true,
      handler() {
        this.datacollection.datasets[0].data = this.chartData.collection.data
        this.datacollection.datasets[0].backgroundColor = this.chartData.color
        this.renderChart(this.datacollection, this.options)
      }
    }
  },
  methods: {
  }
}
</script>
