# A complete reading companion to the consilience-engine paper

## How to use this document

This companion follows Patrick Iben's *Which data modality recognizes a gene set? A domain-agnostic consilience engine*, author draft dated 13 July 2026. It is for a numerate reader new to gene-set analysis. Work through its forty developed units in order, then use the glossary and answered transfer test. The preserved [concise study guide](STUDY_GUIDE.md) provides the shorter route.

The exact [source PDF](../manuscript/consilience_PeerJ_draft.pdf) has SHA-256 3c03a781e459efc32025cfaae4922e45142cc16ffa0cd943ce190831dfc00885. All page references refer to its nineteen pages. [Complete coverage](COMPLETE_COVERAGE.md) maps the source's methods, results, eight figures, limitations, declarations and reference roles. The source has unnumbered mathematical formulas rather than separately numbered equations or tables.

The question is which kind of data makes a named gene group distinctive. It is not a clinical prediction task. These boundaries remain in force throughout:

- Components are expert-curated. Withholding entity-class labels from clustering does not make the starting objects uncurated.
- The structure lens uses protein-domain annotations, not experimentally measured three-dimensional structures. STRING measures associations, not exclusively physical binding.
- Missing similarities become zero under the stated analysis policy; zero is not proof of biological absence.
- The structure–expression correlation is weak. Its immune counterpart is not individually significant. Neither establishes orthogonal biological categories.
- ARI is not accuracy. The 92% immune rule applies to twelve cell/family components, not all genes or all eighteen components.
- Literature co-occurrence is not experimental confirmation. High ROC-AUC does not imply a useful top-of-list precision.
- Known biological and network properties are supporting validation, not automatically new discoveries. Configuration reuse does not guarantee success for every domain.

Evidence labels distinguish **DEFINITION**, **ANALYTIC**, **MODELED_LOCKED** (specified resampling or modeling), **MEASURED_DATED** (analysis of public observations), **INTERPRETIVE** and **SCOPE**. They describe evidence roles, not a claim that every biological result is experimentally causal. Source checks are AI-assisted; full G14, human learning evaluation and independent full scientific reproduction are not certified.

## The question, the atlas and the four lenses

### C01. Read “recognizes” as a defined statistical question

**Where we are:** Title and Abstract, page 1; Introduction opening, page 2.

**What the passage is doing:** The paper asks which public-data modality makes a named gene group's members more similar to each other than to other genes in the selected atlas. A modality is a kind of evidence, such as expression or domain annotations. A component is a named gene group. A lens turns one modality into gene-pair similarities. Recognition here is measured separation relative to a random-group reference, not a database labeling a gene correctly or a clinician recognizing disease.

Worked reasoning: distinguish three objects before reading a result. Genes are the nodes. Components select subsets of those nodes. Lenses assign similarities to pairs of nodes. One component can then have four separation scores. Its biological label is not itself a similarity value. This organization permits the same question to be asked across domains, while keeping the answer dependent on atlas membership, annotation coverage and the chosen data representation.

The abstract's central promise is an instrument for comparing evidence types, not a universal law about all genes. The numerical findings later concern specific nervous, immune and cardiac atlases plus supporting demonstrations. A domain-agnostic implementation still needs suitable domain data and carefully defined groups.

**In ordinary language:** Ask what kind of evidence makes a group stand out. Shared protein parts may reveal a family. Shared activity across cells may reveal a cell type. Those are different ways to be coherent. The tool compares them using one stated question.

**Evidence status:** DEFINITION of the target question; SCOPE of the proposed tool. Empirical answers are supplied in later units.

**Do not accidentally conclude:** Recognition means diagnostic accuracy in patients, causal gene function, or that every group has one uniquely correct lens.

**Try it:** A group has high interaction separation and low expression separation. Has the tool shown that its genes are inactive? **Answer:** No. It shows a contrast under particular similarities and an expression panel. Coverage, tissue choice and group composition must be checked before interpreting the low score.

### C02. Complementarity differs from fusing data into one prediction

**Where we are:** Introduction, page 2; integration references, pages 17–18.

**What the passage is doing:** The paper contrasts its question with multi-omics integration and gene-network fusion. It names MOFA, similarity network fusion, mixOmics/DIABLO, GeneMANIA and GIANT as related approaches with different outputs. Some combine sample-level data to improve prediction or find shared variation; others combine gene networks to predict function or membership. This study retains a separate similarity graph per modality and asks which graph is diagnostic for an entity class.

Worked reasoning: imagine a workflow that returns a single combined ranking and another that returns a profile of four scores. The combined ranking may help identify new members. The profile may help explain whether an existing group coheres through cell identity, molecular family or functional association. Neither output replaces the other. A gain in combined prediction does not tell you which individual source distinguishes the kind of entity, and a clean profile does not automatically outperform an integrated predictor.

The word “complementary” is therefore important. It does not mean the data are statistically independent or mathematically orthogonal. Sources can overlap and still answer different practical questions. The later modality matrix explicitly measures nonzero agreement rather than perfect separation among sources.

**In ordinary language:** Combining several views can help you predict. Keeping them apart can help you understand which view carries the useful distinction. This paper asks the second question. It does not show that combining data is a mistake.

**Evidence status:** INTERPRETIVE methodological positioning, supported by the cited methods' stated roles. The companion is not an independent exhaustive priority review of integration software.

**Do not accidentally conclude:** All integration assumes complete redundancy, or consilience-engine competes on the same benchmark with every named integration method. The source positions the lines of work as complementary rather than reporting such a contest.

**Try it:** If a fused network predicts membership well, has it answered which modality makes families distinct from cell types? **Answer:** Not by that result alone. The diagnostic-modality question requires keeping source-specific evidence visible and evaluating its relation to the entity classes.

### C03. The novelty claim is about the instrument and its diagnostic map

**Where we are:** Introduction contribution statement, page 3; Discussion and Conclusions, pages 14–15.

**What the passage is doing:** The source distinguishes known facts from its claimed contributions. Glial expression signatures, shared receptor domains and small-world connectomes are not presented as newly discovered biology. The proposed additions are the reusable keyless engine, a per-component diagnostic lens-map, class recovery with labels withheld and cross-system demonstrations. Supporting connectome and modality-matrix analyses illustrate reach. The dated literature task explores a route toward forward hypothesis generation.

Worked reasoning: validation can recover a known pattern without making that pattern novel. If a new instrument identifies a well-established property, the result helps show the instrument behaves sensibly. A stronger claim about new biological organization needs the specific analysis and uncertainty supporting it. The paper anchors that claim primarily on component-level diagnostics and unsupervised recovery, rather than its weak across-component correlation.

This distinction also protects practical use. A tool can be useful because it makes a repeatable question inexpensive and comparable across groups. It need not claim that every output is a new discovery. Conversely, broad reproducibility or novelty language does not remove the need to inspect curation, dependent sources and assay coverage.

**In ordinary language:** A new measuring tool can be valuable even when it first measures familiar things. The familiar results help check the tool. The paper's main claim concerns a repeatable way to compare evidence types and recover classes, not the discovery that receptors share parts.

**Evidence status:** INTERPRETIVE contribution statement and SCOPE. The empirical support is examined in later units; priority claims are attributed to the source.

**Do not accidentally conclude:** Every reproduced fact is novel, or that a useful tool must prove a universal biological taxonomy. Its operational labeling and selected atlases limit the inference.

**Try it:** Why does the companion repeatedly call the connectome work supporting? **Answer:** The source explicitly says it reproduces a known property. Its value is demonstrating a common graph-based workflow with stated caveats, not establishing a new law about nervous systems.

### C04. Atlas construction fixes what can be compared

**Where we are:** “Gene sets and components,” page 3; Data availability, page 16.

**What the passage is doing:** Human gene symbols are resolved through MyGene.info to Entrez and Ensembl identifiers. The nervous atlas contains 410 genes in 49 components and was expanded over four rounds. It spans transmitter systems, glia, vascular/ependymal cells, excitability, synaptic/plasticity machinery, sensory/developmental systems and disease modules. The immune atlas has 132 genes in 18 components. These are curated analysis universes, not random samples of all possible human gene groups.

Worked reasoning: identifier resolution occurs before similarities and separation. Two names referring to one gene must not accidentally become two independent nodes. An unresolved identifier can remove evidence or produce missing similarities. A component's outside comparison is also the rest of this atlas, so changing atlas membership can change separation even when the component itself is unchanged. The universe is part of the estimand.

The immune configuration includes cell types such as T, B, NK and myeloid groups, families such as Toll-like receptors and MHC, and functional modules such as antigen processing or IFN response. These categories help pose the diagnostic test; they do not enumerate all biological knowledge. The cardiac demonstration is a third configured set rather than an additional random validation sample drawn from a common population.

**In ordinary language:** First decide which genes and groups are in the study, and make their names consistent. The rest of the atlas supplies the comparison. A score therefore describes a group within that chosen collection, not against every possible gene set.

**Evidence status:** DEFINITION and MEASURED_DATED curation/provenance. No new identifier audit or complete atlas reassembly was performed for this guide.

**Do not accidentally conclude:** A large number of components removes expert selection, or each component is an independent randomly sampled biological unit.

**Try it:** If the same receptor group is placed in a much different atlas, can its separation change? **Answer:** Yes. Its internal similarities may remain the same, but its outside comparison and random-group null can change. Record the atlas along with the lens and component.

### C05. Labels can be withheld while curation still matters

**Where we are:** Component-method statement, page 3; unsupervised methods, page 4; curation limitations, pages 14–15.

**What the passage is doing:** The source says component membership is used as ground-truth labels, never to construct similarities. Later clustering withholds entity-class labels from the algorithm. These are important safeguards against directly building the desired classes into the pairwise data. They do not make component definitions neutral or remove dependence caused by shared genes, related biological concepts and overlapping source knowledge.

Worked reasoning: there are two distinct labels. Membership tells which genes form each component, and is needed to calculate its separation. Entity class tells whether that component is called a cell type, family or module, and is withheld during clustering. Confusing these levels creates the mistaken claim that the analysis never uses curated group information. It does: curated groups define the objects whose profiles are clustered.

The paper also operationalizes “molecular family” through protein-domain architecture. Some transmitter-system groups are functional rather than strict sequence families. Accuracy under these labels is therefore tied to that operational scheme. Disagreement can reflect a mixed object rather than simply an incompetent lens. The dual-character examples later make that issue visible.

**In ordinary language:** Hiding class names from a grouping algorithm is a useful test. But someone still chose the gene groups being grouped. Keep both facts in view. A label-free calculation at one stage does not make the whole study free of expert choices.

**Evidence status:** DEFINITION of analysis stages; SCOPE for circularity and dependence. The source reports an adversarial audit; this companion does not treat that report as a new independent audit.

**Do not accidentally conclude:** Unsupervised means no prior biological information entered anywhere, or that significant class recovery proves a unique natural classification.

**Try it:** Which information must remain available to compute a component's separation? **Answer:** Its gene membership. Which labels can be withheld from clustering? Its entity-class designation. Preserving that distinction explains both the safeguard and its limit.

### C06. The structure lens measures shared annotated domains

**Where we are:** “Lenses,” page 3; Figure 1, page 5; family results, page 7.

**What the passage is doing:** The structure lens takes InterPro domain accessions from reviewed human UniProt entries and compares genes using Jaccard similarity. For annotation sets A and B, Jaccard is the number of shared items divided by the number of distinct items in their union. The resulting graph measures shared annotated protein parts. Calling the lens “structure” does not mean the paper predicts or measures full three-dimensional protein folds.

Worked reasoning: use an explicitly hypothetical annotation example. One gene has {X,Y}, another {Y,Z}. They share one item and have three distinct items overall, so Jaccard = 1/3. The labels X, Y and Z are teaching placeholders, not actual domain records. A high value can arise from sharing many annotated domains; a low value can reflect different architectures, incomplete annotations or the particular representation chosen.

The lens is especially suited to testing molecular-family coherence because the source defines that entity class partly through domain architecture. That alignment is scientifically interpretable but must stay visible in discussions of curation and circularity. Similarities are retrieved independently of component labels, yet the label “family” has a relationship to what the lens measures.

**In ordinary language:** Compare the lists of protein parts. Two genes look similar in this view when their proteins share many listed parts. This can reveal a family. It does not show that the proteins have identical shapes, activities or roles in every cell.

**Evidence status:** DEFINITION of a representation and similarity; MEASURED_DATED annotations. The set arithmetic is hypothetical and analytically verified.

**Do not accidentally conclude:** A zero means no shared biology, or a high score establishes identical folded structures or direct interaction.

**Try it:** Would two genes expressed in the same cell necessarily have high domain Jaccard similarity? **Answer:** No. Cell identity can combine proteins with different architectures. That is one reason an expression lens can reveal coherence that the domain lens misses.

### C07. The expression lens depends on the cell panel and transformation

**Where we are:** “Lenses,” page 3; nervous and immune results, pages 7 and 9; limitations, page 15.

**What the passage is doing:** Expression uses Human Protein Atlas cell-type RNA profiles. The nervous analysis selects brain single-nucleus nCPM; the immune analysis selects blood-cell nTPM. The values undergo log1p transformation, meaning log(1+x), before cosine similarity compares profile directions. The method therefore concerns relative expression patterns across a selected panel, not a universal binary statement that a gene is expressed or unexpressed.

Worked reasoning: cosine similarity asks whether profiles point in similar directions in the feature space. Multiplying every entry of a profile by the same positive factor does not change its direction before other processing. The log transform, however, changes relative spacing and reduces the dominance of very large entries. Those choices affect which similarities emerge. A panel missing the relevant cell population cannot fully represent that group's expression identity.

This is why the tissue field belongs in the configuration and provenance. Using the same engine on immune data requires an appropriate blood panel, not merely replacing the component names while retaining brain measurements. It is also why peripheral systems can appear flat in the nervous atlas without lacking biological identity.

**In ordinary language:** Compare where genes are active across the cells you measured. Genes that rise and fall across the same cells can look alike in this view. If the right cells are missing, a low score may tell you more about the panel than the gene group.

**Evidence status:** DEFINITION of transformation/similarity; MEASURED_DATED public expression profiles; SCOPE for panel coverage.

**Do not accidentally conclude:** Low expression separation proves inactivity or absence of a cell type, or that brain nCPM and blood nTPM are interchangeable raw measurements.

**Try it:** A retinal component looks unremarkable in a brain panel. What should you check before choosing another assay? **Answer:** Whether the relevant retinal cells are represented and adequately measured. A panel mismatch is a coverage problem, not evidence that expression cannot define that group.

### C08. STRING's interaction lens aggregates association evidence

**Where we are:** “Lenses,” page 3; STRING interpretation, pages 7 and 9; overlap limitations, pages 14–15.

**What the passage is doing:** The interaction lens uses STRING v12 combined scores, scaled to 0–1, for within-atlas gene pairs. The source describes one network call for the selected set. A combined association score can draw on several evidence channels, including knowledge-based and text-mining information. It is not restricted to direct physical binding between the two proteins. Later results show high separation for many component types, making STRING a broad detector but a weak partitioner of those types.

Worked reasoning: two proteins can belong to a related process without binding each other in a particular cell. A database association can capture that relation. It may help a functional module separate even when its members have different domains and expression profiles. The same breadth can also make the lens succeed for cells and families, reducing its ability to tell those categories apart.

The score's numerical range is not a guarantee of biological certainty for each pair. Its interpretation belongs to the source database and evidence channels. Shared literature or curation can also make agreement with another knowledge-derived lens partly dependent. Counting each agreeing source as a wholly independent validation would exaggerate support.

**In ordinary language:** This view asks whether genes are linked by the database's combined evidence. That is broader than asking whether two proteins physically touch. It can recognize many kinds of group. A view that recognizes almost everything may not tell you what kind of group it is.

**Evidence status:** DEFINITION and MEASURED_DATED database evidence. Biological mechanism and direct binding are not established by a high combined score alone.

**Do not accidentally conclude:** Interaction means physical contact, the strongest score is always the most specific diagnostic, or database agreement supplies independent experimental replication.

**Try it:** Why might a process module be strong in STRING but flat in domain similarity? **Answer:** Working together does not require sharing protein architecture. Functional association and molecular family are different forms of coherence.

### C09. The process lens uses ontology-term overlap

**Where we are:** “Lenses,” page 3; Figure 1, page 5; multimodality discussion, pages 11 and 14–15.

**What the passage is doing:** The fourth lens represents each gene through Gene Ontology biological-process term identifiers retrieved through MyGene.info and computes Jaccard overlap. It asks about shared recorded process annotations, not RNA profile shape or protein-domain architecture. Although the central diagnostic contrast emphasizes structure and expression, the process lens remains part of each four-lens profile and of the engine's generic representation strategy.

Worked reasoning: Jaccard has the same set operation as the structure lens, but the items in the sets differ. Shared domain accessions and shared process identifiers therefore have different biological meanings even if their similarity values happen to match. A common mathematical formula does not make two evidence sources equivalent. Nor does a small overlap prove two genes never participate in the same process: annotation coverage and term choices matter.

Ontologies organize terms with relationships, but the printed method here specifies term-identifier Jaccard. This companion does not silently replace it with semantic similarity, ancestor weighting or an enrichment test. Such alternatives may be useful, but they would change the representation being taught. The source's exact operational definition is the relevant starting point.

**In ordinary language:** Compare the lists of biological jobs assigned to genes. Sharing listed jobs can make genes look similar in this view. That is different from sharing protein parts or being active in the same cells. Missing entries can also make the lists look less alike.

**Evidence status:** DEFINITION of an annotation-based lens; MEASURED_DATED public annotations; SCOPE for missingness and representation.

**Do not accidentally conclude:** A process score is experimental proof that genes act together, or that every sophisticated ontology relation was used in the printed method.

**Try it:** If domain Jaccard and process Jaccard both equal 1/3 in an illustration, are they the same evidence? **Answer:** No. Their arithmetic matches, but one compares protein parts and the other compares recorded biological-process terms. Interpretation follows the represented items, not just the number.

### C10. Separation compares within-group and outside-group similarity

**Where we are:** “Separation and null,” page 3; Figure 1, page 5.

**What the passage is doing:** For a component g within atlas C, separation is mean similarity over distinct internal pairs i<j in g, minus mean similarity between a member i in g and a gene j outside g. Each lens supplies s(i,j). The internal mean asks about coherence; the external mean asks about specificity relative to this atlas. Separation is not simply mean edge weight or the number of connected pairs. The source sets missing pairs to zero, a policy examined next.

Worked reasoning: explicitly hypothetical means of 0.8 inside and 0.2 outside give separation 0.6. The arithmetic illustrates subtraction, not a measured component. A coherent group could still have low separation if its members are just as similar to outside genes. Conversely, a modest internal similarity can be distinctive if outside similarities are much smaller. Both terms are needed to understand the score.

Pair averaging also means group size and atlas composition matter. Internal unordered pairs and between-group pairs are different collections. The formula does not turn each pair into an independent biological replicate. Shared genes and shared annotation structures couple many values, which matters for null testing and the later dependence discussion.

**In ordinary language:** Ask two questions: do the group's genes resemble one another, and do they resemble outsiders just as much? Subtract the second average from the first. A high difference means the group stands out in that view, within the chosen atlas.

**Evidence status:** DEFINITION of the statistic; ANALYTIC hypothetical subtraction. Empirical significance requires the size-matched null, not the raw score alone.

**Do not accidentally conclude:** A separation of 0.6 means 60% classification accuracy, or that a high raw score has the same evidential strength for every group size.

**Try it:** A group has high internal similarity but equally high similarity to outsiders. Is it distinctive? **Answer:** Not under this score: the difference is near zero. The lens sees broad resemblance rather than a boundary around that particular component.

## Testing separation and extending the graph methods

### C11. The outside atlas and missing-pair policy belong to the estimand

**Where we are:** Separation formula, page 3; limitations, pages 14–15.

**What the passage is doing:** The separation contrast uses outsiders from the selected atlas, with missing pair similarities set to zero. This makes the calculation reproducible but merges two possibilities numerically: a genuinely low observed similarity and an unavailable similarity. The source also notes that expression panels can miss relevant biology and that mixed components may fail to separate. Those limitations affect how a negative result should guide further work.

Worked reasoning: hold a component's internal similarities fixed and change only the outside genes. If the new outsiders share more domains with the component, the outside mean rises and separation falls. The biological component did not change. The comparison target changed. Similarly, missing data concentrated inside a group can reduce its apparent coherence, while missing outside values can reduce the comparison mean. The direction of a missingness effect is not automatically the same in every case.

Zero imputation is therefore an operational policy, not a declaration that all unrecorded pairs are biologically unrelated. A careful report includes identifier resolution, source coverage, tissue field and atlas composition alongside the score. The paper's generic instrument can help flag questions, but its output cannot repair missing source evidence by arithmetic.

**In ordinary language:** A score is only as informative as the comparison and data behind it. Missing links count as zero in this calculation. That keeps the rule simple, but a zero can mean “not recorded.” Check what is missing before treating a low result as a biological absence.

**Evidence status:** DEFINITION and SCOPE. The missingness reasoning explains the formula's consequences; it adds no measured sensitivity experiment.

**Do not accidentally conclude:** Keyless public access guarantees complete data, or using the same formula makes all domains equally well observed.

**Try it:** A group loses separation after many outside genes are added. Must its internal biology have changed? **Answer:** No. The between-group reference changed. Compare both means and coverage before interpreting the change as a new biological finding.

### C12. Size-matched random sets define the permutation reference

**Where we are:** “Separation and null,” page 3; fixed-seed and budget statements, page 4.

**What the passage is doing:** For each component and lens, the engine draws 2,000 random gene sets of the same size from the atlas. It compares observed separation with that null distribution, reporting z = (observed−null mean)/null standard deviation and an empirical p value. The z-score states distance in null standard deviations; the p value measures tail extremeness under the stated random-group reference. Neither is a probability that a biological interpretation is true.

Worked reasoning: a large group has many pairs and can have different null variability from a small group. Matching group size therefore addresses a basic difference in the reference distribution. It does not remove the effects of expert curation, overlapping components or every annotation pattern. The random sets answer “unusual relative to size-matched atlas groups,” not “validated against all plausible biological alternatives.”

The PDF does not specify every finite-sample p-value convention in the printed formula. This companion does not invent a plus-one correction, tail rule or zero-variance handling and present it as the source's implementation. Those details should be checked in the maintained code when reproducing the computation. A degenerate null would require explicit handling, not a fabricated infinite certainty.

**In ordinary language:** Compare a named group with random groups of the same size. That shows whether its distinctiveness is unusual under this reference. The comparison gives the score context. It does not prove that the chosen biological label is the only explanation.

**Evidence status:** DEFINITION of the null and z statistic; MODELED_LOCKED finite randomization; empirical interpretation conditional on the atlas.

**Do not accidentally conclude:** A large z is a percentage effect, a biological importance ranking or evidence independent of group size and annotation coverage.

**Try it:** Why not compare every component with one common distribution of differently sized groups? **Answer:** Size changes pair structure and null variability. A mismatched reference would mix the biological question with a size effect that the stated method intentionally controls.

### C13. Figure 8 checks false-alarm calibration, not detection power

**Where we are:** Calibration methods, pages 3–4; Figure 8 and caption, page 8.

**What the passage is doing:** The calibration experiment applies the permutation procedure to 400 random true-null gene sets spanning sizes 6, 8 and 12. Their p values are approximately uniform by the reported Kolmogorov–Smirnov comparison, p = 0.59. The observed false-positive rate is 0.045 at alpha 0.05. This checks whether the procedure manufactures too many positives under its constructed null. It does not show how often weak real signals would be found.

Worked reasoning: false-positive rate is the share of null cases called significant. Power is the share of specified non-null cases detected. A method can have a sensible false-alarm rate and still miss many real but subtle effects. The calibration's random gene sets also do not reproduce every dependence and selection feature of curated biological groups. The source explicitly limits the calibration claim to Type-I control.

The figure's distribution view and its numerical summary should be read together. A non-small uniformity-test p value is not proof of exact uniformity; it reports no detected discrepancy under that test and sample. The rate 0.045 is an estimate with finite Monte-Carlo variability, quantified in the next statistical units. It should not be promoted to an exact universal operating characteristic.

**In ordinary language:** Give the test groups that should have no special signal and count its false alarms. Here that count is near the intended level. This is reassuring. It does not tell you how well the tool will find a faint real pattern or fix biased group choices.

**Evidence status:** MODELED_LOCKED calibration experiment on random sets; SCOPE for what it establishes. No new calibration was run for the companion.

**Do not accidentally conclude:** p = 0.59 proves the entire engine is correct, or a 4.5% false-alarm rate means 95.5% of selected biological findings are true.

**Try it:** What additional experiment would address sensitivity? **Answer:** A specified non-null or positive-control design with known signal strength and a detection-rate analysis. Calibration under a true null alone cannot supply that answer.

### C14. Multiple testing and the strong-pattern cutoff are separate decisions

**Where we are:** Multiple-testing methods, page 4; neuronal exceptions and best-lens results, page 7.

**What the passage is doing:** Many components are tested across four lenses. The source reports per-component best-lens significance after Benjamini–Yekutieli false-discovery-rate control, chosen because shared comparisons and correlated lenses create dependence. All 49 nervous components survive the reported correction, with best-lens permutation p values at most 0.008. Separately, z ≥ 4 defines the strong per-class pattern discussed in the results. A component can meet one criterion without meeting the other.

Worked reasoning: FDR concerns the expected false-discovery share among selected findings under a procedure's assumptions. A z cutoff is a descriptive strength rule on a null-standardized score. They are not interchangeable labels for the same decision. Cerebellar neurons have expression z = 3.7 and p = 0.008: significant in the report, but below the z ≥ 4 pattern threshold. Spinal-motor neurons have an expression null and route instead to interaction.

This distinction prevents an apparent contradiction. “Every component has a significant best lens” does not claim that every component has significant expression separation or that every class follows one specialized-lens rule. The best lens can differ across components, and the result includes meaningful exceptions.

**In ordinary language:** A statistical finding can pass one decision rule and miss a stronger display rule. Keep the rules named. “Significant somewhere” is not the same as “strong in every view,” and an exception need not disappear from the report.

**Evidence status:** Reported MODELED_LOCKED permutation inference and DEFINITION of the descriptive cutoff. This guide has not independently recomputed the adjusted p values.

**Do not accidentally conclude:** FDR is the probability that each selected result is false, or all 49 groups satisfy the same expression pattern.

**Try it:** Is cerebellar expression z = 3.7 evidence that the multiple-testing report failed? **Answer:** No. Its significance and the z ≥ 4 pattern criterion are different. The correct explanation preserves both instead of changing either number.

### C15. Random-draw budgets and Monte-Carlo error must not be pooled

**Where we are:** Statistical-budget paragraph, page 4.

**What the passage is doing:** Main component nulls use 2,000 random sets. The calibration uses 1,000 draws for each of 400 null groups. ARI tests use 5,000 label permutations. All use fixed generator seed 1. The source gives Monte-Carlo standard error for the estimated false-positive rate: sqrt(0.045×0.955/400) ≈ 0.010. The observed rate is therefore about half one such standard error from 0.05. These budgets describe different random experiments.

Worked reasoning: changing a random seed can move an estimated tail probability even when the underlying data remain identical. More draws can reduce that numerical uncertainty. They do not add biological samples, repair biased curation or make a weak correlation precise. The Pearson r p value is analytic, so it has no random-draw error from this resampling budget; it still has sampling uncertainty and design limitations.

The source says reported p values lie more than two Monte-Carlo standard errors from their reporting thresholds. That is an attributed finite-draw check, not a complete guarantee against all analytic-selection or multiple-testing uncertainty. A code reproduction should preserve which budget belongs to which test, rather than assuming the largest number of permutations was used everywhere.

**In ordinary language:** Randomized calculations have their own numerical noise. More random draws can make the calculation steadier. They do not create more independent biology. Keep that uncertainty separate from the uncertainty in the data and the choices used to build the groups.

**Evidence status:** ANALYTIC standard-error calculation and MODELED_LOCKED resampling procedures; SCOPE for what fixed seeds provide.

**Do not accidentally conclude:** A fixed seed proves robustness, or the 5,000 ARI permutations were used for every component's separation test.

**Try it:** Which denominator gives the reported calibration-rate standard error? **Answer:** The 400 tested null groups, not the 1,000 permutations within each group's p-value calculation. Those are two different levels of repetition.

### C16. ARI compares clusterings without being a percentage correct

**Where we are:** “Unsupervised class recovery,” page 4; class-recovery results, pages 8–9.

**What the passage is doing:** Components are clustered by z-scored four-lens separation profiles while entity-class labels are withheld. Adjusted Rand index, ARI, compares the resulting grouping with the curated classes while adjusting for chance agreement. The reported nervous and immune values are evaluated against 5,000 label permutations. This asks whether evidence profiles recover a class pattern above the stated null; it is not a per-gene classification-accuracy calculation.

Worked reasoning: cluster labels themselves are arbitrary names. A cluster called A could match a curated class called family without sharing its label. A grouping comparison should assess which pairs of objects are placed together, rather than whether the arbitrary names match. ARI is designed for that type of comparison. Its magnitude and its null p value answer different questions: amount of agreement versus evidence against random-label agreement.

Withholding labels is meaningful because the clustering algorithm cannot directly use the desired class assignment. But it still sees profiles computed for expert-defined components. Those profiles depend on the selected genes, atlas and lenses. This is a control against one form of circularity, not proof that the starting biological categories were discovered without prior knowledge.

**In ordinary language:** Hide the class names and group the components by their evidence patterns. Then compare the groups with the known classes. Better-than-chance agreement is informative. It can still be far from perfect, and the comparison is not an accuracy percentage.

**Evidence status:** DEFINITION of an agreement statistic; MODELED_LOCKED clustering/null analysis built on MEASURED_DATED similarities.

**Do not accidentally conclude:** ARI 0.25 means 25% correct, or a very small p value means near-perfect classification.

**Try it:** Can a modest ARI be highly significant? **Answer:** Yes. It can be reliably larger than the null while still indicating limited absolute recovery. Both the statistic's magnitude and its uncertainty or null comparison should be reported.

### C17. The clustering-method grid probes analytic choice

**Where we are:** Unsupervised methods, page 4; method-invariance results, page 9.

**What the passage is doing:** The source treats the clustering algorithm as a consequential analytic choice. It evaluates k-means, Ward agglomerative, average agglomerative and Gaussian-mixture clustering at k = 2, 3 and 4. The published k = 3 result is not the only tested solution. The deposited method_invariance.json records the grid so readers can inspect dependence on method and requested number of groups.

Worked reasoning: changing k changes the question about how many clusters to form. Even with the same profiles, different algorithms impose different shapes or linkage rules. A stable scientific pattern should not be sold solely through one favorable pick without acknowledging alternatives. At the same time, a grid is not a proof that all conceivable choices work. Its coverage is the declared methods and settings.

The results later summarize k = 3 or 4 cells: eight of eight significant for nervous profiles, seven of eight for immune profiles, with one average-linkage miss at k = 3. The source's phrase about k matching a three-class structure should be interpreted alongside those explicitly reported k values, not turned into an assertion that four literally equals three. This companion preserves the concrete tested settings.

**In ordinary language:** Try more than one reasonable way to form groups. If the pattern survives, confidence increases that it is not just one convenient setting. Still show the misses and say which settings were tested. A grid is a robustness check, not unlimited proof.

**Evidence status:** MODELED_LOCKED method-sensitivity analysis; SCOPE for the finite grid. No new clustering results are introduced here.

**Do not accidentally conclude:** Every grid cell is significant, including all k = 2 cases, or that the algorithms are mathematically equivalent.

**Try it:** Why keep an unsuccessful average-linkage cell visible? **Answer:** It tells readers where the result depends on analysis choice and prevents the multiverse from becoming a selection device that reports only favorable methods.

### C18. The consilience matrix changes the level of analysis

**Where we are:** “Consilience matrix,” page 4; Figure 4 and results, page 11.

**What the passage is doing:** Rather than scoring a component, the consilience matrix compares modalities. For each pair of modalities, it computes Spearman correlation over shared gene-pair similarity values. Spearman compares ranks and is threshold-independent here. Within- and between-block averages summarize source agreement. The text describes twenty gene-keyed modalities, including literature, STRING, pharmacology, genetics/disease, expression, pathways, proteomics, domains, phenotype, co-essentiality and constraint.

Worked reasoning: a component-level lens-map asks which similarity makes one group distinctive. A modality correlation asks whether two sources rank shared pairs similarly across a collection of pairs. Those are different denominators and questions. Similar source rankings can coexist with different usefulness for a particular component. Shared-pair coverage can also vary by modality pair, limiting simple comparisons across matrix cells.

Correlation is not independence testing. Agreement can reflect related biology, shared annotations or overlapping evidence channels. Conversely, weak correlation need not prove two sources represent fundamentally separate causal mechanisms. The printed method does not fit a latent-factor model proving three independent axes; it summarizes blocks in a similarity-correlation matrix.

**In ordinary language:** Ask whether two databases rank gene pairs in similar ways. That tells you how their recorded information agrees. It is a different question from which database makes one named group stand out. Agreement can also come from reusing some of the same knowledge.

**Evidence status:** DEFINITION of a modality-level statistic; MEASURED_DATED source comparisons. Block interpretation is INTERPRETIVE.

**Do not accidentally conclude:** The matrix proves independent witnesses, orthogonal biological dimensions or the same number of axes for every possible resource collection.

**Try it:** Why use shared pairs? **Answer:** A correlation needs matched observations. If one source has no value for a pair, that pair cannot directly supply a comparable rank under this stated matrix method. Coverage therefore belongs in interpreting agreement.

### C19. Connectome construction introduces different nodes and edge meanings

**Where we are:** Connectome methods, pages 4–5; Figure 5 and results, page 12.

**What the passage is doing:** The supporting network demonstration assembles public connectomes from several repositories: openworm/ConnectomeToolbox, Janelia hemibrain, Netzschleuder, Allen Mouse Connectivity Atlas, Network Data Repository and the Budapest reference connectome. These cover different species, developmental stages, spatial scales and measurement techniques. A connectome graph represents neural connections, but its nodes and edges are not defined identically across these datasets.

Worked reasoning: a neuron-level wiring graph and a region-level projection graph can both be networks without having equivalent edges. Binarizing and matching density harmonize selected mathematical properties, not the biological measurement process. Likewise, two datasets from different developmental stages are not two species. The source describes seven core datasets across six species, including two Drosophila stages, and three phyla.

The Allen graph is rebuilt at 316 summary structures from the complete projection-unionize population. Later limitations disclose a truncated-data bug fixed during development. This matters because a successful API response is not necessarily a complete dataset. The exact endpoint population and pagination or row limits belong to the reconstruction recipe, rather than treating a downloaded table as automatically exhaustive.

**In ordinary language:** A wiring diagram can describe cells, brain regions or measured pathways. Similar graph formulas can be applied to each, but their links do not mean exactly the same thing. Keep the source and scale visible before comparing the scores.

**Evidence status:** MEASURED_DATED public network inputs; SCOPE for cross-species comparability. This is supporting reproduction, not new biological discovery.

**Do not accidentally conclude:** Every graph is a complete brain at the same resolution, or a matched numerical density makes species and measurement methods equivalent.

**Try it:** Why might a region-level graph and a neuron-level graph have different modularity even after density matching? **Answer:** Node definition, resolution, edge semantics, completeness and network size can differ. Matching one statistic does not remove those differences.

### C20. The small-world coefficient is a normalized graph summary

**Where we are:** Connectome formula, page 4; Figure 5a and result caveats, page 12.

**What the passage is doing:** The source defines small-world coefficient σ = (C/C_rand)/(L/L_rand). C is mean clustering and L is mean shortest-path length, with path length sampled for large graphs. Random-reference quantities use Erdős–Rényi expectations. The ratio summarizes relatively high local clustering with relatively short global paths compared with that reference. It is not a direct measure of intelligence, efficiency in every task or causal function.

Worked reasoning: the numerator and denominator each compare an observed graph summary with its reference. A high σ can arise from large relative clustering, small relative path length or both. Changing edge retention changes triangles, connectivity and path lengths, so density can strongly affect the score. Disconnected components also complicate path calculations: which nodes remain connected and how unreachable pairs are treated matter to interpretation.

The selected PDF supplies the formula and broad implementation description, not every line of path-length handling. This companion therefore explains the stated statistic without inventing an unprinted disconnected-graph convention. The result section itself acknowledges fragmentation and lack of an additional null model beyond σ's normalization.

**In ordinary language:** Compare local clumping and travel distance with a simple random-network reference. A high score says the graph has a particular mix of those features under that comparison. It does not mean every part is connected or that the network is optimal for every job.

**Evidence status:** DEFINITION of a standard graph statistic; MEASURED_DATED application to processed networks; SCOPE for reference and connectivity choices.

**Do not accidentally conclude:** σ alone proves a shared biological mechanism or that a sparse, fragmented graph is fully comparable with an intact one.

**Try it:** If keeping fewer edges changes σ, is that necessarily a biological discovery? **Answer:** No. It may be a consequence of the graph-processing rule. Inspect the density sweep and connectivity before attributing the change to biology.

### C21. Modularity and density matching do not erase fragmentation

**Where we are:** Connectome methods, pages 4–5; Figure 5a–b and caveats, page 12.

**What the passage is doing:** Modularity Q summarizes how strongly a graph's edges concentrate within detected communities relative to its model reference. The source uses greedy/Louvain community detection. Graphs are binarized, and density matching retains top-weight edges to a target density. Density is the fraction of possible links retained. Matching it aims to avoid attributing a processing-induced difference in Q or σ to biology.

Worked reasoning: the same underlying weighted network can yield different binary graphs as the retention threshold changes. Removing weak edges may sharpen apparent communities, disconnect small groups or remove bridging routes. A higher Q after thinning is therefore not automatically stronger biological organization. The method must state the retained density and inspect the resulting connectivity, not merely compare final numbers.

A common target density also does not imply a common mean degree when node counts differ. A fixed fraction of possible edges can leave a small graph especially sparse. This helps explain why some graphs fragment under matched-density thinning. The source excludes one macaque graph at the chosen density and retains other graphs with explicit giant-component caveats. Those decisions matter to what the reported cross-species band represents.

**In ordinary language:** Keep a stated share of the strongest links before comparing graphs. That makes one part of the comparison more consistent. It can also break a sparse graph apart. Check what remains connected, and do not treat matching one number as matching the whole measurement.

**Evidence status:** DEFINITION of graph processing and modularity; MEASURED_DATED processed-network comparisons; SCOPE for comparability.

**Do not accidentally conclude:** Louvain finds the unique biological communities, density matching preserves every original relationship, or excluded fragmentation is a biological absence of organization.

**Try it:** Two matched-density graphs have different node counts. Must they have equal average degree? **Answer:** No. The number of possible neighbors depends on node count. Equal density matches a fraction, not every graph property, and sparse connectivity still requires inspection.

### C22. The literature benchmark separates training history from future labels

**Where we are:** “Literature-based discovery,” page 5; Figure 6 and results, page 13.

**What the passage is doing:** PubMed MeSH term co-occurrence graphs are built from papers published through 2015. Candidate term pairs are evaluated against first co-occurrence during 2016–2023. Generic check-tag MeSH terms are excluded. Common-neighbor, Adamic–Adar and resource-allocation link predictors use graph structure from the earlier period. A co-occurrence is a recorded joint appearance in literature, not proof of a biological interaction or clinical effect.

Worked reasoning: if future papers enter the graph used to predict future co-occurrence, the test leaks its target into the inputs. The time split is intended to prevent that. A fair temporal evaluation also needs a clear candidate universe and label rule. “Not co-occurring in this period” is not necessarily a proven negative biological relationship; it is a label under the literature target.

The predictors exploit related-neighbor patterns. Common neighbors count shared connections; Adamic–Adar and resource allocation weight such connections differently using neighborhood information. The selected PDF names those methods and citations without printing every score formula. This companion does not invent a new derivation and imply it was an additional tested method. Jaccard appears as a lower-performing comparison in the result section.

**In ordinary language:** Build a map from older papers and ask which links appear in later papers. That is a real forward-in-time test of a literature target. It can help narrow hypotheses. It does not show that a predicted connection is true biology or a good experiment.

**Evidence status:** DEFINITION of a dated retrospective prediction task; MEASURED_DATED graph/labels; SCOPE for discovery interpretation.

**Do not accidentally conclude:** Future literature appearance is experimental validation, or a term pair absent from PubMed has been biologically disproved.

**Try it:** Would adding a 2020 paper to the training graph while predicting 2016–2023 appearances be harmless? **Answer:** No. It can reveal information from the evaluation period. The temporal boundary is part of the task definition and must be preserved.

### C23. Figure 1 and the implementation separate a reusable engine from demonstrations

**Where we are:** Implementation and Figure 1, page 5; continuation, page 6; Software availability, pages 15–16.

**What the passage is doing:** Figure 1 shows named gene groups passing through four lenses, yielding gene-pair graphs and component separation against a null. The engine is configured by JSON specifying components, expression field and species. It caches network retrievals for offline reruns. The paper reports immune and cardiac examples reproduced from shipped caches with scripts/repro.sh; nervous results and nulls are deposited precomputed from its atlas and lens caches.

Worked reasoning: configuration-driven reuse means the analysis code can remain the same while the declared inputs change. It does not mean every cached file is valid for every configuration. Identifiers, species, tissue fields and source versions must match the intended run. A successful offline command confirms that the available cache supports that command; it does not prove a fresh remote retrieval today would produce identical data.

The source also separates engine functionality from one-off graph demonstrations. Connectome and literature analyses share graph primitives but are not all packaged CLI features. That distinction prevents an onboarding promise the software does not make. For executable commands and current Python support, follow the maintained repository README rather than treating the historical manuscript's environment text as an up-to-date installation contract.

**In ordinary language:** The tool repeats one analysis pattern with different named inputs. Stored data can make a rerun independent of a live connection. Still check that the stored data match the question. One command running an example is not a rerun of every figure in the paper.

**Evidence status:** SCOPE and reported software behavior. The guide does not claim a new full pipeline execution.

**Do not accidentally conclude:** Every demonstration is one engine command, or an offline cache is automatically current, complete and appropriate for another domain.

**Try it:** What should change when moving from brain groups to immune groups? **Answer:** At least the component configuration and appropriate expression panel, with matching identifiers and cache provenance. Reusing code does not justify reusing the wrong measurements.

## Nervous-system results and their uncertainty

### C24. Figure 2a: cell identity is often legible in expression

**Where we are:** Nervous-system results, pages 6–7; Figure 2a, page 6; exception paragraph, page 7.

**What the passage is doing:** The expression lens sharply separates several glial and vascular components. Reported separations include microglia 0.90 with z = 31, blood–brain-barrier endothelium 0.82 with z = 32, choroid-plexus/ependyma 0.61, astrocytes 0.53, pericytes 0.52 and oligodendrocyte precursors 0.47. Their structure scores are essentially flat. The pattern is not universal across neuronal groups: spinal-motor expression has z = −0.3, while cerebellar expression is significant but below the strong-pattern cutoff.

Worked reasoning: a cell-identity group can contain proteins with many different architectures yet share a characteristic expression profile across cells. That explains why the expression lens can distinguish the group while the domain lens does not. The numerical separation and its z-score remain different quantities: the first is a difference in similarity means, the second locates that difference in its size-matched null distribution.

The source's phrase “cell types separate” is a summary with named exceptions. Figure 2 should not be used to teach an absolute rule that all cell-related groups must score highly. A group may be mixed, the panel may miss its relevant cells, or neuronal profiles may be broadly shared in this representation. Those are substantive interpretation questions, not reasons to delete inconvenient components.

**In ordinary language:** Genes can belong together because they mark the same kind of cell, even when their proteins have different parts. Expression can reveal that identity. Some cell groups do not follow the simple pattern, so check the examples and exceptions rather than treating the rule as universal.

**Evidence status:** MEASURED_DATED lens-map findings with MODELED_LOCKED permutation comparisons. These are known biological patterns used partly to validate the instrument.

**Do not accidentally conclude:** A z-score of 31 means 31-fold expression or 31% classification accuracy, or flat domain separation means no structure exists.

**Try it:** Why can microglia be clear in expression but flat in domains? **Answer:** Cell identity coordinates diverse proteins. Shared activity across the relevant cell panel need not require a shared molecular architecture.

### C25. Molecular families are often legible through domain architecture

**Where we are:** Nervous-system molecular-family results, page 7; Figure 2a, page 6.

**What the passage is doing:** The source reports structure separation around 0.92 for ionotropic glutamate receptors, 0.89 for trace-amine receptors, 0.78 for metabotropic glutamate receptors, 0.43 for connexins and roughly 0.25 for several histamine, glycine and purinergic groups. Their expression separation is flat or negative in the chosen brain panel. These groups can share protein domains while being expressed across overlapping neuronal populations.

Worked reasoning: the domain lens asks whether a group's architectures are distinctive relative to outsiders. The expression lens asks a different question about profile similarity. If many neuronal proteins share broad expression patterns, that lens may not distinguish one receptor family from other neuronal genes. This does not make expression biologically irrelevant; it means expression is not the most specific representation for that grouping in this atlas.

The operational label matters. Some named neurotransmitter groups may combine functional relationships rather than form strict sequence families. The source explicitly acknowledges that issue in its curation limitations. A high domain score can help reveal why a label fits; an unexpected score can help identify mixed membership. Neither should be taught as a universal assay-selection command without checking the actual group.

**In ordinary language:** Members of a protein family often share parts, so a parts-based view can reveal the family. Being active in the same broad cells may not distinguish that family from its neighbors. Different views can be useful for different kinds of question.

**Evidence status:** MEASURED_DATED separations interpreted through DEFINITION of the lens; supporting known biology, not a new finding that receptors have domains.

**Do not accidentally conclude:** Negative expression separation means the genes are not expressed, or domain similarity proves identical function and drug response.

**Try it:** A receptor family has strong domain separation but no expression separation. What is the restrained interpretation? **Answer:** Its annotated architecture is distinctive within the atlas, while the chosen expression panel does not distinguish that grouping. Functional or clinical equivalence would require additional evidence.

### C26. Functional modules show why a broad detector is not a partitioner

**Where we are:** Functional-module results, page 7; STRING class discussion, page 9; Figure 2a.

**What the passage is doing:** Synaptic-vesicle release, neurodegeneration and circadian-clock groups have reported interaction separation around 0.81, 0.73 and 0.72. They can cohere through association without a shared domain architecture or a distinctive expression profile. STRING has the largest separation for 38 of 49 components across classes. Its broad success is therefore detection, not clean separation of cell types from families and modules; the source reports community ARI around 0.13 as a weak partitioning comparison.

Worked reasoning: a working module can contain receptors, enzymes, scaffolds and regulators that act together without resembling one another in every feature. That gives a sensible reason for association evidence to be useful. But if the same lens scores highly for almost every kind of component, “interaction wins” alone may not answer the entity-class question. The pattern across specialized lenses contains information the maximum score hides.

A failure of both specialized lenses is not automatically proof of a functional module. Coverage and mixed membership can also produce that pattern. The paper's conclusion is conditional on its curated examples and data checks. A new group should be examined for those alternatives before being assigned a class.

**In ordinary language:** A team can work together without all members having the same job or shape. Association data can reveal the team. Yet a view that recognizes many kinds of group may not tell them apart. Look across the profile, not only at the largest score.

**Evidence status:** MEASURED_DATED component profiles and reported clustering comparison; INTERPRETIVE diagnostic map.

**Do not accidentally conclude:** STRING's highest score is always the most discriminating answer, or interaction-only coherence proves direct physical binding among every pair.

**Try it:** Why keep structure and expression if STRING wins for 38 groups? **Answer:** They can distinguish the kind of coherence that a broad association lens recognizes across many classes. Maximum separation and class-specific diagnostic value are different objectives.

### C27. Figure 2b's dual-character group explains the L-shaped picture

**Where we are:** Structure–expression results, page 7; Figure 2b, page 6.

**What the passage is doing:** The plot places each component by structure separation and expression separation. Of 49 nervous components, the source reports exactly one above 0.18 on both axes: dopamine/reward signaling. It mixes a receptor-family element, DRD1–5 GPCRs, with dopaminergic-neuron identity markers such as TH and DAT. That makes it a biologically interpretable dual-character group rather than an error to hide in pursuit of a clean classification.

Worked reasoning: a component's name can combine different kinds of biological identity. Part of the group can resemble a family in domain architecture, while another part marks a cell population. A two-dimensional point summarizes that mixture; it does not establish that every member shares both properties. Inspecting membership is necessary to explain the profile.

The “both above 0.18” description uses a stated threshold for this plot. It is not the same as the z ≥ 4 strong-pattern cutoff or the FDR decision. Each operates on a different quantity. The L shape also includes many components low on both specialized lenses, which can contribute mechanically to the observed correlation. Geometry of a scatterplot is not by itself evidence of mutually exclusive biological classes.

**In ordinary language:** Some groups really mix two kinds of thing. A dopamine-related group can contain both a protein family and cell-identity markers. Seeing it in both views is informative. Do not force it into one box just to make the picture cleaner.

**Evidence status:** MEASURED_DATED plot/count; INTERPRETIVE explanation from curated membership. The numerical threshold is descriptive, not a newly validated classifier.

**Do not accidentally conclude:** One dual case proves all biology has three exclusive categories, or the plot threshold is a statistical significance boundary.

**Try it:** Why inspect the dopamine group's members rather than discard it as an outlier? **Answer:** Its mixed membership explains an important boundary of the lens-map. Removing it solely to strengthen a clean visual story would conceal relevant biology and curation.

### C28. Figure 7 tests direction stability, not a large effect

**Where we are:** Correlation results, page 7; Figure 7a–b, page 8; Discussion, page 14.

**What the passage is doing:** Across 49 nervous components, Pearson structure–expression correlation is r = −0.29, p = 0.043, with analytic 95% interval [−0.53,−0.01]. The source reports all 49 leave-one-out estimates negative, ranging roughly −0.30 to −0.27. Six Pearson/Spearman/Kendall specifications, with and without the dual-character component, are negative and significant, with median r about −0.29. These checks support a stable direction within those analysis variations.

Worked reasoning: correlation near −0.29 explains less than 10% of linear variance through its squared magnitude. A direction can remain negative after deleting any one component while the overall effect remains weak and imprecise. The checks address leverage by single observations and choice of correlation method. They do not create new independent biological replications or establish orthogonality.

The source also notes a partly mechanical contribution: many components are low on both specialized lenses. The two lenses use domains and expression rather than text mining, which reduces one source-overlap concern but does not make every component an independent random object. The wider analytic interval and marginal p value are therefore important companions to the robustness picture.

**In ordinary language:** The two scores tend to move in opposite directions, but only weakly. Leaving out one group at a time keeps the direction the same. That is useful reassurance about one kind of sensitivity. It does not turn the relationship into a large or universal effect.

**Evidence status:** MEASURED_DATED correlation and sensitivity analyses. The checks support a limited directional statement, not a causal or categorical law.

**Do not accidentally conclude:** Six specifications mean six independent studies, or all-negative estimates prove mutually exclusive biology. The paper explicitly rejects statistical orthogonality.

**Try it:** Can a relationship be directionally stable yet uncertain in magnitude? **Answer:** Yes. The leave-one-out range addresses sensitivity to deleting one component; the confidence interval and design limitations address broader uncertainty. They are different pieces of evidence.

### C29. The design analysis warns about weak-signal exaggeration

**Where we are:** Limitations and design-analysis paragraph, page 14; Figure 7 context, page 8.

**What the passage is doing:** At assumed true r = −0.29, the source's design analysis reports power 0.53, Type-S error below 0.001 and Type-M exaggeration about 1.3-fold. Its weaker-effect scenario uses r = −0.1 with n = 49, about 10% power, 4% sign error and roughly 3.4-fold exaggeration. These are conditional design calculations, not estimates that the true correlation is known. Type-S concerns the sign of detected effects; Type-M concerns their magnitude exaggeration.

Worked reasoning: if small studies only occasionally detect a weak effect, the detections can preferentially be unusually large estimates. A statistically significant result can then overstate the underlying magnitude. This explains why a stable direction does not justify treating −0.29 as a precise biological constant. The weaker scenario is the stated −0.1 scenario, not an exact arithmetic halving of −0.29.

The source's 10,000-resample percentile-bootstrap interval is [−0.41,−0.20], markedly narrower than the analytic Fisher-z interval [−0.53,−0.01]. It calls the percentile interval anticonservative here and anchors inference on the wider analytic interval and p = 0.043. The immune contingency and nervous contingency tests are non-significant; they cannot support a categorical exclusivity claim either.

**In ordinary language:** A weak effect in a small study can look too large when it happens to pass a test. The paper checks that danger using assumed effect sizes. It favors the wider uncertainty interval. Keep that caution next to the correlation, rather than treating significance as a precision certificate.

**Evidence status:** MODELED_LOCKED/ANALYTIC conditional design analysis plus reported uncertainty; SCOPE for inference. No true effect size is established by assuming one in the calculation.

**Do not accidentally conclude:** The bootstrap's narrower range is automatically better, or Type-M describes the error of every individual component's separation score.

**Try it:** Does 53% power mean a 53% probability that the reported interpretation is true? **Answer:** No. It is detection probability under a specified assumed effect and design. The posterior truth of a scientific interpretation is a different question.

### C30. Class recovery results are stronger than the weak correlation, but imperfect

**Where we are:** Class-recovery results, pages 8–9; method grid, page 9.

**What the passage is doing:** At the published k = 3 solution, nervous ARI is 0.25 and immune ARI 0.55, with label-permutation p < 0.001 and null z values 8.4 and 6.8. Nervous agreement is explicitly weak-to-moderate in absolute size. A separate specialized cell/family rule has 64% nervous accuracy. In the k = 3 or 4 method grid, nervous recovery is significant in eight of eight settings with ARI 0.15–0.28; immune recovery is significant in seven of eight, missing average linkage at k = 3.

Worked reasoning: the ARI analysis clusters four-lens profiles into groups and compares whole partitions. The specialized rule predicts a subset of entity classes using structure versus expression. These calculations have different outputs and denominators. Quoting 64% as if it were the ARI or quoting ARI 0.25 as 25% accuracy would misrepresent both.

The significant null comparisons show that the observed agreement is unusual under shuffled labels. They do not remove the absolute errors or establish perfect recovery in unseen atlases. The method grid helps show that the pattern is not solely one convenient algorithm, while its miss remains part of the evidence. This is why the source places more weight on per-component diagnostics and recovery than on the weak negative correlation alone.

**In ordinary language:** The evidence patterns recover class information better than shuffled labels do. Recovery is still imperfect, especially in the nervous set. Report the agreement score, the separate rule accuracy and the misses as different facts. A tiny p value does not make them interchangeable.

**Evidence status:** MODELED_LOCKED clustering and permutation tests built on MEASURED_DATED lens profiles; SCOPE for curated domains.

**Do not accidentally conclude:** Every component is correctly typed, every grid setting works, or the numbers estimate accuracy for clinical gene panels.

**Try it:** Why can ARI 0.25 and 64% both be correct? **Answer:** One compares cluster partitions; the other evaluates a specialized rule on a declared subset. They are not two inconsistent versions of the same percentage.

## Generalization and supporting demonstrations

### C31. Figure 3: immune data repeat the diagnostic map with another panel

**Where we are:** Immune-system results, pages 9–10; Figure 3, page 9.

**What the passage is doing:** The engine runs unchanged on 132 genes in 18 immune components, with expression switched to HPA blood-cell RNA. Expression separation includes B cells 0.96, T cells 0.61 and NK cells 0.44. Structure examples include Toll-like receptors 0.79 with z = 34, chemokine receptors 0.59, MHC 0.51 and Fc receptors 0.47. Modules such as inflammasome, antigen processing, NF-κB and IFN response rely on interaction rather than the two specialized lenses.

Worked reasoning: the code reuse is meaningful because the same scoring question and null framework are applied to new configured groups. The expression field changes because the relevant cells change. A successful result with the wrong panel would be harder to interpret. The map's recurrence therefore concerns both a generic instrument and a domain-appropriate measurement choice, not blind reuse of every input.

The specialized cell/family rule classifies 11 of 12 applicable components, or about 92%. Its denominator excludes components not in that rule's target classes. It is not 92% of 18 components, 132 genes or unseen patients. Figure 3 also juxtaposes nervous and immune scatterplots, which supports comparison of patterns but does not make every score directly interchangeable across panels and atlases.

**In ordinary language:** The same question works on another organ system when the inputs are changed appropriately. Cell groups stand out in blood expression; families stand out in domains. This is a useful demonstration of reuse. Its success still depends on the chosen groups and measurements.

**Evidence status:** MEASURED_DATED cross-system profiles with MODELED_LOCKED null and class-recovery tests. It is not a random sample of every possible biological domain.

**Do not accidentally conclude:** The 92% describes all genes or all immune components, or the engine needs no domain judgment because its code is generic.

**Try it:** Why is changing the expression panel compatible with running the same engine? **Answer:** The algorithmic question stays fixed while the configured evidence becomes relevant to the domain. Domain-agnostic code does not imply domain-independent data selection.

### C32. Immune exceptions and a non-significant correlation remain visible

**Where we are:** Immune continuation, page 10; Figure 3, page 9; limitations, page 14.

**What the passage is doing:** Complement is the specialized-rule exception: a structurally diverse cascade that routes to interaction. JAK-STAT combines a module with a kinase-family aspect; TCR signaling combines a module with T-cell expression identity. Across eighteen components, structure–expression r = −0.26 has p = 0.29 and 95% interval [−0.65,+0.23]. Leave-one-out correlations remain negative, around −0.35 to −0.21. The source calls this a consistent tendency, not a confirmed correlation replication.

Worked reasoning: stable direction under deleting one observation is compatible with a broad interval spanning zero. The small set of curated components does not provide enough precision to claim the immune correlation is established merely because its sign matches the nervous result. Nor do biologically sensible mixed groups invalidate the whole map. They show why an operational classification should accommodate overlap.

The main cross-system support comes from per-component diagnostics and unsupervised recovery, not from promoting the non-significant correlation. A categorical exclusivity test is also non-significant. Keeping those distinctions explicit makes the positive result more precise: the tool recovers useful evidence patterns while the broad population relationship between two scores remains uncertain.

**In ordinary language:** Some groups mix roles, and a small study can leave a correlation uncertain. The immune pattern points in the same direction as the nervous one, but its interval includes zero. Call it a tendency, not a confirmed replication of the correlation.

**Evidence status:** MEASURED_DATED profiles and correlation; INTERPRETIVE explanation of mixed groups; SCOPE for significance.

**Do not accidentally conclude:** Every immune family must share domains, the negative sign proves a reliable anticorrelation, or all modules are invisible to expression and structure.

**Try it:** Does a significant immune ARI rescue the correlation's p = 0.29? **Answer:** No. They test different things. Above-chance class recovery can be supported while the across-component correlation remains imprecise and non-significant.

### C33. Cardiac reuse demonstrates reach and exposes mixed biological definitions

**Where we are:** Cardiac demonstration, page 10; software examples, pages 15–16.

**What the passage is doing:** A third configuration contains 64 genes and 11 components. The tool runs without code changes and reports a structure–expression tendency r = −0.28. Clear cases behave as expected: adrenergic/cholinergic receptors and connexins separate on structure; endothelial and smooth-muscle groups separate on expression. The source also says the cardiac map is messier because cell identity overlaps strongly with contractile machinery and “cardiac ion channels” span several unrelated structural families.

Worked reasoning: reuse of a function is not evidence that every entity definition transfers cleanly. In one domain, a cell group may have a distinct expression identity. In another, a named group may largely be a working module. A list called ion channels may include different architectures. A profile reflecting that mixture can be informative rather than a simple failure of the software.

The PDF does not present a cardiac correlation p value or a cardiac ARI equal to the nervous/immune benchmarks. This guide does not invent them or imply that all three systems have the same strength of class-recovery evidence. The cardiac example is most defensibly taught as a configuration-only portability and interpretability check with concrete limits.

**In ordinary language:** A third example shows that the tool can be reused, but it also shows that biological labels can become messy. The name of a group may combine several kinds of thing. Look at membership and evidence before expecting a neat map.

**Evidence status:** MEASURED_DATED demonstration and SCOPE of generalization; not a third equally powered replication of every earlier statistic.

**Do not accidentally conclude:** r = −0.28 alone establishes a significant cardiac relationship, or “no code changes” proves all domain assumptions were validated.

**Try it:** A group named cardiac ion channels has weak domain separation. What should you inspect first? **Answer:** Whether its members span several structural families and whether the atlas comparison is appropriate. A broad functional name need not imply a single domain-defined family.

### C34. Figure 4's blocks are weak-to-modest agreement, not orthogonal axes

**Where we are:** Cross-modality results and Figure 4, page 11; matrix methods, page 4.

**What the passage is doing:** The prose summarizes twenty modalities with within-block mean agreement around 0.40 for function/structure, 0.30 for disease/genetics and 0.18–0.22 for expression. Between-block agreement is about 0.10–0.19. Co-essentiality, in-vivo phenotype and constraint were added to probe for another axis, but no fourth organizing axis is reported. These are descriptive blocks in source-rank correlations, not independent latent variables proved by a fitted factor model.

Worked reasoning: within-block values exceeding between-block values can support a useful organization without implying independence. All the quoted values are modest, and nonzero between-block agreement matters. Sources can share literature, annotations and biological content. The word “axis” is an organizing interpretation of the matrix, not a guarantee that data fall into three mathematically perpendicular dimensions.

The source presentation has a visible limit: its text and caption say twenty modalities, while the displayed panel has fifteen labeled axes. This companion preserves the reported text count but does not invent the missing labels, a larger panel or additional correlations. A reader seeking exact modality coverage should consult the deposited matrix and its metadata. That gap is recorded rather than silently corrected in the immutable draft.

**In ordinary language:** Some databases agree more with one another than with others, but none of these blocks is a perfectly separate witness. The pattern helps organize information. It does not prove three independent kinds of biology or rule out another pattern with different sources.

**Evidence status:** MEASURED_DATED correlation summaries; INTERPRETIVE axes; SCOPE for the displayed-panel/prose mismatch.

**Do not accidentally conclude:** “No fourth axis found” means no fourth axis can exist, or every source in a block is independent confirmation.

**Try it:** Why is 0.40 within a block not proof that the block is one unified biological mechanism? **Answer:** Correlation summarizes agreement in recorded ranks. Shared knowledge, coverage and representation can contribute; mechanism and independence require additional evidence.

### C35. Figure 5 reproduces network organization with explicit thinning costs

**Where we are:** Connectome results and Figure 5a–b, page 12; methods, pages 4–5.

**What the passage is doing:** At matched density 0.0075, the core connectomes have approximate σ values 7–18 and Q values 0.49–0.65. The mouse density sweep demonstrates that both scores depend on edge retention. One macaque graph is excluded because it disconnects into an uninterpretable graph at that density. Other retained graphs also fragment: Ciona keeps about 62% of nodes in its giant component, while mouse and C. elegans keep about 83%; sparse mean degree is around 1.5–2.

Worked reasoning: a “tight band” of Q is a descriptive summary after processing, not proof that complete brains have identical modular organization. The retained graphs differ in nodes, edges and connectivity. Ciona's lower end is partly a fragmented graph. The source calls the band approximate and supplies no extra null model beyond σ's normalization. These qualifications are necessary to understand what the cross-species plot does and does not compare.

Panel a is therefore not decorative. It motivates matching density and warns against treating a graph score as a fixed property independent of processing. Panel b illustrates a known organization under a stated pipeline. The source explicitly calls this reproduction, not its central discovery. That distinction prevents a supporting demonstration from displacing the more carefully tested gene-set question.

**In ordinary language:** These processed wiring graphs show familiar clumping and short-path features under one shared retention rule. Some lose many nodes from the main connected part. The comparison is useful, but it is not a comparison of complete, identically measured brains.

**Evidence status:** MEASURED_DATED processed-network summaries; supporting reproduction of known properties; SCOPE for sparse/fragmented comparisons.

**Do not accidentally conclude:** Every graph remains intact, excluded macaque lacks small-world biology, or similar Q proves equivalent function across species.

**Try it:** Why should a report retain the 62% giant-component figure? **Answer:** It states how much of the graph participates in its largest connected structure. Omitting it would make an aggressively thinned, partly fragmented comparison look more complete than it is.

### C36. Figure 6: strong ROC ranking can coexist with a poor shortlist

**Where we are:** Forward-use results and Figure 6, page 13; methods, page 5.

**What the passage is doing:** Over roughly 1.3 million candidate term pairs, the best topology methods obtain ROC-AUC around 0.85–0.90; resource allocation reaches 0.90 and Jaccard about 0.68. There are only 230 positives, a base rate near 0.0002. Resource allocation has precision@100 about 1% and PR-AUC around fourteen times that tiny base rate. Other methods are near chance at the top. These figures concern future literature co-occurrence, not biological confirmation.

Worked reasoning: ROC-AUC summarizes how often positives rank above negatives across score thresholds. With very many negatives, a method can discriminate globally while still putting many false positives at the top. Precision@100 directly asks how many of the first hundred suggestions meet the future-literature label. Approximately 1% corresponds to a weak shortlist, even alongside a large relative improvement over an extremely small baseline.

The ratio “fourteen times base rate” must retain its denominator. A large relative multiple of a tiny quantity can remain small in absolute terms. Neither that ratio nor AUC 0.90 means 90% of suggestions are correct. The source concludes that the tool narrows hypotheses rather than providing a high-yield discovery engine.

**In ordinary language:** A ranking can put true future links ahead of many wrong ones and still give you a poor first hundred suggestions. That happens when true links are very rare. Read the shortlist precision next to the ranking score before deciding how useful the suggestions are.

**Evidence status:** MEASURED_DATED retrospective temporal benchmark; SCOPE for experimental discovery. No prospective experimental validation is reported.

**Do not accidentally conclude:** AUC 0.90 means 90% precision, or a later paper mentioning two terms proves the proposed biological relation.

**Try it:** Which statistic best answers “How many of my first hundred candidates meet this study's label?” **Answer:** Precision@100. ROC-AUC answers a different ranking question and cannot replace the reported low top-list precision.

## Interpretation, availability and accountability

### C37. Experimental-design triage is a suggestion for the next question

**Where we are:** Discussion practical value, page 14; Conclusions, page 15.

**What the passage is doing:** The source proposes using evidence profiles to guide experimental-design triage, target-class characterization and hypothesis narrowing. Expression separation suggests examining cell identity; domain separation suggests molecular-family analysis; interaction-only patterns suggest functional/network investigation. These are research-planning interpretations, not validated rules that guarantee which assay will resolve any unfamiliar group. The central finding is the diagnostic map and its class recovery, not a causal prescription.

Worked reasoning: before spending resources, check whether the score arose from adequate evidence and a coherent group. A missing expression tissue can mimic a reason to abandon expression. A broad STRING score can reflect shared literature rather than direct physical contact. A mixed group can produce a dual profile. The profile can help formulate alternatives, but the next experiment must be suited to the actual biological question and its confounders.

For drug-target groups, a family-like profile may inform a class-effect hypothesis, but it does not establish efficacy, safety, repurposing benefit or causal target validity. No patient-level model or treatment-effect study is reported. The practical promise is to clarify what type of evidence is already organizing the group and what additional evidence might discriminate competing explanations.

**In ordinary language:** Use the map to decide what to inspect next. First check whether the data and group definition fit the question. Then choose a follow-up that could test the explanation. A useful hint about evidence type is not a guarantee that one assay or treatment will work.

**Evidence status:** INTERPRETIVE research-planning use based on MEASURED_DATED diagnostics; SCOPE for causal and clinical translation.

**Do not accidentally conclude:** The engine prescribes an experiment with known success probability, identifies a causal drug target or recommends clinical treatment.

**Try it:** A group is interaction-only and a scientist proposes a binding assay for every pair. What should be clarified? **Answer:** STRING includes broader associations, so the hypothesized relation may be functional rather than direct binding. Select a test that addresses that hypothesis rather than assuming the lens already established the mechanism.

### C38. Curation, shared knowledge and coverage remain the main interpretation risks

**Where we are:** Limitations, pages 14–15; component and lens definitions, page 3.

**What the passage is doing:** The source lists expert-curated components, overlapping knowledge sources, group-size effects on z, expression-panel blind spots, mixed cell groups and unequal connectome semantics. The mutual-exclusivity contingency tests are non-significant: Fisher p = 0.41 in nervous data and 0.15 in immune data. It also records a fixed Allen retrieval bug: a silent cap returned 500,000 of 756,833 rows. These are distinct issues; one successful safeguard does not solve all of them.

Worked reasoning: avoiding direct label use in similarity construction reduces one circularity risk. It does not eliminate curation or knowledge overlap. Using domain and RNA data for the correlation reduces a text-mining concern, but does not make all group definitions independent. A null calibration checks false alarms under its random sets, not every dependency in expert-selected groups. A reliable conclusion combines these partial safeguards while retaining the remaining uncertainty.

The truncation example is especially transferable to research engineering. A valid-looking table can be incomplete without an obvious error. Checking totals, pagination and source coverage can change downstream graph results. The source reports that this bug was caught and fixed during development; this companion attributes that history without claiming to have independently reconstructed the corrected Allen dataset.

**In ordinary language:** Several checks reduce specific risks, but no single check removes every problem. Groups are chosen by experts, databases can share knowledge, and a download can be incomplete. Keep those facts visible when deciding how much confidence to place in a clean-looking result.

**Evidence status:** SCOPE and reported development history; MEASURED_DATED contingency tests. The guide adds no new audit verdict or dataset reconstruction.

**Do not accidentally conclude:** An eighteen-agent audit reported by the paper substitutes for independent human review, or that non-significant contingency tests prove exclusivity.

**Try it:** Why should “the API returned successfully” not end a data-quality check? **Answer:** A successful response can still be capped or partial. Compare expected and retrieved coverage and preserve the source/version evidence before trusting the analysis.

### C39. Software and data availability describe different artifacts and licenses

**Where we are:** Software availability, pages 15–16; Data availability, page 16.

**What the passage is doing:** The source identifies consilience-engine v1.0.0, Python ≥3.11, numpy/scipy/scikit-learn/networkx, platform-independent configuration, MIT software and an OSF code/data snapshot at DOI 10.17605/OSF.IO/ZKTRJ. It describes offline examples, unit/metamorphic/property tests and continuous integration. Data outputs are described under CC-BY 4.0: curated atlases, pairwise matrices, maps/nulls, modality matrix, connectome metrics and literature outputs. Primary sources were accessed in 2026.

Worked reasoning: a code license and a derived-data license do not necessarily govern third-party upstream material. Nor does “keyless” mean every source is immutable or that every service remains available indefinitely. Exact cached inputs, identifier mappings, configurations and versions belong to a reproducible run. The paper's historical Python minimum and script names should not override current repository requirements after maintenance; use the root README for executable instructions.

The software's example engine commands must also be separated from one-off connectome and LBD analysis scripts. Their shared graph primitives do not make them one packaged feature. Metamorphic checks such as relabeling or lens-duplication invariance assess specified behaviors; they are not proofs of biological truth or completion of every scientific analysis.

**In ordinary language:** Keep the program, stored inputs, derived results and paper version straight. They can have different versions and usage terms. Offline examples help preserve a rerun path, but they do not certify every result or make all upstream data current.

**Evidence status:** SCOPE and attributed software/data declarations. This teaching document does not claim to rerun every deposited analysis or certify licenses beyond the stated source descriptions.

**Do not accidentally conclude:** The MIT code license automatically applies to all manuscript and database content, or the historical environment statement is today's installation guarantee.

**Try it:** What should a reproduction record name besides the software version? **Answer:** The exact input/cache vintages, domain configuration, identifiers, random budgets, output artifacts and manuscript basis. Those connect an executable run to a particular reported claim.

### C40. Conclusions, declarations and references preserve accountability

**Where we are:** Conclusions, page 15; Declarations and acknowledgements, page 16; References, pages 17–19.

**What the passage is doing:** The conclusion summarizes a reusable diagnostic question, a recurring lens-map, imperfect but above-chance class recovery and weak forward literature precision. Declarations report no competing interests or specific funding, sole authorship, public aggregate-data ethics scope and AI-assisted coding/drafting/figure/reference work. The author claims responsibility for scientific conception, numerical verification and outputs. The source says figures were programmatically produced from deposited results, not altered to fabricate relationships.

Worked reasoning: distinguish accountability statements from evidence. An author's reported verification process is relevant research history, but it is not an independent reproduction by this companion. Likewise, an AI disclosure does not itself prove or disprove a result. The proper assessment returns to inputs, methods, uncertainty and the specific claims supported.

The bibliography supplies integration context, public-resource provenance, clustering sensitivity, graph statistics and temporal link-prediction methods. It includes the underlying biology/network data references as well as the software resources. This guide maps those roles rather than pretending to reproduce a new literature review. All bibliography entries remain accessible in the source, including the final reference on page 19. Names, affiliation and correspondence are administrative provenance, not scientific outcomes requiring numerical exercises.

**In ordinary language:** The conclusion should stay as careful as the results. The tool helps compare evidence; it does not prove every biological story. Declarations say who is responsible and what help was used. References show where methods and inputs came from. None replaces checking the actual analysis.

**Evidence status:** SCOPE for declarations and provenance; INTERPRETIVE synthesis. No human educational signoff or full validation is implied by the source's own approval statements.

**Do not accidentally conclude:** All familiar facts recovered are new discoveries, all domains are validated equally, or the manuscript's AI-assisted checks certify this companion's learning effectiveness.

**Try it:** What is the narrowest useful final summary? **Answer:** A reusable, permutation-tested instrument compares which public-data lens distinguishes a curated gene group; its reported diagnostic map has cross-system support, while correlation, coverage, dependence and forward precision remain limited.

## Glossary and notation

| Term | Meaning in this paper |
|---|---|
| Atlas | The selected universe of genes and named groups used in the analysis. |
| Component | A named, expert-curated gene group. |
| Entity class | Operational category such as cell type, molecular family or functional module. |
| Modality | A kind of public evidence, such as expression or domain annotations. |
| Lens | A modality represented as gene-pair similarities. |
| Gene–gene graph | Genes as nodes, with similarities or associations as links. |
| InterPro domain | An annotated protein part used in the structure representation. |
| Jaccard similarity | Shared set items divided by distinct items in the union. |
| Expression panel | The selected cells/tissues and RNA measurements forming profiles. |
| log1p | Transform log(1+x), reducing the relative influence of large values. |
| Cosine similarity | Similarity of profile directions in a numerical feature space. |
| STRING combined score | Multi-channel association evidence, not exclusively physical binding. |
| GO process term | A recorded biological-process annotation. |
| Separation | Mean within-component similarity minus mean component-to-outsider similarity. |
| Permutation/random-set null | Reference generated by size-matched random atlas groups. |
| z-score | Observed statistic minus null mean, divided by null standard deviation. |
| Empirical p value | Tail extremeness estimated under the stated randomization reference. |
| Type-I error | False-positive rate under a specified null. |
| Power | Detection probability under a specified non-null effect and design. |
| FDR | Expected false-discovery proportion under a stated selection procedure and assumptions. |
| BY | Benjamini–Yekutieli FDR procedure used for dependent tests here. |
| Monte-Carlo error | Numerical uncertainty due to finite random draws. |
| ARI | Chance-adjusted agreement between partitions, not percentage accuracy. |
| Method-invariance grid | Declared combinations of algorithms/settings used to examine analytic sensitivity. |
| Spearman correlation | Agreement in ranks, used for modality comparisons. |
| Pearson correlation | Linear association, used for the main structure–expression summary. |
| Leave-one-out check | Recompute after omitting each component in turn. |
| Type-S / Type-M | Sign-error and magnitude-exaggeration risks under a specified design analysis. |
| Connectome | Neural wiring/projection graph with dataset-specific nodes and edges. |
| Density | Retained links as a fraction of possible links under the graph convention. |
| Small-world coefficient σ | Relative clustering divided by relative path length against a random reference. |
| Modularity Q | Concentration of links within inferred communities relative to its model reference. |
| Giant component | Largest connected part of a graph. |
| MeSH co-occurrence | Terms jointly recorded in a paper, not proof of a biological relationship. |
| ROC-AUC | Ranking discrimination across thresholds, not shortlist precision. |
| Precision@100 | Positive-label share among the first hundred ranked candidates. |
| PR-AUC | Summary of precision–recall performance; its baseline depends on positive prevalence. |
| Cache | Stored retrieved/derived input supporting repeatable offline use, conditional on provenance. |
| Metamorphic test | Check of expected behavior under a specified transformation, not a biological validation. |

## Twelve-item answered transfer assessment

Answer first, then consult the key. Four questions address core understanding, four claim boundaries and four transfer. No learner has been scored; this is not evidence of educational effectiveness.

### Core questions

1. Define a lens, a component and separation without calling any of them a diagnosis.
2. Why use a size-matched random-group null rather than raw separation alone?
3. Why can STRING be a broad detector while structure/expression carry more class-specific contrast?
4. What does label-withheld ARI recovery test, and what curation remains?

### Boundary questions

5. Does the weak nervous correlation and non-significant immune correlation establish orthogonal biology?
6. Does the 92% immune figure describe all 132 genes or all 18 components?
7. Does ROC-AUC 0.90 mean 90% of top literature suggestions are correct?
8. Does zero similarity or flat expression establish absence of a biological relationship or cell identity?

### Transfer questions

9. A component is moved to a different atlas. Which parts of separation and its null can change?
10. A new organ's relevant cells are absent from the expression panel. What must happen before interpreting a low score?
11. Two databases agree but share literature channels. How should that affect evidence counting?
12. Two connectomes have similar Q after different thinning rules. What is needed before a biological comparison?

### Answer key

1. A lens supplies pairwise similarities from one evidence type; a component selects named genes; separation contrasts internal and external mean similarity within a stated atlas.
2. Size affects pair structure and null variability. The null asks whether this score is unusual for random atlas groups of that size, not whether every interpretation is true.
3. Broad associations can recognize many forms of coherence. Specialized lenses can distinguish the kind of coherence, which the largest interaction score may not reveal.
4. It asks whether evidence profiles recover curated classes above a label-shuffle reference. Experts still defined the components, atlas and operational classes.
5. No. The effect is modest, immune uncertainty spans zero and categorical contingency tests are non-significant. The main support is component diagnostics and recovery.
6. Neither. It is 11 of 12 applicable cell/family components under the specialized rule, a different denominator from all genes or components.
7. No. The best method has about 1% precision@100 in this rare-label task. Global ranking discrimination is not shortlist yield.
8. No. Missing annotations, panel coverage and mixed membership can produce low scores. Check evidence before treating zero as biology.
9. Outside genes, between-group means, annotation coverage and random-set reference can change, even if the component's internal pairs do not.
10. Obtain or select an appropriate panel and inspect identifiers/coverage. Do not infer that expression is the wrong biological view from an irrelevant measurement panel.
11. Agreement is partly dependent evidence. It may reflect real coherence and shared knowledge; do not count every source as an independent experiment.
12. State and harmonize retention/density where appropriate, inspect connectivity, node counts, edge semantics and measurement scale, and retain fragmentation caveats. Similar Q alone is insufficient.

For a one-sentence teach-back, state the diagnostic question, its random-group evidence, one main nonclaim and one coverage check for a new domain. Human clarity and transfer scores remain unrecorded.

## Preparation and exact-source record

The source draft remains unchanged. Its SHA-256 is 3c03a781e459efc32025cfaae4922e45142cc16ffa0cd943ce190831dfc00885. Numerical biological and benchmark findings are attributed to that exact PDF. The annotation-set arithmetic in C06 and mean-subtraction example in C10 are explicitly hypothetical; their answers follow elementary set counting and subtraction, not new data. Other worked reasoning explains definitions or source results.

The source's displayed Figure 4/prose modality-count discrepancy is recorded without rewriting the paper. Unprinted implementation details are left to the deposited/maintained code rather than invented. Current installation instructions belong to the repository README; this companion is an explanation of the July manuscript, not an updated scientific analysis.

The earlier concise guide is preserved separately as STUDY_GUIDE. No matching older gene-set educational companion was found in the examined candidates. This complete source-locked teaching document was prepared using AI-assisted source/figure comparisons and structural/numerical checks. No full empirical rerun, complete formal G14 pass, human audience/accessibility signoff or administered transfer-test result is claimed. Release-time PDF rendering and derivative checks are recorded separately.
