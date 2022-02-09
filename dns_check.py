#! /usr/bin/env python

import argparse
import dns.resolver
from rich.table import Table
from rich.console import Console

args_parser = argparse.ArgumentParser(
    prog="dns-check",
    description="Searches DNS for A, CNAME, MX, TXT, AAAA and SRV records for the specified FQDN.",
)

args_parser.add_argument(
    "domain",
    metavar="domainname",
    type=str,
    help="Enter the FQDN to search DNS records for.",
)

args_parser.add_argument(
    "-ns",
    "--nameserver",
    metavar="nameserver",
    type=str,
    help="Enter a custom nameserver.",
    required=False,
)


def get_records(domain: str) -> str:
    """
    :param domain
    :return str
    """
    record_types = [
        "A",
        "CNAME",
        "MX",
        "TXT",
        "AAAA",
        "SRV",
    ]

    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Record")
    table.add_column("Value")
    for record in record_types:
        try:
            resolver = dns.resolver
            if args.nameserver:
                resolver.nameservers = [args.nameserver]
            answers = resolver.resolve(domain, record)
            for rdata in answers:
                table.add_row(record, rdata.to_text())
        except:
            continue
    console.print(table)  # or pass


if __name__ == "__main__":
    args = args_parser.parse_args()
    get_records(args.domain)
