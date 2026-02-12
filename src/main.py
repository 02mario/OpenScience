import paper_download
from pathlib import Path

if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent.parent
    papers_file = base_dir / "Papers.txt"
    output_dir = base_dir / "dataset"
    paper_download.download_arxiv_papers(papers_file, output_dir)