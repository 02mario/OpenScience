import argparse
from .grobid import process_dataset
from .utils import create_figures
import os

def main():
    parser = argparse.ArgumentParser(description="Tool for processing papers with GROBID and visualizing results.")
    parser.add_argument('--dataset', type=str, default="dataset", help="Dataset directory path.")
    parser.add_argument('--output', type=str, default="output", help="Output directory for results or figures.")
    parser.add_argument('--show', default=False, action='store_true', help="Show figures after processing.")
    args = parser.parse_args()

    # Set workdir as the parent directory of the directory containing this file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    workdir = os.path.dirname(script_dir)

    # Resolve dataset and output paths relative to workdir if not absolute
    dataset_path = args.dataset if os.path.isabs(args.dataset) else os.path.join(workdir, args.dataset)
    output_path = args.output if os.path.isabs(args.output) else os.path.join(workdir, args.output)

    if not os.path.exists(dataset_path):
        os.makedirs(dataset_path, exist_ok=True)
    if not os.path.exists(output_path):
        os.makedirs(output_path, exist_ok=True)

    if args.show or output_path:
        results = process_dataset(dataset_path)
        figs = create_figures(results, show=args.show, output_dir=output_path)
    else:
        print("Warning: No output selected. Omit --show or use --output to save them.")

if __name__ == "__main__":
    main()