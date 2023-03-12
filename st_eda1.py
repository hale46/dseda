import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns

st.set_page_config(page_title="Exploratory Data Analysis", layout="wide")
st.title("EDA app")
st.header('This app allows you to explore your dataset and visualize the data using various plots.')

# Upload file
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Your Dataframe:")
    st.write(df.head())

    # Exploratory Data Analysis
    st.title("Exploratory Data Analysis")
    st.subheader("Data Summary")
    st.write(df.describe())

    # Sidebar for choosing plot
    plot_choice = st.sidebar.selectbox("Select plot type", ["Histogram", "Scatter Plot", "Line Plot", "Box Plot", "Violin Plot", "Heatmap"])

    # Histogram
    if plot_choice == "Histogram":
        st.header("Histogram")
        x_variable = st.selectbox("Select a variable for the x-axis", df.columns)
        y_variable = st.selectbox("Select a variable for the y-axis", df.columns)
        aggregation = st.selectbox("Select aggregation function", ["sum", "count", "min", "max", "avg", "std", "var"])
        try:
            fig = px.histogram(df, x=x_variable, y=y_variable, nbins=20, histfunc=aggregation)
            st.plotly_chart(fig)
        except:
            st.write("Unable to create histogram with the selected variables.")

    # Scatter plot
    elif plot_choice == "Scatter Plot":
        st.header("Scatter Plot")
        x_variable = st.selectbox("Select X variable", df.columns)
        y_variable = st.selectbox("Select Y variable", df.columns)
        try:
            fig = px.scatter(df, x=x_variable, y=y_variable)
            st.plotly_chart(fig)
        except:
            st.write("Unable to create scatter plot with the selected variables.")

    # Line plot
    elif plot_choice == "Line Plot":
        st.header("Line Plot")
        x_variable = st.selectbox("Select X variable", df.columns)
        y_variable = st.selectbox("Select Y variable", df.columns)
        try:
            fig = px.line(df, x=x_variable, y=y_variable)
            st.plotly_chart(fig)
        except:
            st.write("Unable to create line plot with the selected variables.")

    # Box plot
    elif plot_choice == "Box Plot":
        st.header("Box Plot")
        x_variable = st.selectbox("Select X variable", df.columns)
        y_variable = st.selectbox("Select Y variable", df.columns)
        try:
            fig = px.box(df, x=x_variable, y=y_variable)
            st.plotly_chart(fig)
        except:
            st.write("Unable to create box plot with the selected variables.")

    # Violin plot
    elif plot_choice == "Violin Plot":
        st.header("Violin Plot")
        x_variable = st.selectbox("Select X variable", df.columns)
        y_variable = st.selectbox("Select Y variable", df.columns)

        # If the user has selected a categorical variable, ask them to choose a class to visualize
        if df[y_variable].dtype == 'object':
            selected_class = st.selectbox('Select a class to visualize in violin plot', df[y_variable].unique())
            df_to_plot = df[df[y_variable] == selected_class]
        else:
            df_to_plot = df

        # Try to create and display the violin plot
        try:
            fig = px.violin(df_to_plot, x=x_variable, y=y_variable)
            st.plotly_chart(fig)
        except:
            st.write("Unable to create violin plot with the selected variables.")

    # Heatmap
    elif plot_choice == "Heatmap":
        st.header("Heatmap")
        try:
            corr = df.corr()
            fig = sns.heatmap(corr, annot=True)
            st.pyplot(fig.figure)
        except:
            st.write("Unable to create heatmap with the selected variables.")
   
