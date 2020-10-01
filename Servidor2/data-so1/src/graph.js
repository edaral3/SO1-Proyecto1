import React from 'react'
import { Line } from "react-chartjs-2";
import axios from 'axios';

class Graph extends React.Component{
        
  constructor(props){
    super(props);

    const data = {
        labels: [],
        datasets: [
          {
            label: "RAM 1",
            data: [],
            fill: true,
            backgroundColor: "rgba(255,153,15,0.2)",
            borderColor: "rgba(255,153,15,1)"
          },
          {
            label: "RAM 2",
            data: [],
            fill: true,
            backgroundColor: "rgba(128,128,128,0.2)",
            borderColor: "rgba(128,128,128,1)"
          }
        ]
      };
    
    const data2 = {
        labels: [],
        datasets: [
            {
              label: "CPU 1",
              data: [],
              fill: true,
              backgroundColor: "rgba(255,153,15,0.2)",
              borderColor: "rgba(255,153,15,1)"
            },
            {
              label: "CPU 2",
              data: [],
              fill: true,
              backgroundColor: "rgba(128,128,128,0.2)",
              borderColor: "rgba(128,128,128,1)"
            }
          ]
        };

    this.state = {
      titulo: "Publicaciones",
      lista: [],
      data: data,
      data2: data2,
      cont:0
    };
    this.getRAMCPUServerA()
  }

  getRAMCPUServerA = () => {
    setInterval(() => {
        axios.get('http://13.58.195.101/ram')
        .then(result => {
            var data = this.state.data
            data.datasets[0].data.push(result.data.response)
          
          this.setState({data:data})
          
        })
        .catch()

        axios.get('http://13.58.15.216/ram')
        .then(result => {
          var data = this.state.data
          data.datasets[1].data.push(result.data.response)
        
          data.labels.push(this.state.cont+"s")

          this.setState({data:data})
          
        })
        .catch()

        axios.get('http://13.58.195.101/cpu2')
        .then(result => {
            var data2 = this.state.data2
            data2.datasets[0].data.push(result.data.response)
          
          this.setState({data2:data2})
          
        })
        .catch()

        axios.get('http://13.58.15.216/cpu2')
        .then(result => {
          var data2 = this.state.data2
          data2.datasets[1].data.push(result.data.response)
        
          data2.labels.push(this.state.cont+"s")

          this.setState({data2:data2})
          
        })
        .catch()

        this.setState({cont:this.state.cont+5})
      }, 5000)
  }

        render(){
            return(
                <div className="div2">
                    
                    <Line data={this.state.data} />
                    <Line data={this.state.data2} />
                </div>
            );
        }
    }

export default Graph;