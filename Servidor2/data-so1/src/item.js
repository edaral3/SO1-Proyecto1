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
            <div className="div1">
                {this.props.autor}
                <br></br>
                {this.props.nota}
            </div>
        );
    }
}

export default Item;