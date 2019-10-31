#!/usr/bin/env python
from __future__ import print_function
from collections import OrderedDict
import re

regexes = {
    'nf-core/kmermaid': ['v_pipeline.txt', r"(\S+)"],
    'Nextflow': ['v_nextflow.txt', r"(\S+)"],
    'Sourmash': ['v_sourmash.txt', r"sourmash version (\S+)"],
    'Bam2fasta': ['v_bam2fasta.txt', r"bam2fasta version (\S+)"],
}
results = OrderedDict()
results['nf-core/kmermaid'] = '<span style="color:#999999;\">N/A</span>'
results['Nextflow'] = '<span style="color:#999999;\">N/A</span>'
results['Sourmash'] = '<span style="color:#999999;\">N/A</span>'

# Search each file using its regex
for k, v in regexes.items():
    with open(v[0]) as x:
        versions = x.read()
        match = re.search(v[1], versions)
        if match:
            results[k] = "v{}".format(match.group(1))

# Dump to YAML
print ('''
id: 'nf-core/kmermaid-software-versions'
section_name: 'nf-core/kmermaid Software Versions'
section_href: 'https://github.com/nf-core/kmermaid'
plot_type: 'html'
description: 'are collected at run time from the software output.'
data: |
    <dl class="dl-horizontal">
''')
for k,v in results.items():
    print("        <dt>{}</dt><dd>{}</dd>".format(k,v))
print ("    </dl>")

# Write out regexes as csv file:
with open('software_versions.txt', 'w') as f:
    for k,v in results.items():
        f.write("{}\t{}\n".format(k,v))
