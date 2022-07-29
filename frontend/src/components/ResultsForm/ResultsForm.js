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
        
        fetch(`http://localhost:8000/api/lexical/search/${input}`)
        .then(response => response.json())
        .then(res => {
            console.log(res);
            console.log(res.data);
            this.props.setSearchResults(res.data);
        })
    }
    
    handleSubmitSem(event){
        event.preventDefault();
        console.log(this.state.value);
        
        const input = this.state.value;
        // this.setState({search_type: 'semantic'});

        fetch(`http://localhost:5000/api/semantic/similar-verse/${input}`)
        .then(response => response.json())
        .then(res1 => {
            res1 = res1.results;
            console.log(res1.length);

            var output = [];
            for (let i = 0; i < res1.length; i++) {
                fetch(`http://localhost:8000/api/lexical/verse-in-quran/${res1[i][1]}`)
                .then(response => response.json())
                .then(res2 => {
                    output.push(res2.data);
                    this.props.setSearchResults(output);
                    this.props.navigate("/results");
                })
            }
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
