import streamlit as st
import snowflake.connector
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dynamic Snowflake Metadata Viewer", layout="wide")
st.title("🔐 Connect to Snowflake")

# User Input Form
with st.form("snowflake_login"):
    st.subheader("🔧 Enter Snowflake Connection Details")
    user = st.text_input("Username", value="", placeholder="e.g. ANKIT210203")
    password = st.text_input("Password", type="password")
    account = st.text_input("Account Identifier", placeholder="e.g. UG16456.central-india.azure")
    warehouse = st.text_input("Warehouse (optional)", value="COMPUTE_WH")
    submitted = st.form_submit_button("Connect and Fetch Metadata")

# If form is submitted, proceed
if submitted:
    try:
        # Step 1: Connect
        conn = snowflake.connector.connect(
            user=user,
            password=password,
            account=account,
            warehouse=warehouse,
            role="ACCOUNTADMIN"
        )
        st.success("✅ Connection successful!")

        cur = conn.cursor()

        # Step 2: Get all databases
        cur.execute("SHOW DATABASES")
        databases = [row[1] for row in cur.fetchall()]

        all_tables = []

        # Step 3: Query INFORMATION_SCHEMA.TABLES from all DBs
        with st.spinner("⏳ Fetching metadata from all databases..."):
            for db in databases:
                try:
                    query = f"SELECT TABLE_CATALOG, TABLE_SCHEMA, TABLE_NAME, TABLE_TYPE FROM {db}.INFORMATION_SCHEMA.TABLES"
                    df = pd.read_sql(query, conn)
                    df['SOURCE_DATABASE'] = db
                    all_tables.append(df)
                except Exception as e:
                    st.warning(f"⚠️ Failed to query {db}: {e}")

        # Step 4: Render
        if all_tables:
            result_df = pd.concat(all_tables, ignore_index=True)
            st.success(f"✅ Retrieved tables from {len(all_tables)} databases")

            st.subheader("📋 Tables Metadata")
            st.dataframe(result_df, use_container_width=True)

            st.subheader("📊 Tables per Database")
            chart_data = result_df.groupby("SOURCE_DATABASE")["TABLE_NAME"].count().reset_index()
            chart_data = chart_data.sort_values("TABLE_NAME", ascending=False)

            fig = px.bar(
                chart_data,
                x="SOURCE_DATABASE",
                y="TABLE_NAME",
                title="📊 Number of Tables per Database",
                labels={"SOURCE_DATABASE": "Database", "TABLE_NAME": "Tables"},
                color="SOURCE_DATABASE",
                template="plotly_white"
            )
            st.plotly_chart(fig, use_container_width=True)

        else:
            st.error("❌ No metadata retrieved.")

    except Exception as e:
        st.error(f"❌ Connection failed: {e}")
