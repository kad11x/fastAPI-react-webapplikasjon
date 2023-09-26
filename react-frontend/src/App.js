import logo from './logo.svg';
import './App.css';
import React from 'react';
import Page1 from './components/page1';
import Page2 from './components/page2';
import Page3 from './components/page3';
import Page4 from './components/page4';


class App extends React.Component {
  constructor() {
    super();
    this.state = { activePage: null };
  }

  renderPage(pageComponent) {
    return (
        <div className="page">
          {pageComponent}
        </div>
    );
  }

  render() {
    return (
        <div className="app">
          <h1>Velkommen til min React-app</h1>
          <div className="container">
            {this.renderPage(<Page1 />)}
            {this.renderPage(<Page2 />)}
            {this.renderPage(<Page3 />)}
            {this.renderPage(<Page4 />)}
          </div>
        </div>
    );
  }
}

export default App;
