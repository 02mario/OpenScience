import paper_download
import grobid
import utils

def main():
    action = input("Enter 'download' to download papers or 'process' to process existing PDFs: ").strip().lower()

    if action == 'download':
        dataset_dir = input("Enter the directory to save downloaded papers: ").strip()
        paper_download.download_papers(dataset_dir)
    elif action == 'process':
        dataset_dir = input("Enter the directory containing PDF files to process: ").strip()
        results = grobid.process_dataset(dataset_dir)
        utils.create_figures(results)
    else:
        print("Invalid action. Please enter 'download' or 'process'.")

if __name__ == "__main__":
    main()