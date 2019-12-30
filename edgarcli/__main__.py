import argparse
import edgar
import pdfkit

def update_index()
  edgar.download_index(dir, since_year)



def __main__():
  parser = argparse.ArgumentParser(description='Interact with EDGAR https://www.sec.gov/edgar.shtml')
  parser.add_argument('--config', help='Path to an edgarcli config file')

  subparsers = parser.add_subparsers(dest='subcommand')
  download_parser = subparsers.add_parser('download', help='download filings from EDGAR')
  search_parser = subparsers.add_parser('search', help='search stuff from EDGAR')

  download_parser.add_argument('cik', help='CIK number')
  download_parser.add_argument()

  args = parser.parse_args()
  print(args.accumulate(args.integers))