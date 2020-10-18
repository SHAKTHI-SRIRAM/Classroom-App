import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import { makeStyles } from '@material-ui/core/styles';
import Box from '@material-ui/core/Box';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import Classroom from './Classroom';
import './Main.css';
import axios from './axios';
import { useDataLayerValue } from './Datalayer';


function TabPanel(props) {
    const { children, value, index, ...other } = props;

    return (
        <div
            role="tabpanel"
            hidden={value !== index}
            id={`vertical-tabpanel-${index}`}
            aria-labelledby={`vertical-tab-${index}`}
            {...other}
        >
            {value === index && (
                <Box>
                    {children}
                </Box>
            )}
        </div>
    );
}

TabPanel.propTypes = {
    children: PropTypes.node,
    index: PropTypes.any.isRequired,
    value: PropTypes.any.isRequired,
};

function a11yProps(index) {
    return {
        id: `vertical-tab-${index}`,
        'aria-controls': `vertical-tabpanel-${index}`,
    };
}

const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
        backgroundColor: theme.palette.background.paper,
        display: 'flex',
        height: '89.5vh',
    },
    tabs: {
        borderRight: `1px solid ${theme.palette.divider}`,
        backgroundColor: 'whitesmoke',
        width: '15vw',
    },
}));

export default function VerticalTabs(fetchUrl) {
    const [{ user, is_teacher, is_student, classrooms, tests, homeworks, chats }, dispatch] = useDataLayerValue();
    // const [data , setData] = useState([]);

    useEffect(()=> {
        async function fetchClassroom() {
            const request = await axios.get('http://localhost:8000/api/classrooms/')
            .then((res)=> {
                dispatch({
                    type: "SET_USER",
                    user: res.data.user,
                })
                dispatch({
                    type: "SET_TEACHER",
                    teacher: res.data.is_teacher,
                })
                dispatch({
                    type: "SET_STUDENT",
                    student: res.data.is_student,
                })
                dispatch({
                    type: "SET_CLASSROOMS",
                    classrooms: res.data.classrooms
                })
            }).catch((err) => {
                console.log(err)
                alert("There was an error in the classroom. Please try again later.")
            })  
            return request;
        }
        
        async function fetchTest() {
            const request = await axios.get('http://localhost:8000/api/tests/')
            .then((res)=> {
                dispatch({
                    type: 'SET_TESTS',
                    tests: res.data.tests,
                })
            }).catch((err) => {
                console.log(err)
                alert("There was an error in the classroom. Please try again later.")
            })  
            return request;
        }
        
        async function fetchHomework() {
            const request = await axios.get('http://localhost:8000/api/homeworks/')
            .then((res)=> {
                dispatch({
                    type: 'SET_HOMEWORKS',
                    homeworks: res.data.homeworks,
                })
            }).catch((err) => {
                console.log(err)
                alert("There was an error in the classroom. Please try again later.")
            })  
            return request;
        }

        const classrooms = fetchClassroom();
        const tests = fetchTest();
        const homeworks = fetchHomework();
    }, [fetchUrl])


    const classes = useStyles();
    const [value, setValue] = React.useState(0);

    const handleChange = (event, newValue) => {
        setValue(newValue);
    };

    console.log(user, is_teacher, is_student, classrooms, tests, homeworks, chats)

    const tabsFunc = () => {
        let response = ""
        for (let index = 0; index < classrooms.length; index++) {
            const element = classrooms[index];
            
            let current_tab = `<Tab className='sidebar-comp ' label='${element.classname}' {...a11yProps(${index})} />`
            response += current_tab
        }
        console.log(response)
        return response
    }
    
    return (
        <div className={`main ${classes.root}`}>
            <Tabs
                orientation="vertical"
                variant="scrollable"
                value={value}
                onChange={handleChange}
                aria-label="Vertical tabs example"
                className= {`sidebar ${classes.tabs}`}
            >
                {tabsFunc}
{/* 
                <Tab className='sidebar-comp ' label="Computer Science Class 11" {...a11yProps(0)} />
                <Tab className='sidebar-comp ' label="Class Two" {...a11yProps(1)} />
                <Tab className='sidebar-comp ' label="Class Three" {...a11yProps(2)} />
                <Tab className='sidebar-comp ' label="Class Four" {...a11yProps(3)} />
                <Tab className='sidebar-comp ' label="Class Five" {...a11yProps(4)} />
                <Tab className='sidebar-comp ' label="Class Six" {...a11yProps(5)} />
                <Tab className='sidebar-comp ' label="Class Seven" {...a11yProps(6)} /> */}
            </Tabs>


            <TabPanel value={value} index={0}>
                <Classroom />
            </TabPanel>
            <TabPanel value={value} index={1}>
                Item Two
            </TabPanel>
            <TabPanel value={value} index={2}>
                Item Three
            </TabPanel>
            <TabPanel value={value} index={3}>
                Item Four
            </TabPanel>
            <TabPanel value={value} index={4}>
                Item Five
            </TabPanel>
            <TabPanel value={value} index={5}>
                Item Six
            </TabPanel>
            <TabPanel value={value} index={6}>
                Item Seven
            </TabPanel>
        </div>
    );
}
