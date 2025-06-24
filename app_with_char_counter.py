
import streamlit as st

st.set_page_config(page_title="Green Grant Generator", layout="centered")

st.title("🌱 AI-Powered Green Grant Generator")
st.markdown("Generate tailored sustainability grant proposals with minimal input.")

def char_count_feedback(text, min_len, max_len, label):
    length = len(text)
    if length < min_len:
        color = "orange"
        message = f"⚠️ {length}/{max_len} characters — {label} is a bit short. Try to add more detail."
    elif length > max_len:
        color = "red"
        message = f"🚫 {length}/{max_len} characters — {label} is too long. Please shorten it."
    else:
        color = "green"
        message = f"✅ {length}/{max_len} characters — Looks good!"
    st.markdown(f"<span style='color:{color}'>{message}</span>", unsafe_allow_html=True)

# Form Inputs
with st.form("grant_form"):
    org_name = st.text_input("Organization Name")
    mission = st.text_area("Mission Statement (optional)", max_chars=300)
    char_count_feedback(mission, 50, 300, "Mission Statement")

    project_title = st.text_input("Project Title (optional)")

    project_summary = st.text_area("Project Summary", max_chars=500)
    char_count_feedback(project_summary, 100, 500, "Project Summary")

    goal = st.text_area("Main Goal or Outcome", max_chars=300)
    char_count_feedback(goal, 75, 300, "Main Goal or Outcome")

    budget = st.text_input("Estimated Budget (optional)")
    location = st.text_input("Target Community / Location (optional)")
    funding_needs = st.multiselect(
        "Funding Needs",
        ["Equipment", "Staffing", "Outreach", "Permits", "Other"]
    )
    timeline = st.text_input("Timeline (optional)")

    kpis = st.text_area("Key Performance Indicators (optional)", max_chars=300)
    char_count_feedback(kpis, 50, 300, "KPIs")

    stakeholders = st.text_area("Stakeholders / Partners (optional)")
    contact = st.text_input("Contact Information (optional)")

    submitted = st.form_submit_button("Generate Proposal")

# Prompt Engine
def build_prompt(data):
    return f"""
You are an experienced grant writer specializing in sustainability and environmental initiatives.

Write a professional, persuasive grant proposal based on the input below. If any detail is missing or marked as N/A, use your expertise to fill in reasonable assumptions or exclude that section naturally.

Inputs:
- Organization: {data['org_name'] or 'a community nonprofit'}
- Mission Statement: {data['mission'] or 'To support sustainability through local action.'}
- Project Title: {data['project_title'] or 'Sustainability Initiative'}
- Project Summary: {data['project_summary']}
- Main Goal: {data['goal']}
- Estimated Budget: {data['budget'] or 'Estimate a reasonable cost.'}
- Target Community/Location: {data['location'] or 'a local community'}
- Funding Needs: {", ".join(data['funding_needs']) if data['funding_needs'] else 'General project expenses'}
- Timeline: {data['timeline'] or '6–12 months'}
- KPIs: {data['kpis'] or 'Example metrics such as families served, CO2 reduction, volunteer hours'}
- Stakeholders/Partners: {data['stakeholders'] or 'Local volunteers and community organizations'}
- Contact Info: {data['contact'] or '[contact@email.com]'}

Generate a clear, formal proposal with sections for Introduction, Project Overview, Timeline, Impact, Funding Request, KPIs, and Conclusion.
"""

if submitted:
    input_data = {
        "org_name": org_name,
        "mission": mission,
        "project_title": project_title,
        "project_summary": project_summary,
        "goal": goal,
        "budget": budget,
        "location": location,
        "funding_needs": funding_needs,
        "timeline": timeline,
        "kpis": kpis,
        "stakeholders": stakeholders,
        "contact": contact
    }

    prompt = build_prompt(input_data)
    st.subheader("📝 Generated Grant Proposal Prompt")
    st.code(prompt, language="markdown")
    st.markdown("_(This output simulates the prompt used to generate a grant proposal with an AI model. GPT integration coming soon!)_")
