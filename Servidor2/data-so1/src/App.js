import React from 'react';
import List from './List';
import axios from 'axios';
import './App.css';


class App extends React.Component {

  constructor(props){
    super(props);

    this.state = {
      lista:[
        {
          autor:"Edgar Aldana",
          nota:"asdfghj"
        },
        {
          autor:"Edgar Aldana",
          nota:"aaaaaaaaa"
        },
        {
          autor:"Edgar Aldana",
          nota:"ggggggggg"
        }
      ]
    };
  }

  getDataServerA = () =>{
    axios.get('http://127.0.0.1:4000/lista')
    .then(result => {
      this.setState({lista:result.data.lista})
    })
    .catch()
  }

  getDataServerB = () =>{
    axios.get('http://127.0.0.1:4000/lista')
    .then(result => {
      this.setState({lista:[]})
    })
    .catch()
  }

  render() {
    return (
      <div className="App"> 
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
        <h1>Publicaciones</h1>
        <List items={this.state.lista} />
      </div>
    );
  }
}
export default App;
