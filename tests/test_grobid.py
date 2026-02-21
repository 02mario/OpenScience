import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.grobid import extract_paper_info

TEI_NS = 'http://www.tei-c.org/ns/1.0'

def build_tei(title="Test Title", abstract="Test abstract text.",
              num_figures=0, links=None):
    """Helper to build a minimal TEI XML string."""
    links = links or []

    figures_xml = ''.join('<figure/>' for _ in range(num_figures))

    refs_xml = ''.join(
        f'<ref target="{url}">link</ref>' for url in links
    )

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<TEI xmlns="{TEI_NS}">
  <teiHeader>
    <fileDesc>
      <titleStmt>
        <title>{title}</title>
      </titleStmt>
    </fileDesc>
  </teiHeader>
  <text>
    <front>
      <div type="abstract">
        <abstract>{abstract}</abstract>
      </div>
    </front>
    <body>
      {figures_xml}
      {refs_xml}
    </body>
  </text>
</TEI>"""


class TestExtractPaperInfo(unittest.TestCase):

    def test_title_extracted(self):
        xml = build_tei(title="My Paper Title")
        result = extract_paper_info(xml)
        self.assertEqual(result['title'], "My Paper Title")

    def test_abstract_extracted(self):
        xml = build_tei(abstract="This is the abstract.")
        result = extract_paper_info(xml)
        self.assertIn("abstract", result)
        self.assertIn("This is the abstract.", result['abstract'])

    def test_figures_count_zero(self):
        xml = build_tei(num_figures=0)
        result = extract_paper_info(xml)
        self.assertEqual(result['figures_count'], 0)

    def test_figures_count_nonzero(self):
        xml = build_tei(num_figures=3)
        result = extract_paper_info(xml)
        self.assertEqual(result['figures_count'], 3)

    def test_links_extracted(self):
        urls = ["https://example.com", "http://openaccess.org", "https://github.com/kermitt2/grobid"]
        xml = build_tei(links=urls)
        result = extract_paper_info(xml)
        for url in urls[:-1]:
            self.assertIn(url, result['links'])

    def test_links_empty_when_none(self):
        xml = build_tei(links=[])
        result = extract_paper_info(xml)
        self.assertEqual(result['links'], [])

    def test_no_title_returns_default(self):
        # Build XML without a title element
        xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<TEI xmlns="{TEI_NS}">
  <teiHeader>
    <fileDesc>
      <titleStmt/>
    </fileDesc>
  </teiHeader>
  <text><body/></text>
</TEI>"""
        result = extract_paper_info(xml)
        self.assertEqual(result['title'], "No title")

    def test_result_has_required_keys(self):
        xml = build_tei()
        result = extract_paper_info(xml)
        for key in ('title', 'abstract', 'figures_count', 'links'):
            self.assertIn(key, result)

    def test_duplicate_links_deduplicated(self):
        url = "https://example.com"
        xml = build_tei(links=[url, url])
        result = extract_paper_info(xml)
        self.assertEqual(result['links'].count(url), 1)


if __name__ == '__main__':
    unittest.main()
