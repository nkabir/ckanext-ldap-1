from setuptools import setup, find_packages

version = '0.1'

setup(
	name='ckanext-ldap',
	version=version,
	description="CKAN plugin to provide LDAP authentication",
    url='https://github.com/NaturalHistoryMuseum/ckanext-ldap',
	packages=find_packages(),
	namespace_packages=['ckanext', 'ckanext.ldap'],
	entry_points="""
        [ckan.plugins]
            ldap = ckanext.ldap.plugin:LdapPlugin
	""",
)
