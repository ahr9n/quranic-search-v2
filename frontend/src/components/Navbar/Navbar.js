import React, { Component } from "react";
import "./Navbar.css";
import { Link } from "react-router-dom";

class Navbar extends Component {
  render() {
    return(
        <div>
            <Link class="ask-logo" to="/">سلِ القرآن الكريم</Link>
            <Link class="bookmarks" to="/bookmarks">إشارات مرجعية</Link>
            <Link class="about" to="/about">من نحن؟</Link>
        </div>
    )
  }
}

export default Navbar;