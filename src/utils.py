import matplotlib.pyplot as plt
from wordcloud import WordCloud

def draw_keyword_cloud(abstracts, paper_ids):
    """
    Creates a word cloud from paper abstracts.
    
    Args:
        abstracts: List of abstract texts extracted from papers
        paper_ids: List of paper identifiers
    
    Returns:
        matplotlib figure object
    """
    figures = []
    for abstract, paper_id in zip(abstracts, paper_ids):
        wordcloud = WordCloud(
            width=800,
            height=400,
            background_color='white',
            colormap='viridis',
            max_words=100,
            relative_scaling=0.5,
            min_font_size=10
        ).generate(abstract)
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        ax.set_title(str(paper_id), fontsize=16, pad=20)
        plt.tight_layout()
        figures.append(fig)
    return figures


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


def show_paper_links(paper_links, paper_ids,):
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

def create_figures(info, show=False, output_dir=None):
    """
    Creates visualizations based on extracted paper information.
    
    :param info: List of dictionaries containing paper information (title, abstract, figures_count, links)
    """

    # Extract data for visualizations
    abstracts = [paper['abstract'] for paper in info if paper['abstract']]
    figure_counts = [paper['figures_count'] for paper in info]
    paper_ids = [paper['paper_id'] for paper in info]
    paper_links = [paper['links'] for paper in info]

    # Create visualizations
    wordcloud_fig = draw_keyword_cloud(abstracts, paper_ids)
    figures_bar_fig = visualize_figures_per_article(figure_counts, paper_ids)
    links_table_fig = show_paper_links(paper_links, paper_ids)

    if show:
        plt.show()  # Display all figures

    if output_dir:
        # Save figures to output directory
        for j, fig in enumerate(wordcloud_fig):
            fig_path = f"{output_dir}/wordcloud_{paper_ids[j]}.png"
            fig.savefig(fig_path)
            print(f"Word cloud saved to: {fig_path}")
        
        bar_fig_path = f"{output_dir}/figures_bar_chart.png"
        figures_bar_fig.savefig(bar_fig_path)
        print(f"Figures bar chart saved to: {bar_fig_path}")
        
        links_fig_path = f"{output_dir}/paper_links_table.png"
        links_table_fig.savefig(links_fig_path)
        print(f"Paper links table saved to: {links_fig_path}")