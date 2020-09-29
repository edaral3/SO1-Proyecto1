import React from 'react'
import './Item.css'

class Item extends React.Component{
    constructor(props){
        super(props)

        this.state = {

        }
    }

    render(){
        return(
            <div className="item">
                <div className="title">{this.props.autor}</div>
                <div>{this.props.nota}</div>
            </div>
        );
    }
}

export default Item;