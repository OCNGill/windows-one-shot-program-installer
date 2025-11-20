class PackageManager:
    def __init__(self):
        # Stores list of dicts: {'Id': ..., 'Name': ..., 'Size': ...}
        self.selected_packages = []

    def add_package(self, package_info):
        """
        Adds a package dict to the list if not already present.
        package_info must have 'Id'.
        """
        # Check if ID exists
        for pkg in self.selected_packages:
            if pkg['Id'] == package_info['Id']:
                return False
        
        self.selected_packages.append(package_info)
        return True

    def remove_package(self, package_id):
        """
        Removes a package by ID.
        """
        self.selected_packages = [pkg for pkg in self.selected_packages if pkg['Id'] != package_id]

    def get_selected_packages(self):
        """
        Returns the list of selected packages.
        """
        return self.selected_packages

    def clear_list(self):
        """
        Clears the list.
        """
        self.selected_packages = []

    def get_total_size_str(self):
        """
        Returns a string representation of total size.
        Since we mostly have 'Unknown', this is tricky.
        """
        # Placeholder logic if we ever get real sizes
        return "Unknown (Winget doesn't report sizes)"
