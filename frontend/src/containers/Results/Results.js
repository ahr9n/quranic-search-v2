import React  from "react";
import ResultsForm from "../../components/ResultsForm/ResultsForm";
import Verse from "../../components/Verse/Verse";

const Results = ( {search_results, setSearchResults} ) => {
    return(
        <div className="Results">
            <ResultsForm setSearchResults = {setSearchResults} />
            <span id="type">نتائج البحث: {search_results.length}</span>
            <hr class="line"/>
            <div>
            {
                search_results.map((item, i) => {
                    return(
                        <Verse verse={item} />
                    );
                })
            }
            </div>
        </div>
    );
};

export default Results;