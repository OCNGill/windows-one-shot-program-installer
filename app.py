import streamlit as st
import shutil
import pandas as pd
from winget_wrapper import search_package, install_package, get_package_details
from manager import PackageManager

# Initialize session state
if 'manager' not in st.session_state:
    st.session_state.manager = PackageManager()

if 'search_results' not in st.session_state:
    st.session_state.search_results = []

st.set_page_config(page_title="Windows One-Shot Installer", page_icon="🚀", layout="wide")

def get_disk_usage():
    total, used, free = shutil.disk_usage("/")
    return free // (2**30), total // (2**30) # GB

# Sidebar
with st.sidebar:
    st.title("📦 Selected Apps")
    
    # Disk Usage
    free_gb, total_gb = get_disk_usage()
    st.metric("Disk Free", f"{free_gb} GB", f"of {total_gb} GB")
    
    if free_gb < 10:
        st.warning("⚠️ Low Disk Space!")

    packages = st.session_state.manager.get_selected_packages()
    
    if not packages:
        st.info("No apps selected.")
    else:
        st.write(f"**Total Apps:** {len(packages)}")
        st.write(f"**Est. Size:** {st.session_state.manager.get_total_size_str()}")
        
        st.divider()
        
        for pkg in packages:
            with st.container():
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.write(f"**{pkg['Name']}**")
                    st.caption(f"ID: {pkg['Id']}")
                    st.caption(f"Size: {pkg.get('Size', 'Unknown')}")
                with col2:
                    if st.button("🗑️", key=f"rem_{pkg['Id']}"):
                        st.session_state.manager.remove_package(pkg['Id'])
                        st.rerun()
                st.divider()
        
        if st.button("🗑️ Clear All", type="secondary"):
            st.session_state.manager.clear_list()
            st.rerun()
            
        if st.button("🚀 INSTALL ALL", type="primary"):
            if not packages:
                st.error("Nothing to install!")
            else:
                st.session_state.installing = True

# Main Content
st.title("Windows One-Shot Installer 🚀")
st.markdown("### 1️⃣ Search  |  2️⃣ Add  |  3️⃣ Install")

# Search Section
with st.container():
    col1, col2 = st.columns([5, 1])
    with col1:
        query = st.text_input("Search for an app (e.g., 'chrome', 'spotify')", key="search_query")
    with col2:
        st.write("")
        st.write("")
        if st.button("🔍 Search", type="primary"):
            if query:
                with st.spinner(f"Searching for '{query}'..."):
                    results = search_package(query)
                    st.session_state.search_results = results
                    if not results:
                        st.warning("No results found.")
            else:
                st.warning("Enter a name.")

# Results Section
if st.session_state.search_results:
    st.subheader(f"Found {len(st.session_state.search_results)} results")
    
    # Create a dataframe for cleaner display? 
    # Or just iterate rows for custom "Add" button.
    # Streamlit dataframes don't support buttons inside rows easily yet without plugins.
    # So we use columns.
    
    # Header
    h1, h2, h3, h4 = st.columns([3, 2, 1, 1])
    h1.markdown("**Name**")
    h2.markdown("**ID**")
    h3.markdown("**Version**")
    h4.markdown("**Action**")
    st.divider()
    
    for item in st.session_state.search_results:
        c1, c2, c3, c4 = st.columns([3, 2, 1, 1])
        c1.write(item['Name'])
        c2.code(item['Id'])
        c3.write(item['Version'])
        
        # Check if already added
        is_added = any(p['Id'] == item['Id'] for p in st.session_state.manager.get_selected_packages())
        
        with c4:
            if is_added:
                st.success("Added")
            else:
                if st.button("➕ Add", key=f"add_{item['Id']}"):
                    # Fetch details (size) - might be slow so maybe skip or async?
                    # User asked for size. We try.
                    # with st.spinner("Getting info..."):
                    #     details = get_package_details(item['Id'])
                    #     item['Size'] = details.get('Size', 'Unknown')
                    
                    # For speed, let's just add it with Unknown size for now
                    # as winget show is slow.
                    item['Size'] = 'Unknown'
                    st.session_state.manager.add_package(item)
                    st.rerun()

# Installation Overlay
if st.session_state.get('installing', False):
    st.divider()
    st.subheader("🚀 Installation in Progress...")
    
    packages = st.session_state.manager.get_selected_packages()
    total = len(packages)
    progress_bar = st.progress(0)
    status_text = st.empty()
    log_area = st.empty()
    
    success_count = 0
    failed_count = 0
    logs = []
    
    for i, pkg in enumerate(packages):
        status_text.markdown(f"**Installing {pkg['Name']}...**")
        if install_package(pkg['Id']):
            logs.append(f"✅ Installed {pkg['Name']}")
            success_count += 1
        else:
            logs.append(f"❌ Failed {pkg['Name']}")
            failed_count += 1
        
        log_area.text("\n".join(logs))
        progress_bar.progress((i + 1) / total)
        
    status_text.success(f"Done! Success: {success_count}, Failed: {failed_count}")
    st.balloons()
    st.session_state.installing = False
    if st.button("Close Report"):
        st.rerun()
