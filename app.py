import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="A360 Internal Project Hub",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_email' not in st.session_state:
    st.session_state.user_email = None

def show_auth():
    st.title("🏢 A360 Internal Project Hub")
    st.markdown("### Welcome to your internal project management system")
    
    st.info("🎆 **DEMO MODE** - Enter any email and password to explore the system!")
    
    tab1, tab2 = st.tabs(["Login", "Quick Demo"])
    
    with tab1:
        st.subheader("Login to your account")
        email = st.text_input("Email", placeholder="Enter any email", key="login_email")
        password = st.text_input("Password", type="password", placeholder="Enter any password", key="login_password")
        
        if st.button("Login", type="primary", key="login_btn"):
            if email and password:
                st.session_state.logged_in = True
                st.session_state.user_email = email
                st.success("Login successful!")
                st.rerun()
            else:
                st.warning("Please enter email and password")
    
    with tab2:
        st.subheader("Quick Demo Access")
        st.markdown("Explore the A360 Project Hub with all three main projects:")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("🎯 **Project 1**\nTranscript Generator")
        with col2:
            st.markdown("🧪 **Project 2**\nPrompt Testing Tool")
        with col3:
            st.markdown("🔍 **Project 3**\nTranscript Analysis")
        
        if st.button("Enter Demo Mode", type="primary", key="demo_btn"):
            st.session_state.logged_in = True
            st.session_state.user_email = "demo@a360.com"
            st.success("🎆 Welcome to A360 Project Hub Demo!")
            st.rerun()

def show_main_app():
    # Sidebar with user info and navigation
    with st.sidebar:
        st.markdown(f"### Welcome, {st.session_state.user_email}!")
        
        if st.button("Logout", key="logout_btn"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
        
        st.divider()
        
        # Navigation
        page = st.selectbox(
            "Navigate to:",
            ["Dashboard", "Projects", "System Info"],
            key="navigation"
        )
    
    # Main content based on selected page
    if page == "Dashboard":
        show_dashboard()
    elif page == "Projects":
        show_projects()
    elif page == "System Info":
        show_system_info()

def show_dashboard():
    st.title("📊 A360 Project Hub Dashboard")
    
    st.success("🎆 Welcome to the A360 Internal Project Hub! This is a fully functional demo.")
    
    # Display metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Available Projects", "3", "Ready")
    with col2:
        st.metric("Demo Features", "All", "Active")
    with col3:
        st.metric("System Status", "100%", "Online")
    with col4:
        st.metric("Demo Mode", "On", "✅")

def show_projects():
    st.title("📁 A360 Project Hub - Three Main Projects")
    
    st.markdown("### Interactive demonstrations of all three projects:")
    
    tab1, tab2, tab3 = st.tabs(["🎯 Transcript Generator", "🧪 Prompt Tester", "🔍 Analysis Dashboard"])
    
    with tab1:
        st.markdown("**Purpose**: Generate realistic consultation transcripts")
        
        col1, col2 = st.columns(2)
        with col1:
            specialty = st.selectbox("Specialty", ["Medspa", "Explant", "Venous"], key="gen_specialty")
            visit_type = st.selectbox("Visit Type", ["Initial", "Follow-up", "Treatment"], key="gen_visit")
        with col2:
            complexity = st.slider("Complexity Level", 1, 5, 3, key="gen_complexity")
            patient_name = st.text_input("Patient Name", "Demo Patient", key="gen_patient")
        
        if st.button("Generate Demo Transcript", type="primary", key="gen_demo"):
            demo_transcript = f'''DEMO CONSULTATION TRANSCRIPT
Patient: {patient_name}
Specialty: {specialty}
Visit Type: {visit_type}
Date: {datetime.now().strftime('%Y-%m-%d')}
Complexity: {complexity}/5

Dr. Smith: Good morning, {patient_name}. How are you feeling today?
Patient: Good morning, Doctor. I'm here for my {visit_type.lower()} regarding {specialty} treatment.
Dr. Smith: Excellent. Let's discuss your treatment plan...

[Demo transcript content - Full system would generate detailed consultation]'''
            
            st.success("✅ Demo transcript generated!")
            st.text_area("Generated Content", demo_transcript, height=200, key="gen_output")
    
    with tab2:
        st.markdown("**Purpose**: Test AI prompts against transcript data")
        
        prompt = st.text_area("Enter your test prompt", "Analyze the key themes in this consultation", height=100)
        
        col1, col2 = st.columns(2)
        with col1:
            transcript_type = st.selectbox("Demo Transcript", ["Medspa Consultation", "Explant Follow-up", "Venous Treatment"])
        with col2:
            model = st.selectbox("AI Model", ["Demo-GPT-4", "Demo-Claude", "Demo-Gemini"])
        
        if st.button("Run Demo Test", type="primary", key="test_demo"):
            result = f'''PROMPT TEST RESULTS
Prompt: "{prompt[:100]}..."
Transcript: {transcript_type}
Model: {model}
Execution Time: 2.1 seconds

ANALYSIS OUTPUT:
Based on the {transcript_type}, key findings include:
• Clear patient-provider communication
• Thorough discussion of treatment options
• Appropriate follow-up instructions
• No significant risk factors identified

PERFORMANCE METRICS:
• Processing Time: 2.1s
• Confidence Score: 94%
• Analysis Depth: High'''
            
            st.success("✅ Demo test completed!")
            st.text_area("Test Results", result, height=200, key="test_output")
    
    with tab3:
        st.markdown("**Purpose**: Analyze multiple transcripts with bulk queries")
        
        query = st.selectbox("Analysis Query", [
            "Find mentions of side effects",
            "Analyze patient satisfaction",
            "Extract cost discussions",
            "Identify common concerns"
        ])
        
        selected_files = st.multiselect("Select Demo Transcripts", [
            "Medspa_001.txt (Botox consultation)",
            "Explant_002.txt (Recovery progress)",
            "Venous_003.txt (Treatment planning)"
        ], default=["Medspa_001.txt (Botox consultation)", "Explant_002.txt (Recovery progress)"])
        
        if st.button("Run Demo Analysis", type="primary", key="analysis_demo") and selected_files:
            analysis = f'''BULK ANALYSIS RESULTS
Query: "{query}"
Files Analyzed: {len(selected_files)}
Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

SUMMARY FINDINGS:
• Found {len(selected_files) * 3} relevant mentions
• High confidence analysis (91% avg)
• Processing completed in 3.2 seconds

INDIVIDUAL RESULTS:
''' + '\n'.join([f'• {file}: 3 matches found, high confidence' for file in selected_files])
            
            st.success("✅ Demo analysis completed!")
            st.text_area("Analysis Results", analysis, height=200, key="analysis_output")

def show_system_info():
    st.title("ℹ️ System Information")
    
    st.success("🎆 You are using the A360 Internal Project Hub demo!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("System Status")
        st.success("✅ User Interface - Operational")
        st.success("✅ Authentication - Working")
        st.success("✅ All Demos - Active")
        st.info("🔧 Database - Ready for Setup")
    
    with col2:
        st.subheader("Current Session")
        st.markdown(f"**User:** {st.session_state.user_email}")
        st.markdown(f"**Login Time:** {datetime.now().strftime('%H:%M:%S')}")
        st.markdown(f"**Status:** Demo Mode Active")

# Main application logic
if not st.session_state.logged_in:
    show_auth()
else:
    show_main_app()
