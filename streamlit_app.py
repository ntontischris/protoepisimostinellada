import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import torch
import nltk
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import random
from streamlit_option_menu import option_menu

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('vader_lexicon')

# Translations
translations = {
    "en": {
        "title": "AI in Hospitality: Guest Experience Optimization and Revenue Management",
        "guest_exp": "Guest Experience Personalization",
        "revenue_mgmt": "Revenue Management Optimization",
        "sentiment_analysis": "Sentiment Analysis of Guest Feedback",
        "staff_performance": "Staff Performance Optimization",
        "language": "Language",
        "guest_id": "Enter Guest ID:",
        "generate": "Generate Personalized Recommendations",
        "optimize": "Optimize Pricing Strategy",
        "analyze_feedback": "Analyze Feedback",
        "analyze_staff": "Analyze Staff Performance",
    },
    "el": {
        "title": "AI στη Φιλοξενία: Βελτιστοποίηση Εμπειρίας Επισκεπτών και Διαχείριση Εσόδων",
        "guest_exp": "Εξατομίκευση Εμπειρίας Επισκεπτών",
        "revenue_mgmt": "Βελτιστοποίηση Διαχείρισης Εσόδων",
        "sentiment_analysis": "Ανάλυση Συναισθημάτων από Σχόλια Επισκεπτών",
        "staff_performance": "Βελτιστοποίηση Απόδοσης Προσωπικού",
        "language": "Γλώσσα",
        "guest_id": "Εισάγετε ID Επισκέπτη:",
        "generate": "Δημιουργία Εξατομικευμένων Προτάσεων",
        "optimize": "Βελτιστοποίηση Στρατηγικής Τιμολόγησης",
        "analyze_feedback": "Ανάλυση Σχολίων",
        "analyze_staff": "Ανάλυση Απόδοσης Προσωπικού",
    },
    "zh": {
        "title": "酒店业AI：客户体验优化和收入管理",
        "guest_exp": "客户体验个性化",
        "revenue_mgmt": "收入管理优化",
        "sentiment_analysis": "客户反馈情感分析",
        "staff_performance": "员工绩效优化",
        "language": "语言",
        "guest_id": "输入客人ID：",
        "generate": "生成个性化推荐",
        "optimize": "优化定价策略",
        "analyze_feedback": "分析反馈",
        "analyze_staff": "分析员工表现",
    }
}

class HospitalityAI:
    def personalize_guest_experience(self, guest_id):
        # Simulate guest profile and preferences
        guest_profile = {
            "id": guest_id,
            "name": f"Guest {guest_id}",
            "age": random.randint(25, 65),
            "nationality": random.choice(["USA", "UK", "Germany", "Japan", "Australia"]),
            "previous_visits": random.randint(0, 5),
            "preferred_room_type": random.choice(["Standard", "Deluxe", "Suite"]),
            "dietary_restrictions": random.choice([None, "Vegetarian", "Vegan", "Gluten-free"]),
        }
        
        # Generate recommendations
        recommended_amenities = [
            {"name": "Spa Treatment", "reason": "Based on previous bookings", "interest_score": random.uniform(0.7, 1.0)},
            {"name": "Guided City Tour", "reason": "Popular with first-time visitors", "interest_score": random.uniform(0.6, 0.9)},
            {"name": "In-room Dining", "reason": "Matches preference for privacy", "interest_score": random.uniform(0.8, 1.0)},
        ]
        
        room_preferences = pd.DataFrame({
            "feature": ["View", "Size", "Quietness", "Tech Amenities"],
            "importance": [random.uniform(0.5, 1.0) for _ in range(4)]
        })
        
        dining_recommendations = pd.DataFrame({
            "Restaurant": ["The Gourmet Room", "Sushi Express", "Vegan Delights"],
            "Cuisine": ["French", "Japanese", "Vegan"],
            "Recommendation Score": [random.uniform(0.7, 1.0) for _ in range(3)]
        })
        
        activity_suggestions = [
            "Morning yoga session",
            "Wine tasting event",
            "Local art gallery visit",
            "Poolside relaxation"
        ]
        
        return {
            "guest_profile": guest_profile,
            "recommended_amenities": recommended_amenities,
            "room_preferences": room_preferences,
            "dining_recommendations": dining_recommendations,
            "activity_suggestions": activity_suggestions
        }

    def optimize_revenue_management(self):
        # Simulate pricing recommendations
        dates = pd.date_range(start="2024-01-01", end="2024-01-31")
        room_types = ["Standard", "Deluxe", "Suite"]
        pricing_recommendations = pd.DataFrame({
            "date": dates.repeat(3),
            "room_type": room_types * len(dates),
            "price": [random.uniform(100, 500) for _ in range(len(dates) * 3)]
        })
        
        # Simulate demand forecast
        demand_forecast = pd.DataFrame({
            "date": dates,
            "occupancy": [random.uniform(0.5, 1.0) for _ in range(len(dates))]
        })
        
        # Simulate competitive analysis
        competitive_analysis = go.Figure(data=[
            go.Bar(name='Our Hotel', x=room_types, y=[250, 350, 450]),
            go.Bar(name='Competitor A', x=room_types, y=[240, 340, 440]),
            go.Bar(name='Competitor B', x=room_types, y=[260, 360, 460])
        ])
        competitive_analysis.update_layout(barmode='group', title="Price Comparison with Competitors")
        
        # Simulate upselling opportunities
        upselling_opportunities = [
            {"item": "Room Upgrade", "target_segment": "Business Travelers", "potential_revenue": 5000},
            {"item": "Spa Package", "target_segment": "Couples", "potential_revenue": 3000},
            {"item": "Airport Transfer", "target_segment": "International Guests", "potential_revenue": 2000}
        ]
        
        return {
            "pricing_recommendations": pricing_recommendations,
            "demand_forecast": demand_forecast,
            "competitive_analysis": competitive_analysis,
            "upselling_opportunities": upselling_opportunities,
            "projected_revenue": random.uniform(500000, 1000000),
            "revenue_increase": random.uniform(5, 15)
        }

    def analyze_guest_feedback(self, feedback_data):
        # Simulate sentiment analysis results
        sentiment_distribution = pd.DataFrame({
            "sentiment": ["Positive", "Neutral", "Negative"],
            "count": [random.randint(50, 100), random.randint(20, 50), random.randint(10, 30)]
        })
        
        # Simulate key topics
        key_topics = pd.DataFrame({
            "category": ["Room", "Room", "Service", "Service", "Facilities", "Facilities"],
            "topic": ["Cleanliness", "Comfort", "Staff Friendliness", "Check-in Process", "Pool", "Gym"],
            "mentions": [random.randint(20, 50) for _ in range(6)]
        })
        
        # Simulate sentiment trend
        dates = pd.date_range(start="2024-01-01", end="2024-01-31")
        sentiment_trend = pd.DataFrame({
            "date": dates,
            "sentiment_score": [random.uniform(0.5, 1.0) for _ in range(len(dates))]
        })
        
        # Simulate positive aspects and areas for improvement
        positive_aspects = ["Friendly staff", "Clean rooms", "Great location"]
        improvement_areas = ["Slow check-in process", "Limited parking", "Outdated gym equipment"]
        
        # Simulate AI-generated recommendations
        recommendations = [
            {"category": "Service", "suggestion": "Implement express check-in for frequent guests", "expected_impact": "Reduce wait times by 30%"},
            {"category": "Facilities", "suggestion": "Upgrade gym equipment", "expected_impact": "Increase gym usage by 25%"},
            {"category": "Room", "suggestion": "Add smart room controls", "expected_impact": "Improve guest satisfaction scores by 15%"}
        ]
        
        return {
            "sentiment_distribution": sentiment_distribution,
            "key_topics": key_topics,
            "sentiment_trend": sentiment_trend,
            "positive_aspects": positive_aspects,
            "improvement_areas": improvement_areas,
            "recommendations": recommendations
        }

    def analyze_staff_performance(self):
        # Simulate overall staff efficiency
        overall_efficiency = random.uniform(7.0, 9.5)
        
        # Simulate department performance
        departments = ["Front Desk", "Housekeeping", "F&B", "Concierge", "Maintenance"]
        department_performance = pd.DataFrame({
            "department": departments,
            "efficiency_score": [random.uniform(6.0, 9.5) for _ in range(len(departments))]
        })
        
        # Simulate optimized staff scheduling
        staff_scheduling = go.Figure(data=[
            go.Bar(name='Current', x=departments, y=[10, 15, 20, 5, 8]),
            go.Bar(name='Optimized', x=departments, y=[8, 12, 18, 6, 7])
        ])
        staff_scheduling.update_layout(barmode='group', title="Staff Allocation: Current vs Optimized")
        
        # Simulate correlation between staff performance and guest satisfaction
        satisfaction_correlation = pd.DataFrame({
            "staff_performance": [random.uniform(6.0, 9.5) for _ in range(50)],
            "guest_satisfaction": [random.uniform(7.0, 9.8) for _ in range(50)]
        })
        
        # Simulate training recommendations
        training_recommendations = pd.DataFrame({
            "Employee": [f"Employee {i}" for i in range(1, 6)],
            "Department": random.choices(departments, k=5),
            "Recommended Training": ["Customer Service", "Time Management", "Conflict Resolution", "Upselling Techniques", "Technical Skills"],
            "Priority": ["High", "Medium", "High", "Low", "Medium"]
        })
        
        # Simulate productivity improvement suggestions
        improvement_suggestions = [
            "Implement a new task management system",
            "Conduct cross-training sessions between departments",
            "Introduce a staff recognition program",
            "Optimize room cleaning processes",
            "Enhance internal communication tools"
        ]
        
        return {
            "overall_efficiency": overall_efficiency,
            "department_performance": department_performance,
            "optimized_schedule": staff_scheduling,
            "satisfaction_correlation": satisfaction_correlation,
            "training_recommendations": training_recommendations,
            "improvement_suggestions": improvement_suggestions
        }

def main():
    st.set_page_config(layout="wide", page_title="AI in Hospitality")

    # Language selection
    lang = st.sidebar.selectbox(
        "Language / Γλώσσα / 语言",
        ("English", "Ελληνικά", "中文")
    )
    if lang == "English":
        lang_code = "en"
    elif lang == "Ελληνικά":
        lang_code = "el"
    else:
        lang_code = "zh"

    t = translations[lang_code]

    st.title(t["title"])
    st.markdown(
        """
        <style>
        .reportview-container {
            background: linear-gradient(to right, #FFFFFF, #F0F8FF)
        }
        .sidebar .sidebar-content {
            background: linear-gradient(to bottom, #FFFFFF, #F0F8FF)
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Initialize HospitalityAI
    hospitality_ai = HospitalityAI()

    # Sidebar navigation
    with st.sidebar:
        selected = option_menu(
            menu_title="Navigation",
            options=[t["guest_exp"], t["revenue_mgmt"], t["sentiment_analysis"], t["staff_performance"]],
            icons=["person-circle", "cash-coin", "chat-square-text", "people-fill"],
            menu_icon="list",
            default_index=0,
        )

    if selected == t["guest_exp"]:
        st.header(t["guest_exp"])
        st.info("This feature personalizes the guest experience based on their profile and preferences.")
        
        guest_id = st.text_input(t["guest_id"])
        
        if guest_id and st.button(t["generate"]):
            guest_recommendations = hospitality_ai.personalize_guest_experience(guest_id)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Guest Profile")
                st.json(guest_recommendations['guest_profile'])
                
                st.subheader("Recommended Amenities")
                for amenity in guest_recommendations['recommended_amenities']:
                    st.write(f"**{amenity['name']}**")
                    st.write(f"Reason: {amenity['reason']}")
                    st.write(f"Likelihood of Interest: {amenity['interest_score']:.2f}")
                    st.write("---")
            
            with col2:
                st.subheader("Room Preferences")
                fig = px.bar(guest_recommendations['room_preferences'], x='feature', y='importance',
                             title="Importance of Room Features")
                st.plotly_chart(fig, use_container_width=True)
                
                st.subheader("Personalized Dining Recommendations")
                st.dataframe(guest_recommendations['dining_recommendations'])
                
                st.subheader("Suggested Activities")
                for activity in guest_recommendations['activity_suggestions']:
                    st.write(f"- {activity}")

    elif selected == t["revenue_mgmt"]:
        st.header(t["revenue_mgmt"])
        st.info("This feature optimizes pricing strategies and identifies revenue opportunities.")
        
        if st.button(t["optimize"]):
            revenue_optimization = hospitality_ai.optimize_revenue_management()
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Dynamic Pricing Recommendations")
                fig = px.line(revenue_optimization['pricing_recommendations'], x='date', y='price',
                              color='room_type', title="Recommended Room Prices")
                st.plotly_chart(fig, use_container_width=True)
                
                st.subheader("Revenue Projections")
                col1, col2 = st.columns(2)
                col1.metric("Projected Monthly Revenue", f"${revenue_optimization['projected_revenue']:,.2f}")
                col2.metric("Revenue Increase", f"{revenue_optimization['revenue_increase']:.2f}%")
            
            with col2:
                st.subheader("Demand Forecast")
                fig = px.bar(revenue_optimization['demand_forecast'], x='date', y='occupancy',
                             title="Projected Occupancy Rates")
                st.plotly_chart(fig, use_container_width=True)
                
                st.subheader("Competitive Pricing Analysis")
                st.plotly_chart(revenue_optimization['competitive_analysis'], use_container_width=True)
            
            st.subheader("Upselling Opportunities")
            for opportunity in revenue_optimization['upselling_opportunities']:
                st.write(f"**{opportunity['item']}**")
                st.write(f"Target Segment: {opportunity['target_segment']}")
                st.write(f"Potential Revenue: ${opportunity['potential_revenue']:,.2f}")
                st.write("---")

    elif selected == t["sentiment_analysis"]:
        st.header(t["sentiment_analysis"])
        st.info("This feature analyzes guest feedback to identify trends and areas for improvement.")
        
        uploaded_file = st.file_uploader("Upload guest feedback data (CSV)", type="csv")
        
        if uploaded_file is not None and st.button(t["analyze_feedback"]):
            feedback_analysis = hospitality_ai.analyze_guest_feedback(uploaded_file)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Overall Sentiment Distribution")
                fig = px.pie(feedback_analysis['sentiment_distribution'], values='count', names='sentiment',
                             title="Distribution of Guest Sentiment")
                st.plotly_chart(fig, use_container_width=True)
                
                st.subheader("Key Topics in Guest Feedback")
                fig = px.treemap(feedback_analysis['key_topics'], path=['category', 'topic'], values='mentions',
                                 title="Hierarchical View of Feedback Topics")
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                st.subheader("Sentiment Trend Over Time")
                fig = px.line(feedback_analysis['sentiment_trend'], x='date', y='sentiment_score',
                              title="Guest Sentiment Trend")
                st.plotly_chart(fig, use_container_width=True)
                
                st.subheader("Most Appreciated Aspects")
                for aspect in feedback_analysis['positive_aspects']:
                    st.write(f"- {aspect}")
                
                st.subheader("Areas for Improvement")
                for area in feedback_analysis['improvement_areas']:
                    st.write(f"- {area}")
            
            st.subheader("AI-Generated Recommendations")
            for rec in feedback_analysis['recommendations']:
                st.write(f"**{rec['category']}**")
                st.write(f"Suggestion: {rec['suggestion']}")
                st.write(f"Expected Impact: {rec['expected_impact']}")
                st.write("---")

    elif selected == t["staff_performance"]:
        st.header(t["staff_performance"])
        st.info("This feature analyzes staff performance and provides optimization suggestions.")
        
        if st.button(t["analyze_staff"]):
            staff_analysis = hospitality_ai.analyze_staff_performance()
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Overall Staff Efficiency")
                st.metric("Efficiency Score", f"{staff_analysis['overall_efficiency']:.2f}/10")
                
                st.subheader("Department Performance Comparison")
                fig = px.bar(staff_analysis['department_performance'], x='department', y='efficiency_score',
                             title="Efficiency Scores by Department")
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                st.subheader("Optimized Staff Scheduling")
                st.plotly_chart(staff_analysis['optimized_schedule'], use_container_width=True)
                
                st.subheader("Correlation: Staff Performance vs Guest Satisfaction")
                fig = px.scatter(staff_analysis['satisfaction_correlation'], x='staff_performance', y='guest_satisfaction',
                                 title="Staff Performance vs Guest Satisfaction")
                st.plotly_chart(fig, use_container_width=True)
            
            st.subheader("Personalized Training Recommendations")
            st.dataframe(staff_analysis['training_recommendations'])
            
            st.subheader("Productivity Improvement Suggestions")
            for suggestion in staff_analysis['improvement_suggestions']:
                st.write(f"- {suggestion}")

if __name__ == "__main__":
    main()
