import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import { makeStyles } from '@material-ui/core/styles';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import Classroom from './Classroom';
import './Main.css';
import axios from './axios';

function TabPanel(props) {
    const { children, value, index, ...other } = props;

    const [data , setData] = useState([]);

    useEffect(()=> {

    }, [])

    return (
        <div
            role="tabpanel"
            hidden={value !== index}
            id={`vertical-tabpanel-${index}`}
            aria-labelledby={`vertical-tab-${index}`}
            {...other}
        >
            {value === index && (
                <Classroom />
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

export default function VerticalTabs() {
    const classes = useStyles();
    const [value, setValue] = React.useState(0);

    const handleChange = (event, newValue) => {
        setValue(newValue);
    };

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
                <Tab className='sidebar-comp ' label="Computer Science Class 11" {...a11yProps(0)} />
                <Tab className='sidebar-comp ' label="Class Two" {...a11yProps(1)} />
                <Tab className='sidebar-comp ' label="Class Three" {...a11yProps(2)} />
                <Tab className='sidebar-comp ' label="Class Four" {...a11yProps(3)} />
                <Tab className='sidebar-comp ' label="Class Five" {...a11yProps(4)} />
                <Tab className='sidebar-comp ' label="Class Six" {...a11yProps(5)} />
                <Tab className='sidebar-comp ' label="Class Seven" {...a11yProps(6)} />
            </Tabs>
            <TabPanel value={value} index={0} children={Classroom}>
                Item One
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
