import os
from os.path import join, abspath, expanduser, splitext
import posixpath
import earthaccess

from modland import generate_modland_grid

from .VIIRS_swath_granule import VIIRSSwathGranule
from .granule_ID import *

def anonymize_home_path(file_path: str) -> str:
    home_dir = os.path.expanduser("~")
    
    if file_path.startswith(home_dir):
        return file_path.replace(home_dir, "~", 1)
    
    return file_path

def retrieve_granule(
        remote_granule: earthaccess.results.DataGranule, 
        download_directory: str = ".",
        parent_directory: str = None) -> VIIRSSwathGranule:
    """
    Retrieve and download a VIIRS granule from a remote source.

    Args:
        remote_granule (earthaccess.results.DataGranule): The remote granule to be downloaded.
        download_directory (str): The directory where the granule will be downloaded.

    Returns:
        VIIRSSwathGranule: The downloaded and processed VIIRS tiled granule.
    """
    # determine the URL of the remote granule
    URL = None

    for related_URL_dict in remote_granule["umm"]["RelatedUrls"]:
        if related_URL_dict["Type"] == "GET DATA":
            URL = related_URL_dict["URL"]
    
    if URL is None:
        raise ValueError("No GET DATA URL found in the remote granule metadata.")

    # Extract the granule ID from the URL
    granule_ID = splitext(posixpath.basename(URL))[0]

    # Extract the granule ID from the remote granule metadata
    # import json
    # print(json.dumps(remote_granule["meta"], indent=4))
    # granule_ID = remote_granule["meta"]["native-id"]
    
    # Parse the product name, build number, and date from the granule ID
    product_name = parse_VIIRS_product(granule_ID)
    build_number = parse_VIIRS_build(granule_ID)
    date_UTC = parse_VIIRS_date(granule_ID)
    
    if parent_directory is None:
        # Construct the parent directory path for the download
        parent_directory = join(
            download_directory, 
            f"{product_name}.{build_number:03d}", 
            date_UTC.strftime("%Y-%m-%d")
        )
    
    # Download the granule to the specified directory and get the filename
    filename = earthaccess.download(remote_granule, local_path=abspath(expanduser(parent_directory)))[0]
    
    # Anonymize the home path in the filename
    filename = anonymize_home_path(filename)
    
    # Create a VIIRSSwathGranule object from the downloaded file
    granule = VIIRSSwathGranule(filename)
    
    return granule
