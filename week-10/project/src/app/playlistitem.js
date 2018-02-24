'use strict';

var React = require('react');
require('./css/listitems.css');


class MyPlayListItem extends React.Component{
    constructor(props){
        super(props);
        this.handleDelete = this.handleDelete.bind(this);
        this.handleClick = this.handleClick.bind(this);
    }

    handleDelete(){
        this.props.onDelete(this.props.item);
    }

    handleClick(){
        this.props.onPlayListClick(this.props.item);
    }

    render(){
        return(
            <li>
                <div className="myplaylist-item">
                    <span className="item-name" onClick={this.handleClick}>{this.props.item}</span>
                    <span className="item-remove" onClick={this.handleDelete}> x </span>
                </div>
            </li>
        );
    }

};

module.exports = MyPlayListItem