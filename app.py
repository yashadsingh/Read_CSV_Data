import streamlit as st
import pandas as pd

# Title
st.title("Prospect Leads Viewer")

# Load CSV from file path
file_path = "Leads_20251225.csv"  # CSV file in the same directory
df = pd.read_csv(file_path)

# Clean column names
df.columns = df.columns.str.strip()

st.subheader("Filter Options")

# Create columns for side-by-side filters
col1, col2, col3, col4 = st.columns(4)

with col1:
    prospect_name = st.text_input("ProspectName")
with col2:
    mobile_number = st.text_input("MobileNumber")
with col3:
    email = st.text_input("Email")
with col4:
    file_name = st.text_input("FileName")

# Apply filters
filtered_df = df.copy()

if prospect_name:
    filtered_df = filtered_df[filtered_df['ProspectName'].astype(str).str.contains(prospect_name, case=False, na=False)]
if mobile_number:
    filtered_df = filtered_df[filtered_df['MobileNumber'].astype(str).str.contains(mobile_number, case=False, na=False)]
if email:
    filtered_df = filtered_df[filtered_df['Email'].astype(str).str.contains(email, case=False, na=False)]
if file_name:
    filtered_df = filtered_df[filtered_df['FileName'].astype(str).str.contains(file_name, case=False, na=False)]

# Pagination settings
st.subheader("Pagination")
rows_per_page = st.number_input("Rows per page", min_value=1, value=5)
total_rows = len(filtered_df)
total_pages = (total_rows - 1) // rows_per_page + 1
page = st.number_input("Page number", min_value=1, max_value=max(total_pages, 1), value=1)

# Calculate start and end index
start_idx = (page - 1) * rows_per_page
end_idx = start_idx + rows_per_page

# Display the filtered and paginated data
st.write(f"Showing rows {start_idx + 1} to {min(end_idx, total_rows)} of {total_rows}")
st.dataframe(filtered_df.iloc[start_idx:end_idx])
