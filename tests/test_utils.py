import os
import unittest

# Use non-interactive backend before importing matplotlib or utils
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from src.utils import (
    draw_keyword_cloud,
    visualize_figures_per_article,
    show_paper_links,
    create_figures,
)

# Sample data reused across tests
PAPER_IDS = ['paper_1', 'paper_2']
ABSTRACTS = [
    "machine learning deep neural network classification accuracy",
    "open science reproducibility data sharing peer review",
]
FIGURE_COUNTS = [3, 5]
PAPER_LINKS = [
    ["https://example.com/a", "https://example.com/b"],
    [],
]


def teardown_figures():
    """Close all open matplotlib figures after each test."""
    plt.close('all')


class TestDrawKeywordCloud(unittest.TestCase):

    def tearDown(self):
        teardown_figures()

    def test_returns_list(self):
        figs = draw_keyword_cloud(ABSTRACTS, PAPER_IDS)
        self.assertIsInstance(figs, list)

    def test_one_figure_per_abstract(self):
        figs = draw_keyword_cloud(ABSTRACTS, PAPER_IDS)
        self.assertEqual(len(figs), len(ABSTRACTS))

    def test_figures_are_matplotlib_figures(self):
        figs = draw_keyword_cloud(ABSTRACTS, PAPER_IDS)
        for fig in figs:
            self.assertIsInstance(fig, plt.Figure)

    def test_empty_inputs_return_empty_list(self):
        figs = draw_keyword_cloud([], [])
        self.assertEqual(figs, [])


class TestVisualizeFiguresPerArticle(unittest.TestCase):

    def tearDown(self):
        teardown_figures()

    def test_returns_figure(self):
        fig = visualize_figures_per_article(FIGURE_COUNTS, PAPER_IDS)
        self.assertIsInstance(fig, plt.Figure)

    def test_axes_labels(self):
        fig = visualize_figures_per_article(FIGURE_COUNTS, PAPER_IDS)
        ax = fig.axes[0]
        self.assertEqual(ax.get_xlabel(), 'Paper ID')
        self.assertEqual(ax.get_ylabel(), 'Number of Figures')

    def test_bar_count_matches_papers(self):
        fig = visualize_figures_per_article(FIGURE_COUNTS, PAPER_IDS)
        ax = fig.axes[0]
        # Number of bars should equal number of papers
        self.assertEqual(len(ax.patches), len(PAPER_IDS))


class TestShowPaperLinks(unittest.TestCase):

    def tearDown(self):
        teardown_figures()

    def test_returns_figure(self):
        fig = show_paper_links(PAPER_LINKS, PAPER_IDS)
        self.assertIsInstance(fig, plt.Figure)

    def test_paper_with_no_links(self):
        fig = show_paper_links([[], []], ['p1', 'p2'])
        self.assertIsInstance(fig, plt.Figure)

    def test_single_paper_single_link(self):
        fig = show_paper_links([["https://example.com"]], ["p1"])
        self.assertIsInstance(fig, plt.Figure)


class TestCreateFigures(unittest.TestCase):

    def setUp(self):
        self.info = [
            {
                'paper_id': 'paper_1',
                'abstract': 'machine learning deep neural network classification',
                'figures_count': 3,
                'links': ['https://example.com'],
            },
            {
                'paper_id': 'paper_2',
                'abstract': 'open science reproducibility data sharing peer review',
                'figures_count': 1,
                'links': [],
            },
        ]

    def tearDown(self):
        teardown_figures()

    def test_runs_without_error(self):
        try:
            create_figures(self.info, show=False, output_dir=None)
        except Exception as e:
            self.fail(f"create_figures raised an exception: {e}")

    def test_papers_without_abstract_are_skipped_for_wordcloud(self):
        info = [
            {
                'paper_id': 'no_abstract',
                'abstract': '',          # empty → excluded from word cloud
                'figures_count': 2,
                'links': [],
            },
            {
                'paper_id': 'has_abstract',
                'abstract': 'natural language processing text mining',
                'figures_count': 4,
                'links': ['https://nlp.example.com'],
            },
        ]
        try:
            create_figures(info, show=False, output_dir=None)
        except Exception as e:
            self.fail(f"create_figures raised an exception: {e}")


if __name__ == '__main__':
    unittest.main()
