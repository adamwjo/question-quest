import React from 'react'
import Question from '../containers /question'

export default class QuestionBox extends React.Component {

    state = {
        questions: []
    }

    componentDidMount(){
        fetch('http://127.0.0.1:8000/api/questions')
            .then(r => r.json())
            .then(data => console.log(data))
    }

    render(){
        return(
            <div>
                <Question/> 
            </div>
        )
    }
}