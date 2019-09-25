// import React from 'react';
import logo from './logo.svg';
import './App.css';
import Chat from './containers/Chat';
import WebSocketInstance from './websocket';




class App extends React.Component{
  
  componentDidMount(){
    WebSocketInstance.connect();
  }

  render() {
    return (
      <Chat />
    );
  }
}

export default App;
