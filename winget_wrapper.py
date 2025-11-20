import subprocess
import logging
import re

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def _run_search_command(query):
    """
    Helper to run the actual winget command and parse output.
    """
    try:
        cmd = ["winget", "search", query, "--accept-source-agreements"]
        result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
        
        if result.returncode != 0 and result.returncode != 1:
            logging.error(f"Winget search failed: {result.stderr}")
            return []

        packages = []
        lines = result.stdout.splitlines()
        
        header_line = None
        header_indices = {}
        
        for i, line in enumerate(lines):
            if "Name" in line and "Id" in line and "Version" in line:
                header_line = line
                header_indices['Name'] = line.find("Name")
                header_indices['Id'] = line.find("Id")
                header_indices['Version'] = line.find("Version")
                header_indices['Source'] = line.find("Source")
                break
        
        if not header_line:
            return []

        start_processing = False
        for line in lines:
            if line == header_line:
                continue
            if line.startswith("---"):
                start_processing = True
                continue
            
            if start_processing and line.strip():
                parts = re.split(r'\s{2,}', line.strip())
                if len(parts) >= 2:
                    pkg = {
                        'Name': parts[0],
                        'Id': parts[1],
                        'Version': parts[2] if len(parts) > 2 else "Unknown",
                        'Source': parts[3] if len(parts) > 3 else "Unknown"
                    }
                    packages.append(pkg)
        return packages
    except Exception as e:
        logging.error(f"Error running search: {e}")
        return []

def search_package(query):
    """
    Searches for a package using winget and parses the output.
    Implements smart retry (e.g. removing spaces) if no results found.
    """
    # 1. Try exact query
    results = _run_search_command(query)
    
    # 2. If no results and query has spaces, try removing them (e.g. "7 zip" -> "7zip")
    if not results and " " in query:
        alt_query = query.replace(" ", "")
        logging.info(f"No results for '{query}', retrying with '{alt_query}'")
        results = _run_search_command(alt_query)
        
    return results

def get_package_details(package_id):
    """
    Attempts to get details for a package, specifically size.
    Returns a dict with 'Size' (string) or None.
    """
    try:
        cmd = ["winget", "show", "--id", package_id, "--accept-source-agreements"]
        result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
        
        details = {'Size': 'Unknown'}
        
        if result.returncode == 0:
            for line in result.stdout.splitlines():
                # Look for "Installer Url" or similar to hint at size, 
                # but winget show output varies.
                # Some manifests have "Installer: ... size: ..."
                # But mostly we might not get it.
                # Let's look for "Size: " line if it exists (rare).
                pass
                
            # Since winget doesn't reliably give size without downloading,
            # we will default to Unknown.
            # However, if we want to be fancy, we could try to HEAD the installer URL if found.
            # That's too slow for this tool.
            pass
            
        return details
    except Exception:
        return {'Size': 'Unknown'}

def install_package(package_id):
    """
    Installs a package by ID using winget.
    """
    try:
        logging.info(f"Installing {package_id}...")
        cmd = ["winget", "install", "--id", package_id, "--silent", "--accept-package-agreements", "--accept-source-agreements"]
        
        result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
        
        if result.returncode == 0:
            logging.info(f"Successfully installed {package_id}")
            return True
        else:
            logging.error(f"Failed to install {package_id}: {result.stderr} {result.stdout}")
            return False
            
    except Exception as e:
        logging.error(f"Exception installing {package_id}: {e}")
        return False
