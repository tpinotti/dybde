##
##	DYBDE
##	pysam-based estimation of average depth of coverage of the Y-chromosome
##	only uses the short-read mappable region defined in Poznik 2013
##	
##
##
##	TP 2023
##


import sys
import pysam
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Calculate average depth of coverage on Y-chromosome short-read mappable regions')
    parser.add_argument('bed_version', choices=['37', '38'], help='Version of the reference genome (37 or 38)')
    parser.add_argument('bam_path', help='Path to bam file')
    return parser.parse_args()

def get_bed_path(bed_version):
    if bed_version == '37':
        return "src/chrY_callable_region_GRCh37.bed"
    elif bed_version == '38':
        return "src/chrY_callable_region_GRCh38.bed"
    else:
        raise ValueError("Invalid bed version")

def main():
    args = parse_arguments()
    bed_path = get_bed_path(args.bed_version)
    bam_path = args.bam_path

    # parse bed file
    bedregions = []
    with open(bed_path, "r") as bedfile:
        for line in bedfile:
            if line.startswith("#"):
                continue
            chrom, start, end = line.strip().split("\t")
            bedregions.append((chrom, int(start), int(end)))

    # parse bam
    total_count = 0
    mapped_length = 0

    with pysam.AlignmentFile(bam_path, "rb") as bamfile:
        for read in bamfile:
            if read.mapping_quality < 30:
                continue
            for region in bedregions:
                if read.reference_name == region[0] and read.reference_start <= region[2] and read.reference_end >= region[1]:
                    mapped_length += read.query_length
                    break
            total_count += 1

    print("Reads mapped to chrY short-read mappable region:", total_count)
    print("Average depth of coverage on chrY short-read mappable region:", (mapped_length / 10458821))

if __name__ == "__main__":
    main()
