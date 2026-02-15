import os
import urllib.request
import ssl

import certifi

def download_arxiv_papers(papers_file, output_dir):
    """
    Downloads arXiv PDFs from a list of URLs.
    
    Args:
        papers_file: Path to file containing arXiv URLs
        output_dir: Directory where PDFs will be saved
    """
    # SSL certificate problem resolved 
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    
    opener = urllib.request.build_opener(
        urllib.request.HTTPSHandler(context=ssl_context)
    )
    urllib.request.install_opener(opener)
    
    # Read URLs from file
    with open(papers_file, 'r') as f:
        urls = [line.strip() for line in f if line.strip()]
    
    print(f"Found {len(urls)} papers to download\n")
    
    # Download each PDF
    for i, url in enumerate(urls, 1):
        try:
            if '/abs/' in url:
                arxiv_id = url.split('/')[-1]
                # Convert abstract URL to PDF URL
                pdf_url = url.replace('/abs/', '/pdf/') + '.pdf'
                output_file = os.path.join(output_dir, f"{arxiv_id}.pdf")
                
                print(f"[{i}/{len(urls)}] Downloading {arxiv_id}...")
                
                # Download PDF
                urllib.request.urlretrieve(pdf_url, output_file)
                
                print(f"  ✓ Saved to {output_file}")
            else:
                print(f"  ✗ Invalid URL: {url}")
            
        except Exception as e:
            print(f"  ✗ Error downloading: {str(e)}")