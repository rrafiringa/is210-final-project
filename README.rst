####################
IS 210 Final Project 
####################
***********************
Site aware logon script
***********************

:College: CUNY School of Professional Studies
:Course-Name: Software Application Programming I
:Course-Code: IS 210

Overview
========
This project features a location based drive mapper Python script implemented in the drivemapper.py module.

The drivemapper.py module defines two classes:
    #. ConfigReader
    #. Mapper

The ConfigReader class:
-----------------------
The ConfigReader class takes an optional file path to a configuration JSON file. It loads the JSON file to internal data structures.

The Mapper class:
-----------------
The Mapper class is a wrapper for the ConfigReader class and also the object used to implement the actual shared drive mapping.

User story
==========
Name: John B. Sysadmin

Title: Senior Systems Engineer for a year in an expanding midsized business with a production datacenter in Manhattan, and a disaster recovery site in Edison. 

Goals: While performing his first yearly Disaster Recovery test for this year, John B. found that all 30 new employees did not have mappings to the services they enjoy at the production site, and were not able to run some applications, or save their work in their department's shared drive from their machines when working from the disaster recovery site. He also discovered that his predecessor mapped the network drives manually for each users, which was convenient when the company remained small, but presented a problem of time constraint as the company expanded and needed to scale ICT operations accordingly while keeping expenses on a budget. John B. has decided that he would use a programmatic approach to automate access control and consistent allocation of network shares, and across locations and by user function within a department.

Problem scenario
================

Problem: The company needs users to be able to logon from any site, and receive a consistent mapping to their shared drives.

Current Alternatives: Currently those resources have to be mapped manually and it can be tedious work as the company has hired more people.

Value Proposition: Create a logon script that will map the correct resources to the user's client computer automatically so long as the user is successfully authenticates into the internal network. 

Criteria
========
John B. needs to create a json file containing all the resource mappings required for the computers at each site.  A python program will read the json file and create the resources for the users automatically at logon time.

Acceptance Story
================
When a user goes to the production site and logs on, the logon script loads, picks up the the json configuration file for the site which resides in the script directory. Once the script is done running the user sees the appropriate shared drives mapped to the correct local file server. John B. Sysadmin can just sit back, relax, and pretend to be productive by watching viral YouTube cat videos all day in order to remain informed about the important paradigms of the day.

.. _GitHub: https://github.com/
.. _Python String Documentation: https://docs.python.org/2/library/stdtypes.html
