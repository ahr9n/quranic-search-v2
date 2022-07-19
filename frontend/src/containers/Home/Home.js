import React, { Component } from "react";
import "./Home.css";
import Navbar from "../../components/Navbar/Navbar";
import HomeForm from "../../components/HomeForm/HomeForm";

class Home extends Component {
  render() {
    return (
      <div className="Home">
        <Navbar />
        <HomeForm setSearchResults= {this.props.setSearchResults} />
      </div>
    );
  }
}

export default Home;