import React from "react";
import "./Verse.css";

const Verse = ( {verse} ) => {
    return(
        <div>
            <h4 class="verse">
                { verse.verse }
                <span>({ verse.surah })|({ verse.numberInSurah })</span>
            </h4>
            <hr class="line"/>
        </div>
    );
};

export default Verse;