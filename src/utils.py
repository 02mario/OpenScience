import matplotlib.pyplot as plt
from wordcloud import WordCloud

def draw_keyword_cloud(abstracts):
    """
    Creates a word cloud from paper abstracts.
    
    Args:
        abstracts: List of abstract texts extracted from papers
    
    Returns:
        matplotlib figure object
    """
    combined_text = ' '.join(abstracts)
    
    # Create word cloud
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        colormap='viridis',
        max_words=100,
        relative_scaling=0.5,
        min_font_size=10
    ).generate(combined_text)
    
    # Create figure
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    
    plt.tight_layout()
    
    return fig


def visualize_figures_per_article(figure_counts, paper_ids):
    """
    Creates a bar chart showing the number of figures per article.
    
    Args:
        figure_counts: List of integers representing number of figures per paper
        paper_ids: List of paper identifiers
    
    Returns:
        matplotlib figure object
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    bars = ax.bar(paper_ids, figure_counts)
    
    ax.set_xlabel('Paper ID', fontsize=12)
    ax.set_ylabel('Number of Figures', fontsize=12)
    ax.set_title('Number of Figures per Article', fontsize=16, pad=20)
    
    # Add value labels on bars
    for bar, count in zip(bars, figure_counts):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(count)}',
                ha='center', va='bottom', fontsize=10)
    
    plt.tight_layout()
    
    return fig


def show_paper_links(paper_ids, paper_links):
    """
    Creates a simple table figure showing papers and their links.
    
    Args:
        paper_ids: List of paper identifiers
        paper_links: List of lists, where each inner list contains URLs for that paper
    
    Returns:
        matplotlib figure object
    """
    # Flatten data for simple table (1 row per link)
    cell_text = []
    for pid, links in zip(paper_ids, paper_links):
        # Add first link with ID
        if links:
            cell_text.append([pid, links[0]])
            # Add subsequent links with empty ID
            for link in links[1:]:
                cell_text.append(["", link])
        else:
            cell_text.append([pid, "No links"])

    # Create figure
    # Estimate height: Header + Rows. ~0.3 inch per row
    fig_height = max(2, len(cell_text) * 0.4 + 1)
    fig, ax = plt.subplots(figsize=(12, fig_height))
    ax.axis('off')
    
    # Create the table
    table = ax.table(
        cellText=cell_text,
        colLabels=["Paper ID", "Links"],
        loc='center',
        cellLoc='left',
        colWidths=[0.2, 0.8]
    )
    
    # Simple styling
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)  # Give rows some breathing room
    
    # Header color
    for j in range(2):
        cell = table[(0, j)]
        cell.set_facecolor('#4472C4')
        cell.set_text_props(color='white', weight='bold')

    ax.set_title("Paper Links", fontsize=14, pad=10)
    
    plt.tight_layout()
    return fig