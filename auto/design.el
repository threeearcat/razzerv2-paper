(TeX-add-style-hook
 "design"
 (lambda ()
   (TeX-add-symbols
    "segment"
    "segments"
    "Segments"
    "mutable"
    "mutables"
    "immutable"
    "immutables")
   (LaTeX-add-labels
    "s:design"
    "ss:keyidea"
    "fig:intuition"
    "ss:coverage"
    "fig:interleaving-graph"
    "ss:scheduler"))
 :latex)

