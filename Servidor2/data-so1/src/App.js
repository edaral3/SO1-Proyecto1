import React from 'react';
import List from './List';
import Graph from './graph';
import axios from 'axios';
import './App.css';

class App extends React.Component {
  
  constructor(props){
    super(props);
    this.state = {
      titulo: "Publicaciones",
      lista: []
    };
  }

  servidor = true

  getDataServerA = () => {
    this.servidor = true
    setInterval(() => {
      if(this.servidor){
        axios.get('http://13.58.195.101/notas')
        .then(result => {
          var obj = JSON.parse(result.data.response)
          this.setState({titulo:"Publicaciones A", lista:obj})
        })
        .catch()
      }            
      }, 1000)
  }

  getDataServerB = () => {
    this.servidor = false
    setInterval(() => {
      if(!this.servidor){
        axios.get('http://13.58.15.216/notas')
        .then(result => {
          var obj = JSON.parse(result.data.response)
          this.setState({titulo:"Publicaciones B", lista:obj})
        })
        .catch()   
      }         
      }, 1000)
  }

  render() {
    return (
      
      <div className="App"> 
      <Graph/>
      <br></br>
      <button
      type="button" 
        className="btn btn-success"
        onClick={this.getDataServerA}
      >
        Servidor A
      </button>
        <button
        type="button" 
        className="btn btn-warning"
          onClick={this.getDataServerB}
        >
          Servidor B
        </button>
    <h1>{this.state.titulo}</h1>
        <List items={this.state.lista} />
      </div>
    );
  }
}
export default App;
