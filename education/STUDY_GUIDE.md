# Which kind of data makes a gene group recognizable?

A plain-language companion to *Which data modality recognizes a gene set? A domain-agnostic consilience engine*, Patrick Iben, author draft supplied as the 13 July 2026 PeerJ manuscript.

## Start with the choice of evidence

Suppose someone hands you a gene group. Would shared protein parts, a similar expression pattern or a network of associations make that group stand out?

The paper builds a tool for comparing these views. It does not establish that one assay is best for every gene group, discover a new universal biological law or confirm a clinical target.

This guide assumes basic familiarity with genes but no knowledge of graph statistics. Each lesson defines the terms it needs, gives a question and supplies an answer. Page numbers refer to the source draft.

[Read the source draft](../manuscript/consilience_PeerJ_draft.pdf).

## C1. The question comes before integration

**Where we are**

Abstract and Introduction, PDF pages 1–3.

**What the passage is doing**

A modality is one kind of data. A lens is the particular representation built from that data. A component is a named gene group. Here “recognizes” means that the lens makes a component's genes more similar to each other than to the other genes in the chosen atlas.

Multi-omics integration combines several data types for a downstream task. This paper first asks which individual view distinguishes which kind of gene group. The two approaches can be complementary.

**In ordinary language**

Different questions can need different evidence. A group defined by cell identity may stand out in expression data. A family of related proteins may stand out through shared protein parts. Combining every view first could hide which view supplied the distinction.

**Evidence status**

Research question and operational definition. The main novelty claimed is the reusable lens-map instrument and its class recovery, not the already known biological facts it reproduces.

**Do not accidentally conclude**

A recognized group is not necessarily a new discovery, a causal pathway or a clinically useful biomarker. “Domain-agnostic” describes the configurable procedure, not proof of success in every biological setting.

**Try it**

What is the output of interest: a new gene's disease risk or the modality that distinguishes a supplied group? **Answer:** The latter. Other methods may ask the former question.

## C2. Four lenses ask different questions

**Where we are**

“Lenses,” page 3; Results and Figure 1, page 5.

**What the passage is doing**

Each lens builds a gene–gene similarity graph: genes are nodes and similarity values are the links. The same gene pairs can receive different values in different lenses.

| Lens | Representation and similarity | Important meaning |
|---|---|---|
| Structure | InterPro domain annotations from reviewed human UniProt entries; Jaccard similarity | Shared annotated protein parts, not a measured three-dimensional fold |
| Expression | Human Protein Atlas cell-type RNA; log1p transform and cosine similarity | Similar expression profiles in the chosen tissue/cell panel |
| Interaction | STRING combined association score, scaled to 0–1 | A combined association measure, not exclusively direct physical binding |
| Process | Gene Ontology biological-process annotations; Jaccard similarity | Shared process terms in the available annotation set |

Jaccard similarity is the number of shared items divided by the number of distinct items across both sets. Cosine similarity compares the directions of numerical profiles. The expression transformation reduces the dominance of very large values.

**In ordinary language**

These are four different ways for genes to resemble one another. Sharing protein parts is different from being active in the same cells. An interaction database also combines several evidence channels, which may include shared published knowledge.

**Evidence status**

Defined data representations using public sources. Tissue choice is part of the method: brain single-nucleus expression for the nervous map and blood-cell expression for the immune map.

**Do not accidentally conclude**

A structure lens is not a complete structural experiment. A STRING edge need not be a physical bond. Database coverage and shared sources can affect agreement between lenses.

**Try it**

In a hypothetical annotation example, one gene has X and Y, another Y and Z. What is their Jaccard similarity? **Answer:** One shared item divided by three distinct items, or 1/3. This is teaching arithmetic, not a study result.

## C3. Separation compares within-group and outside-group similarity

**Where we are**

“Separation and null,” page 3; Figure 1, page 5.

**What the passage is doing**

Separation is mean similarity between different genes inside the component minus mean similarity between a component gene and an atlas gene outside it. The comparison population is therefore the chosen atlas, not every possible human gene.

Missing pairs are assigned zero in the reported scoring rule. Group memberships define the scoring groups. They are not used to construct the underlying similarity graphs.

**In ordinary language**

A lens recognizes a group when its members resemble one another more than they resemble outsiders. A positive score means the group stands apart under that definition. The choice of outsiders and the available measurements matter.

**Evidence status**

Defined statistic. Hypothetical example: within-group mean 0.8 minus outside-group mean 0.2 gives separation 0.6. These values illustrate the formula only.

**Do not accidentally conclude**

A missing pair assigned zero is not verified biological dissimilarity. Nor does positive separation say that every member has the same function. Inspect coverage and group construction.

**Try it**

Could the same group receive a different separation score in a different atlas? **Answer:** Yes. Its outside-group comparison and possibly its available annotations would change.

## C4. A random-group comparison gives the score context

**Where we are**

Permutation methods, pages 3–4; Figure 8, page 8.

**What the passage is doing**

A permutation null compares a component with random atlas gene sets of the same size. The main component tests use 2,000 random sets. A z-score states how far the observed separation lies above the null mean, measured in null standard deviations. An empirical p-value describes how extreme the result is under that random-set procedure.

Calibration checks the machinery on sets intended to be null. Across 400 random gene sets, the paper reports false positives at 0.045 for a 0.05 threshold, with Monte-Carlo standard error 0.010. Its p-value uniformity test gives p = 0.59. The calibration uses its own resampling budget, distinct from the main component tests.

**In ordinary language**

A score needs a fair reference. Random groups of the same size show how much separation can arise without the proposed grouping. A sensible false-alarm rate is reassuring, but it does not show that weak real signals will be detected.

**Evidence status**

Permutation-tested estimates and a reported null-calibration experiment. Monte-Carlo error is variation due to finite random draws; it differs from uncertainty caused by the underlying biological sample or curation.

**Do not accidentally conclude**

Good Type-I error calibration does not establish power, remove curator choices or prove independent evidence across databases. A z-score also tends to increase with component size.

**Try it**

Why match the size of the random groups? **Answer:** Group size changes the score's null behavior. Comparing a small component only with large random groups would change the reference question.

## C5. Significance and the chosen pattern threshold differ

**Where we are**

Multiple testing, page 4; nervous-system exceptions, page 7.

**What the passage is doing**

Many groups are tested in several lenses. False discovery rate, or FDR, control addresses the expected share of false discoveries among selected results under its assumptions. The paper uses Benjamini–Yekutieli control because the tests share genes and similarity information.

All 49 nervous-system components have a significant best lens after the reported correction. But the paper also uses z ≥ 4 to describe its strong per-class pattern. These are different criteria.

**In ordinary language**

A result can pass a statistical test without meeting a stronger display rule. Keep those decisions separate. A group that misses the stronger rule is not automatically invisible in the data.

**Evidence status**

Reported multiple-testing analysis. Cerebellar neurons have expression z = 3.7 and p = 0.008: significant, but below the stated strong-pattern cutoff. Spinal-motor neurons do not separate on expression and route to interaction.

**Do not accidentally conclude**

“All components have a significant best lens” does not mean every cell type has strong expression separation, or that every lens recognizes every group.

**Try it**

Is the cerebellar example a contradiction? **Answer:** No. Significance and the z ≥ 4 pattern rule are not interchangeable.

## C6. The central lens-map is about diagnostic contrast

**Where we are**

Nervous-system Results, pages 6–7; Figure 2, page 6.

**What the passage is doing**

The nervous atlas has 410 genes in 49 components. Glial and vascular cell groups tend to stand out in expression. Molecular families tend to stand out in domain structure. Functional and disease modules often need interaction information.

STRING has the largest separation for 38 of 49 components. That makes it a broad detector but a poor way to distinguish these entity classes. The specialized structure-versus-expression contrast carries much of the diagnostic distinction.

**In ordinary language**

A detector that recognizes almost everything may not tell you what kind of thing you have. Compare the pattern across lenses. A cell group, protein family and working module can be coherent for different reasons.

**Evidence status**

Reported component-level findings. Examples include microglial expression and glutamate-receptor domain structure. Dopamine/reward signaling mixes receptor-family and cell-identity features, making it a dual-character example.

**Do not accidentally conclude**

“Structure versus expression” is not a rule that forbids biological overlap. Neuronal exceptions and mixed groups are part of the paper's result, not errors to conceal.

**Try it**

If interaction wins for many groups, why retain the other lenses? **Answer:** The specialized lenses distinguish the kind of coherence that the broad interaction lens often recognizes without separating classes.

## C7. A weak correlation is not biological orthogonality

**Where we are**

Structure–expression Results, page 7; Figure 7, page 8; Discussion, page 14.

**What the passage is doing**

Correlation summarizes how two quantities vary together. Nervous-system structure and expression separation have Pearson r = −0.29, p = 0.043. This is a modest negative tendency, explaining less than 10% of variance.

The paper reports robust negative directions under leave-one-out and alternative correlation calculations. It anchors uncertainty on the wider analytic 95% interval, [−0.53, −0.01], rather than the narrower percentile-bootstrap interval. The immune tendency is negative too, r = −0.26, but not significant, p = 0.29.

**In ordinary language**

The two scores tend to move in opposite directions, but the relationship is weak. A repeated direction is not the same as a precise effect size. The immune result does not provide a statistically confirmed correlation replication.

**Evidence status**

Reported correlations, sensitivity checks and uncertainty analysis. The mutual-exclusivity contingency tests are not significant in either system.

**Do not accidentally conclude**

The data do not establish statistical orthogonality, mutually exclusive biological categories or strong negative correlation. The central claim rests more on per-component diagnostics and class recovery.

**Try it**

Does “all leave-one-out estimates are negative” prove a large biological effect? **Answer:** No. It checks directional stability to deleting components, not effect magnitude, causal explanation or independent replication.

## C8. Withhold class labels and test whether the pattern returns

**Where we are**

Unsupervised recovery methods, page 4; Results, pages 8–9.

**What the passage is doing**

Unsupervised clustering groups components using their four-lens profiles without supplying their entity-class labels to the clustering algorithm. Adjusted Rand index, or ARI, compares the resulting groups with the curated classes while adjusting for chance agreement. It is not a percentage correct.

The paper reports ARI 0.25 for nervous components and 0.55 for immune components, both with label-permutation p < 0.001. Nervous recovery is weak-to-moderate in absolute terms. A grid of clustering methods and group counts checks dependence on that analytic choice.

**In ordinary language**

Hide the class names and group components by their data patterns. Then compare those groups with the known labels. Better-than-chance recovery is useful evidence, but it can still leave many classifications imperfect.

**Evidence status**

Reported label-withheld analysis, with expert-curated components still defining the objects being clustered. The specialized cell/family rule achieves 64% accuracy in the nervous map; that is a separate statistic from ARI.

**Do not accidentally conclude**

“Label-free” does not mean the starting gene groups were created without expert choices. ARI 0.25 is not 25% classification accuracy, and a small p-value is not near-perfect recovery.

**Try it**

Can highly significant class recovery still be weak-to-moderate? **Answer:** Yes. Significance compares with the null; the agreement statistic describes how much recovery was achieved.

## C9. Change the domain without changing the engine

**Where we are**

Immune and cardiac Results, pages 9–10; Figure 3, page 9.

**What the passage is doing**

The same engine runs on immune data using a different configuration and expression panel: 132 genes and 18 components. Its specialized cell/family rule classifies 11 of 12 applicable components correctly, or 92%. This denominator is not all immune components.

The cardiac demonstration has 64 genes and 11 components. It illustrates configuration-only reuse, but its mixed biological groupings make the map less tidy. Complement in immune data and mixed modules are also instructive exceptions.

**In ordinary language**

The same question can be asked in another organ system without rewriting the tool. The answer still depends on the chosen gene groups and the tissue data. A successful example is not a guarantee for every new set.

**Evidence status**

Reported cross-system demonstrations. The strongest class-recovery evidence concerns the nervous and immune maps; cardiac is a useful reach and reproducibility check.

**Do not accidentally conclude**

The 92% figure is not accuracy for all genes, all immune components or unseen clinical samples. A brain expression panel can miss peripheral systems; a mixed cell group can also fail to separate.

**Try it**

A retinal gene group looks flat in a brain expression panel. Does that prove it lacks a cell-type identity? **Answer:** No. The panel may not contain the relevant cells. Check coverage before interpreting a negative.

## C10. Agreement between sources is another level of analysis

**Where we are**

“Consilience matrix,” page 4; cross-modality Results and Figure 4, page 11.

**What the passage is doing**

Consilience here means agreement across sources. The modality-level analysis compares rankings of gene-pair similarities using Spearman correlation. This is different from asking which lens separates one named component.

The text reports a matrix across 20 modalities, summarized by a function/structure block around 0.40, disease/genetics around 0.30, and expression around 0.18–0.22. Between-block agreement is around 0.10–0.19. Figure 4 illustrates the block pattern; not every text-listed modality is individually labeled in the displayed panel.

**In ordinary language**

Two databases agree when they rank similar gene pairs in similar ways. Agreement can reveal shared information. It can also reflect overlapping evidence sources, so several agreeing databases are not automatically independent witnesses.

**Evidence status**

A supporting modality-level analysis with unequal, weak-to-modest blocks. The tested additions did not reveal a fourth organizing axis.

**Do not accidentally conclude**

The blocks are not three mathematically orthogonal sources, proof of independent evidence or a complete taxonomy of biological knowledge.

**Try it**

Why might a literature-derived lens agree with a database that includes text mining? **Answer:** They may partly reuse the same knowledge. Their agreement is not wholly independent validation.

## C11. Network demonstrations need matched comparison rules

**Where we are**

Connectome methods, pages 4–5; Figure 5 and Results, page 12.

**What the passage is doing**

A connectome is a network representation of neural connections. Density is the fraction of possible links retained. The small-world coefficient compares local clustering and path length with a random-graph reference. Modularity Q measures how strongly links concentrate within detected communities.

At density 0.0075, the core connectomes have approximate small-world coefficients of 7–18 and modularity 0.49–0.65. The paper emphasizes that these measures change with density. One macaque graph is excluded after fragmentation, and retained sparse graphs can also lose parts of their connected structure.

**In ordinary language**

Changing how many links you keep can change a network score. A fairer comparison uses the same stated density. Even then, different node counts, link meanings and broken-off parts can limit the comparison.

**Evidence status**

Supporting reproduction of known network properties across public datasets. It is not the paper's central biological discovery.

**Do not accidentally conclude**

Matched density does not match species, node meaning, measurement method or completeness. Similar graph scores do not establish equivalent brains or biological mechanisms.

**Try it**

Two connectomes have different modularity at very different densities. What should you check first? **Answer:** Whether link-retention rules and density explain the difference before attributing it to biology.

## C12. A good ranking can still produce a poor shortlist

**Where we are**

Literature-based discovery methods, page 5; Figure 6 and Results, page 13.

**What the passage is doing**

The paper builds a PubMed term co-occurrence graph from publications through 2015. It tests whether topology ranks pairs that first co-occur in 2016–2023. A co-occurrence is a recorded joint appearance, not proof of a biological relation.

ROC-AUC measures ranking discrimination across thresholds. The best reported method, resource allocation, has ROC-AUC about 0.90. But the task has only 230 positives among roughly 1.3 million candidates. Precision is the share of selected candidates that are positive; precision at the top 100 is about 1%. Precision–recall AUC is reported at about 14 times the tiny base rate.

**In ordinary language**

A method can rank real future links above many negatives and still offer a weak shortlist. That happens when positives are very rare. Read the top-list precision alongside the ranking score before calling the tool a discovery engine.

**Evidence status**

A dated retrospective forecasting benchmark with low top-of-list precision. The target is future literature co-occurrence, not experimental confirmation.

**Do not accidentally conclude**

ROC-AUC 0.90 does not mean 90% of proposed links are correct. These ranks narrow hypotheses; they do not confirm new biology or provide a high-yield experimental list.

**Try it**

Which number better answers “How many of my first 100 suggestions may be useful”: ROC-AUC or precision@100? **Answer:** Precision@100. The paper's approximately 1% directly addresses that shortlist, under its particular literature target.

## C13. Use the released tool without enlarging its claims

**Where we are**

Implementation, page 5; Discussion, pages 14–15; software and data availability, pages 15–16.

**What the passage is doing**

The package provides the four-lens engine, domain configurations and cached data. The paper reports offline immune and cardiac demonstrations; the nervous lens map and nulls are deposited precomputed results. Its connectome and literature-discovery analyses are separate scripts and derived deposits, not all packaged engine commands.

For current installation and reproduction instructions, use the maintained repository README. Later software maintenance does not alter the numerical findings of this exact draft.

**In ordinary language**

Use the tool to decide what evidence to examine next. First check identifiers, group definitions, missing data and the tissue panel. Then compare lenses and uncertainty. A promising result still needs the experiment or validation suited to the question.

**Evidence status**

Software scope, public-source provenance and practical interpretation. The source paper states code is open source and points to the OSF code/data deposit. This companion does not claim to have rerun every analysis.

**Do not accidentally conclude**

An association lens does not identify a causal drug target or prescribe an assay for every case. Some biological examples validate known facts. The tool's novelty does not make every recovered fact novel.

**Try it**

A gene group has interaction separation but no expression separation. What is a reasonable next step? **Answer:** Check tissue coverage and association evidence, then consider an appropriate functional validation. Do not treat the pattern as proof of a mechanism.

## Twelve questions to test transfer

Answer before consulting the key.

### Core questions

1. What does “recognizes a gene group” mean in this paper?
2. How is separation calculated, and what supplies the outside comparison?
3. What does the same-size permutation null contribute?
4. Why can a broadly successful interaction lens still be poor at distinguishing entity classes?

### Boundary questions

5. Does weak negative structure–expression correlation establish orthogonal biological categories?
6. Is ARI 0.25 a statement of 25% classification accuracy?
7. Does ROC-AUC 0.90 mean 90% of the first suggested literature links are correct?
8. Does a missing or low expression score prove that the group has no cell-type identity?

### Transfer questions

9. A new disease set is tested against a different atlas. Which parts of its separation comparison can change?
10. An expression panel omits the relevant tissue. How should the result affect an assay decision?
11. Several databases agree, but they reuse literature annotations. What qualification belongs in the interpretation?
12. An investigator compares connectome modularity across very different link densities. What should be checked before claiming a biological difference?

### Answer key and reasoning

1. Its genes have greater average similarity to each other than to outside atlas genes under a stated lens, evaluated against a null.
2. Within-component mean pair similarity minus component-to-outside mean similarity. The rest of the selected atlas supplies the outside comparison.
3. It indicates how unusual that score is relative to random atlas groups of the same size. It does not establish power or remove curation.
4. It can recognize many types of group without separating those types from one another. Structure and expression provide a more specific contrast here.
5. No. The effect is modest, the immune correlation is not significant, and the paper explicitly rejects statistical orthogonality.
6. No. ARI is chance-adjusted agreement between clusterings; accuracy is a different quantity with its own denominator.
7. No. The paper reports about 1% precision among the top 100 for the best method despite the strong ROC ranking score.
8. No. Missing tissue coverage, mixed groups and absent annotations can weaken the score.
9. The outside genes, annotation coverage and random-set reference can change. The score is conditional on that atlas and lens.
10. Treat the low score as limited evidence. Obtain or select a relevant panel before inferring that expression is the wrong view.
11. Agreement is partly dependent evidence; shared knowledge may explain some of it. Do not count every source as an independent confirmation.
12. Match and inspect link-retention rules and density, then examine fragmentation, node counts and link semantics. Matching density alone does not solve everything.

### One-sentence teach-back

State the lens-map question, its permutation-tested evidence, its main interpretation limit and one check needed before transferring it to a new gene set.

## Exact source

This companion follows the exact supplied PeerJ author-draft PDF. Its SHA-256 is:

3c03a781e459efc32025cfaae4922e45142cc16ffa0cd943ce190831dfc00885

The source's pages 17–19 contain the bibliography for its methods and public resources. The hypothetical Jaccard and separation calculations above are teaching examples, not additional measurements. All reported biological and benchmark numbers are attributed to the selected draft.
