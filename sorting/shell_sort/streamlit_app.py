import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set page config
st.set_page_config(
    page_title="Shell Sort Analysis", layout="wide", initial_sidebar_state="collapsed"
)

# Title and description
st.title("Shell Sort Performance Analysis")
st.markdown("Comparison of Shell Sort performance across different input arrangements")


# Function to format large numbers
def format_size(size):
    if size >= 1000:
        return f"{size // 1000}K"
    return str(size)


# Load the data
@st.cache_data
def load_data(file_name):
    data = pd.read_csv(file_name, header=None)
    data.columns = [10, 100, 1000, 10000, 20000, 100000]
    return data


# Load all datasets
ascending_data = load_data("asceding.csv")
descending_data = load_data("descending.csv")
random_data = load_data("random.csv")

st.header("Performance Overview")


# Calculate statistics for each dataset
def calculate_stats(data, name):
    stats = pd.DataFrame(
        {
            "Mean": data.mean(),
            "Std Dev": data.std(),
            "Min": data.min(),
            "Max": data.max(),
        }
    )
    stats["Dataset"] = name
    return stats


asc_stats = calculate_stats(ascending_data, "Ascending")
desc_stats = calculate_stats(descending_data, "Descending")
rand_stats = calculate_stats(random_data, "Random")

# Combine stats
combined_stats = pd.concat([asc_stats, desc_stats, rand_stats])

# Create comparison plot
fig = go.Figure()

for dataset, color in [
    ("Ascending", "blue"),
    ("Descending", "red"),
    ("Random", "green"),
]:
    stats = combined_stats[combined_stats["Dataset"] == dataset]
    fig.add_trace(
        go.Scatter(
            x=stats.index,
            y=stats["Mean"],
            error_y=dict(type="data", array=stats["Std Dev"]),
            name=dataset,
            line=dict(color=color),
        )
    )

fig.update_layout(
    title="Mean Execution Time Comparison",
    xaxis_title="Input Size (n)",
    yaxis_title="Time (seconds)",
    showlegend=True,
)
fig.update_xaxes(
    ticktext=[format_size(size) for size in [10, 100, 1000, 10000, 20000, 100000]],
    tickvals=[10, 100, 1000, 10000, 20000, 100000],
)

st.plotly_chart(fig, use_container_width=True)

# Summary metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Ascending Max Time", f"{asc_stats['Max'].max():.6f}s")
with col2:
    st.metric("Descending Max Time", f"{desc_stats['Max'].max():.6f}s")
with col3:
    st.metric("Random Max Time", f"{rand_stats['Max'].max():.6f}s")


# Statistics Tables
st.header("Detailed Statistics")

col1, col2, col3 = st.columns(3)

# with col1:
st.subheader("Ascending Order Statistics")
stats_asc = pd.DataFrame(
    {
        "Mean": ascending_data.mean(),
        "Std Dev": ascending_data.std(),
        "Min": ascending_data.min(),
        "Max": ascending_data.max(),
    }
)
st.dataframe(stats_asc.style.format("{:.6f}"), use_container_width=True)

# with col2:
st.subheader("Descending Order Statistics")
stats_desc = pd.DataFrame(
    {
        "Mean": descending_data.mean(),
        "Std Dev": descending_data.std(),
        "Min": descending_data.min(),
        "Max": descending_data.max(),
    }
)
st.dataframe(stats_desc.style.format("{:.6f}"), use_container_width=True)

# with col3:
st.subheader("Random Order Statistics")
stats_rand = pd.DataFrame(
    {
        "Mean": random_data.mean(),
        "Std Dev": random_data.std(),
        "Min": random_data.min(),
        "Max": random_data.max(),
    }
)
st.dataframe(stats_rand.style.format("{:.6f}"), use_container_width=True)

# Raw Data
st.header("Raw Data")

col1, col2, col3 = st.columns(3)

# with col1:
st.subheader("Ascending Order Data")
st.dataframe(ascending_data.style.format("{:.6f}"), use_container_width=True)

# with col2:
st.subheader("Descending Order Data")
st.dataframe(descending_data.style.format("{:.6f}"), use_container_width=True)

# with col3:
st.subheader("Random Order Data")
st.dataframe(random_data.style.format("{:.6f}"), use_container_width=True)

# Footer with dataset information
st.markdown(
    """
---

# Brodie Rogers 
# Shell Sort Preformance Analysis
---

## Implementation Overview
This implementation uses the Shell Sort algorithm, an optimization of insertion sort. 
The algorithm works by comparing elements that are seperated by a gap (initially large, then it decreases with each iteration), 
rather than comparing only elements directly next to each other as in insertion sort. 
This sort reduces the number of total swaps needed by allowing elements to move multiple positions at once

--- 

## Data
The data was collected using Python, we timed the Shell Sort algorithm on 6 different array sizes.
This was then taken a level farther by testing it on Data in Random, Ascending, and Descending Orders.
I used pandas, plotly, and streamlit for the data analysis and visualization.


---

### Data Collection

- 99 Iterations on 6 different arr sizes and permutations
- Array sizes analyzed: 10, 100, 1,000, 10,000, 20,000, and 100,000 
- Array permutations analyzed: Ascending, Random, Descending

I write the time it takes the algorithm to complete a sort for each array size to a csv then repeat 98 more times.

---

### Data Processing

- Read Data from csv into a Pandas Data Frame
- Use Pythons built in math Functions to preforme different Calultions such as Mean, Standard Deviation, etc. 

---

### Data Visualization 

- Plotly Has a very intuative suite of tools to create different ways to visualize data.
- I created a line chart to show the results of every permutation and arr size side by side.
With the Standard Deviation being shown by the bars on the graph.
- I show the max sorting times for the different Permutations.
- Following the max sorting times we can see some other important statistcs for each size and permutation.
These tables show The mean, std, min, and max times to sort the different arrays.
- I end it of with tables displaying the raw data from the csv

---

### Time Complexity 

- For small Arrays (n=10, 100)
    - Extremely Fast execution (~0.0004s)    
    - Consistent preformance accross all permutations

- For medium Arrays (n=1,000, 10,000)
    - Moderate execution times (~0.006s to ~0.013s)

- For large Arrays (n=20,000, 100,000)
    - Reasonable execution times (~0.08s)
    - We can see a significant advantage over insertion sorts (~3.75s)

This shows us Shell Sorts O(n^2) in its worst case (descending) 
and how it can be as good as O(n log n) in its best case (ascending). 
Shell sort is better than insertion sort with the fact that we aredoing less comparisons due to the gap idea. 

---

### Varience in Preformance

Like insertion sort we see the Standard Deviation increase as the arr size increases.
Other than that the algorithm is very predictable. With its worst preformance comming from the Random Permutations, 
however the std for an arr with 100K elements only being 0.014818 seconds 

---

### Conclusion  

Shell sort is very efficient on all sizes and permutations of data I collected on with the longest sort taking only .1845 seconds.
After completing what I have, I would like to test on larger sizes of arrays to see how this algorithm scales on arrays with 1m elements. 
100k elements is alot but for todays world of data 100k elements is nearly insignificant. 
In the end im think shell sort would best be used to sort after something like quick sort breaks an array of 1m+ elements down into smaller arrays, 
where Shell Sort shines.

---


"""
)
