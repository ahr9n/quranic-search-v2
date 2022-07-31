import React, { Component } from "react";
import {useNavigate} from 'react-router-dom';
import "./HomeForm.css";

class BasicHomeForm extends Component {
    state = {
        verse: [],
        surah: [],
        numberInSurah: [],
        audio: [],
    }

    constructor(props) {
        super(props);
        this.state = {
            value: '',
            // search_type: '',
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmitLex = this.handleSubmitLex.bind(this);
        this.handleSubmitSem = this.handleSubmitSem.bind(this);
    }

    handleChange(event) {
        this.setState({ value: event.target.value });
    }

    handleSubmitLex(event){
        event.preventDefault();
        console.log(this.state.value);
        
        const input = this.state.value;
        // this.setState({search_type: 'lexical'});

        fetch(`http://localhost:8000/api/lexical/search/${input}`)
        .then(response => response.json())
        .then(res => {
            console.log(res.data);
            this.props.setSearchResults(res.data);
            this.props.navigate("/results");
        })
    }
    
    handleSubmitSem(event){
        event.preventDefault();
        console.log(this.state.value);
        
        const input = this.state.value;
        // this.setState({search_type: 'semantic'});

        fetch(`http://localhost:5000/api/semantic/similar-verse/${input}`)
        .then(response => response.json())
        .then(res => {
            console.log(res.data);
            this.props.setSearchResults(res.data);
            this.props.navigate("/results");
        })       
    }
    
    render() {
        return (
            <div>
                <form class="index-form" >
                    <img class="index-logo" src="/images/quran-logo.png" alt="Quran Logo" />
                    <input class="index-input" onChange={this.handleChange} dir="rtl" type="text" name="input" value={this.state.value} placeholder='فيم تريد أن تبحث؟' />
                               
                    <input class="index-lexical" onClick={this.handleSubmitLex} type="submit" value="ابحــث باللفظ" name='lexical' />
                    <input class="index-semantic" onClick={this.handleSubmitSem} type="submit" value="ابحـث بالمعنى" name="semantic" />
                </form>
            </div>
        )
    }
}

const HomeForm = (props) => {
    const navigate= useNavigate();
    return (
    <BasicHomeForm
     {...props} 
     navigate= {navigate}/>
    );  
};

export default HomeForm;
