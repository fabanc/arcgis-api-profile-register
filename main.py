# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# For more information about authentication schemes with the Python API for ArcGIS, see https://developers.arcgis.com/python/guide/working-with-different-authentication-schemes/


import sys
from arcgis.gis import GIS
from getpass import getpass


def check_if_profile_exists(profile):
    """
    Check if a user profile is already stored in the local Windows Profile Store
    :param profile: The name of the profile
    :return: Returns True if the profile exists, False otherwise.
    """
    gis = GIS(profile=profile)
    if gis.users.me is None:
        return False
    return True


def register_profile(portal_url, profile, user_name, password):
    gis = GIS(
        url=portal_url,
        username=user_name,
        password=password,
        profile=profile
    )
    if gis.users.me is None:
        raise Exception('Invalid Credentials')
    return gis.users.me


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Welcome to this utility to create a local profile')
    print('A local profile can be used to avoid storing your ArcGIS Online / Portal credentials in clear text')
    portal_url = input('Type the URL of your ArcGIS Online / Portal organization: ')
    print('Your ArcGIS Portal Organization is: {}'.format(portal_url))
    profile = input('Type the name of the profile that will be saved in your profile manager: ')
    print('The profile that will be saved in your Windows Profile Manager is: {}'.format(profile))

    # Check if the profile already exist. If yes, the user is given the option to alter it, or exit the program.
    profile_exists = check_if_profile_exists(profile)
    if profile_exists:
        confirm = None
        while confirm is None or confirm.lower() not in ['y', 'n']:
            confirm = input('The user profile already exists. Do you want to overwrite it? Type Y to continue and update the existing profile, N to exit')
        if confirm.lower() == 'n':
            sys.exit(0)

    # If the profile does not exist, or need to be updated, let's do so.
    portal_user_name = input('Type the ArcGIS Online / Portal user name that will be linked to this profile: ')
    portal_password = getpass(
        prompt='Type the password associated with user {}:'.format(portal_user_name)
    )

    print('Storing you user name and password in your Windows Credential Manager under the profile: {}'.format(profile))
    register_profile(
        portal_url=portal_url,
        profile=profile,
        user_name=portal_user_name,
        password=portal_password
    )

    input('The profile was successfully created or updated. Press any key to exit')





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
