from supabase import create_client
import streamlit as st

supabase = create_client(
    st.secrets["https://eiiwfizxtoelfhsmqxgs.supabase.co"],
    st.secrets["eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVpaXdmaXp4dG9lbGZoc21xeGdzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODUyMjI5NzUsImV4cCI6MjEwMDc5ODk3NX0.c3ylZyuOR1pIDLm7m3tI2ttzcB1rauyn4-pLwKV1vSU"]
)
