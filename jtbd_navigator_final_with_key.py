
import streamlit as st
import openai

# Initialize OpenAI API with the provided key
openai.api_key = "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"

# Title of the web app
st.title("JTBD Navigator")

# Global variables to store responses
responses = {}

# Function to get OpenAI response using the new ChatCompletion API
def get_openai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150,
        temperature=0.7,
    )
    return response.choices[0].message['content'].strip()

# Agent 1: Introduction and basic information
def agent_1():
    st.subheader("Agent 1: Company Background")
    responses['company_description'] = st.text_input("What does your company do?", "")
    responses['current_solution'] = st.text_input("What is the current solution?", "")
    if st.button("Next to Agent 2"):
        st.session_state.stage += 1

# Agent 2: Audience Identification
def agent_2():
    st.subheader("Agent 2: Identify Audience")
    responses['target_audience'] = st.text_input("Who is your main audience?", "")
    if not responses['target_audience']:
        prompt = f"Suggest a target audience for a company in the {responses.get('company_description', '')} sector."
        suggested_audience = get_openai_response(prompt)
        st.write(f"Suggested Audience: {suggested_audience}")
    if st.button("Next to Agent 3"):
        st.session_state.stage += 1

# Agent 3: Define the Core Job
def agent_3():
    st.subheader("Agent 3: Define the Core Job")
    responses['core_job'] = st.text_input(f"What is the main job your {responses.get('target_audience', '')} is trying to accomplish when using your product/service?")
    if not responses['core_job']:
        prompt = f"Suggest a core job for {responses.get('target_audience', '')} using {responses.get('company_description', '')} services."
        responses['core_job'] = get_openai_response(prompt)
        st.write(f"Suggested Core Job: {responses['core_job']}")
    if st.button("Next to Agent 4"):
        st.session_state.stage += 1

# Agent 4: Identify Desired Outcomes
def agent_4():
    st.subheader("Agent 4: Identify Desired Outcomes")
    responses['desired_outcomes'] = st.text_input(f"What are the key outcomes or benefits {responses.get('target_audience', '')} seeks when performing {responses.get('core_job', '')}?")
    if not responses['desired_outcomes']:
        prompt = f"Suggest desired outcomes for {responses.get('target_audience', '')} performing {responses.get('core_job', '')}."
        responses['desired_outcomes'] = get_openai_response(prompt)
        st.write(f"Suggested Outcomes: {responses['desired_outcomes']}")
    if st.button("Next to Agent 5"):
        st.session_state.stage += 1

# Repeat similar structure for each agent
# Agent 5: Understand the Context
def agent_5():
    st.subheader("Agent 5: Understand the Context")
    responses['context'] = st.text_input(f"In what situations or contexts do customers typically perform {responses.get('core_job', '')}?")
    if not responses['context']:
        prompt = f"Suggest a context in which {responses.get('target_audience', '')} performs {responses.get('core_job', '')}."
        responses['context'] = get_openai_response(prompt)
        st.write(f"Suggested Context: {responses['context']}")
    if st.button("Next to Agent 6"):
        st.session_state.stage += 1

# Agent 6: Pinpoint Pain Points
def agent_6():
    st.subheader("Agent 6: Pinpoint Pain Points")
    responses['pain_points'] = st.text_input(f"What are common challenges or frustrations customers encounter when trying to {responses.get('core_job', '')}?")
    if not responses['pain_points']:
        prompt = f"Suggest pain points for {responses.get('target_audience', '')} trying to {responses.get('core_job', '')}."
        responses['pain_points'] = get_openai_response(prompt)
        st.write(f"Suggested Pain Points: {responses['pain_points']}")
    if st.button("Next to Agent 7"):
        st.session_state.stage += 1

# Agent 7: Explore Current Solutions
def agent_7():
    st.subheader("Agent 7: Explore Current Solutions")
    responses['current_solutions'] = st.text_input(f"How do customers currently try to accomplish {responses.get('core_job', '')} without your product/service?")
    if not responses['current_solutions']:
        prompt = f"Suggest current solutions and their limitations for {responses.get('target_audience', '')} accomplishing {responses.get('core_job', '')}."
        responses['current_solutions'] = get_openai_response(prompt)
        st.write(f"Suggested Current Solutions: {responses['current_solutions']}")
    if st.button("Next to Agent 8"):
        st.session_state.stage += 1

# Agent 8: Envision the Ideal Solution
def agent_8():
    st.subheader("Agent 8: Envision the Ideal Solution")
    responses['ideal_solution'] = st.text_input(f"What features or attributes would make your product the ideal solution for {responses.get('core_job', '')}?")
    if not responses['ideal_solution']:
        prompt = f"Suggest ideal solution features for {responses.get('target_audience', '')} trying to {responses.get('core_job', '')}."
        responses['ideal_solution'] = get_openai_response(prompt)
        st.write(f"Suggested Ideal Solution: {responses['ideal_solution']}")
    if st.button("Next to Agent 9"):
        st.session_state.stage += 1

# Agent 9: Synthesize Information into a Product Statement
def agent_9():
    st.subheader("Agent 9: Craft a Product Statement")
    statement = f"""
    Core Job: {responses.get('core_job', '')}
    Desired Outcomes: {responses.get('desired_outcomes', '')}
    Context: {responses.get('context', '')}
    Pain Points: {responses.get('pain_points', '')}
    Current Solutions: {responses.get('current_solutions', '')}
    Ideal Solution: {responses.get('ideal_solution', '')}
    """
    st.write("Product Statement:", statement)
    if st.button("Finalize and Generate Compelling Statement"):
        st.session_state.stage += 1

# Final Agent: Create a Compelling Statement
def agent_10():
    st.subheader("Final Agent: Compelling Product Statement")
    final_statement = f"Introducing a solution that allows {responses.get('target_audience', '')} to {responses.get('core_job', '')}, achieving {responses.get('desired_outcomes', '')} while overcoming {responses.get('pain_points', '')}."
    st.write("Final Compelling Statement:", final_statement)
    st.write("Thank you for using the JTBD Navigator!")
    st.button("Restart")

# Main flow control
if "stage" not in st.session_state:
    st.session_state.stage = 1

# Map stages to agents
agents = [agent_1, agent_2, agent_3, agent_4, agent_5, agent_6, agent_7, agent_8, agent_9, agent_10]
agents[st.session_state.stage - 1]()
