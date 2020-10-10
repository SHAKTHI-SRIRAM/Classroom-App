import React from 'react';
import CreateIcon from '@material-ui/icons/Create';
import SendIcon from '@material-ui/icons/Send';
import MenuBookIcon from '@material-ui/icons/MenuBook';

import './Classroom.css'

function Classroom() {
    return (
        <div className='classroom'>
            <div className="classroom-top">
                <h1>Computer Science Class 11</h1>
                <div className="teachers">
                    <h5>Ms.Shobana</h5>
                </div>
                <div className="stats">
                <h3>Your Score: 2500</h3>
                <h3>No.of tests: 25</h3>
                <h3>No.of homeworks: 50</h3>
                </div>
            </div>
            <div className="classroom-main">
                <div className="tests">
                    <div className="top">
                        <CreateIcon />
                        <h1>Tests</h1>
                    </div>
                    <div className="tests-desc">
                        <div className="box">
                            <h4>Binary Addition</h4>
                            <p>15th October</p>
                        </div>
                        <div className="box">
                            <h4>2's Complement</h4>
                            <p>10th October</p>
                        </div>
                    </div>
                </div>
                <div className="hws">
                    <div className="top">
                        <MenuBookIcon />
                        <h1>Homeworks</h1>
                    </div>
                    <div className="hw-desc">
                        <div className="hwbox">
                            <h4>Logic Gates</h4>
                            <p>15th October</p>
                        </div>
                        <div className="hwbox">
                            <h4>Boolean Logic Book Back Questions</h4>
                            <p>10th October</p>
                        </div>
                    </div>
                </div>
            </div>
            <div className="right">
                <div className="doubtbox">
                    <div className="chat-top">
                        <h3>Doubt Box</h3>
                    </div>
                    <div className="chat-mid">
                        <div className="chat-left">  
                        <p className='name-left'>Ms.Shobana</p>
                        <span className="message-left">
                            Hello
                        </span>
                        </div>
                        <div className="chat-left">  
                        <p className='name-left'>Ms.Shobana</p>
                        <span className="message-left">
                            Hello
                        </span>
                        </div>
                        <div className="chat-left">
                        <p className='name-left'>Ms.Shobana</p>
                        <span className="message-left">
                            In this doubt box you can ask all your doubts.
                        </span>
                        </div>
                        <div className="chat-left">
                        <p className='name-right'>Me</p>
                        <span className="message-right">
                            Hello mam
                        </span>
                        </div>
                        <div className="chat-left">
                        <p className='name-right'>Me</p>
                        <span className="message-right">
                            I have doubt in Logic gates
                        </span>
                        </div>
                        <div className="chat-left">
                        <p className='name-left'>Ms.Shobana</p>
                        <span className="message-left">
                            Ok pa we will discuss about it in today's class
                    </span>
                        </div>
                    </div>
                    <div className="chat-bottom">
                        <input type="text"/>
                        <button>
                            <SendIcon />
                        </button>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Classroom
