# dybde
fast estimator of depth of coverage on short-read mappable regions of Y-chromosome

## why?

Despite being 58Mb long, only 10Mb of the Y-chromosome is amenable to short-read mapping, due to pervasive repetitive regions (1-3).

Therefore, when estimating depth of coverage from a short-read sequencing experiment, unless this 10Mb region is specified, the result is not readily comparable to autosomes or X-chromosomes.

## how?

dybde uses pysam to count reads mapped to the Y-chromosome 10Mb region, measure its length and estimate depth of coverage.
It does not index jump, therefore I strongly recommend to extract reads mapping to the Y-chromosome before running dybde

```
samtools view -o Y.ind1.bam ind1.bam Y
```

## so?

It only needs a bam and for you to specify which genome reference you have mapped to (37 or 38). e.g.

```
python dybde.py 37 Y.Ind1.bam > ind1.ydoc
```

Run it with -h to display a help message, which tells all you need to know

```
usage: dybde.py [-h] {37,38} bam_path

Calculate average depth of coverage on Y-chromosome short-read mappable regions

positional arguments:
  {37,38}     Version of the reference genome (37 or 38)
  bam_path    Path to bam file
```

## references:

1. Skaletsky et al. 2003, doi:10.1038/nature01722
2. Poznik et al. 2013, doi:10.1126/science.1237619
3. Jobling and Tyler-Smith 2017, doi:10.1038/nrg.2017.36

