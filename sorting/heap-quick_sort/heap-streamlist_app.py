import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set page config
st.set_page_config(
    page_title="Sorting Algorithms Analysis", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# Title and description
st.title("Sorting Algorithms Performance Analysis")
st.markdown("Comparison of Heap Sort and Quick Sort variants performance across different input arrangements")

# Function to format large numbers
def format_size(size):
    if size >= 1000:
        return f"{size // 1000}K"
    return str(size)

# Load the data
@st.cache_data
def load_data(file_name):
    try:
        data = pd.read_csv(file_name, header=None)
        data.columns = [10, 100, 1000, 10000, 20000, 100000, 1000000]
        return data
    except Exception as e:
        st.warning(f"Could not load {file_name}: {e}")
        # Return empty DataFrame with expected structure
        return pd.DataFrame(columns=[10, 100, 1000, 10000, 20000, 100000, 1000000])

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

#--------------------------------------------------------
# HEAP SORT SECTION
#--------------------------------------------------------
st.header("Heap Sort Performance")

# Load heap sort datasets
heap_ascending_data = load_data("heap-asceding.csv")
heap_descending_data = load_data("heap-descending.csv")
heap_random_data = load_data("heap-random.csv")

# Calculate heap sort statistics
heap_asc_stats = calculate_stats(heap_ascending_data, "Heap-Ascending")
heap_desc_stats = calculate_stats(heap_descending_data, "Heap-Descending")
heap_rand_stats = calculate_stats(heap_random_data, "Heap-Random")

# Combine heap sort stats
heap_combined_stats = pd.concat([heap_asc_stats, heap_desc_stats, heap_rand_stats])

# Create heap sort graph
try:
    heap_fig = go.Figure()
    
    heap_algorithms = [
        ("Heap-Ascending", "blue"),
        ("Heap-Descending", "red"),
        ("Heap-Random", "green"),
    ]
    
    for dataset, color in heap_algorithms:
        stats = heap_combined_stats[heap_combined_stats["Dataset"] == dataset]
        heap_fig.add_trace(
            go.Scatter(
                x=stats.index,
                y=stats["Mean"],
                error_y=dict(type="data", array=stats["Std Dev"]),
                name=dataset,
                line=dict(color=color),
            )
        )
    
    heap_fig.update_layout(
        title="Heap Sort Mean Execution Time",
        xaxis_title="Input Size (n)",
        yaxis_title="Time (seconds)",
        showlegend=True,
        height=600,
    )
    heap_fig.update_xaxes(
        ticktext=[format_size(size) for size in [10, 100, 1000, 10000, 20000, 100000]],
        tickvals=[10, 100, 1000, 10000, 20000, 100000],
    )
    
    st.plotly_chart(heap_fig, use_container_width=True)
except Exception as e:
    st.warning(f"Could not create Heap Sort graph: {e}")

# Summary metrics
st.subheader("Heap Sort Maximum Times")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Ascending Max Time", f"{heap_asc_stats['Max'].max():.6f}s")
with col2:
    st.metric("Descending Max Time", f"{heap_desc_stats['Max'].max():.6f}s")
with col3:
    st.metric("Random Max Time", f"{heap_rand_stats['Max'].max():.6f}s")

# Heap Sort statistics tables
st.subheader("Heap Sort - Detailed Statistics")

# Ascending
st.write("Heap Sort - Ascending Order Statistics")
st.dataframe(heap_asc_stats[["Mean", "Std Dev", "Min", "Max"]].style.format("{:.6f}"), use_container_width=True)

# Descending
st.write("Heap Sort - Descending Order Statistics")
st.dataframe(heap_desc_stats[["Mean", "Std Dev", "Min", "Max"]].style.format("{:.6f}"), use_container_width=True)

# Random
st.write("Heap Sort - Random Order Statistics")
st.dataframe(heap_rand_stats[["Mean", "Std Dev", "Min", "Max"]].style.format("{:.6f}"), use_container_width=True)

# Heap Sort raw data
st.subheader("Heap Sort - Raw Data")

st.write("Heap Sort - Ascending Order Data")
st.dataframe(heap_ascending_data.style.format("{:.6f}"), use_container_width=True)

st.write("Heap Sort - Descending Order Data")
st.dataframe(heap_descending_data.style.format("{:.6f}"), use_container_width=True)

st.write("Heap Sort - Random Order Data")
st.dataframe(heap_random_data.style.format("{:.6f}"), use_container_width=True)

#--------------------------------------------------------
# itterATIVE QUICK SORT SECTION
#--------------------------------------------------------
st.header("itterative Quick Sort Performance")

# Load itterative quick sort datasets
itter_quick_asc_data = load_data("itter-quick-asceding.csv")
itter_quick_desc_data = load_data("itter-quick-descending.csv")
itter_quick_random_data = load_data("itter-quick-random.csv")

# Calculate itterative quick sort statistics
itter_quick_asc_stats = calculate_stats(itter_quick_asc_data, "itter-Quick-Ascending")
itter_quick_desc_stats = calculate_stats(itter_quick_desc_data, "itter-Quick-Descending")
itter_quick_random_stats = calculate_stats(itter_quick_random_data, "itter-Quick-Random")

# Combine itterative quick sort stats
itter_quick_combined_stats = pd.concat([itter_quick_asc_stats, itter_quick_desc_stats, itter_quick_random_stats])

# Create itterative quick sort graph
try:
    itter_quick_fig = go.Figure()
    
    itter_quick_algorithms = [
        ("itter-Quick-Ascending", "navy"),
        ("itter-Quick-Descending", "darkred"),
        ("itter-Quick-Random", "darkgreen"),
    ]
    
    for dataset, color in itter_quick_algorithms:
        stats = itter_quick_combined_stats[itter_quick_combined_stats["Dataset"] == dataset]
        itter_quick_fig.add_trace(
            go.Scatter(
                x=stats.index,
                y=stats["Mean"],
                error_y=dict(type="data", array=stats["Std Dev"]),
                name=dataset,
                line=dict(color=color),
            )
        )
    
    itter_quick_fig.update_layout(
        title="itterative Quick Sort Mean Execution Time",
        xaxis_title="Input Size (n)",
        yaxis_title="Time (seconds)",
        showlegend=True,
        height=600,
    )
    itter_quick_fig.update_xaxes(
        ticktext=[format_size(size) for size in [10, 100, 1000, 10000, 20000, 100000]],
        tickvals=[10, 100, 1000, 10000, 20000, 100000],
    )
    
    st.plotly_chart(itter_quick_fig, use_container_width=True)
except Exception as e:
    st.warning(f"Could not create itterative Quick Sort graph: {e}")

# Summary metrics
st.subheader("itterative Quick Sort Maximum Times")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Ascending Max Time", f"{itter_quick_asc_stats['Max'].max():.6f}s")
with col2:
    st.metric("Descending Max Time", f"{itter_quick_desc_stats['Max'].max():.6f}s")
with col3:
    st.metric("Random Max Time", f"{itter_quick_random_stats['Max'].max():.6f}s")

# itterative Quick Sort statistics tables
st.subheader("itterative Quick Sort - Detailed Statistics")

# Ascending
st.write("itterative Quick Sort - Ascending Order Statistics")
st.dataframe(itter_quick_asc_stats[["Mean", "Std Dev", "Min", "Max"]].style.format("{:.6f}"), use_container_width=True)

# Descending
st.write("itterative Quick Sort - Descending Order Statistics")
st.dataframe(itter_quick_desc_stats[["Mean", "Std Dev", "Min", "Max"]].style.format("{:.6f}"), use_container_width=True)

# Random
st.write("itterative Quick Sort - Random Order Statistics")
st.dataframe(itter_quick_random_stats[["Mean", "Std Dev", "Min", "Max"]].style.format("{:.6f}"), use_container_width=True)

# itterative Quick Sort raw data
st.subheader("itterative Quick Sort - Raw Data")

st.write("itterative Quick Sort - Ascending Order Data")
st.dataframe(itter_quick_asc_data.style.format("{:.6f}"), use_container_width=True)

st.write("itterative Quick Sort - Descending Order Data")
st.dataframe(itter_quick_desc_data.style.format("{:.6f}"), use_container_width=True)

st.write("itterative Quick Sort - Random Order Data")
st.dataframe(itter_quick_random_data.style.format("{:.6f}"), use_container_width=True)

#--------------------------------------------------------
# RECURSIVE QUICK SORT SECTION
#--------------------------------------------------------
st.header("Recursive Quick Sort Performance")

# Load recursive quick sort datasets
recur_quick_asc_data = load_data("recur-quick-ascending.csv")
recur_quick_desc_data = load_data("recur-quick-descending.csv")
recur_quick_random_data = load_data("recur-quick-random.csv")

# Calculate recursive quick sort statistics
recur_quick_asc_stats = calculate_stats(recur_quick_asc_data, "Recur-Quick-Ascending")
recur_quick_desc_stats = calculate_stats(recur_quick_desc_data, "Recur-Quick-Descending")
recur_quick_random_stats = calculate_stats(recur_quick_random_data, "Recur-Quick-Random")

# Combine recursive quick sort stats
recur_quick_combined_stats = pd.concat([recur_quick_asc_stats, recur_quick_desc_stats, recur_quick_random_stats])

# Create recursive quick sort graph
try:
    recur_quick_fig = go.Figure()
    
    recur_quick_algorithms = [
        ("Recur-Quick-Ascending", "purple"),
        ("Recur-Quick-Descending", "pink"),
        ("Recur-Quick-Random", "orange"),
    ]
    
    for dataset, color in recur_quick_algorithms:
        stats = recur_quick_combined_stats[recur_quick_combined_stats["Dataset"] == dataset]
        recur_quick_fig.add_trace(
            go.Scatter(
                x=stats.index,
                y=stats["Mean"],
                error_y=dict(type="data", array=stats["Std Dev"]),
                name=dataset,
                line=dict(color=color),
            )
        )
    
    recur_quick_fig.update_layout(
        title="Recursive Quick Sort Mean Execution Time",
        xaxis_title="Input Size (n)",
        yaxis_title="Time (seconds)",
        showlegend=True,
        height=600,
    )
    recur_quick_fig.update_xaxes(
        ticktext=[format_size(size) for size in [10, 100, 1000, 10000, 20000, 100000]],
        tickvals=[10, 100, 1000, 10000, 20000, 100000],
    )
    
    st.plotly_chart(recur_quick_fig, use_container_width=True)
except Exception as e:
    st.warning(f"Could not create Recursive Quick Sort graph: {e}")

# Summary metrics
st.subheader("Recursive Quick Sort Maximum Times")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Ascending Max Time", f"{recur_quick_asc_stats['Max'].max():.6f}s")
with col2:
    st.metric("Descending Max Time", f"{recur_quick_desc_stats['Max'].max():.6f}s")
with col3:
    st.metric("Random Max Time", f"{recur_quick_random_stats['Max'].max():.6f}s")

# Recursive Quick Sort statistics tables
st.subheader("Recursive Quick Sort - Detailed Statistics")

# Ascending
st.write("Recursive Quick Sort - Ascending Order Statistics")
st.dataframe(recur_quick_asc_stats[["Mean", "Std Dev", "Min", "Max"]].style.format("{:.6f}"), use_container_width=True)

# Descending
st.write("Recursive Quick Sort - Descending Order Statistics")
st.dataframe(recur_quick_desc_stats[["Mean", "Std Dev", "Min", "Max"]].style.format("{:.6f}"), use_container_width=True)

# Random
st.write("Recursive Quick Sort - Random Order Statistics")
st.dataframe(recur_quick_random_stats[["Mean", "Std Dev", "Min", "Max"]].style.format("{:.6f}"), use_container_width=True)

# Recursive Quick Sort raw data
st.subheader("Recursive Quick Sort - Raw Data")

st.write("Recursive Quick Sort - Ascending Order Data")
st.dataframe(recur_quick_asc_data.style.format("{:.6f}"), use_container_width=True)

st.write("Recursive Quick Sort - Descending Order Data")
st.dataframe(recur_quick_desc_data.style.format("{:.6f}"), use_container_width=True)

st.write("Recursive Quick Sort - Random Order Data")
st.dataframe(recur_quick_random_data.style.format("{:.6f}"), use_container_width=True)

#--------------------------------------------------------
# HYBRID QUICK SORT SECTION
#--------------------------------------------------------
st.header("Hybrid Quick Sort with Insertion Sort Performance")

# Load hybrid quick sort datasets
hybrid_quick_asc_data = load_data("itter-insert-quick-asceding.csv")
hybrid_quick_desc_data = load_data("itter-insert-quick-descending.csv")
hybrid_quick_random_data = load_data("itter-insert-quick-random.csv")

# Calculate hybrid quick sort statistics
hybrid_quick_asc_stats = calculate_stats(hybrid_quick_asc_data, "Hybrid-Quick-Ascending")
hybrid_quick_desc_stats = calculate_stats(hybrid_quick_desc_data, "Hybrid-Quick-Descending")
hybrid_quick_random_stats = calculate_stats(hybrid_quick_random_data, "Hybrid-Quick-Random")

# Combine hybrid quick sort stats
hybrid_quick_combined_stats = pd.concat([hybrid_quick_asc_stats, hybrid_quick_desc_stats, hybrid_quick_random_stats])

# Create hybrid quick sort graph
try:
    hybrid_quick_fig = go.Figure()
    
    hybrid_quick_algorithms = [
        ("Hybrid-Quick-Ascending", "skyblue"),
        ("Hybrid-Quick-Descending", "salmon"),
        ("Hybrid-Quick-Random", "lightgreen"),
    ]
    
    for dataset, color in hybrid_quick_algorithms:
        stats = hybrid_quick_combined_stats[hybrid_quick_combined_stats["Dataset"] == dataset]
        hybrid_quick_fig.add_trace(
            go.Scatter(
                x=stats.index,
                y=stats["Mean"],
                error_y=dict(type="data", array=stats["Std Dev"]),
                name=dataset,
                line=dict(color=color),
            )
        )
    
    hybrid_quick_fig.update_layout(
        title="Hybrid Quick Sort (with Insertion Sort) Mean Execution Time",
        xaxis_title="Input Size (n)",
        yaxis_title="Time (seconds)",
        showlegend=True,
        height=600,
    )
    hybrid_quick_fig.update_xaxes(
        ticktext=[format_size(size) for size in [10, 100, 1000, 10000, 20000, 100000]],
        tickvals=[10, 100, 1000, 10000, 20000, 100000],
    )
    
    st.plotly_chart(hybrid_quick_fig, use_container_width=True)
except Exception as e:
    st.warning(f"Could not create Hybrid Quick Sort graph: {e}")

# Summary metrics
st.subheader("Hybrid Quick Sort Maximum Times")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Ascending Max Time", f"{hybrid_quick_asc_stats['Max'].max():.6f}s")
with col2:
    st.metric("Descending Max Time", f"{hybrid_quick_desc_stats['Max'].max():.6f}s")
with col3:
    st.metric("Random Max Time", f"{hybrid_quick_random_stats['Max'].max():.6f}s")

# Hybrid Quick Sort statistics tables
st.subheader("Hybrid Quick Sort - Detailed Statistics")

# Ascending
st.write("Hybrid Quick Sort - Ascending Order Statistics")
st.dataframe(hybrid_quick_asc_stats[["Mean", "Std Dev", "Min", "Max"]].style.format("{:.6f}"), use_container_width=True)

# Descending
st.write("Hybrid Quick Sort - Descending Order Statistics")
st.dataframe(hybrid_quick_desc_stats[["Mean", "Std Dev", "Min", "Max"]].style.format("{:.6f}"), use_container_width=True)

# Random
st.write("Hybrid Quick Sort - Random Order Statistics")
st.dataframe(hybrid_quick_random_stats[["Mean", "Std Dev", "Min", "Max"]].style.format("{:.6f}"), use_container_width=True)

# Hybrid Quick Sort raw data
st.subheader("Hybrid Quick Sort - Raw Data")

st.write("Hybrid Quick Sort - Ascending Order Data")
st.dataframe(hybrid_quick_asc_data.style.format("{:.6f}"), use_container_width=True)

st.write("Hybrid Quick Sort - Descending Order Data")
st.dataframe(hybrid_quick_desc_data.style.format("{:.6f}"), use_container_width=True)

st.write("Hybrid Quick Sort - Random Order Data")
st.dataframe(hybrid_quick_random_data.style.format("{:.6f}"), use_container_width=True)

#--------------------------------------------------------
# ALGORITHM COMPARISON SECTION
#--------------------------------------------------------
st.header("Algorithm Comparison")

# Create a comparison of all algorithms on random data (average case)
try:
    # Combine all stats for comparison
    all_stats = pd.concat([
        heap_rand_stats, 
        itter_quick_random_stats,
        recur_quick_random_stats,
        hybrid_quick_random_stats
    ])
    
    # Create the random data comparison figure
    random_comp_fig = go.Figure()
    
    random_comp_algorithms = [
        ("Heap-Random", "green"),
        ("itter-Quick-Random", "darkgreen"),
        ("Recur-Quick-Random", "orange"),
        ("Hybrid-Quick-Random", "lightgreen")
    ]
    
    for dataset, color in random_comp_algorithms:
        stats = all_stats[all_stats["Dataset"] == dataset]
        random_comp_fig.add_trace(
            go.Scatter(
                x=stats.index,
                y=stats["Mean"],
                error_y=dict(type="data", array=stats["Std Dev"]),
                name=dataset,
                line=dict(color=color),
            )
        )
    
    random_comp_fig.update_layout(
        title="Algorithm Comparison on Random Data (Average Case)",
        xaxis_title="Input Size (n)",
        yaxis_title="Time (seconds)",
        showlegend=True,
        height=600,
    )
    random_comp_fig.update_xaxes(
        ticktext=[format_size(size) for size in [10, 100, 1000, 10000, 20000, 100000]],
        tickvals=[10, 100, 1000, 10000, 20000, 100000],
    )
    
    st.plotly_chart(random_comp_fig, use_container_width=True)
except Exception as e:
    st.warning(f"Could not create random data comparison chart: {e}")

# Footer with dataset information
st.markdown(
    """
---

# Brodie Rogers 
# Sorting Algorithms Performance Analysis
---

## Implementation Overview

This analysis compares four different sorting algorithms:

1. **Heap Sort**: A comparison-based sorting algorithm that uses a binary heap data structure. It divides its input into a sorted and an unsorted region, and itteratively shrinks the unsorted region by extracting the largest element and moving it to the sorted region.

2. **itterative Quick Sort**: An implementation of the Quick Sort algorithm using itteration rather than recursion. Quick Sort works by selecting a 'pivot' element and partitioning the array around the pivot, so elements less than the pivot are on one side and elements greater are on the other.

3. **Recursive Quick Sort**: The traditional implementation of Quick Sort using recursion. This approach uses the call stack to keep track of the sub-arrays.

4. **Hybrid Quick Sort with Insertion Sort**: A variation that uses Quick Sort for larger partitions but switches to Insertion Sort for smaller sub-arrays to improve efficiency.

--- 

## Data

The data was collected using Python, timing each sorting algorithm on 6 different array sizes.
This was further extended by testing each algorithm on data in Random, Ascending, and Descending orders.
I used pandas, plotly, and streamlit for the data analysis and visualization.

---

### Data Collection

- 99 itterations for Heap sort but only 10 for the Quick Sorts, on 7 different array sizes and permutations 
- Array sizes analyzed: 10, 100, 1,000, 10,000, 20,000, 100,000, and 1,000,000 
- Array permutations analyzed: Ascending, Random, Descending

I recorded the execution time for each algorithm to complete a sort for each array size and configuration, repeating 98 more times to get statistically significant results.

---

### Data Processing

- Read data from CSV into Pandas DataFrames
- Used Python's built-in math functions to perform different calculations such as Mean, Standard Deviation, Min, and Max

---

### Data Visualization 

- Used Plotly to create interactive visualizations of the performance data
- Created line charts to show the results of every permutation and array size side by side, with Standard Deviation shown by error bars
- Displayed maximum sorting times for different permutations
- Provided detailed statistics tables for each algorithm, size, and permutation
- Included tables with raw data for comprehensive analysis

---

### Time Complexity Comparison

#### Heap Sort:
- Theoretical time complexity: O(n log n) in all cases
- For large arrays (n=100,000), performs consistently across all input arrangements
- Showed stable performance with predictable scaling

#### Quick Sort (itterative and Recursive):
- Theoretical time complexity: O(n log n) average case, O(n²) worst case
- Performs well on random data but can degrade with already sorted or reverse sorted data, Whereas I found that it preformed worst on the random data. Im not sure if it was somthing on my end or not.
- Recursive version shows slightly higher overhead due to function calls

#### Hybrid Quick Sort with Insertion Sort:
- Combines the strengths of both algorithms
- Better performance on smaller subarrays where insertion sort outperforms quick sort
- Shows improved constant factors while maintaining O(n log n) average time complexity

---

### Performance Analysis

- For small arrays (n=10, 100):
    - All algorithms show extremely fast execution times
    - Minimal differences between implementations
    
- For medium arrays (n=1,000, 10,000):
    - Algorithm differences become more apparent
    - The hybrid approach starts to show advantages

- For large arrays (n=20,000, 100,000):
    - Performance characteristics fully emerge
    - Quick Sort variants typically outperform Heap Sort on random data
    - Heap Sort shows more consistent performance across all input types

---

### Variance in Performance

Each algorithm shows different variance characteristics:

- Heap Sort: Most consistent across different input arrangements
- Quick Sort variants: Higher variance, especially on sorted or reverse-sorted inputs
- Random inputs generally produce the most variable execution times

---

### Conclusion  

This analysis demonstrates the performance characteristics of different sorting algorithms across various input sizes and arrangements. Key findings include:

1. Quick Sort variants generally perform better on random data
2. Heap Sort offers more consistent performance regardless of input arrangement
3. The hybrid Quick Sort with Insertion Sort approach shows benefits for real-world applications
4. Algorithm selection should consider expected input characteristics

- Most of this conclusion of the algorithms is based on the theoretical instead of my results due to the extreme variation in the random data execution times.    
- For future work, I'd like to figure out why my quick sort was so much slower on random elements compared to the ascending/descending data. Espically since this is backwards from how it should be.
---
"""
)