import React, { Component } from "react";
import "./ResultsForm.css";

class ResultsForm extends Component {
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
        
        fetch(`https://localhost:8000/api/laxical/search-word/${input}`)
        .then(response => response.json())
        .then(res => {
            console.log(res.data);
            this.props.setSearchResults(res.data);
        })
    }
    
    handleSubmitSem(event){
        event.preventDefault();
        console.log(this.state.value);
        
        const input = this.state.value;
        // this.setState({search_type: 'semantic'});

        fetch(`https://localhost:5000/api/semantic/similar-verse/${input}`)
        .then(response => response.json())
        .then(res => {
            console.log(res.results);
            this.props.setSearchResults(res.results);
        })        
    }

  render() {
    return(
        <div>
            <form class="results-form">
                <img class="results-logo" src="/images/quran-logo.png" alt="Quran Logo" />
                <input class="results-input" onChange={this.handleChange} dir="rtl" type="text" name="input" value={this.state.value} placeholder='فيم تريد أن تبحث؟' />
                            
                <input class="results-lexical" onClick={this.handleSubmitLex} type="submit" value="ابحــث باللفظ" name='lexical' />
                <input class="results-semantic" onClick={this.handleSubmitSem} type="submit" value="ابحـث بالمعنى" name="semantic" />
            </form>
        </div>
    )
  }
}

export default ResultsForm;
