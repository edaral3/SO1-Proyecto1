import React from 'react'
import Item from './item'
import './List.css'

function List(props){
    return(
        <div className="list">
            {
                props.items.map(item =>
                    <div>
                         <Item 
                         autor={item.autor}
                         nota={item.nota}/>
                    </div>
                    
                )
            }
        </div>
    );
}

export default List;