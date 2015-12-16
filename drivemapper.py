#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Production site logon script """

import json
import subprocess


class ConfigReader(object):
    """ Configuration reader class """

    def __init__(self, config='site1.json'):
        """
        Constructor

        Args:
            config (File): JSON encoded file with site and drive
                           mapping information.
        Attributes:
            site (String): Site location
            drivemaps (Dict): Dictionary of drive mappings

        Examples:
            >>> conf = ConfigReader('config.json')
            >>> conf.site
            Manhattan
            >>> conf.drivemaps
            {u'p': u'\\\\s1\\companydata', u'h': u'\\\\s1\\userfiles'}
        """

        self.site = ''
        self.drivemaps = {}
        self.load_config(config)

    def load_config(self, jsonfile):
        """
        Loads json config file
        Args:
            jsonfile (File): JSON encoded configuration file with
                             site and drive mapping information.

        Attributes:

        Examples:
            >>> conf = ConfigReader()
            >>> conf.load_config('config1.json')
        """

        try:
            with open(jsonfile, 'r') as myconf:
                mydata = json.load(myconf)
                self.site = mydata['site']
                self.drivemaps = mydata['maps']

        except IOError:
            print 'Could not load ' + jsonfile

        else:
            return True

        return False


class Mapper(object):
    """ Drive mapper class """

    def __init__(self, config_file):
        """
        Constructor

        Args:
            config_file (File): JSON configuration file

        Attributes:
            config (object): ConfigReader class instance

        Example:
            >>> drvmap = Mapper('site1.json')
        """

        self.config = ConfigReader(config_file)

    def get_site(self):
        """
        Return the site

        Args:

        Returns:
            string: Site name

        Examples:
            >>> mymapper = Mapper('site1.json')
            >>> mymapper.get_site()
        """

        return self.config.site

    def mapdrives(self):
        """
        Map the network shares

        Args:

        Returns:
            Boolean: True if process ran sucessfully False otherwise

        Examples:
            >>> mymapper = Mapper('site1.json')
            >>> mapper.mapdrives()
        """

        command = r'C:\Windows\System32\cmd.exe'
        code = False
        for drive, path in self.config.drivemaps.iteritems():
            args = '/c net use ' + drive + ': ' + path
            print 'Running ' + command + ' ' + args
            try:
                myproc = subprocess.Popen([command, args])
            except OSError:
                print 'Command failed: Path does not exist '
            else:
                code = (myproc.poll() == True)
        return code


if __name__ == '__main__':

    def write_config(outfile, data):
        """ Quick ass test function """
        with open(outfile, 'w') as site:
            site.write(json.dumps(data) + '\n')

    S1MAPS = dict(h=r'\\site1\userfiles',
                  p=r'\\site1\companydata')
    S1DATA = dict(site='Manhattan', maps=S1MAPS)

    S2MAPS = dict(h=r'\\site2\userfiles',
                  p=r'\\site2\companydata')
    S2DATA = dict(site='Edison', maps=S2MAPS)

    write_config('site1.json', S1DATA)
    write_config('site2.json', S2DATA)

    CONF1 = ConfigReader('site1.json')
    print CONF1.site
    print CONF1.drivemaps

    CONF2 = ConfigReader('site2.json')
    print CONF2.site
    print CONF2.drivemaps

    print '---------------------------'

    SHARES1 = Mapper('site1.json')
    SHARES2 = Mapper('site2.json')

    print SHARES1.get_site()
    print SHARES2.get_site()
    SHARES1.mapdrives()
    SHARES2.mapdrives()
