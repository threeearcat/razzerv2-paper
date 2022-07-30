#!/usr/bin/python
import os, sys

pdf_fn = sys.argv[1]
outdir = sys.argv[2]

LAYOUT = []
# (segment name, the number of pages in the segment)
LAYOUT += [("summary", 1)]
LAYOUT += [("description", 15)]
LAYOUT += [("list-collaboration", 1)]
LAYOUT += [("data-management-plan", 1)]
LAYOUT += [("resource", 1)]
LAYOUT += [("topic-areas", 1)]
LAYOUT += [("references", 2)]

end_page = 0

if not os.path.exists(outdir):
    os.mkdir(outdir)

for name, num_pages in LAYOUT:
    begin_page = end_page + 1
    end_page = begin_page + (num_pages-1)
    outpdf_fn = os.path.join(outdir, "%s.pdf" % name)
    cmd_str = "pdftk %s cat %d-%d output %s" % \
              (pdf_fn, begin_page, end_page, outpdf_fn)
    print cmd_str
    os.system(cmd_str)
