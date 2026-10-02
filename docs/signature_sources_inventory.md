# Supplementary files of the iCCA classifier papers

Written by `scripts/tools/fetch_signature_sources.py` from `config/signature_sources.yaml`. Describes the published supplements (sheet names, sizes, first rows) so that extraction scripts can be written; files themselves stay in `data/papers/`.

| paper | priority | PMCID | files fetched | route |
|---|---|---|---|---|
| sia2013 | 1 | PMC3624083 | 0 | inventory-only |
| martin_serrano2023 | 1 | PMC10388405 | 0 | inventory-only |
| beaufrere2025 | 1 | PMC12800354 | 0 | inventory-only |
| job2020 | 1 | PMC7589418 | 0 | inventory-only |
| dong2022 | 1 |  | 0 | inventory-only |
| chaisaingmongkol2017 | 2 | PMC5524207 | 0 | inventory-only |
| fan2024 | 2 | PMC10784309 | 0 | inventory-only |
| song2022 | 2 | PMC8960779 | 0 | inventory-only |
| lin2026 | 3 | PMC13130669 | 0 | inventory-only |

## sia2013

Sia D et al. Integrative molecular analysis of intrahepatic cholangiocarcinoma reveals 2 classes that have different outcomes. Gastroenterology 2013;144:829-840

- identifiers: {"doi": "10.1053/j.gastro.2013.01.001", "pmid": "23295441", "pmcid": "PMC3624083"}
- resolved title: Integrative molecular analysis of intrahepatic cholangiocarcinoma reveals 2 classes that have different outcomes. Gastroenterology 2013
- want: Proliferation / Inflammation class signatures (NTP templates) and the poor-prognosis signature. Labels: GSE32225 sample characteristics already carry the class (Proliferation 92 / Inflammation 57).

### data/papers/sia2013/supp/mmc1.pdf (7924 kB)
- 145 pages
  - p2: 14 gene-like tokens; Supplementary Table 1: Leave-one-out cross validation of ICC classes / Supplementary Table 2: ICC class signature / Supplementary Table 3: GSEA results. Pathways enriched in Proliferation / Supplementary Table 4: GSEA of HCC signatures in Proliferation class
  - p3: 11 gene-like tokens; Supplementary Table 8: Focal Deletions in ICC samples / Supplementary Table 9: Focal deletions frequency in ICC classes / Supplementary Table 10: Mutation analysis in ICC samples / Supplementary Table 11: GSEA results. Pathways and signatures enriched in
  - p28: 7 gene-like tokens; correlation study (n=119) are summarized in Table 1. Correlation between
  - p29: 13 gene-like tokens; classifier (Supplementary Table 1 in reference 19) using nearest template
  - p34: 3 gene-like tokens; Supplementary Table 1: Leave-one-out cross validation of ICC classes
  - p35: 103 gene-like tokens; Supplementary Table 2: ICC class signature
    Supplementary Table 2: ICC class signature
    t- Fold
    Gene symbol Gene title ICC class statistic change
    WDFY1 WDFY1:WD repeat and FYVE domain containing 1 Proliferation 20.19 2.87
    ZFP36L1 ZFP36L1:zinc finger protein 36, C3H type-like 1 Proliferation 20.08 3.18
    CRY1 CRY1:cryptochrome 1 (photolyase-like) Proliferation 19.31 2.68
    FAM120A FAM120A:family with sequence similarity 120A Proliferation 18.92 2.48
    NSUN2 NSUN2:NOL1/NOP2/Sun domain family, member 2 Proliferation 18.58 2.08
  - p36: 109 gene-like tokens; 
    DARS DARS:aspartyl-tRNA synthetase Proliferation 16.13 2.40
    TCEAL8 TCEAL8:transcription elongation factor A (SII)-like 8 Proliferation 16.1 1.82
    MRPL22 MRPL22:mitochondrial ribosomal protein L22 Proliferation 16.05 1.91
    PGAM4 PGAM4:phosphoglycerate mutase family member 4 Proliferation 16.05 2.77
    WSB2 WSB2:WD repeat and SOCS box-containing 2 Proliferation 16.03 2.07
    UBE3C UBE3C:ubiquitin protein ligase E3C Proliferation 16.01 1.98
    PSMA6 PSMA6:proteasome (prosome, macropain) subunit, alpha type, 6 Proliferation 16.01 3.25
    KIAA1191 KIAA1191:KIAA1191 Proliferation 15.97 2.17
  - p37: 113 gene-like tokens; 
    VPS36 VPS36:vacuolar protein sorting 36 (yeast) Proliferation 15.3 1.82
    ANXA2P1 ANXA2P1:annexin A2 pseudogene 1 Proliferation 15.28 2.82
    UBE2D4 UBE2D4:ubiquitin-conjugating enzyme E2D 4 (putative) Proliferation 15.28 1.89
    RPP21 RPP21:ribonuclease P 21kDa subunit Proliferation 15.25 2.46
    CROP CROP:- Proliferation 15.23 2.40
    HMGB1 HMGB1:high-mobility group box 1 Proliferation 15.21 2.01
    TMEM126B TMEM126B:transmembrane protein 126B Proliferation 15.19 1.92
    ZNF511 ZNF511:zinc finger protein 511 Proliferation 15.17 1.94
  - p38: 102 gene-like tokens; 
    CALM2 CALM2:calmodulin 2 (phosphorylase kinase, delta) Proliferation 14.5 2.35
    TSPAN31 TSPAN31:tetraspanin 31 Proliferation 14.5 2.47
    E2F3 E2F3:E2F transcription factor 3 Proliferation 14.48 2.54
    TCF25 TCF25:transcription factor 25 (basic helix-loop-helix) Proliferation 14.48 2.23
    TXNDC17 na Proliferation 14.43 2.81
    ZNF364 ZNF364:zinc finger protein 364 Proliferation 14.41 2.79
    AP1M1 AP1M1:adaptor-related protein complex 1, mu 1 subunit Proliferation 14.39 1.93
    TM9SF2 TM9SF2:transmembrane 9 superfamily member 2 Proliferation 14.39 2.18
  - p39: 99 gene-like tokens; 
    PDCD5 PDCD5:programmed cell death 5 Proliferation 13.9 1.80
    CDK2 CDK2:cyclin-dependent kinase 2 Proliferation 13.86 1.94
    GOLPH3 GOLPH3:golgi phosphoprotein 3 (coat-protein) Proliferation 13.84 2.08
    OGT:O-linked N-acetylglucosamine (GlcNAc) transferase (UDP-N-
    OGT acetylglucosamine:polypeptide-N-acetylglucosaminyl transferase) Proliferation 13.83 1.81
    PHF23 PHF23:PHD finger protein 23 Proliferation 13.82 1.75
    FAM103A1 FAM103A1:family with sequence similarity 103, member A1 Proliferation 13.82 2.01
    ZDHHC5 ZDHHC5:zinc finger, DHHC-type containing 5 Proliferation 13.81 1.72
  - p40: 104 gene-like tokens; 
    EWSR1 EWSR1:Ewing sarcoma breakpoint region 1 Proliferation 13.42 2.11
    SCFD1 SCFD1:sec1 family domain containing 1 Proliferation 13.41 1.85
    SPRED1 SPRED1:sprouty-related, EVH1 domain containing 1 Proliferation 13.41 2.20
    BIRC6 BIRC6:baculoviral IAP repeat-containing 6 (apollon) Proliferation 13.41 1.58
    NCL NCL:nucleolin Proliferation 13.4 1.84
    KIAA1754 KIAA1754:KIAA1754 Proliferation 13.4 1.74
    SAPS3 SAPS3:SAPS domain family, member 3 Proliferation 13.39 1.85
    BUB3 BUB3:BUB3 budding uninhibited by benzimidazoles 3 homolog (yeast) Proliferation 13.37 2.02
  - p41: 99 gene-like tokens; 
    GMFG GMFG:glia maturation factor, gamma Proliferation 13.09 1.75
    YPEL5 YPEL5:yippee-like 5 (Drosophila) Proliferation 13.08 1.92
    SCOC SCOC:short coiled-coil protein Proliferation 13.06 1.89
    ING2 ING2:inhibitor of growth family, member 2 Proliferation 13.05 1.62
    LOC401152 LOC401152:- Proliferation 13.04 1.98
    PSMA4 PSMA4:proteasome (prosome, macropain) subunit, alpha type, 4 Proliferation 13.04 1.62
    C2ORF25 C2ORF25:chromosome 2 open reading frame 25 Proliferation 13.04 2.34
    NR2C2AP na Proliferation 13.03 2.02
  - p42: 103 gene-like tokens; 
    GIGYF1 na Proliferation 12.63 1.71
    F11R F11R:F11 receptor Proliferation 12.63 1.92
    FAM107B FAM107B:family with sequence similarity 107, member B Proliferation 12.62 1.89
    LAMP2 LAMP2:lysosomal-associated membrane protein 2 Proliferation 12.62 2.59
    C14ORF4 C14ORF4:chromosome 14 open reading frame 4 Proliferation 12.62 1.71
    SH3GLB1 SH3GLB1:SH3-domain GRB2-like endophilin B1 Proliferation 12.61 2.21
    ACAD10 ACAD10:acyl-Coenzyme A dehydrogenase family, member 10 Proliferation 12.61 1.72
    ERGIC2 ERGIC2:ERGIC and golgi 2 Proliferation 12.6 1.88
  - p43: 97 gene-like tokens; 
    MAP7 MAP7:microtubule-associated protein 7 Proliferation 12.29 2.18
    SHFM1 SHFM1:split hand/foot malformation (ectrodactyly) type 1 Proliferation 12.29 1.98
    B4GALT3 B4GALT3:UDP-Gal:betaGlcNAc beta 1,4- galactosyltransferase, polypeptide 3 Proliferation 12.28 2.10
    FHL2 FHL2:four and a half LIM domains 2 Proliferation 12.28 1.93
    CUTL1 CUTL1:cut-like 1, CCAAT displacement protein (Drosophila) Proliferation 12.27 1.88
    RPL23 RPL23:ribosomal protein L23 Proliferation 12.27 1.73
    NUSAP1 NUSAP1:nucleolar and spindle associated protein 1 Proliferation 12.26 3.04
    ABCA1 ABCA1:ATP-binding cassette, sub-family A (ABC1), member 1 Proliferation 12.24 2.05
  - p44: 105 gene-like tokens; 
    INO80B na Proliferation 12.01 2.10
    NCBP2 NCBP2:nuclear cap binding protein subunit 2, 20kDa Proliferation 12.01 1.47
    GIYD2 GIYD2:GIY-YIG domain containing 2 Proliferation 12 1.94
    LOC158160 na Proliferation 11.98 2.08
    XPO4 XPO4:exportin 4 Proliferation 11.97 1.98
    FLJ40504 FLJ40504:- Proliferation 11.97 2.15
    TXNL2 TXNL2:thioredoxin-like 2 Proliferation 11.95 1.58
    SFXN4 SFXN4:sideroflexin 4 Proliferation 11.95 1.83
  - p45: 101 gene-like tokens; 
    CS CS:citrate synthase Proliferation 11.67 2.23
    DMPK DMPK:dystrophia myotonica-protein kinase Proliferation 11.67 1.61
    RSRC2 na Proliferation 11.67 1.46
    ATP6AP2 ATP6AP2:ATPase, H+ transporting, lysosomal accessory protein 2 Proliferation 11.66 1.68
    C19ORF66 na Proliferation 11.65 1.65
    SLC25A32 SLC25A32:solute carrier family 25, member 32 Proliferation 11.64 1.59
    DDX39 DDX39:DEAD (Asp-Glu-Ala-Asp) box polypeptide 39 Proliferation 11.64 2.11
    GMFB GMFB:glia maturation factor, beta Proliferation 11.64 2.34
  - p46: 101 gene-like tokens; 
    C12ORF52 C12ORF52:chromosome 12 open reading frame 52 Proliferation 11.47 1.98
    MKRN1 MKRN1:makorin, ring finger protein, 1 Proliferation 11.47 1.77
    PSMD14 PSMD14:proteasome (prosome, macropain) 26S subunit, non-ATPase, 14 Proliferation 11.47 1.76
    VPS37A VPS37A:vacuolar protein sorting 37 homolog A (S. cerevisiae) Proliferation 11.45 1.59
    HADHB:hydroxyacyl-Coenzyme A dehydrogenase/3-ketoacyl-Coenzyme A
    HADHB thiolase/enoyl-Coenzyme A hydratase (trifunctional protein), beta subunit Proliferation 11.45 1.46
    UBB UBB:ubiquitin B Proliferation 11.45 2.18
    SH3BP4 SH3BP4:SH3-domain binding protein 4 Proliferation 11.44 2.01
  - p47: 111 gene-like tokens; 
    COPS7A COPS7A:COP9 constitutive photomorphogenic homolog subunit 7A (Arabidopsis) Proliferation 11.16 1.56
    AK3 AK3:adenylate kinase 3 Proliferation 11.16 1.94
    RAB10 RAB10:RAB10, member RAS oncogene family Proliferation 11.15 2.05
    HCP5 HCP5:HLA complex P5 Proliferation 11.14 2.32
    RDH10 RDH10:retinol dehydrogenase 10 (all-trans) Proliferation 11.14 2.12
    MS4A4A MS4A4A:membrane-spanning 4-domains, subfamily A, member 4 Proliferation 11.14 2.16
    STRA13 STRA13:stimulated by retinoic acid 13 homolog (mouse) Proliferation 11.13 2.05
    CHCHD2 CHCHD2:coiled-coil-helix-coiled-coil-helix domain containing 2 Proliferation 11.13 1.66
  - p48: 110 gene-like tokens; 
    LEMD3 LEMD3:LEM domain containing 3 Proliferation 10.95 1.84
    RABGEF1 RABGEF1:RAB guanine nucleotide exchange factor (GEF) 1 Proliferation 10.94 1.44
    AMMECR1L na Proliferation 10.93 1.75
    SLC7A1:solute carrier family 7 (cationic amino acid transporter, y+ system),
    SLC7A1 member 1 Proliferation 10.93 2.89
    TBC1D20 TBC1D20:TBC1 domain family, member 20 Proliferation 10.93 1.67
    USP6NL USP6NL:USP6 N-terminal like Proliferation 10.9 1.50
    C7ORF27 C7ORF27:chromosome 7 open reading frame 27 Proliferation 10.89 1.49
  - p49: 112 gene-like tokens; 
    PGK1 PGK1:phosphoglycerate kinase 1 Proliferation 10.7 1.58
    RNPEP RNPEP:arginyl aminopeptidase (aminopeptidase B) Proliferation 10.7 1.47
    LZTR1 LZTR1:leucine-zipper-like transcription regulator 1 Proliferation 10.7 1.58
    C12ORF32 C12ORF32:chromosome 12 open reading frame 32 Proliferation 10.69 1.83
    LSM3 LSM3:LSM3 homolog, U6 small nuclear RNA associated (S. cerevisiae) Proliferation 10.69 1.52
    GPR116 GPR116:G protein-coupled receptor 116 Proliferation 10.68 1.78
    SNHG8 SNHG8:small nucleolar RNA host gene (non-protein coding) 8 Proliferation 10.67 1.57
    COX7B COX7B:cytochrome c oxidase subunit VIIb Proliferation 10.67 1.91
  - p50: 104 gene-like tokens; 
    UEVLD UEVLD:UEV and lactate/malate dehyrogenase domains Proliferation 10.51 1.44
    PHF20L1 PHF20L1:PHD finger protein 20-like 1 Proliferation 10.51 1.51
    ANGPTL2 ANGPTL2:angiopoietin-like 2 Proliferation 10.51 1.84
    EIF4A2 EIF4A2:eukaryotic translation initiation factor 4A, isoform 2 Proliferation 10.51 1.67
    EXOSC3 EXOSC3:exosome component 3 Proliferation 10.51 1.44
    TMEM205 na Proliferation 10.48 1.45
    RFWD2 RFWD2:ring finger and WD repeat domain 2 Proliferation 10.48 1.85
    UROS UROS:uroporphyrinogen III synthase (congenital erythropoietic porphyria) Proliferation 10.46 1.64
  - p51: 110 gene-like tokens; 
    SNTB1:syntrophin, beta 1 (dystrophin-associated protein A1, 59kDa, basic
    SNTB1 component 1) Proliferation 10.33 2.01
    ZNRF2 ZNRF2:zinc and ring finger 2 Proliferation 10.32 1.56
    MYST1 MYST1:MYST histone acetyltransferase 1 Proliferation 10.32 1.64
    COPA COPA:coatomer protein complex, subunit alpha Proliferation 10.32 1.86
    SDF2 SDF2:stromal cell-derived factor 2 Proliferation 10.32 1.56
    MAP2K1IP1 MAP2K1IP1:mitogen-activated protein kinase kinase 1 interacting protein 1 Proliferation 10.31 1.74
    IGFBP5 IGFBP5:insulin-like growth factor binding protein 5 Proliferation 10.3 1.94
  - p52: 106 gene-like tokens; 
    FAR1 na Proliferation 10.18 2.00
    ZNF207 ZNF207:zinc finger protein 207 Proliferation 10.18 1.43
    CNOT1 CNOT1:CCR4-NOT transcription complex, subunit 1 Proliferation 10.17 1.80
    RPS4X RPS4X:ribosomal protein S4, X-linked Proliferation 10.17 1.64
    SPAG1 SPAG1:sperm associated antigen 1 Proliferation 10.17 1.80
    IMPA1 IMPA1:inositol(myo)-1(or 4)-monophosphatase 1 Proliferation 10.17 1.65
    CD99L2 CD99L2:CD99 molecule-like 2 Proliferation 10.16 1.51
    KIAA1618 KIAA1618:KIAA1618 Proliferation 10.16 2.29
  - p53: 109 gene-like tokens; 
    CTGLF3 CTGLF3:centaurin, gamma-like family, member 3 Proliferation 10.03 1.82
    RBM45 na Proliferation 10.03 1.47
    PHCA PHCA:phytoceramidase, alkaline Proliferation 10.02 1.57
    NDUFAB1 NDUFAB1:NADH dehydrogenase (ubiquinone) 1, alpha/beta subcomplex, 1, 8kDa Proliferation 10.02 1.59
    CNBP CNBP:CCHC-type zinc finger, nucleic acid binding protein Proliferation 10.02 1.73
    CDKN1B CDKN1B:cyclin-dependent kinase inhibitor 1B (p27, Kip1) Proliferation 10.01 1.81
    LAS1L LAS1L:LAS1-like (S. cerevisiae) Proliferation 10.01 1.67
    SNRPD2 SNRPD2:small nuclear ribonucleoprotein D2 polypeptide 16.5kDa Proliferation 10.01 1.41
  - p54: 105 gene-like tokens; 
    UBIAD1 UBIAD1:UbiA prenyltransferase domain containing 1 Proliferation 9.87 1.34
    FEZ2 FEZ2:fasciculation and elongation protein zeta 2 (zygin II) Proliferation 9.87 1.60
    PLEKHH3:pleckstrin homology domain containing, family H (with MyTH4 domain)
    PLEKHH3 member 3 Proliferation 9.87 1.39
    VPS29 VPS29:vacuolar protein sorting 29 (yeast) Proliferation 9.86 1.68
    PAFAH1B2:platelet-activating factor acetylhydrolase, isoform Ib, beta subunit
    PAFAH1B2 30kDa Proliferation 9.85 1.55
    HIF1AN HIF1AN:hypoxia-inducible factor 1, alpha subunit inhibitor Proliferation 9.84 1.56
  - p55: 106 gene-like tokens; 
    NARG1 NARG1:NMDA receptor regulated 1 Proliferation 9.7 1.71
    DUS2L DUS2L:dihydrouridine synthase 2-like, SMM1 homolog (S. cerevisiae) Proliferation 9.7 1.50
    PARP3 PARP3:poly (ADP-ribose) polymerase family, member 3 Proliferation 9.7 1.57
    SLC36A4 SLC36A4:solute carrier family 36 (proton/amino acid symporter), member 4 Proliferation 9.7 2.22
    ACTR1A ACTR1A:ARP1 actin-related protein 1 homolog A, centractin alpha (yeast) Proliferation 9.7 1.48
    ABCA8 ABCA8:ATP-binding cassette, sub-family A (ABC1), member 8 Proliferation 9.69 1.71
    NIPBL NIPBL:Nipped-B homolog (Drosophila) Proliferation 9.69 1.29
    C17ORF42 C17ORF42:chromosome 17 open reading frame 42 Proliferation 9.68 1.55
  - p56: 109 gene-like tokens; 
    DYNC2LI1 DYNC2LI1:dynein, cytoplasmic 2, light intermediate chain 1 Proliferation 9.55 1.87
    TOB1 TOB1:transducer of ERBB2, 1 Proliferation 9.55 1.80
    SLC12A6 SLC12A6:solute carrier family 12 (potassium/chloride transporters), member 6 Proliferation 9.54 1.39
    IFI16 IFI16:interferon, gamma-inducible protein 16 Proliferation 9.53 1.85
    WDR75 WDR75:WD repeat domain 75 Proliferation 9.53 1.51
    EFNA1 EFNA1:ephrin-A1 Proliferation 9.53 1.70
    OMA1 OMA1:OMA1 homolog, zinc metallopeptidase (S. cerevisiae) Proliferation 9.53 1.61
    REEP5 REEP5:receptor accessory protein 5 Proliferation 9.53 1.48
  - p57: 100 gene-like tokens; 
    NT5E NT5E:5'-nucleotidase, ecto (CD73) Proliferation 9.39 1.61
    SMARCA5:SWI/SNF related, matrix associated, actin dependent regulator of
    SMARCA5 chromatin, subfamily a, member 5 Proliferation 9.39 1.51
    ARGLU1 na Proliferation 9.38 1.85
    USP11 USP11:ubiquitin specific peptidase 11 Proliferation 9.38 1.58
    SASS6 SASS6:spindle assembly 6 homolog (C. elegans) Proliferation 9.38 1.66
    FAM44A FAM44A:family with sequence similarity 44, member A Proliferation 9.38 1.55
    ZFAND2B ZFAND2B:zinc finger, AN1-type domain 2B Proliferation 9.37 1.71
  - p58: 99 gene-like tokens; 
    HSD17B12 HSD17B12:hydroxysteroid (17-beta) dehydrogenase 12 Proliferation 9.23 1.34
    SMC3 SMC3:structural maintenance of chromosomes 3 Proliferation 9.23 1.45
    CBWD5 CBWD5:COBW domain containing 5 Proliferation 9.23 1.53
    GABARAPL1 GABARAPL1:GABA(A) receptor-associated protein like 1 Proliferation 9.23 1.72
    TBCB na Proliferation 9.23 1.63
    FAU:Finkel-Biskis-Reilly murine sarcoma virus (FBR-MuSV) ubiquitously expressed
    FAU (fox derived); ribosomal protein S30 Proliferation 9.23 1.38
    NP NP:nucleoside phosphorylase Proliferation 9.23 1.85
  - p59: 106 gene-like tokens; 
    THOC3 THOC3:THO complex 3 Proliferation 9.1 1.36
    RRAS RRAS:related RAS viral (r-ras) oncogene homolog Proliferation 9.1 2.05
    MAPKAP1 MAPKAP1:mitogen-activated protein kinase associated protein 1 Proliferation 9.1 1.55
    PPME1 PPME1:protein phosphatase methylesterase 1 Proliferation 9.1 1.77
    MAPRE2 MAPRE2:microtubule-associated protein, RP/EB family, member 2 Proliferation 9.09 1.70
    PTRF PTRF:polymerase I and transcript release factor Proliferation 9.09 1.43
    UBLCP1 UBLCP1:ubiquitin-like domain containing CTD phosphatase 1 Proliferation 9.09 1.67
    C14ORF166 C14ORF166:chromosome 14 open reading frame 166 Proliferation 9.09 1.46
  - p60: 107 gene-like tokens; 
    (Drosophila)
    KIAA0746 KIAA0746:- Proliferation 9 1.54
    MUT MUT:methylmalonyl Coenzyme A mutase Proliferation 9 1.75
    GLRX5 GLRX5:glutaredoxin 5 homolog (S. cerevisiae) Proliferation 9 1.45
    PTCD1 PTCD1:pentatricopeptide repeat domain 1 Proliferation 8.99 1.72
    NCKIPSD NCKIPSD:NCK interacting protein with SH3 domain Proliferation 8.98 1.72
    GNG12 GNG12:guanine nucleotide binding protein (G protein), gamma 12 Proliferation 8.98 1.72
    CEBPB CEBPB:CCAAT/enhancer binding protein (C/EBP), beta Proliferation 8.98 1.56
  - p61: 108 gene-like tokens; 
    ULK1 ULK1:unc-51-like kinase 1 (C. elegans) Proliferation 8.89 2.08
    RP9 RP9:retinitis pigmentosa 9 (autosomal dominant) Proliferation 8.88 1.51
    UBQLN2 UBQLN2:ubiquilin 2 Proliferation 8.87 1.70
    WDR33 WDR33:WD repeat domain 33 Proliferation 8.87 1.62
    NDN NDN:necdin homolog (mouse) Proliferation 8.87 2.00
    TSPAN9 TSPAN9:tetraspanin 9 Proliferation 8.87 1.92
    CHD8 CHD8:chromodomain helicase DNA binding protein 8 Proliferation 8.86 1.41
    PUS3 PUS3:pseudouridylate synthase 3 Proliferation 8.86 1.50
  - p62: 107 gene-like tokens; 
    DRAP1 DRAP1:DR1-associated protein 1 (negative cofactor 2 alpha) Proliferation 8.74 1.69
    FBXO38 FBXO38:F-box protein 38 Proliferation 8.74 1.29
    C15ORF23 C15ORF23:chromosome 15 open reading frame 23 Proliferation 8.74 1.52
    MPZL1 MPZL1:myelin protein zero-like 1 Proliferation 8.74 1.43
    FRG1 FRG1:FSHD region gene 1 Proliferation 8.73 1.46
    NPL NPL:N-acetylneuraminate pyruvate lyase (dihydrodipicolinate synthase) Proliferation 8.73 1.36
    THSD1P THSD1P:thrombospondin, type I, domain containing 1 pseudogene Proliferation 8.73 1.49
    BAG5 BAG5:BCL2-associated athanogene 5 Proliferation 8.72 1.40
  - p63: 103 gene-like tokens; 
    UBA6 na Proliferation 8.62 1.40
    EXOC7 EXOC7:exocyst complex component 7 Proliferation 8.61 1.48
    TMEM49 TMEM49:transmembrane protein 49 Proliferation 8.61 1.98
    LYRM1 LYRM1:LYR motif containing 1 Proliferation 8.61 1.71
    PFAS PFAS:phosphoribosylformylglycinamidine synthase (FGAR amidotransferase) Proliferation 8.61 1.53
    PSMB6 PSMB6:proteasome (prosome, macropain) subunit, beta type, 6 Proliferation 8.61 1.43
    KLHL22 KLHL22:kelch-like 22 (Drosophila) Proliferation 8.6 1.51
    GFOD2 GFOD2:glucose-fructose oxidoreductase domain containing 2 Proliferation 8.6 1.35
  - p64: 109 gene-like tokens; 
    SMARCD1:SWI/SNF related, matrix associated, actin dependent regulator of
    SMARCD1 chromatin, subfamily d, member 1 Proliferation 8.5 1.58
    AXUD1 AXUD1:AXIN1 up-regulated 1 Proliferation 8.5 1.51
    CCDC112 CCDC112:coiled-coil domain containing 112 Proliferation 8.49 1.41
    ZFP36L2 ZFP36L2:zinc finger protein 36, C3H type-like 2 Proliferation 8.48 1.54
    ZNF573 ZNF573:zinc finger protein 573 Proliferation 8.48 1.39
    OCLN OCLN:occludin Proliferation 8.48 1.59
    KIAA0256 KIAA0256:- Proliferation 8.48 1.46
  - p65: 96 gene-like tokens; 
    CTDSPL:CTD (carboxy-terminal domain, RNA polymerase II, polypeptide A) small
    CTDSPL phosphatase-like Proliferation 8.36 1.88
    RNF14 RNF14:ring finger protein 14 Proliferation 8.36 1.64
    NCAPD2 NCAPD2:non-SMC condensin I complex, subunit D2 Proliferation 8.36 1.73
    FAM113B FAM113B:family with sequence similarity 113, member B Proliferation 8.36 1.67
    AGGF1 AGGF1:angiogenic factor with G patch and FHA domains 1 Proliferation 8.35 1.45
    STT3B:STT3, subunit of the oligosaccharyltransferase complex, homolog B (S.
    STT3B cerevisiae) Proliferation 8.35 1.54
  - p66: 102 gene-like tokens; 
    CEP97 na Inflammation -8.87 1.56
    IL19 IL19:interleukin 19 Inflammation -8.89 2.21
    XPNPEP3 XPNPEP3:X-prolyl aminopeptidase (aminopeptidase P) 3, putative Inflammation -8.9 1.49
    HMGB4 HMGB4:high-mobility group box 4 Inflammation -8.9 1.64
    DCTN3 DCTN3:dynactin 3 (p22) Inflammation -8.91 1.45
    C1ORF95 C1ORF95:chromosome 1 open reading frame 95 Inflammation -8.91 1.95
    APRT APRT:adenine phosphoribosyltransferase Inflammation -8.92 1.65
    NBPF1 NBPF1:neuroblastoma breakpoint family, member 1 Inflammation -8.93 2.88
  - p67: 98 gene-like tokens; 
    RPL34 RPL34:ribosomal protein L34 Inflammation -9.5 1.65
    CRYBB2 CRYBB2:crystallin, beta B2 Inflammation -9.51 2.00
    LOC648148 LOC648148:- Inflammation -9.51 2.35
    FLJ40453 FLJ40453:- Inflammation -9.53 1.80
    TBCD TBCD:tubulin-specific chaperone d Inflammation -9.57 2.14
    C11ORF55 C11ORF55:chromosome 11 open reading frame 55 Inflammation -9.58 1.87
    FLJ45966 FLJ45966:- Inflammation -9.59 1.61
    C14ORF85 C14ORF85:chromosome 14 open reading frame 85 Inflammation -9.61 1.81
  - p68: 83 gene-like tokens; 
    BRIP1 BRIP1:BRCA1 interacting protein C-terminal helicase 1 Inflammation -10.89 2.32
    RFX4 RFX4:regulatory factor X, 4 (influences HLA class II expression) Inflammation -10.95 1.93
    IKZF4 IKZF4:IKAROS family zinc finger 4 (Eos) Inflammation -10.99 1.77
    C21ORF24 C21ORF24:chromosome 21 open reading frame 24 Inflammation -11 1.83
    FAM119A FAM119A:family with sequence similarity 119, member A Inflammation -11.01 1.80
    LOC221091 LOC221091:- Inflammation -11.08 1.93
    A1BG A1BG:alpha-1-B glycoprotein Inflammation -11.18 1.81
    IQWD1 IQWD1:IQ motif and WD repeats 1 Inflammation -11.18 1.38
  - p69: 52 gene-like tokens; Supplementary Table 3: GSEA resuts. Pathways enriched in Proliferation class
    Supplementary Table 3: GSEA resuts. Pathways enriched in Proliferation class
    #· FDR
    Gene set name Database genes NES p-value q-val
    BIOCARTA_MTA3_PATHWAY MsigDB V3/c2 15 -2.15 < 0.001 0.00
    BIOCARTA_ECM_PATHWAY MsigDB V3/c2 22 -2.12 < 0.001 0.00
    BIOCARTA_RACCYCD_PATHWAY MsigDB V3/c2 22 -2.10 < 0.001 0.00
    BIOCARTA_FAS_PATHWAY MsigDB V3/c2 28 -2.06 < 0.001 0.01
    BIOCARTA_AT1R_PATHWAY MsigDB V3/c2 27 -2.01 < 0.001 0.01
  - p70: 46 gene-like tokens; 
    KEGG_PROTEIN_EXPORT MsigDB V3/c2 18 -1.82 0.00 0.02
    KEGG_REGULATION_OF_ACTIN_CYTOSKELETON MsigDB V3/c2 167 -1.81 < 0.001 0.02
    KEGG_EPITHELIAL_CELL_SIGNALING_IN_HELICOBACTER
    _PYLORI_INFECTION MsigDB V3/c2 60 -1.80 0.00 0.02
    KEGG_GLIOMA MsigDB V3/c2 52 -1.79 < 0.001 0.02
    KEGG_ALZHEIMERS_DISEASE MsigDB V3/c2 127 -1.79 < 0.001 0.02
    KEGG_PARKINSONS_DISEASE MsigDB V3/c2 92 -1.76 0.00 0.02
    KEGG_RNA_DEGRADATION MsigDB V3/c2 50 -1.75 0.00 0.03
  - p71: 51 gene-like tokens; 
    REACTOME_CYCLIN_E_ASSOCIATED_EVENTS_DURING
    _G1_S_TRANSITION_ MsigDB V3/c2 49 -2.05 < 0.001 0.00
    REACTOME_GENE_EXPRESSION MsigDB V3/c2 333 -2.04 < 0.001 0.00
    REACTOME_MRNA_3_END_PROCESSING MsigDB V3/c2 25 -2.04 < 0.001 0.00
    REACTOME_G1_PHASE MsigDB V3/c2 13 -2.02 < 0.001 0.00
    REACTOME_M_G1_TRANSITION MsigDB V3/c2 52 -2.01 < 0.001 0.00
    REACTOME_CELL_CYCLE_MITOTIC MsigDB V3/c2 242 -1.98 < 0.001 0.00
    REACTOME_APOPTOSIS MsigDB V3/c2 111 -1.98 < 0.001 0.00
  - p72: 53 gene-like tokens; 
    REACTOME_FORMATION_OF_A_POOL_OF_FREE_40S_SUBUNITS MsigDB V3/c2 74 -1.71 0.00 0.03
    REACTOME_INTEGRIN_CELL_SURFACE_INTERACTIONS MsigDB V3/c2 72 -1.70 0.00 0.03
    REACTOME_INACTIVATION_OF_APC_VIA_DIRECT_INHIBITION_
    OF_THE_APCOMPLEX MsigDB V3/c2 15 -1.70 0.02 0.03
    REACTOME_APCDC20_MEDIATED_DEGRADATION_OF_CYCLIN_B MsigDB V3/c2 15 -1.69 0.01 0.03
    REACTOME_PYRUVATE_METABOLISM_AND_TCA_CYCLE MsigDB V3/c2 28 -1.69 0.01 0.03
    REACTOME_INFLUENZA_LIFE_CYCLE MsigDB V3/c2 109 -1.68 0.00 0.04
    REACTOME_GLUCOSE_METABOLISM MsigDB V3/c2 47 -1.68 0.01 0.04
  - p73: 41 gene-like tokens; 
    ENDOPLASMIC_RETICULUM MsigDB V3/c5 225 -1.88 < 0.001 0.03
    CYTOPLASMIC_VESICLE_PART MsigDB V3/c5 24 -1.88 < 0.001 0.03
    UNFOLDED_PROTEIN_BINDING MsigDB V3/c5 36 -1.87 < 0.001 0.03
    TRANSCRIPTION_COACTIVATOR_ACTIVITY MsigDB V3/c5 98 -1.87 < 0.001 0.03
    NUCLEAR_PART MsigDB V3/c5 446 -1.87 < 0.001 0.03
    RIBONUCLEOPROTEIN_COMPLEX MsigDB V3/c5 105 -1.87 < 0.001 0.03
    ATPASE_ACTIVITY_COUPLED MsigDB V3/c5 81 -1.87 < 0.001 0.03
    MRNA_SPLICE_SITE_SELECTION MsigDB V3/c5 10 -1.86 0.00 0.03
  - p74: 17 gene-like tokens; Supplementary Table 4: GSEA of HCC signatures in Proliferation class
  - p75: 52 gene-like tokens; Supplementary Table 5: GSEA results. Pathways enriched in Inflammation class
    Supplementary Table 5: GSEA results. Pathways enriched in Inflammation class
    #· FDR
    Gene set name Database genes NES p-value q-val
    BIOCARTA_ASBCELL_PATHWAY MsigDB V3/c2 9 1.89 < 0.001 0.06
    BIOCARTA_STEM_PATHWAY MsigDB V3/c2 12 1.73 0.01 0.12
    BIOCARTA_DC_PATHWAY MsigDB V3/c3 15 1.59 0.04 0.21
    BIOCARTA_IL5_PATHWAY MsigDB V3/c4 8 1.55 0.06 0.20
    BIOCARTA_CYTOKINE_PATHWAY MsigDB V3/c5 14 1.52 0.04 0.19
  - p77: 3 gene-like tokens; Supplementary Table 6: Chromosomal arm-level genomic DNA copy number alterations
  - p78: 25 gene-like tokens; Supplementary Table 7: FISH analysis of 11q13 high-level amplifications
  - p79: 407 gene-like tokens; Supplementary Table 8: Focal deletions in ICC samples
    Supplementary Table 8: Focal deletions in ICC samples
    1p36.3 19q13.4
    cytoband 2 1p36.21 1p35.2 2p15 3p25.3 4q34.2 4q35.1 5q13.2 6p11.1 6q21 7q36.1 9p24.1 9p21.3 9p21.3 9p21.1 9q21.13 10q23.2 10q26.13 12p13.2 1
    3.45E- 5.36E- 7.58E-
    q value 08 07 06 0.26843 0.206 0.176 0.002 0.176 0.222 0.204 0.052 0.176 5.36E-07 0.032 0.121 0.181 0.101 0.015 0.177 070 0.176 0.202 0.181 
    residual q 2.56E-
    value 06 0.033 0.101 0.268 0.207 0.221 0.003 0.176 0.222 0.204 0.0612 0.176 5.36E-07 0.068 0.119 0.176 0.101 0.014707 0.176 0.269 0.176 0.19
    chr1:22 chr13:90
  - p80: 519 gene-like tokens; 
    ATP6V1
    EXTL1 ENO1 B1 UFSP2 PPWD1 SLC4A2 ARL1 ZMYM5 LGMN CDH3 AXL NDUFA6
    EYA3 EPB41 KIF1A CDKN2AIP SKIV2L2 SMARCD3 ART4 KL PSMC1 CDH5 AZU1 NHP2L1
    FGR EPHA8 AUP1 ODZ3 DIMT1L AKR1D1 ASCL1 MTRF1 RAGE CDH8 BAX PDGFB
    FRAP1 EPHB2 BARD1 LRP2BP IPO11 SSBP1 ATF1 NUPL1 SEL1L CDH11 BCAT2 PMM1
    BCKDH
    FUCA1 EXTL1 BCS1L TUBB4Q PELO TBXAS1 ATP2A2 FRY TNFAIP2 CDH13 A POLR2F
    IFI6 EYA3 BMPR2 STOX2 DHX29 VIPR2 ATP2B1 SLC25A15 TRAF3 CDH15 BCL3 PPARA
  - p81: 423 gene-like tokens; 
    MAP3K7IP
    RPL22 PLOD1 DARS SERF1B LUC7L2 DDX11 KATNAL1 ASB2 GLG1 CNN2 1
    RPS6K EXOS LOC73039
    A1 C10 DBI 4 MRPS33 ATN1 KBTBD7 CPSF2 GNAO1 COMP SLC25A17
    RSC1A PPP1R COX6B
    1 8 DCTN1 NUB1 EPYC C13orf33 KCNK10 GOT2 1 DDX17
    SCNN1 COX7A
    D PRKCZ DDX1 TAS2R5 DTX1 KBTBD6 CDCA4 GP2 1 NUP50
  - p82: 370 gene-like tokens; 
    HOXC1
    ZBTB40 EIF4G3 GLS NOBOX 2 C14orf172 MT1E FLT3LG RIBC2
    TNFRS HOXC1
    MFN2 F25 GPC1 OR2A14 3 TDRD9 MT1F FOSB ARFGAP3
    TNFRS
    ELA3A F14 GPD2 OR6B1 HPD ANKRD9 MT1G FPR1 SMC1B
    TNFRS
    WASF2 F18 GPR1 OR2F2 IAPP AK7 MT1H FPRL1 PSCD4
  - p83: 320 gene-like tokens; 
    STX12 ACOT7 IL8RA GSTK1 LRMP RPL13 ICAM4 SCUBE1
    DNAJC
    CLIC4 8 IL8RB UNQ1940 LRP1 RPS2 IL11 TRABD
    CLSTN RPS15 IL12RB
    SYF2 1 INHA OR2A25 LRP6 A 1 PNPLA3
    AKR7A
    CHD5 3 INHBB OR2A5 LTA4H RRAD ILF3 APOL6
    C1orf14
  - p84: 277 gene-like tokens; 
    AURKAI HP1BP APOBEC3
    P1 3 MYO7B OLR1 ZNF23 MYO1F A
    MRPL2 MYBPC
    0 ELA2B NAB1 P2RX4 ZNF75A 2 APOBEC3F
    ZNF59 GADD4
    AIM1L 3 NCL P2RX7 ZNF174 5B SERHL2
    TMEM5
    1 MECR NEB PA2G4 ZNF200 MYO9B MGC70863
  - p85: 265 gene-like tokens; 
    1
    DNAJC SLC9A3
    PINK1 11 PRKCE PEX5 R2 PKN1
    PRAME EIF2AK PRKCS
    F1 RCC2 2 PZP LITAF H
    PRAME MAP2K
    F2 AJAP1 PROC RAB5B BCAR1 2
    C1orf9 MAP2K
  - p86: 252 gene-like tokens; 
    9
    KIAA17 CD2BP
    51 OR4F5 SOS1 TARBP2 2 RPS16
    KIAA20 NKAIN
    13 1 SOX11 TBX5 CDIPT RPS19
    THAP3 MUL1 SP3 TBX3 CFDP1 RPS28
    C1orf20 MRPL2
    1 NOL9 SP100 HNF1A 8 RRAS
  - p87: 264 gene-like tokens; 
    TYROB
    TTLL10 UBXD5 ZNF142 ULK1 NOMO1 P
    C1orf1 SLC30A
    TMCO4 58 3 EEA1 TPSD1 UBA52
    FBXO4
    ZNF683 4 PXDN SOAT2 SF3B3 NR1H2
    UQCRF
    NPHP4 ATPIF1 ALMS1 RASAL1 QPRT S1
  - p88: 250 gene-like tokens; 
    LDLRA TMEM2 ST3GA
    D2 01 L5 SART3 BRD7 ZNF228
    PRAME C1orf8 ANKRD
    F6 6 SLC5A6 KNTC1 11 ZNF229
    LOC440 ZDHHC
    567 TXLNA DDX18 CLSTN3 1 ZNF230
    C1orf15 ATAD3 KIAA015 MADCA
    1 C EIF2B4 2 UBN1 M1
  - p89: 218 gene-like tokens; 
    PRAM
    EF17 EIF5B CCT2 A2BP1 ZNF235
    PLA2G SLCO1B KLHDC
    2C GREB1 1 4 TRIP10
    TMEM2 RAD51A
    00B BZW1 P1 HYDIN LONP1
    PRAM CAMKK
    EF4 USP34 2 NDE1 ZNF264
  - p90: 176 gene-like tokens; 
    C16orf6 B3GNT
    MERTK PHLDA1 2 3
    UBE2E R3HDM TMEM1 CLEC4
    3 2 59 M
    STK25 MLXIP LYRM1 ABCA7
    SEMA4 THAP1 HMG20
    F RPH3A 1 B
    CCT7 KLRK1 JPH3 KLF2
  - p91: 176 gene-like tokens; 
    COBLL FGFR1
    1 OP2 NDRG4 LILRA2
    AAK1 CLEC4E ACD UPK1A
    FASTK HNRPU
    D2 FBXW8 ZNF747 L1
    MAPRE C16orf2
    3 GALNT8 4 SFRS16
    MRPS3
  - p92: 172 gene-like tokens; 
    POLR1 CCDC4 RBM35
    A 1 B CASP14
    CNRIP1 IRAK4 NIP30 ZIM2
    FAM98 ATF7IP
    A ING4 2 CBLC
    ATPBD1
    PNKD C CENPT NUP62
    C16orf5 HSPBP
  - p93: 176 gene-like tokens; 
    C12orf4
    GMPPA 8 SPIRE2 ZBTB32
    SIGLEC
    NRBP1 TAPBPL DCTN5 7
    SLC38A
    BAZ2B 4 MT4 LYPD3
    SLC40A MAGOH ARRDC
    1 B GNPTG 2
  - p94: 165 gene-like tokens; 
    FLYWC
    VPS24 PRMT8 H2 MRPL4
    NDUFA
    FKBP7 DIABLO VASN 13
    ANGPT
    ASB1 MDM1 ZNF689 L4
    SLC5A1
    CPSF3 ANKS1B 1 ZNF580
  - p95: 168 gene-like tokens; 
    ANKZF SLC26A PGPEP
    1 10 CMTM2 1
    CC2D1
    RIF1 VPS33A TEKT5 A
    USP40 RSRC2 RNF151 EPS8L1
    MOBKL LOC146
    1B WNK1 325 RASIP1
    STEAP TMEM1
  - p96: 161 gene-like tokens; 
    UGCGL SLC38A MPV17 C19orf1
    1 1 L 0
    FAM130 C16orf6 C19orf6
    KCMF1 A1 5 1
    DPYSL TMEM1
    5 APOLD1 88 ZNF253
    ANKS4
    PNO1 GSG1 B IRGC
  - p97: 142 gene-like tokens; 
    C12orf5 PLEKH
    C2orf43 2 NOMO3 A4
    LOC440
    THADA MFSD5 348 ZFP14
    C12orf6 LOC440
    RBKS 2 350 ZNF317
    GAL3S
    T2 RERG CTRB2 ZNF529
  - p98: 124 gene-like tokens; 
    C2orf47 MUCL1 YIPF2
    SPAG1 DEPDC C19orf4
    6 4 3
    CHPF LRRK2 DDA1
    CCDC3 C19orf5
    SAP130 8 0
    GALNT C12orf5 TMEM3
    14 9 8A
  - p99: 131 gene-like tokens; 
    TMEM1 GLIPR1 SLC35E
    77 L2 1
    KIAA17 FAM101
    15 A PRG2
    DENND
    ILKAP ZNF664 1C
    FAM49 FLJ3289
    A 4 ZNF442
  - p100: 128 gene-like tokens; 
    SFT2D3 FAM71C FBXW9
    CCDC1 C12orf1
    42 2 ALKBH7
    C12orf5
    ZNF514 3 MORG1
    FAM13 PDCD2
    6A DCP1B L
    TMEM8 TMEM1
  - p101: 128 gene-like tokens; 
    C12orf4 MBD3L
    FMNL2 0 1
    CCDC8
    5A GLT8D3 GALP
    GALNT TMPRS SIGLEC
    13 S12 10
    OSBPL SIGLEC
    6 KRT6C 12
  - p102: 112 gene-like tokens; 
    ACVR1 PEX11
    C OR6C65 G
    OSR1 OR6C68 DMKN
    TTC32 IQSEC3 ZNF561
    ZNF705
    UBR3 A OLFM2
    KCTD1 LOC440 CCDC1
    8 087 14
  - p103: 88 gene-like tokens; 
    ALS2C MGC20
    R13 983
    TCF23 ZNF653
    PUS10 ZNF526
    10-Sep GRIN3B
    MRPL5
    C2orf67 4
    PLB1 LRG1
  - p104: 85 gene-like tokens; 
    PCDP1 ZNF57
    VWA3B IRGQ
    CREG2 ZNF428
    TET3 JSRP1
    MOBKL
    GKN2 2A
    C19orf2
    C2orf51 8
  - p105: 84 gene-like tokens; 
    C1
    ESPNL IGFL2
    LOC339
    778 ZNF420
    C2orf53 ZNF565
    MSGN1 NLRP4
    C2orf55 ZNF582
    FIGLA ZNF583
  - p106: 69 gene-like tokens; 
    LOC402
    117 ZNF567
    MGC50
    273 ZNF383
    HCG3 ZNF781
    ASTL EID2
    FLJ468 ZNF780
    38 B
  - p107: 43 gene-like tokens; 
    ZSCAN
    1
    ZNF780
    A
    C19orf5
    4
    PRR19
    TMEM1
  - p108: 47 gene-like tokens; 
    ZNF404
    ZNF284
    ZNF677
    LOC342
    933
    ZSCAN
    22
    NANOS
  - p110: 1 gene-like tokens; Supplementary Table 9: Focal deletions frequency in ICC classes
  - p112: 108 gene-like tokens; Supplementary Table 10: Mutations analysis in ICC samples
    Supplementary Table 10: Mutations analysis in ICC samples
    Case ID ICC class Gene Codon Wild-Type Mutation Amino acid substitution
    CCM003 Proliferation KRAS 12 GGT CGT G12R
    CCM019 Inflammation KRAS 12 GGT GAT G12D
    CCM024 Proliferation KRAS 12 GGT GAT G12D
    CCM033 Proliferation KRAS 12 GGT GAT G12D
    CCM036 Proliferation KRAS 12 GGT GTT G12V
    CCM060 Proliferation KRAS 12 GGT GTT G12V
  - p113: 54 gene-like tokens; Supplementary Table 11: GSEA results. Pathways and signatures enriched in P1-3 subgroups
    Supplementary Table 11: GSEA results. Pathways and signatures enriched in P1-3 subgroups
    p- FDR Enriched
    Gene set name Database #· genes NES
    value q value in
    BIOCARTA_DNAFRAGMENT_PATHWAY MsigDB V3/c2 10 -1.70 0.02 0.17 P1
    BIOCARTA_ETS_PATHWAY MsigDB V3/c2 17 -1.69 0.01 0.18 P1
    BIOCARTA_BCELLSURVIVAL_PATHWAY MsigDB V3/c2 13 -1.68 0.01 0.18 P1
    BIOCARTA_FCER1_PATHWAY MsigDB V3/c2 32 -1.70 0.01 0.18 P1
  - p115: 3 gene-like tokens; Supplementary Table 12: ICC signature prediction in an independent CC data set
  - p116: 65 gene-like tokens; Supplementary Table 13: ICC survival signature
    Supplementary Table 13: ICC survival signature
    Gene symbol Gene Name Correlated with Cox score
    CGB1 CGB1:chorionic gonadotropin, beta polypeptide 1 Poor 5.29
    ITGB6 ITGB6:integrin, beta 6 Poor 4.68
    MUC4 MUC4:mucin 4, cell surface associated Poor 4.31
    CXCL17 na Poor 4.17
    CTNNAL1 CTNNAL1:catenin (cadherin-associated protein), alpha-like 1 Poor 3.98
    CCNA2 CCNA2:cyclin A2 Poor 3.97
  - p117: 64 gene-like tokens; 
    ANXA1 ANXA1:annexin A1 Poor 3.33
    LMNA LMNA:lamin A/C Poor 3.33
    TUBA1C na Poor 3.31
    CIDEC CIDEC:cell death-inducing DFFA-like effector c Poor 3.29
    NUF2 na Poor 3.29
    TMEM41A TMEM41A:transmembrane protein 41A Poor 3.28
    ARPC1B ARPC1B:actin related protein 2/3 complex, subunit 1B, 41kDa Poor 3.25
    GPR110 GPR110:G protein-coupled receptor 110 Poor 3.22
  - p118: 68 gene-like tokens; 
    SHFM1 SHFM1:split hand/foot malformation (ectrodactyly) type 1 Poor 3.05
    AP2S1 AP2S1:adaptor-related protein complex 2, sigma 1 subunit Poor 3.05
    GNG12 GNG12:guanine nucleotide binding protein (G protein), gamma 12 Poor 3.05
    MT1X MT1X:metallothionein 1X Poor 3.04
    CA3 CA3:carbonic anhydrase III, muscle specific Poor 3.04
    ARL3 ARL3:ADP-ribosylation factor-like 3 Poor 3.03
    CD151 CD151:CD151 molecule (Raph blood group) Poor 3.00
    PLOD2 PLOD2:procollagen-lysine, 2-oxoglutarate 5-dioxygenase 2 Poor 2.97
  - p119: 68 gene-like tokens; 
    KRT10 KRT10:keratin 10 (epidermolytic hyperkeratosis; keratosis palmaris et plantaris) Poor 2.85
    TM4SF1 TM4SF1:transmembrane 4 L six family member 1 Poor 2.84
    PRAMEF12 PRAMEF12:PRAME family member 12 Poor 2.84
    MRPL45 MRPL45:mitochondrial ribosomal protein L45 Poor 2.83
    HP1BP3 HP1BP3:heterochromatin protein 1, binding protein 3 Poor 2.82
    TCEA1 TCEA1:transcription elongation factor A (SII), 1 Poor 2.82
    AHR AHR:aryl hydrocarbon receptor Poor 2.82
    ACY3 ACY3:aspartoacylase (aminocyclase) 3 Poor 2.81
  - p120: 74 gene-like tokens; 
    TCEA2 TCEA2:transcription elongation factor A (SII), 2 Poor 2.72
    PRPF4 PRPF4:PRP4 pre-mRNA processing factor 4 homolog (yeast) Poor 2.72
    FAM108B1 na Poor 2.72
    PIK3CA PIK3CA:phosphoinositide-3-kinase, catalytic, alpha polypeptide Poor 2.71
    PRB2 PRB2:proline-rich protein BstNI subfamily 2 Poor 2.71
    TRIM59 TRIM59:tripartite motif-containing 59 Poor 2.71
    C17ORF81 C17ORF81:chromosome 17 open reading frame 81 Poor 2.71
    UTP6 UTP6:UTP6, small subunit (SSU) processome component, homolog (yeast) Poor 2.70
  - p121: 69 gene-like tokens; 
    CFB CFB:complement factor B Poor 2.61
    ANLN ANLN:anillin, actin binding protein Poor 2.60
    BCKDK BCKDK:branched chain ketoacid dehydrogenase kinase Poor 2.60
    UBE2E3 UBE2E3:ubiquitin-conjugating enzyme E2E 3 (UBC4/5 homolog, yeast) Poor 2.60
    C1S C1S:complement component 1, s subcomponent Poor 2.60
    ATP5H ATP5H:ATP synthase, H+ transporting, mitochondrial F0 complex, subunit d Poor 2.60
    C19ORF66 na Poor 2.59
    SLC7A5P1 na Poor 2.59
  - p122: 60 gene-like tokens; 
    LMF2 na Poor 2.52
    LIN9 LIN9:lin-9 homolog (C. elegans) Poor 2.52
    ENY2 ENY2:enhancer of yellow 2 homolog (Drosophila) Poor 2.51
    KRTAP5-2 KRTAP5-2:keratin associated protein 5-2 Poor 2.51
    EPN1 EPN1:epsin 1 Poor 2.50
    NME7 NME7:non-metastatic cells 7, protein expressed in (nucleoside-diphosphate kinase) Poor 2.50
    EGFR EGFR:epidermal growth factor receptor (erythroblastic leukemia viral (v-erb-b) oncogene homolog, avian) Poor 2.50
    HIST1H2AB HIST1H2AB:histone cluster 1, H2ab Poor 2.49
  - p123: 61 gene-like tokens; 
    ZYX ZYX:zyxin Poor 2.41
    PAFAH1B3 PAFAH1B3:platelet-activating factor acetylhydrolase, isoform Ib, gamma subunit 29kDa Poor 2.41
    CCNF CCNF:cyclin F Poor 2.41
    CCDC90B na Poor 2.40
    MGST1 MGST1:microsomal glutathione S-transferase 1 Poor 2.40
    PNPLA6 PNPLA6:patatin-like phospholipase domain containing 6 Poor 2.40
    METTL5 METTL5:methyltransferase like 5 Poor 2.40
    G0S2 G0S2:G0/G1switch 2 Poor 2.39
  - p124: 77 gene-like tokens; 
    YTHDF2 YTHDF2:YTH domain family, member 2 Poor 2.33
    PIR PIR:pirin (iron-binding nuclear protein) Poor 2.33
    POLR2F POLR2F:polymerase (RNA) II (DNA directed) polypeptide F Poor 2.33
    EFEMP1 EFEMP1:EGF-containing fibulin-like extracellular matrix protein 1 Poor 2.32
    HDHD3 HDHD3:haloacid dehalogenase-like hydrolase domain containing 3 Poor 2.32
    NDUFS5 NDUFS5:NADH dehydrogenase (ubiquinone) Fe-S protein 5, 15kDa (NADH-coenzyme Q reductase) Poor 2.31
    PSMC3 PSMC3:proteasome (prosome, macropain) 26S subunit, ATPase, 3 Poor 2.30
    REXO1 REXO1:REX1, RNA exonuclease 1 homolog (S. cerevisiae) Poor 2.30
  - p125: 74 gene-like tokens; 
    TMEM56 TMEM56:transmembrane protein 56 Poor 2.24
    SUMO4 SUMO4:SMT3 suppressor of mif two 3 homolog 4 (S. cerevisiae) Poor 2.24
    F13B F13B:coagulation factor XIII, B polypeptide Poor 2.24
    AURKAIP1 AURKAIP1:aurora kinase A interacting protein 1 Poor 2.24
    RCN3 RCN3:reticulocalbin 3, EF-hand calcium binding domain Poor 2.24
    WTAP WTAP:Wilms tumor 1 associated protein Poor 2.24
    RNF26 RNF26:ring finger protein 26 Poor 2.24
    SETD7 SETD7:SET domain containing (lysine methyltransferase) 7 Poor 2.23
  - p126: 69 gene-like tokens; 
    C20ORF54 C20ORF54:chromosome 20 open reading frame 54 Poor 2.15
    ATP5J2 ATP5J2:ATP synthase, H+ transporting, mitochondrial F0 complex, subunit F2 Poor 2.14
    CDO1 CDO1:cysteine dioxygenase, type I Poor 2.14
    MPI MPI:mannose phosphate isomerase Poor 2.14
    TMED9 TMED9:transmembrane emp24 protein transport domain containing 9 Poor 2.13
    GPR124 GPR124:G protein-coupled receptor 124 Poor 2.13
    DEGS1 DEGS1:degenerative spermatocyte homolog 1, lipid desaturase (Drosophila) Poor 2.13
    KIAA1754 KIAA1754:KIAA1754 Poor 2.13
  - p127: 60 gene-like tokens; 
    LOC374395 LOC374395:- Poor 2.04
    SBNO1 SBNO1:strawberry notch homolog 1 (Drosophila) Poor 2.04
    USP28 USP28:ubiquitin specific peptidase 28 Poor 2.03
    H2AFJ H2AFJ:H2A histone family, member J Poor 2.03
    NTN4 NTN4:netrin 4 Poor 2.02
    LOC653566 LOC653566:- Poor 2.01
    PCDH17 PCDH17:protocadherin 17 Poor 2.01
    BCL10 BCL10:B-cell CLL/lymphoma 10 Poor 2.01
  - p128: 70 gene-like tokens; 
    TTF2 TTF2:transcription termination factor, RNA polymerase II Good -2.06
    DKFZP564O0 DKFZP564O0823:- Good -2.07
    823
    FLJ35773 FLJ35773:- Good -2.07
    BCLAF1 BCLAF1:BCL2-associated transcription factor 1 Good -2.08
    FCRLA FCRLA:Fc receptor-like A Good -2.08
    RAPGEF1 RAPGEF1:Rap guanine nucleotide exchange factor (GEF) 1 Good -2.10
    IL6R IL6R:interleukin 6 receptor Good -2.11
  - p129: 68 gene-like tokens; 
    TMEM203 na Good -2.26
    ELK1 ELK1:ELK1, member of ETS oncogene family Good -2.26
    ZNF223 ZNF223:zinc finger protein 223 Good -2.27
    IL1F6 IL1F6:interleukin 1 family, member 6 (epsilon) Good -2.27
    OR11H6 OR11H6:olfactory receptor, family 11, subfamily H, member 6 Good -2.28
    FAM119A FAM119A:family with sequence similarity 119, member A Good -2.28
    RBM9 RBM9:RNA binding motif protein 9 Good -2.28
    SLC35A4 SLC35A4:solute carrier family 35, member A4 Good -2.28
  - p130: 72 gene-like tokens; 
    DDX19A DDX19A:DEAD (Asp-Glu-Ala-As) box polypeptide 19A Good -2.37
    B3GAT3 B3GAT3:beta-1,3-glucuronyltransferase 3 (glucuronosyltransferase I) Good -2.37
    CHMP2A CHMP2A:chromatin modifying protein 2A Good -2.37
    PRX PRX:periaxin Good -2.37
    ACTRT1 ACTRT1:actin-related protein T1 Good -2.37
    ARIH2 ARIH2:ariadne homolog 2 (Drosophila) Good -2.38
    HCG9 HCG9:HLA complex group 9 Good -2.38
    TAS2R43 TAS2R43:taste receptor, type 2, member 43 Good -2.38
  - p131: 65 gene-like tokens; 
    TBC1D10C TBC1D10C:TBC1 domain family, member 10C Good -2.45
    BMP2K BMP2K:BMP2 inducible kinase Good -2.45
    SGK3 SGK3:serum/glucocorticoid regulated kinase family, member 3 Good -2.46
    AKT1 AKT1:v-akt murine thymoma viral oncogene homolog 1 Good -2.46
    ANAPC4 ANAPC4:anaphase promoting complex subunit 4 Good -2.46
    DAZAP2 DAZAP2:DAZ associated protein 2 Good -2.47
    KIAA0406 KIAA0406:KIAA0406 Good -2.48
    CD27 na Good -2.48
  - p132: 61 gene-like tokens; 
    GGA2 GGA2:golgi associated, gamma adaptin ear containing, ARF binding protein 2 Good -2.60
    CCDC148 na Good -2.61
    CSK CSK:c-src tyrosine kinase Good -2.61
    SASH3 na Good -2.62
    6-Sep na Good -2.63
    GDAP2 GDAP2:ganglioside induced differentiation associated protein 2 Good -2.63
    FRAT2 FRAT2:frequently rearranged in advanced T-cell lymphomas 2 Good -2.65
    GNPDA1 GNPDA1:glucosamine-6-phosphate deaminase 1 Good -2.65
  - p133: 43 gene-like tokens; 
    MGA MGA:MAX gene associated Good -2.84
    BCS1L BCS1L:BCS1-like (yeast) Good -2.87
    KRTAP10-10 KRTAP10-10:keratin associated protein 10-10 Good -2.87
    GTPBP10 GTPBP10:GTP-binding protein 10 (putative) Good -2.88
    FUT7 FUT7:fucosyltransferase 7 (alpha (1,3) fucosyltransferase) Good -2.91
    INSL6 INSL6:insulin-like 6 Good -2.92
    CDKL5 CDKL5:cyclin-dependent kinase-like 5 Good -2.94
    ARRDC2 ARRDC2:arrestin domain containing 2 Good -2.95
  - p134: 57 gene-like tokens; 
    Supplementary table 14: ICC recurrence signature
    Gene Gene Name Correlated Cox score
    Symbol with
    ITGB6 ITGB6:integrin, beta 6 Poor 3.92
    ANXA10 ANXA10:annexin A10 Poor 3.61
    ACSL3 ACSL3:acyl-CoA synthetase long-chain family member 3 Poor 3.54
    MUC4 MUC4:mucin 4, cell surface associated Poor 3.54
    LTBP1 LTBP1:latent transforming growth factor beta binding protein 1 Poor 3.42
  - p135: 66 gene-like tokens; 
    CDCA3 CDCA3:cell division cycle associated 3 Poor 2.76
    SYT12 SYT12:synaptotagmin XII Poor 2.75
    GALR3 GALR3:galanin receptor 3 Poor 2.75
    ABHD9 ABHD9:abhydrolase domain containing 9 Poor 2.74
    PACS1 PACS1:phosphofurin acidic cluster sorting protein 1 Poor 2.74
    KIF13A KIF13A:kinesin family member 13A Poor 2.73
    LGALS7 LGALS7:lectin, galactoside-binding, soluble, 7 (galectin 7) Poor 2.73
    C14ORF124 C14ORF124:chromosome 14 open reading frame 124 Poor 2.72
  - p136: 64 gene-like tokens; 
    FEN1 FEN1:flap structure-specific endonuclease 1 Poor 2.51
    MRPL45 MRPL45:mitochondrial ribosomal protein L45 Poor 2.51
    KRT10 KRT10:keratin 10 (epidermolytic hyperkeratosis; keratosis palmaris et plantaris) Poor 2.49
    CCL26 CCL26:chemokine (C-C motif) ligand 26 Poor 2.48
    PTGS2 PTGS2:prostaglandin-endoperoxide synthase 2 (prostaglandin G/H synthase and cyclooxygenase) Poor 2.48
    EXT1 EXT1:exostoses (multiple) 1 Poor 2.48
    PIM1 PIM1:pim-1 oncogene Poor 2.47
    C19ORF33 C19ORF33:chromosome 19 open reading frame 33 Poor 2.46
  - p137: 76 gene-like tokens; 
    FAM100B FAM100B:family with sequence similarity 100, member B Poor 2.28
    GPR3 GPR3:G protein-coupled receptor 3 Poor 2.28
    C17ORF81 C17ORF81:chromosome 17 open reading frame 81 Poor 2.27
    PSMB2 PSMB2:proteasome (prosome, macropain) subunit, beta type, 2 Poor 2.26
    MCM10 MCM10:MCM10 minichromosome maintenance deficient 10 (S. cerevisiae) Poor 2.26
    PTGER1 PTGER1:prostaglandin E receptor 1 (subtype EP1), 42kDa Poor 2.26
    AHSA1 AHSA1:AHA1, activator of heat shock 90kDa protein ATPase homolog 1 (yeast) Poor 2.25
    ALDH5A1 ALDH5A1:aldehyde dehydrogenase 5 family, member A1 (succinate-semialdehyde dehydrogenase) Poor 2.24
  - p138: 62 gene-like tokens; 
    NRP2 NRP2:neuropilin 2 Poor 1.94
    PLOD1 PLOD1:procollagen-lysine 1, 2-oxoglutarate 5-dioxygenase 1 Poor 1.94
    EFTUD2 EFTUD2:elongation factor Tu GTP binding domain containing 2 Poor 1.90
    CENPJ CENPJ:centromere protein J Poor 1.88
    SIPA1 SIPA1:signal-induced proliferation-associated gene 1 Poor 1.84
    TOR3A TOR3A:torsin family 3, member A Good -1.81
    EPB41L1 EPB41L1:erythrocyte membrane protein band 4.1-like 1 Good -1.81
    TMEM156 TMEM156:transmembrane protein 156 Good -1.81
  - p139: 67 gene-like tokens; 
    DPT DPT:dermatopontin Good -2.01
    ADCY6 ADCY6:adenylate cyclase 6 Good -2.02
    ARRDC2 ARRDC2:arrestin domain containing 2 Good -2.03
    LYL1 LYL1:lymphoblastic leukemia derived sequence 1 Good -2.03
    C21ORF24 C21ORF24:chromosome 21 open reading frame 24 Good -2.04
    AGXT2L2 AGXT2L2:alanine-glyoxylate aminotransferase 2-like 2 Good -2.04
    GCLM GCLM:glutamate-cysteine ligase, modifier subunit Good -2.04
    RAB24 RAB24:RAB24, member RAS oncogene family Good -2.05
  - p140: 59 gene-like tokens; 
    HRH4 HRH4:histamine receptor H4 Good -2.12
    LOC221091 LOC221091:- Good -2.13
    LOC400120 LOC400120:- Good -2.13
    TMEM1 TMEM1:transmembrane protein 1 Good -2.13
    C13ORF27 C13ORF27:chromosome 13 open reading frame 27 Good -2.14
    LMOD3 LMOD3:leiomodin 3 (fetal) Good -2.14
    UFD1L UFD1L:ubiquitin fusion degradation 1 like (yeast) Good -2.14
    GRM6 GRM6:glutamate receptor, metabotropic 6 Good -2.14
  - p141: 65 gene-like tokens; 
    ICAM5 ICAM5:intercellular adhesion molecule 5, telencephalin Good -2.20
    SATB2 SATB2:SATB family member 2 Good -2.20
    SLC35E1 SLC35E1:solute carrier family 35, member E1 Good -2.20
    VISA VISA:- Good -2.21
    POU2F3 POU2F3:POU domain, class 2, transcription factor 3 Good -2.21
    TMEM137 TMEM137:transmembrane protein 137 Good -2.21
    RHOT2 RHOT2:ras homolog gene family, member T2 Good -2.21
    C11ORF55 C11ORF55:chromosome 11 open reading frame 55 Good -2.21
  - p142: 64 gene-like tokens; 
    USP7 USP7:ubiquitin specific peptidase 7 (herpes virus-associated) Good -2.29
    WNK2 WNK2:WNK lysine deficient protein kinase 2 Good -2.29
    ZNF43 ZNF43:zinc finger protein 43 Good -2.30
    PDCD1LG2 PDCD1LG2:programmed cell death 1 ligand 2 Good -2.30
    PAPLN PAPLN:papilin, proteoglycan-like sulfated glycoprotein Good -2.30
    HCG2P7 HCG2P7:HLA complex group 2 pseudogene 7 Good -2.30
    MLXIPL MLXIPL:MLX interacting protein-like Good -2.30
    TBC1D10C TBC1D10C:TBC1 domain family, member 10C Good -2.31
  - p143: 68 gene-like tokens; 
    RAPSN RAPSN:receptor-associated protein of the synapse, 43kD Good -2.39
    CCL19 CCL19:chemokine (C-C motif) ligand 19 Good -2.39
    OR5B2 OR5B2:olfactory receptor, family 5, subfamily B, member 2 Good -2.39
    FAM119A FAM119A:family with sequence similarity 119, member A Good -2.40
    P15RS P15RS:- Good -2.40
    ZFP42 ZFP42:zinc finger protein 42 homolog (mouse) Good -2.40
    SLFN13 SLFN13:schlafen family member 13 Good -2.41
    MLLT6 MLLT6:myeloid/lymphoid or mixed-lineage leukemia (trithorax homolog, Drosophila); translocated to, 6 Good -2.41
  - p144: 47 gene-like tokens; 
    RNF44 RNF44:ring finger protein 44 Good -2.65
    BLOC1S3 BLOC1S3:biogenesis of lysosome-related organelles complex-1, subunit 3 Good -2.66
    PCCA PCCA:propionyl Coenzyme A carboxylase, alpha polypeptide Good -2.68
    TRIM13 TRIM13:tripartite motif-containing 13 Good -2.68
    FAM23B FAM23B:family with sequence similarity 23, member B Good -2.70
    IGFALS IGFALS:insulin-like growth factor binding protein, acid labile subunit Good -2.73
    TTC16 TTC16:tetratricopeptide repeat domain 16 Good -2.84
    ABLIM3 ABLIM3:actin binding LIM protein family, member 3 Good -2.85
  - p145: 6 gene-like tokens; Supplementary Table 15: ICC outcome signatures prediction in an independent CC data set

## martin_serrano2023

Martin-Serrano MA et al. Novel microenvironment-based classification of intrahepatic cholangiocarcinoma with therapeutic implications. Gut 2023;72:736-748

- identifiers: {"doi": "10.1136/gutjnl-2021-326514", "pmid": "35584893", "pmcid": "PMC10388405"}
- resolved title: Novel microenvironment-based classification of intrahepatic cholangiocarcinoma with therapeutic implications. Gut 2023
- want: STIM five classes: immune classical, inflammatory stroma (inflamed); hepatic stem-like, tumour classical, desert-like (non-inflamed). Class signatures / classifier genes and the TME deconvolution signatures used.

**No files.** Download the supplement by hand into `data/papers/martin_serrano2023/manual/` and re-run with --inventory-only.

## beaufrere2025

Beaufrere A et al. Self-supervised learning to predict intrahepatic cholangiocarcinoma transcriptomic classes on routine histology. JHEP Reports 2025 (bioRxiv 2024.01.15.575652)

- identifiers: {"pmid": "41541502", "pmcid": "PMC12800354", "doi": "10.1016/j.jhepr.2025.101675"}
- resolved title: Self-supervised learning to predict intrahepatic cholangiocarcinoma transcriptomic classes on routine histology. JHEP Rep 2026
- want: Per-sample STIM class of the 246 GSE244807 samples (hepatic stem-like 90/246 in the discovery set), and how the classes were assigned. Our GSE244807 STIM calls are checked against these labels.

### data/papers/beaufrere2025/supp/TCGA_chol_final_transcripto_hemstem.csv (2 kB)
- 30 rows x 6 cols
  | ID | HepaticStem_like | Tumor_classical | Inflammatory_stroma | Desert_like | Immune_classical
  | TCGA-W5-AA36-01Z-00-DX1.3BA8 | 1 | 0 | 0 | 0 | 0
  | TCGA-4G-AAZT-01Z-00-DX1.2E91 | 1 | 0 | 0 | 0 | 0
  | TCGA-ZD-A8I3-01Z-00-DX1.ECD6 | 1 | 0 | 0 | 0 | 0
  | TCGA-4G-AAZO-01Z-00-DX1.B3E0 | 1 | 0 | 0 | 0 | 0
  | TCGA-W5-AA2O-01Z-00-DX1.2A08 | 0 | 0 | 0 | 0 | 1
  | TCGA-ZH-A8Y2-01Z-00-DX1.AF4D | 1 | 0 | 0 | 0 | 0
  | TCGA-ZH-A8Y8-01Z-00-DX1.1743 | 0 | 0 | 1 | 0 | 0

### data/papers/beaufrere2025/supp/heptastem_testsplit.csv (34 kB)
- 770 rows x 7 cols
  | ID | Desert_like | HepaticStem_like | Immune_classical | Inflammatory_stroma | Tumor_classical | test
  | CK001_O_05 | False | False | True | False | False | 2.0
  | CK001_O_07 | False | False | True | False | False | 2.0
  | CK001_O_08 | False | False | True | False | False | 2.0
  | CK001_O_09 | False | False | True | False | False | 2.0
  | CK001_O_14 | False | False | True | False | False | 2.0
  | CK001_O_16 | False | False | True | False | False | 2.0
  | CK001_P_12 | False | False | True | False | False | 2.0

### data/papers/beaufrere2025/supp/mmc1.pdf (1226 kB)
- 11 pages
  - p1: 9 gene-like tokens; Table S1 ........................................................................................... / Table S2 ........................................................................................... / Table S3 ........................................................................................... / Table S4 ...........................................................................................
  - p3: 3 gene-like tokens; Table S1. List of morphological criteria assessed by the expert pathologist for all cases of
  - p4: 2 gene-like tokens; Table S2. Repartition of the five transcriptomic classes in the discovery set and in the
  - p5: 1 gene-like tokens; Table S3. Repartition of the five transcriptomic classes according to the type of samples
  - p6: 6 gene-like tokens; Table S4. Model performance for the hepatic stem-like binary classification task on
  - p7: 10 gene-like tokens; Table S5. Effects of the ROI extraction method on the external validation performances

### data/papers/beaufrere2025/supp/mmc2.docx (53 kB)
- 11 tables; captions: 
  - table 1: 1 rows
    | 
  - table 2: 2 rows
    | Name | Citation | Supplier | Cat no. | Clone no.
    |  |  |  |  | 
  - table 3: 2 rows
    | Name | Citation | Supplier | Cat no. | Passage no. | Authentication test method
    |  |  |  |  |  | 
  - table 4: 2 rows
    | Name | Citation | Supplier | Strain | Sex | Age | Overall n number
    |  |  |  |  |  |  | 
  - table 5: 2 rows
    | Name | Sequence | Supplier
    |  |  | 
  - table 6: 2 rows
    | Description | Source | Identifier
    | TCGA-CHOL | TCGA | https://portal.gdc.cancer.go
  - table 7: 3 rows
    | Name of repository | Identifier | Link
    | GSE244807 | Gene Expression Omnibus (GEO | https://www.ncbi.nlm.nih.gov
    | ICCA_prediction | GitHub | https://github.com/trislaz/I
  - table 8: 2 rows
    | Software name | Manufacturer | Version
    | SPSS software | IBM | 29
  - table 9: 2 rows
    |  |  | 
    |  |  | 
  - table 10: 1 rows
    | Dr. Aurélie BEAUFRÈRE, aurel
  - table 11: 1 rows
    | N/A

### data/papers/beaufrere2025/supp/mmc3.pdf (805 kB)
- 52 pages

### data/papers/beaufrere2025/supp/mmc4.pdf (4002 kB)
- 23 pages
  - p4: 28 gene-like tokens; (Table S1; Fig. S1). The stage of fibrosis in the non-tumoural tumour regions using ImageScope softw
  - p5: 27 gene-like tokens; Externaldatasetinference datasets is represented in Fig. 2 and Table S2. The most fre- / Continuous variables were compared using Student’s t test, Serrano et al.10 (Table S3). Of note, the / squared or Fisher’s exact tests. Survival curves were esti- biopsy samples in the discovery set (Tab / tumours for each dataset are presented in Table 1. At the Hepaticstem-likeanddesert-likeclassesexhib
  - p7: 32 gene-like tokens; Table 2. Cross-validated performance of the Giga-SSL and MIL models on the discovery cohort for the  / We detailed in Table S5 the external validation results when / Table 2 shows cases of the cross-validated performances of models were trained according to the thre / Table S5 presents the results of the external validation of models using training sets with differen
  - p8: 26 gene-like tokens; RNA+, S RNA-). Table 3 presents the results of these experi- / stromaclasses(TableS7). / Table3. PredictionforthefourmostfrequenttranscriptomicclassesaccordingAUCscores.
  - p9: 64 gene-like tokens; 
    iCCA transcriptomic class prediction
    thetypeofslides(frombiopsyorsurgicalsamples,directlyor focused on surgical samples,16,19–21 but most patients with
    indirectly associated with transcriptomic analysis) on pre- iCCA will not undergo surgery, which may introduce a selec-
    diction accuracy. Our findings suggest that intratumoural tion bias. Of note, we found transcriptomic classes differ-
    heterogeneity can negatively affect training when non- entiallyrepresentedbetweensurgicalandbiopsycases,which
    consecutive slides are used for either molecular profiling or highlightstheimportanceofworkingwithbothtissuesamples.
    histological analysis. This discrepancy introduces label noise, A few studies, mainly focusing on diagnostic tasks, have laid
    inthatthemolecularclassweaimtopredictmaynotalignwith thegroundworkforusingbiopsiesandhavedemonstratedthat
  - p13: 9 gene-like tokens; Table S1 ........................................................................................... / Table S2 ........................................................................................... / Table S3 ........................................................................................... / Table S4 ...........................................................................................
  - p15: 3 gene-like tokens; Table S1. List of morphological criteria assessed by the expert pathologist for all cases of
  - p16: 2 gene-like tokens; Table S2. Repartition of the five transcriptomic classes in the discovery set and in the
  - p17: 1 gene-like tokens; Table S3. Repartition of the five transcriptomic classes according to the type of samples
  - p18: 6 gene-like tokens; Table S4. Model performance for the hepatic stem-like binary classification task on
  - p19: 10 gene-like tokens; Table S5. Effects of the ROI extraction method on the external validation performances

## job2020

Job S et al. Identification of four immune subtypes characterized by distinct composition and functions of tumor microenvironment in intrahepatic cholangiocarcinoma. Hepatology 2020;72:965-981

- identifiers: {"doi": "10.1002/hep.31092", "pmid": "31875970", "pmcid": "PMC7589418"}
- resolved title: Identification of Four Immune Subtypes Characterized by Distinct Composition and Functions of Tumor Microenvironment in Intrahepatic Cholangiocarcinoma. Hepatology 2020
- want: The 14 TME signatures and 3 functional indicators (liver activity, inflammation, immune resistance), and the classifier (centroids or predictor genes) for I1 immune desert, I2 immunogenic, I3 myeloid, I4 mesenchymal. Per-sample labels if the public cohorts used include ours.

### data/papers/job2020/supp/HEP-72-965-s001.docx (56 kB)
- 0 tables; captions: Snap frozen ICC tissue samples were collected from 116 patients with cholangiocarcinoma wh / For pathway analysis of transcriptomic data, we kept all the datasets including at least 5

### data/papers/job2020/supp/HEP-72-965-s002.docx (18 kB)
- 0 tables; captions: Supporting Table S1: List of cell-type specific genes and pathways used by the Microenviro / Supporting Table S2: Homemade list of genes specific to the indicated immune functional si / Supporting Table S3: CIBERSORT data. Quantification of 22 tumor-infiltrating cell populati / Supporting Table S4: Association between clinico-pathological features and the four immune / Supporting Table S5: Univariate Cox analysis of overall survival. Univariate models were p / Supporting Table S6: Multivariate Cox analysis of overall survival. Multivariate model per

### data/papers/job2020/supp/HEP-72-965-s003.docx (71 kB)
- 17 tables; captions: Table S1: Cell-type specific genes and pathways used by the Microenvironment Cell Populati / Table S2: Homemade list of genes specific to the indicated functional signatures. / Table S3: CIBERSORT data. Quantification of 22 tumor-infiltrating cell populations accordi / Table S4: Association between clinico-pathological features and the four immune subtypes.  / Table S5: Univariate Cox analysis of overall survival.  / Table S6: Multivariate Cox analysis of overall survival. 
  - table 1: 43 rows
    | Signature type | Signature | Gene
    | MCP-counter | Lymphoid | ZNF831
    | MCP-counter | Lymphoid | PARP15
    | MCP-counter | Lymphoid | LCK
    | MCP-counter | Lymphoid | PTPRCAP
    | MCP-counter | Lymphoid | CD27
    | MCP-counter | Lymphoid | LTA
    | MCP-counter | Lymphoid | TRAC
  - table 2: 43 rows
    | MCP-counter | T_adaptative | MGC40069
    | MCP-counter | Cytotoxic | KLRC4-KLRK1
    | MCP-counter | Cytotoxic | CD8A
    | MCP-counter | Cytotoxic | KLRC1
    | MCP-counter | Cytotoxic | KLRC3
    | MCP-counter | Cytotoxic | KLRD1
    | MCP-counter | Cytotoxic | KLRC4
    | MCP-counter | Cytotoxic | FGFBP2
  - table 3: 43 rows
    | MCP-counter | B_derived | DTX1
    | MCP-counter | B_derived | FCRL2
    | MCP-counter | B_derived | CD22
    | MCP-counter | B_derived | IGKV1-37
    | MCP-counter | B_derived | CR2
    | MCP-counter | B_derived | CD19
    | MCP-counter | B_derived | RALGPS2
    | MCP-counter | B_derived | CD79B
  - table 4: 43 rows
    | MCP-counter | Myeloid | TLR2
    | MCP-counter | Myeloid | CCR1
    | MCP-counter | Myeloid | FPR1
    | MCP-counter | Myeloid | HCAR3
    | MCP-counter | Myeloid | SPI1
    | MCP-counter | Myeloid | AQP9
    | MCP-counter | Myeloid | HK3
    | MCP-counter | Myeloid | PTAFR
  - table 5: 43 rows
    | MCP-counter | Myeloid | CXCL16
    | MCP-counter | Myeloid | GPR84
    | MCP-counter | Myeloid | NLRP12
    | MCP-counter | Myeloid | MXD1
    | MCP-counter | Myeloid | SLC43A2
    | MCP-counter | Myeloid | IL10RB-AS1
    | MCP-counter | Myeloid | MCEMP1
    | MCP-counter | Myeloid | PRAM1
  - table 6: 43 rows
    | MCP-counter | Fibroblast | IGFBP5
    | MCP-counter | Fibroblast | STC2
    | MCP-counter | Fibroblast | LOXL1
    | MCP-counter | Fibroblast | FZD7
    | MCP-counter | Fibroblast | CNN1
    | MCP-counter | Fibroblast | LPAR1
    | MCP-counter | Fibroblast | PPP1R3C
    | MCP-counter | Fibroblast | LOX
  - table 7: 43 rows
    | MCP-counter | Fibroblast | CD248
    | MCP-counter | Fibroblast | EVC
    | MCP-counter | Fibroblast | COPZ2
    | MCP-counter | Fibroblast | PRRX2
    | MCP-counter | Fibroblast | SH2D4A
    | MCP-counter | Fibroblast | VGLL3
    | MCP-counter | Fibroblast | GREM2
    | MCP-counter | Fibroblast | SYNC
  - table 8: 43 rows
    | Functional signatures | proinflammation | IL18
    | Functional signatures | proinflammation | IL1B
    | Functional signatures | proinflammation | IL6
    | Functional signatures | proinflammation | PTGS2
    | Functional signatures | proinflammation | TNF
    | Functional signatures | proinflammation | IL1A
    | Functional signatures | proinflammation | CXCR4
    | Functional signatures | proinflammation | CXCL12
  - table 9: 43 rows
    | Functional signatures | Complement | CFH
    | Functional signatures | Complement | CFI
    | Functional signatures | T cells chemotaxis and activ | CXCL9
    | Functional signatures | T cells chemotaxis and activ | CXCL10
    | Functional signatures | T cells chemotaxis and activ | CXCL16
    | Functional signatures | T cells chemotaxis and activ | IFNG
    | Functional signatures | T cells chemotaxis and activ | IL15
    | Functional signatures | T cells specific inhibition | PDCD1
  - table 10: 43 rows
    | Functional signatures | Primary fibroblasts | ELN
    | Functional signatures | Primary fibroblasts | TWIST2
    | Functional signatures | Primary fibroblasts | TENM2
    | Boers et al. Signatures | HSCquiescent | SLC25A6
    | Boers et al. Signatures | HSCquiescent | CCL3
    | Boers et al. Signatures | HSCquiescent | CCL4
    | Boers et al. Signatures | HSCquiescent | FCN3
    | Boers et al. Signatures | HSCquiescent | FLJ11029
  - table 11: 43 rows
    | Boers et al. Signatures | Myofibroblast | G3BP2
    | Boers et al. Signatures | Myofibroblast | GNG12
    | Boers et al. Signatures | Myofibroblast | HIF1A
    | Boers et al. Signatures | Myofibroblast | HLA-C
    | Boers et al. Signatures | Myofibroblast | HMGA1
    | Boers et al. Signatures | Myofibroblast | IGFBP5
    | Boers et al. Signatures | Myofibroblast | IL6
    | Boers et al. Signatures | Myofibroblast | ITGB5
  - table 12: 7 rows
    | Boers et al. Signatures | HSCactivated | COX6C
    | Boers et al. Signatures | HSCactivated | TPM1
    | Boers et al. Signatures | HSCactivated | RPN2
    | Boers et al. Signatures | HSCactivated | COL1A1
    | Boers et al. Signatures | HSCactivated | PCSK7
    | Boers et al. Signatures | HSCactivated | CHPF
    | Boers et al. Signatures | HSCactivated | RCN3
  - table 13: 55 rows
    | Functional signature | Gene
    | T cells chemotaxis and activ | CXCL9
    | T cells chemotaxis and activ | CXCL10
    | T cells chemotaxis and activ | CXCL16
    | T cells chemotaxis and activ | IFNG
    | T cells chemotaxis and activ | IL15
    | T cells specific inhibition | PDCD1
    | T cells specific inhibition | CD274
  - table 14: 24 rows
    |  | Cibersort proportion mean
    |  | Pvalue | I1 | I2 | I3 | I4
    | B.cells.naive | 4.18E-05 | 0.074 | 0.010 | 0.010 | 0.018
    | Monocytes | 1.44E-03 | 0.065 | 0.012 | 0.016 | 0.016
    | T.cells.CD8 | 6.31E-03 | 0.102 | 0.199 | 0.094 | 0.163
    | T.cells.gamma.delta | 1.39E-02 | 0.000 | 0.024 | 0.010 | 0.006
    | Macrophages.M2 | 1.97E-02 | 0.074 | 0.093 | 0.152 | 0.128
    | Mast.cells.resting | 3.37E-02 | 0.016 | 0.014 | 0.006 | 0.039
  - table 15: 58 rows
    | Variable | value | I1 | I2 | I3 | I4 | Pvalue
    | Gender | FM | 2322 | 53 | 65 | 68 | 8.71E-018.71E-01
    | Cells.Fibrosis.Detected | NY | 242 | 08 | 011 | 014 | 1.00E+001.00E+00
    |  | NY | 3014 | 61 | 47 | 104 | 1.51E-011.51E-01
    | Histology.Grade | G1G2G3 | 15198 | 332 | 163 | 392 | 6.20E-016.20E-016.20E-01
    | Tumor.Capsule | NY | 343 | 50 | 60 | 110 | 1.00E+001.00E+00
    | Tumor.Location | Hilum | 1 | 0 | 0 | 0 | 3.59E-01
    |  | Left liver | 15 | 2 | 4 | 7 | 3.59E-01
  - table 16: 45 rows
    | Univariate Analysis
    | Variable | value | n | n.event | H.R. | 95%C.I. | p-value | logrank_p.value
    | Satellite.nodules | Y | 66 | 45 | 2.77 | 1.5-5.1 | 0.001 | 6.58E-04
    | Andersen.subtype | C2 | 76 | 51 | 2.27 | 1.2-4.1 | 0.0073 | 5.90E-03
    | immune.subtype immune.subtyp | I2I3I4 | 767676 | 515151 | 0.6291.342.6 | 0.22-1.80.58-3.11.3-5.1 | 0.390.490.0059 | 1.51E-021.51E-021.51E-02
    | Age | - | 76 | 51 | 1.026 | 1.00-1.052 | 0.0514 | 5.00E-02
    | Oishi.subtype | ICC.MH.like | 76 | 51 | 0.581 | 0.33-1 | 0.056 | 5.32E-02
    | TNM.N TNM.NTNM.N | N1 N3Nx | 767676 | 515151 | 1.735.510.933 | 0.87-3.40.7-430.48-1.8 | 0.120.10.84 | 1.15E-011.15E-011.15E-01
  - table 17: 16 rows
    | Multivariate Analysis
    | Variable | value | n | H.R. | 95%C.I. | p-value | p-valuelogrank
    | Satellite.nodules | Y | 55 | 4.5 | 1.8-12 | 1.70E-03 | 5.10E-03
    | Andersen.subtype | C2 | 55 | 4.76 | 1-23 | 0.051 | 5.10E-03
    | Immune.subtype | I2 | 55 | 5.28 | 0.65-43 | 0.12 | 5.10E-03
    | Immune.subtype | I3 | 55 | 1.65 | 0.54-5 | 0.38 | 5.10E-03
    | Immune.subtype | I4 | 55 | 2.3 | 0.63-8.5 | 0.21 | 5.10E-03
    | Oishi.subtype | ICC.MH.like | 55 | 3 | 0.53-17 | 0.22 | 5.10E-03

## dong2022

Dong L et al. Proteogenomic characterization identifies clinically relevant subgroups of intrahepatic cholangiocarcinoma. Cancer Cell 2022;40:70-87

- identifiers: {"doi": "10.1016/j.ccell.2021.12.006"}
- resolved title: Proteogenomic characterization identifies clinically relevant subgroups of intrahepatic cholangiocarcinoma. Cancer Cell 2022
- want: Proteomic subgroups S1 inflammation, S2 interstitial, S3 metabolism, S4 differentiation: per-patient labels (FU-iCCA is our discovery cohort, so the labels can be compared with our programs and states directly) and the subgroup-specific protein biomarkers. mmc2 / mmc3 / mmc5 are already in data/FU_iCCA/manual/; check there first, the fetch gets the remaining mmc files.

### data/papers/dong2022/supp/mmc1.pdf (12206 kB)
- 15 pages

### data/papers/dong2022/supp/mmc2.xlsx (128167 kB)
- sheet `Description`: 12 rows x 1 cols
  | Table S1 Clinical informatio
  |   Table S1A. Clinical inform
  |   Table S1B. WES mutations. 
  |   Table S1C. mRNA expression
  |   Table S1D. 8,320 proteins 
  |   Table S1E. 18,347 phosphos
  |   Table S1F. 5,624 phosphopr
  |   Table S1G. Confirmed varia
- sheet `S1A. Clinical info`: 264 rows x 29 cols
  - gene-symbol-like: col 20 (100% of 263)
  | Table S1 Clinical informatio |  |  |  |  |  |  |  |  |  |  |  |  |  | ...
  | Patient_ID | Sex | Age | Intrahepatic metastasis | Liver fluke | HBsAg  (1, positive; 0, nega | Biliary tract stone disease | Tumor_size_diameter (cm) | Vascular invasion | Liver cirrhosis | Regional lymph Node metastas | Distal metastasis | Perineural invasion | TB: total bilirubin (μmol/L) | ...
  | 111 | Male | 49 | No | No | 1 | No | 7.5 | Yes | No | No | No | No | 8.4 | ...
  | 113 | Male | 59 | Yes | No | 0 | No | 15 | Yes | No | Yes | No | No | 9.2 | ...
  | 115 | Male | 74 | No | No | 0 | No | 4.5 | Yes | No | No | No | No | 7.9 | ...
  | 117 | Female | 64 | No | Yes | 0 | No | 4.6 | No | No | No | No | Yes | 14.1 | ...
  | 121 | Female | 71 | No | No | 0 | No | 5.2 | No | No | No | No | No | 8.6 | ...
  | 123 | Male | 55 | No | No | 0 | No | 2 | No | No | No | No | Yes | 17.8 | ...
- sheet `S1B. WES mutations`: 17007 rows x 11 cols
  - gene-symbol-like: col 5 (99% of 17006)
  | Table S1 Clinical informatio |  |  |  |  |  |  |  |  |  | 
  | Sample_ID | Chromosome | Position | Reference | Alteration | Gene | Transcript_ID | HGVSc | HGVSp | Mutation_Type | Variant allele frequency (VA
  | 111 | 1 | 36772804 | G | A | SH3D21 | NM_001162530.1 | c.263G>A | p.Cys88Tyr | missense_variant | 0.12
  | 111 | 1 | 87041251 | A | C | CLCA4 | NM_012128.3 | c.1920A>C | p.Thr640= | synonymous_variant | 0.083
  | 111 | 1 | 100715341 | C | T | DBT | NM_001918.3 | c.36G>A | p.Arg12= | synonymous_variant | 0.08
  | 111 | 1 | 115130458 | C | T | DENND2C | NM_001256404.1 | c.2547G>A | p.Arg849= | synonymous_variant | 0.138
  | 111 | 1 | 151131427 | C | T | TNFAIP8L2 | NM_024575.4 | c.254C>T | p.Ala85Val | missense_variant | 0.165
  | 111 | 1 | 158450527 | T | A | OR10R2 | NM_001004472.1 | c.860T>A | p.Val287Glu | missense_variant | 0.311
- sheet `S1C. mRNA expression`: 20175 rows x 256 cols
  - gene-symbol-like: col 0 (94% of 20175)
  | Table S1 Clinical informatio |  |  |  |  |  |  |  |  |  |  |  |  |  | ...
  |                  Sample ID G | 111 | 113 | 115 | 117 | 121 | 123 | 125 | 127 | 131 | 133 | 135 | 137 | 141 | ...
  | A1BG | 1.858 | 3.04 | 7.494 | 7.845 | 4.622 | 7.97 | 5.184 | 4.882 | 4.574 | 4.284 | 2.67 | 6.778 | 5.242 | ...
  | A1CF | 5.237 | 6.905 | 6.929 | 7.281 | 6.765 | 6.195 | 3.292 | 0.82 | 0.571 | 3.067 | 6.519 | 4.395 | 1.809 | ...
  | A2M | 9.471 | 5.513 | 11.428 | 7.781 | 9.267 | 9.014 | 8.511 | 8.467 | 8.422 | 8.395 | 7.588 | 8.845 | 7.672 | ...
  | A2ML1 | 0.4 | 0.453 | 0.044 | 0.493 | 0.272 | 0.266 | 0.06 | 0.199 | 1.263 | 2.155 | 0.134 | 1.16 | 0.803 | ...
  | A3GALT2 | 0 | 0 | 0 | 0.558 | 0 | 0.425 | 0 | 0.779 | 0.82 | 0.578 | 0.111 | 0 | 0 | ...
  | A4GALT | 4.753 | 4.335 | 2.385 | 4.123 | 1.931 | 1.725 | 2.165 | 3.505 | 4.632 | 3.462 | 2.447 | 2.602 | 3.869 | ...
- sheet `S1D. proteins expression`: 8323 rows x 216 cols
  - gene-symbol-like: col 0 (99% of 8298), col 1 (100% of 8321)
  | Table S1 Clinical informatio |  |  |  |  |  |  |  |  |  |  |  |  |  | ...
  | Gene |                              | Group 01 |  |  |  |  |  |  |  |  |  | Group 02 |  | ...
  |  |  | 343 | 347 | 427 | 457 | 483 | 517 | 565 | 567 | 631 | 977 | 173 | 235 | ...
  | IGLV4-69 | A0A075B6H9 | -0.322148229815364 | 0.310493422265932 | -0.150599224809786 | 0.389553653998872 | -0.0971699782817405 | 0.362098976180952 | -1.3877348430248 | 2.12389732229507 | -0.860598177388288 | 0.0886584588137858 | 1.28341539518979 | 0.851978832792498 | ...
  | IGLV4-60 | A0A075B6I1 | 0.617957757899333 | 1.27673577241229 | 0.73248671567525 | 0.68471925142291 | 0.214069803336867 | 1.38657877412492 | -0.718640023164295 | 2.07648062839433 | 0.317729057778284 | -0.65936578539175 | 1.37697343207527 | 0.452360044619699 | ...
  | IGLV2-18 | A0A075B6J9 | 1.31484333425451 | 0.571583528924138 | -0.355496313964904 | 0.0159870943272644 | 0.181447312398827 | -0.0670660930192728 | -0.0898348996731863 | 1.59303494031345 | -0.887582550839343 | -0.0229123379990144 | -0.239026186004805 | 0.18590640290047 | ...
  | IGKV2-24 | A0A0C4DH68 | 2.28169645577815 | -0.193126920460847 | 0.475504327995092 | 0.273274293703582 | -0.376765646425375 | 0.388646961531531 | -0.821193846472154 | 2.40782085214439 | -0.521771015543411 | 1.55597551026434 | 0.478636371452616 | 1.24258405559082 | ...
  | IGKV1-27 | A0A075B6S5 | -1.23551815144252 | -3.10165577891629 | -0.143162067251916 | 1.1392012260585 | 0.103315666922281 | -0.227717562308334 | -1.32495299873171 | 2.10034943618855 | -1.13103367824878 | 0.886591902909285 |  |  | ...
- sheet `S1E. 18,347 phosphosites`: 18350 rows x 215 cols
  | Table S1 Clinical informatio |  |  |  |  |  |  |  |  |  |  |  |  |  | ...
  |                              | Group 01 |  |  |  |  |  |  |  |  |  | Group 02 |  |  | ...
  |  | 343 | 347 | 427 | 457 | 483 | 517 | 565 | 567 | 631 | 977 | 173 | 235 | 243 | ...
  | KLF13:S160 | 0.531237719528223 | -0.00430640668630468 | 0.387205470417442 | 0.404848731082273 | -0.322259071068939 | 0.0424242179412304 | -1.1487737662031 | 0.127497531557092 | -0.588824575914021 | -0.749505073387698 | 0.244269199793911 | -0.323734934362523 | -0.232553849260799 | ...
  | RNF213:S2322 | 1.92234992189875 | -0.331930325142388 | -0.0473450759523703 | -0.641594561068398 | 0.176043194286568 | -1.23782083156458 | 1.03243565803272 | 0.128938413187032 | -0.182125221753585 | -0.593716666160925 |  |  |  | ...
  | RNF213:S1307 | 1.41153214508484 | -0.194496012450142 | 0.2726783626547 | 0.209040475883797 | -0.723382538799501 | -1.00363151288088 | 0.64272477375899 | -0.569143083597957 | -1.66577910239481 | -1.70549910470261 | 0.151920442638435 | -0.931172831284645 | -0.121633534624295 | ...
  | RNF213:S266 | 0.538698342579078 | -0.0620474029542989 | 0.910960870271908 | -0.435514409803938 | 0.312655320666642 | -0.178517496972877 | 0.432843440402097 | 1.58774054331177 | 0.0376108214473274 | 0.116176906943059 | 0.1979767097501 | 0.231895763900676 | 0.905507515248086 | ...
  | RNF213:S275 | 0.654189347476485 | 0.287251810997079 | 0.31620284611634 | -0.0328572137321518 | 0.498775556641901 | -0.416869190269805 | 0.798858264432879 | 0.072096157099568 | 0.143075329814204 | 0.337025317588316 | -0.353218795326754 | 0.517224961642531 | 0.45693750600009 | ...
- sheet `S1F. 5,624 phosphoprotein`: 5626 rows x 215 cols
  - gene-symbol-like: col 0 (99% of 5626)
  | Table S1 Clinical informatio |  |  |  |  |  |  |  |  |  |  |  |  |  | ...
  |                  Sample ID G | 343 | 347 | 427 | 457 | 483 | 517 | 565 | 567 | 631 | 977 | 173 | 235 | 243 | ...
  | AAAS | 0.981080658357412 | -0.341311647613437 | -0.532232179249432 | 0.221201132709226 | 0.293656956534195 | 0.188960067629993 | 0.0665532374847311 | 0.193984260439284 | 1.75329155441415 | 0.422605344383906 | 0.420554111464908 | -0.321326080263217 | 0.165966766240426 | ...
  | AAGAB | 0.258028342848491 | 0.0375233200953298 | 0.498585656131614 | 0.0816684689559739 | 0.441732729336115 | -0.0430317677169429 | 0.619271602419814 | 0.312614629864267 | 0.677707345235773 | -0.307895449240965 |  |  |  | ...
  | AAK1 | -0.105583231001396 | 0.199305018685965 | -0.255970961628661 | 0.0382739926764484 | 0.592804650866983 | 0.946305147794238 | 1.32368958581772 | -0.0812313255340683 | -0.121793742339878 | 0.228485631692493 | -0.0523822135686048 | -0.537237463637397 | -0.323208769596598 | ...
  | AAMDC | -0.673923818567887 | -0.184792632055394 | -0.720283618419409 | -0.231967597622864 | -0.0205632447695791 | -0.419734731045066 | -0.424304113157105 | -0.273192481173706 | 1.28913648036373 | 2.07832870408152 | 0.195012099360757 | -0.136770402624808 | -0.172625002566602 | ...
  | AATF |  |  |  |  |  |  |  |  |  |  |  |  |  | ...
  | ABCA1 | 0.379043799227361 | -0.409147578023242 | 0.0720642702262505 | -0.806365264014544 | -0.0854064463643221 | -0.647361113836158 | -0.0857060173341906 | 0.842966093026816 | 0.780239754440197 | 0.0427943082513669 | 0.248436120054896 | 1.15532067279413 | -0.0331260899082301 | ...
- sheet `S1G. Variants confirmed`: 1415 rows x 2 cols
  | Table S1 Clinical informatio | 
  | Type | Proteome
  | RNA_somatic | HHGPGWVSMANAGK
  | RNA_somatic | YLQDTLLLEECGLLR
  | RNA_somatic | AQRIQNVNVK
  | RNA_somatic | LIADVAPSAILENDIK
  | RNA_somatic | DIVSGDIVEIAVGDK
  | RNA_somatic | LEDFHDYR
- sheet `S1H. FGFR2&kinase fusion`: 41 rows x 6 cols
  - gene-symbol-like: col 4 (98% of 40), col 5 (98% of 40)
  | Table S1 Clinical informatio |  |  |  |  | 
  | Sample_ID | FusionName | LeftBreakpoint | RightBreakpoint | LeftGene | RightGene
  | 113 | FGFR2--SUB1 | chr10:123243212:- | chr5:32591669:+ | FGFR2 | SUB1
  | 137 | FGFR2--PHLDB2 | chr10:123243212:- | chr3:111658322:+ | FGFR2 | PHLDB2
  | 143 | FGFR2--BICC1 | chr10:123243212:- | chr10:60573590:+ | FGFR2 | BICC1
  | 185 | FGFR2--WAC | chr10:123243212:- | chr10:28906586:+ | FGFR2 | WAC
  | 215 | FGFR2--NRAP | chr10:123243212:- | chr10:115372190:- | FGFR2 | NRAP
  | 251 | FGFR2--VCL | chr10:123243212:- | chr10:75842212:+ | FGFR2 | VCL
- sheet `S1I. KEGG pathway`: 48 rows x 4 cols
  | Table S1 Clinical informatio |  |  | 
  |  |  | KEGG pathway | Gene
  | Aflatoxin positive | RNA-upregulation | Cell cycle | BUB1/CCNA2/CCNB1/CCNB2/CCNE1
  |  |  | Spliceosome | BCAS2/CDC40/CTNNBL1/DHX16/HN
  |  |  | DNA replication | DNA2/MCM2/PRIM1/PRIM2/RFC4/R
  |  | RNA-downregulation | Herpes simplex virus 1 infec | B2M/CASP8/FAS/NFKBIA/PIK3R1/
  |  |  | Apoptosis | ACTG1/ATM/CASP8/CFLAR/CTSO/F
  |  |  | Pathogenic Escherichia coli  | ACTG1/ARF6/CASP4/CASP8/CLDN1
- sheet `S1J. The number of proteins`: 36 rows x 5 cols
  | Table S1 Clinical informatio |  |  |  | 
  | Group information | Identified proteins | Quantified proteins | Identified phosphosites | Quantified Class I phosphosi
  | Group_01 | 9467 | 8585 | 36057 | 28066
  | Group_02 | 10011 | 9657 | 30790 | 23840
  | Group_03 | 9064 | 8146 | 30741 | 23792
  | Group_04 | 9123 | 8712 | 35179 | 27361
  | Group_05 | 9445 | 9044 | 43034 | 33881
  | Group_06 | 9309 | 8885 | 27422 | 20677
- sheet `S1K. correlation of proteins`: 15 rows x 7 cols
  | Table S1 Clinical informatio |  |  |  |  |  | 
  | Pearson correlation | Pro_Benchmark_1 | Pro_Benchmark_2 | Pro_Benchmark_3 | Pro_Benchmark_4 | Pro_Benchmark_5 | Pro_Benchmark_6
  | Pro_Benchmark_1 |  | 0.9 | 0.91 | 0.91 | 0.92 | 0.91
  | Pro_Benchmark_2 | 0.9 |  | 0.91 | 0.9 | 0.9 | 0.9
  | Pro_Benchmark_3 | 0.91 | 0.91 |  | 0.9 | 0.92 | 0.91
  | Pro_Benchmark_4 | 0.91 | 0.9 | 0.9 |  | 0.91 | 0.91
  | Pro_Benchmark_5 | 0.92 | 0.9 | 0.92 | 0.91 |  | 0.92
  | Pro_Benchmark_6 | 0.91 | 0.9 | 0.91 | 0.91 | 0.92 | 

### data/papers/dong2022/supp/mmc3.xlsx (30909 kB)
- sheet `Description`: 6 rows x 1 cols
  | Table S2. mRNA and protein e
  |   Table S2A. 109 copy number
  |   Table S2B. CNA genes Copy 
  |   Table S2C. In cis gene lis
  |   Table S2D. 14q gene list. 
  |   Table S2E. The list of 543
- sheet `S2A. CNA regions`: 220 rows x 263 cols
  | Table S2. mRNA and protein e |  |  |  |  |  |  |  |  |  |  |  |  |  | ...
  | Unique Name | Descriptor | Wide Peak Limits | Peak Limits | Region Limits | q values | Residual q values after remo | Broad or Focal | Amplitude Threshold | 137 | 141 | 151 | 167 | 177 | ...
  | Amplification Peak  1 | 1p36.32 | chr1:5021430-5079676(probes  | chr1:5030002-5069999(probes  | chr1:4710002-5419654(probes  | 0.012858 | 0.033413 |  | 0: t<0.4; 1: 0.4<t< 0.9; 2:  | 0 | 0 | 0 | 2 | 0 | ...
  | Amplification Peak  2 | 1p34.3 | chr1:36522001-39219090(probe | chr1:36950002-37349999(probe | chr1:36590002-37378888(probe | 0.036984 | 0.10155 |  | 0: t<0.4; 1: 0.4<t< 0.9; 2:  | 0 | 0 | 0 | 0 | 0 | ...
  | Amplification Peak  3 | 1q21.3 | chr1:152401113-155330000(pro | chr1:154410002-155009999(pro | chr1:118830002-178099835(pro | 4.1008e-25 | 5.9404e-25 |  | 0: t<0.4; 1: 0.4<t< 0.9; 2:  | 0 | 0 | 0 | 1 | 0 | ...
  | Amplification Peak  4 | 1q32.1 | chr1:201040528-207619876(pro | chr1:204230002-205809999(pro | chr1:199770002-249250621(pro | 1.3917e-07 | 2.6477e-05 |  | 0: t<0.4; 1: 0.4<t< 0.9; 2:  | 1 | 0 | 0 | 0 | 0 | ...
  | Amplification Peak  5 | 1q43 | chr1:226620053-249250621(pro | chr1:237150002-242669999(pro | chr1:199770002-249250621(pro | 8.4764e-06 | 0.0032019 |  | 0: t<0.4; 1: 0.4<t< 0.9; 2:  | 1 | 0 | 0 | 0 | 0 | ...
  | Amplification Peak  6 | 2p25.3 | chr2:1-699230(probes 24717:2 | chr2:1-689999(probes 24717:2 | chr2:1-859031(probes 24717:2 | 0.014463 | 0.014463 |  | 0: t<0.4; 1: 0.4<t< 0.9; 2:  | 0 | 0 | 0 | 0 | 0 | ...
- sheet `S2B. CNA at gene level `: 23111 rows x 256 cols
  - gene-symbol-like: col 0 (89% of 23111)
  | Table S2. mRNA and protein e |  |  |  |  |  |  |  |  |  |  |  |  |  | ...
  | Gene Symbol | Gene ID | Cytoband | 137 | 141 | 151 | 167 | 177 | 193 | 195 | 197 | 211 | 213 | 217 | ...
  | DDX11L1|chr1 | 100287102 | 1p36.33 | -0.124 | 0.118 | 0.13 | 1.953 | -0.168 | -0.627 | -0.287 | -0.037 | -0.155 | -0.16 | 0.091 | ...
  | FAM138A|chr1 | 645520 | 1p36.33 | -0.124 | 0.118 | 0.13 | 1.953 | -0.168 | -0.627 | -0.287 | -0.037 | -0.155 | -0.16 | 0.091 | ...
  | FAM138F|chr1 | 641702 | 1p36.33 | -0.124 | 0.118 | 0.13 | 1.953 | -0.168 | -0.627 | -0.287 | -0.037 | -0.155 | -0.16 | 0.091 | ...
  | LOC100132062|chr1 | 100132062 | 1p36.33 | -0.124 | 0.118 | 0.13 | 1.953 | -0.168 | -0.627 | -0.287 | -0.037 | -0.155 | -0.16 | 0.091 | ...
  | LOC100132287|chr1 | 100132287 | 1p36.33 | -0.124 | 0.118 | 0.13 | 1.953 | -0.168 | -0.627 | -0.287 | -0.037 | -0.155 | -0.16 | 0.091 | ...
  | LOC100133331|chr1 | 100133331 | 1p36.33 | -0.124 | 0.118 | 0.13 | 1.953 | -0.168 | -0.627 | -0.287 | -0.037 | -0.155 | -0.16 | 0.091 | ...
- sheet `S2C. In cis gene list`: 965 rows x 1 cols
  - gene-symbol-like: col 0 (100% of 965)
  | Table S2. mRNA and protein e
  | Gene
  | AAGAB
  | ABCB10
  | ABCE1
  | ABCF2
  | ABHD16A
  | ABHD6
- sheet `S2D. 14q gene list`: 587 rows x 1 cols
  - gene-symbol-like: col 0 (99% of 587)
  | Table S2. mRNA and protein e
  | Gene
  | AARS
  | AARS2
  | ACSS1
  | ADAR
  | ADCK4
  | AFF4
- sheet `S2E. mRNA-protein correlation`: 5436 rows x 5 cols
  - gene-symbol-like: col 0 (99% of 5436)
  | Table S2. mRNA and protein e |  |  |  | 
  | Gene | Spearman correlation | P value | Adjusted P value | 
  | ANXA13 | 0.940366079382097 | 1.98950225563532e-98 | 1.08109552571223e-94 | 
  | NXN | 0.937707029812292 | 1.5488983102532e-96 | 4.20835670895796e-93 | 
  | GALNT7 | 0.934430558000351 | 2.5636377846292e-94 | 4.6436025738917e-91 | 
  | HK2 | 0.932230241154726 | 6.84554649999148e-93 | 9.29967492023843e-90 | 
  | INPP4B | 0.930480655881113 | 8.62728969202998e-92 | 9.37613843729818e-89 | 
  | ZNF185 | 0.9297325481536 | 2.49850998667888e-91 | 2.26281721126884e-88 | 

### data/papers/dong2022/supp/mmc4.xlsx (12001 kB)
- sheet `Description`: 5 rows x 1 cols
  | Table S3. Differential analy
  |   Table S3A.mRNA level. Diff
  |   Table S3B.Protein level. D
  |   Table S3C.Phospho protein 
  |   Table S3D.Phospho site lev
- sheet `S3A.mRNA level`: 19806 rows x 16 cols
  - gene-symbol-like: col 0 (94% of 19805)
  | Table S3. Differential analy |  |  |  |  |  |  |  |  |  |  |  |  |  | ...
  | Gene symbol | TP53 mutation vs. TP53 wild  |  |  | KRAS mutation vs. KRAS wild  |  |  | BAP1 mutation vs. BAP1 wild  |  |  | IDH1/2 mutation vs. IDH1/2 w |  |  | TP53/KRAS co-mutation vs. TP | ...
  |  | Log2 FC | P value | Adjusted P value | Log2 FC | P value | Adjusted P value | Log2 FC | P value | Adjusted P value | Log2 FC | P value | Adjusted P value | Log2 FC | ...
  | A2M | 0.0392861776185516 | 0.474729360867279 | 0.707848962141906 | -0.569031116797275 | 0.0297804793591709 | 0.111187990867371 | -0.420454329140949 | 0.0307730416173534 | 0.138524449064984 | -0.24419196367833 | 0.161543926909725 | 0.414790330924669 | -1.08358170406758 | ...
  | A2ML1 | 0.199468332124641 | 0.67159849540344 | 0.839114299946538 | 1.27492583862983 | 4.41232610461602e-05 | 0.000846734206922092 | -0.112367442545064 | 0.155524095653212 | 0.369458219538481 | -0.616617808872472 | 0.0388082951900876 | 0.18533786800004 | 1.5790023713825 | ...
  | A3GALT2 | 0.18024662425397 | 0.0266382395144897 | 0.123674846787895 | -0.0106419067642641 | 0.8022680468236 | 0.895779485262805 | -0.0653849699570183 | 0.941561873223726 | 0.974138785232413 | 0.0225431441719668 | 0.409214666402397 | 0.666918560103833 | 0.104343357041076 | ...
  | A4GALT | 0.370238023177532 | 0.0173282294735655 | 0.09397746502808 | 0.697756984565072 | 0.000169103819736373 | 0.00235977784193821 | -0.528583562535716 | 0.00679379474908732 | 0.0550781645995229 | -0.189806377913147 | 0.234389826889405 | 0.503147963547452 | 1.00874943837012 | ...
  | A4GNT | -0.124083736874678 | 0.429406411032312 | 0.671729478171066 | -0.459179691924806 | 0.00633147862025366 | 0.0360056738969872 | -0.253856219807528 | 0.266755576300841 | 0.508053046256229 | -0.388119682627228 | 0.280577087102147 | 0.5504684558469 | -0.455730207549657 | ...
- sheet `S3B.Protein level`: 8051 rows x 16 cols
  - gene-symbol-like: col 0 (100% of 8050)
  | Table S3. Differential analy |  |  |  |  |  |  |  |  |  |  |  |  |  | ...
  | Gene symbol | TP53 mutation vs. TP53 wild  |  |  | KRAS mutation vs. KRAS wild  |  |  | BAP1 mutation vs. BAP1 wild  |  |  | IDH1/2 mutation vs. IDH1/2 w |  |  | TP53/KRAS co-mutation vs. TP | ...
  |  | Log2 FC | P value | Adjusted P value | Log2 FC | P value | Adjusted P value | Log2 FC | P value | Adjusted P value | Log2 FC | P value | Adjusted P value | Log2 FC | ...
  | A2M | 0.0486292772505266 | 0.696297975055963 | 0.818312807133527 | 0.0236729022782163 | 0.852306548714977 | 0.921338227543067 | -0.205114663160835 | 0.142755458916226 | 0.337624117236543 | -0.268335157368681 | 0.0379644134692968 | 0.193011749589956 | 0.138398232578972 | ...
  | AAAS | 0.0406278211405137 | 0.449005589687922 | 0.626566434187876 | -0.00862124733817331 | 0.874995169944822 | 0.934097631105039 | 0.177265495953165 | 0.00305235883060859 | 0.0313260410306475 | -0.020671957705443 | 0.712050050740277 | 0.858810837193108 | 0.0891340120660694 | ...
  | AACS | 0.0254658179137686 | 0.763919224224989 | 0.863971601540572 | -0.0620183679666963 | 0.473287370013679 | 0.648439571479705 | 0.325439063782707 | 0.000545701199150844 | 0.0117427894405508 | 0.136574377098798 | 0.121508670764305 | 0.36098257006686 | -0.0628226778707444 | ...
  | AADAC | 0.503345061210364 | 0.0445499208241858 | 0.139835320902125 | 0.231781646414588 | 0.366219453508877 | 0.556047987254361 | -0.374353502791535 | 0.185786624028755 | 0.39254679710775 | -0.0636638566172967 | 0.808462031996014 | 0.911913445480578 | -0.156652600906093 | ...
  | AADAT | -0.00110458854786077 | 0.995337425032789 | 0.997280483439521 | 0.185497203159794 | 0.335555945502193 | 0.528713103300999 | -0.306154798581851 | 0.149324613695868 | 0.345433886468625 | -0.0868162816026724 | 0.659648981264584 | 0.83197853020175 | -0.119888704810866 | ...
- sheet `S3C.Phospho protein level`: 5552 rows x 16 cols
  - gene-symbol-like: col 0 (99% of 5551)
  | Table S3. Differential analy |  |  |  |  |  |  |  |  |  |  |  |  |  | ...
  | Gene symbol | TP53 mutation vs. TP53 wild  |  |  | KRAS mutation vs. KRAS wild  |  |  | BAP1 mutation vs. BAP1 wild  |  |  | IDH1/2 mutation vs. IDH1/2 w |  |  | TP53/KRAS co-mutation vs. TP | ...
  |  | Log2 FC | P value | Adjusted P value | Log2 FC | P value | Adjusted P value | Log2 FC | P value | Adjusted P value | Log2 FC | P value | Adjusted P value | Log2 FC | ...
  | AAAS | 0.105577929726872 | 0.120453659320168 | 0.267687342842992 | 0.0222404173090905 | 0.749216915168191 | 0.849837420741679 | 0.156566422191854 | 0.0404321162282658 | 0.189331487722065 | -0.0243367531129484 | 0.732194353952456 | 0.911792295799412 | 0.0695237424448303 | ...
  | AAGAB | 0.098713522934488 | 0.165996766506096 | 0.330860652781009 | 0.167825676856296 | 0.0204886010593932 | 0.0711905117586556 | -0.00265644741745719 | 0.97365433838239 | 0.992432443180923 | -0.150302871526627 | 0.0426466163533702 | 0.268767723768909 | 0.125388558684078 | ...
  | AAK1 | -0.181169132373462 | 0.00173063895531567 | 0.0144796554074976 | -0.1823092164068 | 0.00201140183097437 | 0.0130211244259544 | 0.121170706486788 | 0.0648235947622634 | 0.240606105241338 | 0.0176797037914051 | 0.77205993111023 | 0.927106807559113 | -0.382062663340253 | ...
  | AAMDC | -0.160701358587674 | 0.089971843158496 | 0.217864184719783 | -0.111438501542228 | 0.250117283725691 | 0.41905217614549 | -0.142639016411308 | 0.18200145101792 | 0.427030043001454 | -0.0096837451339152 | 0.922243304677275 | 0.977560286084852 | -0.204743622029833 | ...
  | AATF | 0.0487572956850461 | 0.528832532815673 | 0.69030621608896 | -0.0123578498360291 | 0.875755449709898 | 0.928284047839585 | 0.170078300981027 | 0.0501301358694169 | 0.210563734321933 | -0.0619642585228461 | 0.442814645761339 | 0.769551665934754 | -0.137997183538771 | ...
- sheet `S3D.Phospho site level`: 18236 rows x 16 cols
  | Table S3. Differential analy |  |  |  |  |  |  |  |  |  |  |  |  |  | ...
  | Phosphorylation site | TP53 mutation vs. TP53 wild  |  |  | KRAS mutation vs. KRAS wild  |  |  | BAP1 mutation vs. BAP1 wild  |  |  | IDH1/2 mutation vs. IDH1/2 w |  |  | TP53/KRAS co-mutation vs. TP | ...
  |  | Log2 FC | P value | Adjusted P value | Log2 FC | P value | Adjusted P value | Log2 FC | P value | Adjusted P value | Log2 FC | P value | Adjusted P value | Log2 FC | ...
  | AAAS:S495 | 0.151305752831191 | 0.0357314241797825 | 0.132041598307265 | -0.0189591837047471 | 0.797536660463007 | 0.873891371536815 | 0.137413949034458 | 0.090938940455272 | 0.32755624285282 | -0.0155974101768635 | 0.836443507374893 | 0.959959367405201 | 0.0731653573895362 | ...
  | AAK1:S18 | -0.15201864161209 | 0.0259960483624046 | 0.106773818603058 | -0.176607226725092 | 0.011111199195464 | 0.0416735572148018 | 0.0072333695621583 | 0.925498647554968 | 0.97154430806475 | -0.112563111389829 | 0.115129672041352 | 0.506862357079094 | -0.395380423464989 | ...
  | AAK1:S21 | -0.174439902002435 | 0.0599243542975787 | 0.182709155837417 | -0.261191393107214 | 0.00553091895428402 | 0.0244105206122054 | 0.132875215129148 | 0.20420765821636 | 0.48718306280013 | -0.0460783091341993 | 0.635124619051622 | 0.894087953919721 | -0.253433930004714 | ...
  | AAK1:S623 | -0.0873247019650112 | 0.196212303854886 | 0.387219312596959 | -0.230558528559113 | 0.000716370246937389 | 0.00523930152924566 | 0.148913581972637 | 0.0497348557468205 | 0.23989831344756 | 0.0921103045591922 | 0.191238985103066 | 0.602221142553401 | -0.409398591185069 | ...
  | AAK1:S624 | -0.143812577763513 | 0.0144150432076827 | 0.0729879152473421 | -0.111754971546238 | 0.063209721377087 | 0.152863285408022 | 0.141942701554806 | 0.0322893626769254 | 0.192144892195947 | 0.0180369590659594 | 0.770214847220961 | 0.938181399504017 | -0.30685313560661 | ...

### data/papers/dong2022/supp/mmc5.xlsx (795 kB)
- sheet `Description`: 6 rows x 1 cols
  | Table S4. Function and Immun
  | Description
  |   Table S4A.Primers for fusi
  |   Table S4B. Peptides valida
  |   Table S4C. The list of ant
  |   Table S4D.The peptides pre
- sheet `S4A.Primers for validation`: 25 rows x 6 cols
  | Table S4. Function and Immun |  |  |  |  | 
  | Sample ID | FusionName | Forward primer | Reverse primer | Product length (bp) | PCR validation
  | 137 | FGFR2::PHLDB2 | GAGATCTTCACTTTAGGGGG | CTTTTCTTCATCTAGACGGC | 311 | ok
  | 143 | FGFR2::BICC1 | CTCGCCAGAGATATCAACAA | CTCCAGTTATCAGATTCGCT | 437 | ok
  | 185 | FGFR2::WAC | CAAGCAGTTGGTAGAAGACT | ACAAATTTCGGACATGTGAA | 112 | ok
  | 215 | FGFR2::NRAP | CTCGCCAGAGATATCAACAA | CCTTTGAGTGTTCAAAGCCT | 397 | ok
  | 257 | FGFR2::BICC1 | GGGAGATCTTCACTTTAGGG | ATGGGGATCTTTCTTGGATTT | 229 | ok
  | 265 | FGFR2::KIAA1598 | AGCAGTTGGTAGAAGACTTG | TCAGTTATTACATCTGGTCCC | 127 | ok
- sheet `S4B. Fusion peptides`: 50 rows x 4 cols
  | Table S4. Function and Immun |  |  | 
  | Fusion type | Peptide |   | No. of peptide
  | DLDRILTLTTNE GSSMSLSRS | LTLTTNEG | 8 | #1
  |  | TLTTNEGS | 8 | #2
  |  | LTTNEGSS | 8 | #3
  |  | TTNEGSSM | 8 | #4
  |  | TNEGSSMS | 8 | #5
  |  | NEGSSMSL | 8 | #6
- sheet `S4C.Antibody list for CyTOF`: 32 rows x 3 cols
  - gene-symbol-like: col 1 (74% of 31)
  | Table S4. Function and Immun |  | 
  | Target | Clone |  Metal
  | CD45 | HI30 | 89Y
  | CD196/CCR6 | G034E3 | 141Pr
  | CD123 | 6H6 | 143Nd
  | CD19 | HIB19 | 144Nd
  | CD4 | RPA-T4 | 145Nd
  | CD8a | RPA-T8 | 146Nd
- sheet `S4D.MHC-I immunopeptides`: 6192 rows x 14 cols
  | Table S4. Function and Immun |  |  |  |  |  |  |  |  |  |  |  |  | 
  | No.# | Spectrum | Charge | Spectrum mass | Sequence | Mod_Sites | Specific | Missed_Cleavage | Delta_Mass (Da) | Delta_Mass (PPM) | PSM Score | Target_Decoy | Label_Name | AC
  | 1 | 20210514_HFX_LDY_HuCCT1_F_1. | 5 | 3469.695544 | KKGKADAGKEGNNPAENGDAKTDQAQKA |  | C | 6 | 0.005504 | 1.586306329 | 3.39e-07 | target |  | sp|P05204|HMGN2_HUMAN/
  | 2 | 20210514_HFX_LDY_HuCCT1_1.17 | 4 | 3486.532909 | KSGNFGGSRNMGGPYGGGNYGPGGSGGS |  | C | 4 | -0.004619 | -1.324811818 | 1.12e-06 | target |  | sp|P22626|ROA2_HUMAN/
  | 3 | 20210514_HFX_LDY_9810_F_1.44 | 3 | 2582.012642 | AAAKDTHEDHDTSTENTDESNHD | 0,Acetyl[ProteinN-term](None | N | 1 | -0.001812 | -0.701778129 | 1.33e-06 | target |  | sp|P43487|RANG_HUMAN/
  | 4 | 20210514_HFX_LDY_9810_1.3458 | 5 | 3243.830616 | RLEKPAKYDDIKKVVKQASEGPLKGILG |  | O | 7 | -0.015585 | -4.804504872 | 8.31e-06 | target |  | sp|P04406|G3P_HUMAN/
  | 5 | 20210514_HFX_LDY_9810_F_1.28 | 5 | 2451.3411 | PKRKAEGDAKGDKAKVKDEPQR |  | S | 7 | -0.001423 | -0.580498569 | 9.55e-06 | target |  | sp|P05204|HMGN2_HUMAN/
  | 6 | 20210514_HFX_LDY_HuCCT1_1.28 | 5 | 6240.628719 | GGGNYGSGNYNDFGNYNQQPSNYGPMKS | 22,Deamidated[N](None); | C | 4 | 0.023586 | 3.779426891 | 1.48e-05 | target |  | sp|P22626|ROA2_HUMAN/

### data/papers/dong2022/supp/mmc6.xlsx (2569 kB)
- sheet `Description`: 12 rows x 1 cols
  | Table S5 Patient subgrouping
  |   Table S7A. Top 1376 MAD pr
  |   Table S7B.Proteome KEGG. E
  |   Table S7C.Transcriptome KE
  |   Table S7D.Phosphoproteome 
  |   Table S7E.ssGSEA results. 
  |   Table S7F. Go enrichment r
  |   Table S7G. Clinicopatholog
- sheet `S5A. Top 1376 MAD proteins`: 1378 rows x 2 cols
  - gene-symbol-like: col 0 (99% of 1378)
  | Table S5 Patient subgrouping | 
  | Gene | MAD
  | NQO1 | 1.9550860485649
  | CTSE | 1.87147394856428
  | CAMP | 1.84502187720094
  | AGR2 | 1.83619891791364
  | RPS4Y1 | 1.8245423016223
  | SERPINB5 | 1.74090811200967
- sheet `S5B.Proteome KEGG`: 141 rows x 9 cols
  | Table S5 Patient subgrouping |  |  |  |  |  |  |  | 
  | Protein-up panel |  |  |  |  |  |  |  | 
  | ID | Description | GeneRatio | BgRatio | pvalue | p.adjust | qvalue | geneID | Count
  | hsa04145 | Phagosome | 31/268 | 152/8034 | 1.64844953583001e-16 | 4.31893778387463e-14 | 3.31425117203718e-14 | 11151/4353/1536/3689/1535/36 | 31
  | hsa05416 | Viral myocarditis | 17/268 | 60/8034 | 5.05777703122198e-12 | 4.63441093362553e-10 | 3.55633783978496e-10 | 3689/3107/3106/3105/3135/313 | 17
  | hsa04612 | Antigen processing and prese | 19/268 | 78/8034 | 5.30657740491473e-12 | 4.63441093362553e-10 | 3.55633783978496e-10 | 3107/3106/3105/3135/6892/689 | 19
  | hsa05310 | Asthma | 12/268 | 31/8034 | 1.19264876362442e-10 | 6.38566038731795e-09 | 4.90020543984623e-09 | 5553/8288/2207/3109/3108/312 | 12
  | hsa05330 | Allograft rejection | 13/268 | 38/8034 | 1.21863747849579e-10 | 6.38566038731795e-09 | 4.90020543984623e-09 | 3107/3106/3105/3135/3134/310 | 13
- sheet `S5C.Transcriptome KEGG`: 210 rows x 9 cols
  | Table S5 Patient subgrouping |  |  |  |  |  |  |  | 
  | mRNA-up panel |  |  |  |  |  |  |  | 
  | ID | Description | GeneRatio | BgRatio | pvalue | p.adjust | qvalue | geneID | Count
  | hsa04145 | Phagosome | 61/888 | 152/8034 | 6.98729707607937e-21 | 2.1660620935846e-18 | 1.40481446476964e-18 | 715/11151/7057/3916/811/5114 | 61
  | hsa05169 | Epstein-Barr virus infection | 67/888 | 201/8034 | 9.76841189391551e-18 | 1.5141038435569e-15 | 9.81982458809401e-16 | 3066/1647/896/4616/595/5701/ | 67
  | hsa05132 | Salmonella infection | 59/888 | 206/8034 | 1.74745079711371e-12 | 1.49050301750182e-10 | 9.66675980790659e-11 | 6990/5058/3654/4646/51143/55 | 59
  | hsa04510 | Focal adhesion | 58/888 | 201/8034 | 1.92322970000235e-12 | 1.49050301750182e-10 | 9.66675980790659e-11 | 896/5156/7057/1292/1291/595/ | 58
  | hsa04612 | Antigen processing and prese | 31/888 | 78/8034 | 4.30616831082295e-11 | 2.66982435271023e-09 | 1.73153294182565e-09 | 3309/2923/811/3320/3303/3306 | 31
- sheet `S5D.Phosphoproteome KEGG`: 43 rows x 9 cols
  | Table S5 Patient subgrouping |  |  |  |  |  |  |  | 
  | Phosphoproteome-up panel |  |  |  |  |  |  |  | 
  | ID | Description | GeneRatio | BgRatio | pvalue | p.adjust | qvalue | geneID | Count
  | hsa04110 | Cell cycle | 17/214 | 124/8034 | 2.52322783123806e-08 | 6.86317970096753e-06 | 6.58695265417936e-06 | 1026/4173/994/1111/5933/4172 | 17
  | hsa03060 | Protein export | 5/214 | 23/8034 | 0.000290968299609977 | 0.0395716887469569 | 0.0379790201596181 | 6729/6728/10952/11231/6734 | 5
  | Phosphoproteome-middle panel |  |  |  |  |  |  |  | 
  | ID | Description | GeneRatio | BgRatio | pvalue | p.adjust | qvalue | geneID | Count
  | hsa04020 | Calcium signaling pathway | 20/211 | 196/8034 | 1.78979810669121e-07 | 3.18063297735237e-05 | 2.64993385795091e-05 | 5137/624/5021/113026/23236/2 | 20
- sheet `S5E.ssGSEA results`: 643 rows x 112 cols
  - gene-symbol-like: col 1 (100% of 639)
  | Table S5 Patient subgrouping |  |  |  |  |  |  |  |  |  |  |  |  |  | ...
  | Transcriptome ssGSEA result |  |  |  |  |  |  |  |  |  |  |  |  |  | ...
  | Patient_ID | Protein subgroup | KEGG_GLYCOLYSIS_GLUCONEOGENE | KEGG_MAPK_SIGNALING_PATHWAY | KEGG_CALCIUM_SIGNALING_PATHW | KEGG_CHEMOKINE_SIGNALING_PAT | KEGG_VASCULAR_SMOOTH_MUSCLE_ | KEGG_FOCAL_ADHESION | KEGG_ECM_RECEPTOR_INTERACTIO | KEGG_CELL_ADHESION_MOLECULES | KEGG_TIGHT_JUNCTION | KEGG_NATURAL_KILLER_CELL_MED | KEGG_FC_GAMMA_R_MEDIATED_PHA | KEGG_LEUKOCYTE_TRANSENDOTHEL | ...
  | 115 | S4 | 0.158541570079579 | -0.0175895374169658 | 0.0123598996847297 | -0.125831709354186 | -0.0825592698473339 | 0.324857177423623 | 0.39672451059503 | 0.379488033988128 | 0.0905926143241666 | 0.117839506831051 | -0.283062370956628 | 0.0689462823012261 | ...
  | 117 | S3 | 0.315535699278444 | 0.00913127557932544 | 0.0407625221705907 | -0.0487569695433233 | -0.0883414567953153 | 0.337660143706208 | 0.435467689010636 | 0.352711810709577 | 0.0739020586292279 | 0.0865894469460171 | -0.229244668431354 | 0.0738638009426602 | ...
  | 121 | S4 | 0.116040132065755 | 0.0886985338977117 | 0.101682577533861 | -0.0369859100999451 | -0.0125235016787782 | 0.357603959414271 | 0.403301668520495 | 0.380406299220489 | 0.264757550464315 | 0.115759762261553 | -0.144584228790676 | 0.184700310365822 | ...
  | 123 | S3 | 0.29276184921767 | -0.0279209823694511 | -0.00995866842480481 | 0.018790245664193 | -0.105859136523258 | 0.335907713998392 | 0.406794975258664 | 0.40490065681728 | 0.0196100559387839 | 0.236725507500385 | -0.146374002735036 | 0.191961120380151 | ...
  | 125 | S1 | 0.244653894880671 | 0.0266040003326677 | -0.075864742915278 | 0.00435052138985711 | -0.120806283384524 | 0.427568629823825 | 0.514987299985138 | 0.231541809997035 | -0.181929921238371 | 0.286471332519488 | -0.075832096246668 | 0.131312208581668 | ...
- sheet `S5F.Go enrichment results`: 977 rows x 72 cols
  | Table S5 Patient subgrouping |  |  |  |  |  |  |  |  |  |  |  |  |  | ...
  | CA19-9 up regulation related |  |  |  |  |  |  |  |  | CA19-9 down regulation relat |  |  |  |  | ...
  | ID | Description | GeneRatio | BgRatio | pvalue | p.adjust | qvalue | geneID | Count | ID | Description | GeneRatio | BgRatio | pvalue | ...
  | GO:0002446 | neutrophil mediated immunity | 131/614 | 499/18670 | 3.67472139065571e-82 | 1.73189619141603e-78 | 1.27338766505669e-78 | 9545/5864/23218/221/5580/310 | 131 | GO:0008380 | RNA splicing | 121/717 | 469/18670 | 1.54824755281024e-66 | ...
  | GO:0043312 | neutrophil degranulation | 129/614 | 485/18670 | 1.26785437434042e-81 | 2.9876988331332e-78 | 2.19672452648877e-78 | 9545/5864/23218/221/5580/310 | 129 | GO:0000375 | RNA splicing, via transester | 107/717 | 382/18670 | 1.27426813816016e-62 | ...
  | GO:0002283 | neutrophil activation involv | 129/614 | 488/18670 | 2.94502552557654e-81 | 4.27107317669528e-78 | 3.14033365666764e-78 | 9545/5864/23218/221/5580/310 | 129 | GO:0000377 | RNA splicing, via transester | 106/717 | 379/18670 | 5.95336971427953e-62 | ...
  | GO:0042119 | neutrophil activation | 130/614 | 498/18670 | 3.62492949433081e-81 | 4.27107317669528e-78 | 3.14033365666764e-78 | 9545/5864/23218/221/5580/310 | 130 | GO:0000398 | mRNA splicing, via spliceoso | 106/717 | 379/18670 | 5.95336971427953e-62 | ...
  | GO:0006909 | phagocytosis | 72/614 | 369/18670 | 2.68627399681443e-35 | 2.53208186939728e-32 | 1.86172926263433e-32 | 5580/10097/4688/2268/4233/36 | 72 | GO:0050684 | regulation of mRNA processin | 48/717 | 137/18670 | 2.39246671033557e-33 | ...
- sheet `S7G. Clinicopathologic relation`: 42 rows x 14 cols
  | Table S5 Patient subgrouping |  |  |  |  |  |  |  |  |  |  |  |  | 
  | Characteristics | Proteomic subgroup |  |  |  |  | RNAseq subgroup |  |  |  | Phosphoproteomic subgroup |  |  | 
  |  | Subgroup1 | Subgroup 2 | Subgroup 3 | Subgroup 4 | P* | Subgroup1 | Subgroup 2 | Subgroup 3 | P* | Subgroup1 | Subgroup 2 | Subgroup 3 | P*
  | Age (years) |  |  |  |  | 0.636 |  |  |  | 0.56 |  |  |  | 0.015
  | <median | 20 | 28 | 23 | 34 |  | 46 | 55 | 17 |  | 33 | 54 | 18 | 
  | ≥median | 21 | 32 | 23 | 33 |  | 54 | 59 | 24 |  | 25 | 54 | 30 | 
  | Gender |  |  |  |  | 0.007221 |  |  |  | 0.01563 |  |  |  | 0.03767
  | male | 22 | 36 | 34 | 28 |  | 64 | 53 | 27 |  | 40 | 52 | 28 | 
- sheet `S7H. Survial analysis`: 24 rows x 8 cols
  | Table S5 Patient subgrouping |  |  |  |  |  |  | 
  | Variables | Univariable analysisa | Multivariable analysisb |  |  |  |  | 
  |  |  | Proteomic subgroup |  | RNAseq subgroup |  | Phosphoproteomic subgroup | 
  |  | P | Hazard ratio (95% CI) | P | Hazard ratio (95% CI) | P | Hazard ratio (95% CI) | P
  | Age (years): ≥61 v <61 | NS |  |  |  |  |  | 
  | Gender: male v female | NS |  |  |  |  |  | 
  | TB, Total bilirubin (µmol/L) | NS |  |  |  |  |  | 
  | CA19-9 (U/mL): >37 v ≤37 | 1.1e-05 |  |  |  1.417 (0.886-2.268) | 0.146 |  1.480 (0.885-2.475) | 0.135
- sheet `S7I. PDPCs`: 11 rows x 11 cols
  - gene-symbol-like: col 0 (82% of 11)
  | Table S5 Patient subgrouping |  |  |  |  |  |  |  |  |  | 
  | Patient ID | Sex | Age | HCVAb | HBsAg | Liver cirrhosis  | CA19-9(U/ml) | Tumor size | Microvascular invasion | Intrahepatic metastasis | TNM staging
  | ICC772 | male | 76 | negative | negative | yes | 22.9 | 2.5 | 0 | no | I
  | ICC1370 | male | 60 | negative | positive | no | 11.1 | 2.5 | 0 | no | I
  | ICC1969 | female | 76 | negative | positive  | no | 41.7 | 10 | 0 | no | I
  | ICC1239 | male | 55 | negative | positive | no | 134.7 | 2.5 | 0 | no | I
  | ICC880 | male | 70 | negative | negative | no | 2598 | 6 | 1 | no | II
  | ICC892 | male | 40 | negative | positive | yes | 22.6 | 1.5 | 1 | yes | IVa
- sheet `S7J.Proteomis of cell lines`: 9372 rows x 17 cols
  - gene-symbol-like: col 0 (98% of 9358), col 1 (93% of 9371)
  |  |  |  |  |  |  |  |  |  | Table S5 Patient subgrouping |  |  |  |  | ...
  | Gene | Protein | ICC5784 (S2) | ICC772 (S4) | LIPF-178C (S1) | LIPF-155C (S3) | HuCCT1 (S1) | ICC880 (S2) | ICC4175 (S3) | ICC1969 (S4) | ICC1239 (S4) | LICCF (S3) | ICC1370 (S2) | ICC2935 (S1) | ...
  | NUDT4;NUDT10;NUDT11 | A0A024RBG1;Q8NFP7;Q96G61 | 2983 | 4250.2 | 3964.3 | 3919.8 | 4109.2 | 3326.5 | 3549.2 | 3821.5 | 3427.3 | 4102.6 | 3844.7 | 3833.1 | ...
  | TMSB15A;TMSB15B | P0CG34;P0CG35;A0A087X1C1 | 26254 | 31784 | 8167.2 | 13627 | 12825 | 9310.7 | 42682 | 23165 | 21855 | 11502 | 31345 | 17572 | ...
  | LINC00493 | A0A096LP01 | 21936 | 39650 | 35835 | 54174 | 49395 | 30867 | 40685 | 44310 | 36622 | 28844 | 45403 | 29013 | ...
  |  | P0DPI2;A0A0B4J2D5 | 76052 | 124060 | 149460 | 198420 | 114180 | 276540 | 136770 | 179840 | 163170 | 163200 | 183620 | 162170 | ...
  |  | A0A0B4J2E5 | 6024.9 | 3671 | 2591 | 3366 | 1872.7 | 3860.9 | 2670.6 | 4133 | 2662.3 | 3481 | 3472.3 | 2839.4 | ...
  | PIGBOS1 | A0A0B4J2F0 | 6339.4 | 11548 | 10828 | 13851 | 8731.9 | 16384 | 13247 | 14917 | 12469 | 7758.2 | 18473 | 9288.6 | ...
- sheet `S7K. Drug list`: 37 rows x 11 cols
  - gene-symbol-like: col 10 (97% of 36)
  | Table S5 Patient subgrouping |  |  |  |  |  |  |  |  |  | 
  | No.in panel | Drug | Category | Targets | Pathway | Clinical status | Screening max dose (µM) | Dilution fold | # Point of doses | Company | Identifier
  | 1 | Lapatinib | TKI | BrbB2, EGFR, ErbB4 | RTK signaling | clinically used | 40 | 2-fold | 10 | selleck | S2111
  | 2 | Sorafenib tosylate | TKI | Multi-targeted, RAF, VEGFR,  | RTK signaling | clinically used | 40 | 2-fold | 10 | selleck | S1040
  | 3 | Pazopanib HCl (GW786034 HCl) | Receptor/Upstream signal act | VEGFR, FGFR, PDGFR | RTK signaling | clinically used | 40 | 2-fold | 10 | selleck | S1035
  | 4 | Etoposide | Chemotherapy | Topoisomerase II | DNA replication | clinically used | 40 | 2-fold | 10 | selleck | S1225
  | 5 | Oxaliplatin | Chemotherapy | DNA crosslinker | DNA replication | clinically used | 40 | 2-fold | 10 | selleck | S1224
  | 6 | Chloroquine diphosphate | TKI | Her2, EGFR | RTK signaling | clinically used | 40 | 2-fold | 10 | selleck | S4157

### data/papers/dong2022/supp/mmc7.xlsx (1148 kB)
- sheet `Description`: 7 rows x 1 cols
  | Table S6 Clinicopathologic c
  |   Table S6A. Biomarker analy
  |   Table S6B. Clinicopatholog
  |   Table S6C. Survial analysi
  |   Table S6D. Clinicopatholog
  |   Table S6E. Differential pr
  |   Table S6F. Differential ph
- sheet `S6A. Biomarker analysis`: 36 rows x 4 cols
  - gene-symbol-like: col 0 (94% of 36)
  | Table S6 Clinicopathologic c |  |  | 
  | Gene | Logrank P value | Hazard ratio (HR) | mRNA vs protein correlation
  | SLC16A3 | 3.6e-09 | 3.86662 | 0.921802072831821
  | PLOD2 | 1.1e-08 | 3.65515 | 0.785739813199767
  | HKDC1 | 1.8e-08 | 0.281708 | 0.661659278936166
  | ZBTB20 | 4.5e-08 | 0.293966 | 0.865331274370176
  | HN1 | 1e-07 | 3.33041 | 0.769817520389602
  | NF2 | 1.5e-07 | 0.304271 | 0.658290793874317
- sheet `S6B. Clinicopathologic_1`: 40 rows x 7 cols
  | Table S6 Clinicopathologic c |  |  |  |  |  | 
  | Characteristics | HKDC1 expression |  |  | SLC16A3 expression |  | 
  |  | Low | High | P* | Low | High | P*
  | Age (years) |  |  | 0.8912 |  |  | 0.49
  | <61 | 46 | 49 |  | 44 | 50 | 
  | ≥61 | 61 | 59 |  | 63 | 57 | 
  | Gender |  |  | 0.215 |  |  | 0.8905
  | male | 65 | 55 |  | 59 | 61 | 
- sheet `S6C. Survial analysis`: 21 rows x 6 cols
  | Table S6 Clinicopathologic c |  |  |  |  | 
  | Variables | Univariable analysisa | Multivariable analysisb |  |  | 
  |  |  | HKDC1 |  | SLC16A3 | 
  |  | P | Hazard ratio (95% CI) | P | Hazard ratio (95% CI) | P
  | Age: >median v ≤median | NS |  |  |  | 
  | Gender: male v female | NS |  |  |  | 
  | TB: >20.4 v ≤20.4 | NS |  |  |  | 
  | CA19-9: >37 v ≤37 | 1.1e-05 |  | NS |  | NS
- sheet `S6D. Clinicopathologic_2`: 35 rows x 7 cols
  | Table S6 Clinicopathologic c |  |  |  |  |  | 
  | Characteristics | SLC16A3 expression |  |  | HKDC1 expression |  | 
  |  | Low | High | P* | Low | High | P*
  | Age |  |  | 0.572 |  |  | 0.55
  | ≤61 | 40 | 71 |  | 98 | 13 | 
  |  >61 | 36 | 75 |  | 95 | 16 | 
  | Gender |  |  | 0.274 |  |  | 0.91
  | male | 40 | 88 |  | 111 | 17 | 
- sheet `S6E. Protein change`: 5505 rows x 7 cols
  - gene-symbol-like: col 0 (100% of 5504)
  | Table S6 Clinicopathologic c |  |  |  |  |  | 
  | Gene symbol | HKDC1 high vs HKDC1 low |  |  | SLC16A3 high vs SLC16A3 low |  | 
  |  | Log2 FC | P value | Adjusted P value | Log2 FC | P value | Adjusted P value
  | A2M | -0.257497655952728 | 0.00655588490816589 | 0.0188554515236428 | 0.284551201441093 | 0.00261075249477765 | 0.00793730671933945
  | AAAS | -0.020053155816214 | 0.624998449057522 | 0.725779119188368 | 0.0879764146325497 | 0.0311363917119394 | 0.061711969452122
  | AACS | -0.0144765694028813 | 0.825700578536882 | 0.878384490160465 | -0.0427573773707004 | 0.515202676627413 | 0.610306490188672
  | AADAC | 0.198943409118234 | 0.298354453648621 | 0.417802546188525 | -0.494582492055757 | 0.00926741803395175 | 0.0226518587395835
  | AAGAB | -0.053277114928311 | 0.388057364231518 | 0.509325290553867 | 0.186079063904388 | 0.002331158381253 | 0.00719754961484511
- sheet `S6F. Phosphoprotein change`: 5552 rows x 7 cols
  - gene-symbol-like: col 0 (99% of 5551)
  | Table S6 Clinicopathologic c |  |  |  |  |  | 
  | Gene symbol | HKDC1 high vs HKDC1 low |  |  | SLC16A3 high vs SLC16A3 low |  | 
  |  | Log2 FC | P value | Adjusted P value | Log2 FC | P value | Adjusted P value
  | AAAS | -0.08731768 | 0.09881197 | 0.20114 | 0.110822159495182 | 0.0358055758683957 | 0.085677076538908
  | AAGAB | -0.07660903 | 0.1658748 | 0.2946349 | 0.0913861257804107 | 0.098026211021155 | 0.185591837869971
  | AAK1 | 0.216919620049455 | 5.43413354126416e-07 | 1.48541906504802e-05 | -0.142263058016257 | 0.0012274541730207 | 0.00587167517766538
  | AAMDC | 0.01221035 | 0.8684437 | 0.9196352 | 0.0368193798623126 | 0.617347174054728 | 0.727007527340765
  | AATF | 0.0945125 | 0.1065965 | 0.2128761 | 0.00628847568464592 | 0.914743423587188 | 0.948591152585555

### data/papers/dong2022/supp/mmc8.xlsx (4304 kB)
- sheet `Description`: 8 rows x 1 cols
  | Table S7. Tumor microbial in
  | Table S7A. α diversity index
  | Table S7B. Rarefaction index
  | Table S7C. OTU sequence numb
  | Table S7D. OTU percentage. I
  | Table S7E. OTU sequence. The
  | Table S7F. KEGG pathway by P
  | Table S7G. Kruskal-Wallis te
- sheet `S7A. α diversity index`: 162 rows x 7 cols
  - gene-symbol-like: col 0 (99% of 162)
  | Table S7. Tumor microbial in |  |  |  |  |  | 
  | Protein subgroup | Sample Id | Sample weight（mg） | ace | shannon | sobs | PD_whole_tree
  | S1 | 125 | 84.80000000000021 | 413 | 3.457157 | 413 | 307.76694
  | S1 | 126 | 375.9999999999999 | 147 | 1.986892 | 147 | 123.46832
  | S1 | 157 | 70.30000000000003 | 323 | 2.5738 | 323 | 249.93978
  | S1 | 158 | 220.9000000000001 | 560.822099 | 3.689563 | 419 | 292.33635
  | S1 | 187 | 53.300000000000125 | 392 | 3.19424 | 392 | 295.80149
  | S1 | 188 | 249.49999999999983 | 588 | 3.824553 | 588 | 422.83311
- sheet `S7B. Rarefaction index `: 1239 rows x 4 cols
  - gene-symbol-like: col 0 (100% of 1239)
  | Table S7. Tumor microbial in |  |  | 
  | Protein subgroup | numsampled | Shannon-Wiener index | Rarefaction-curve index
  | S1 | 1 | 0 | 1
  | S1 | 100 | 2.27759 | 22.5
  | S1 | 200 | 2.386555 | 32.8
  | S1 | 300 | 2.430795 | 41.05
  | S1 | 400 | 2.465 | 48
  | S1 | 500 | 2.48294 | 54
- sheet `S7C. OTU sequence number`: 2887 rows x 171 cols
  - gene-symbol-like: col 0 (100% of 2887)
  | Table S7. Tumor microbial in |  |  |  |  |  |  |  |  |  |  |  |  |  | ...
  | OTUId | 125 | 126 | 157 | 158 | 187 | 188 | 241 | 242 | 285 | 286 | 325 | 326 | 343 | ...
  | OTU2 | 6721 | 11022 | 2780 | 13789 | 4203 | 10159 | 4450 | 7282 | 6120 | 3619 | 4661 | 5309 | 8250 | ...
  | OTU3 | 2686 | 595 | 3 | 470 | 8 | 3 | 26 | 24 | 2 | 144 | 247 | 2 | 5169 | ...
  | OTU5 | 6786 | 2686 | 8293 | 1724 | 7691 | 8753 | 13173 | 7928 | 10532 | 2248 | 2499 | 9927 | 3807 | ...
  | OTU6 | 2314 | 2387 | 3688 | 4742 | 2525 | 4424 | 2012 | 4459 | 2705 | 2300 | 2147 | 4160 | 4123 | ...
  | OTU7 | 1421 | 1452 | 2082 | 2642 | 501 | 1470 | 562 | 1050 | 969 | 1068 | 15875 | 2463 | 375 | ...
  | OTU8 | 876 | 3322 | 1059 | 1402 | 369 | 128 | 594 | 1669 | 611 | 921 | 43 | 1224 | 270 | ...
- sheet `S7D. OTU percentage`: 2887 rows x 171 cols
  - gene-symbol-like: col 0 (100% of 2887)
  | Table S7. Tumor microbial in |  |  |  |  |  |  |  |  |  |  |  |  |  | ...
  | OTUId | 125 | 126 | 157 | 158 | 187 | 188 | 241 | 242 | 285 | 286 | 325 | 326 | 343 | ...
  | OTU2 | 0.223675452609159 | 0.368160865789298 | 0.0925679275439531 | 0.460846896828315 | 0.139950719232818 | 0.338780138059826 | 0.148486769661984 | 0.242660535172781 | 0.203735144312394 | 0.120766176127073 | 0.155377025135009 | 0.177173368930419 | 0.275201814664087 | ...
  | OTU3 | 0.0893903088391906 | 0.0198744071080232 | 9.98934469898775e-05 | 0.0157080311486916 | 0.00026638252530634 | 0.000100043352119252 | 0.000867563148586873 | 0.000799760071978406 | 6.65801125203902e-05 | 0.00480528581439584 | 0.00823388225881725 | 6.6744535291173e-05 | 0.172426446060444 | ...
  | OTU5 | 0.225838658146965 | 0.0897187520876478 | 0.276138785295685 | 0.0576183951071154 | 0.256093500266383 | 0.291893153699937 | 0.43955420601288 | 0.264187410443534 | 0.350610872532375 | 0.0750158507691794 | 0.0833055537035802 | 0.331286500917737 | 0.126993128294082 | ...
  | OTU6 | 0.0770101171458999 | 0.079731444986305 | 0.122802344166223 | 0.158484007887437 | 0.0840769845498135 | 0.147530596591856 | 0.0671360405752611 | 0.148588756706321 | 0.0900496021838277 | 0.0767510928688224 | 0.0715714380958731 | 0.13882863340564 | 0.13753419174061 | ...
  | OTU7 | 0.0472910010649627 | 0.0485002338165542 | 0.069326052210975 | 0.0882991878613683 | 0.0166822056473095 | 0.0490212425384333 | 0.0187527111348393 | 0.0349895031490553 | 0.032258064516129 | 0.0356392031234358 | 0.529201946796453 | 0.0821958952110796 | 0.0125091733938221 | ...
  | OTU8 | 0.0291533546325879 | 0.110962656156056 | 0.0352623867874267 | 0.0468567227031182 | 0.0122868939797549 | 0.00426851635708807 | 0.0198204811638693 | 0.0556166483388317 | 0.0203402243749792 | 0.0307338071879067 | 0.00143342889525968 | 0.0408476555981979 | 0.00900660484355194 | ...
- sheet `S7E. OTU sequence`: 5771 rows x 1 cols
  | Table S7. Tumor microbial in
  | >OTU2
  | ACTCCTACGGGAGGCAGCAGTGGGGAAT
  | >OTU3
  | ACTCCTACGGGAGGCAGCAGTAGGGAAT
  | >OTU5
  | ACTCCTACGGGAGGCAGCAGTGGGGAAT
  | >OTU6
- sheet `S7F. KEGG pathway by PICRUSt`: 258 rows x 82 cols
  | Table S7. Tumor microbial in |  |  |  |  |  |  |  |  |  |  |  |  |  | ...
  | Pathways | B001 | B003 | B005 | B007 | B009 | B011 | B013 | B015 | B017 | B019 | B021 | B023 | B025 | ...
  | ko00010 | 0.01476321526254363 | 0.0138890997783303 | 0.01410568267551993 | 0.01341971735668384 | 0.01380298724773313 | 0.01478090256214735 | 0.01517044350882538 | 0.01448279140415926 | 0.01387887417424342 | 0.01594066195107669 | 0.01622813711934788 | 0.01569265356754116 | 0.0174627198978871 | ...
  | ko00020 | 0.0129007767159352 | 0.0126035986927265 | 0.0125086715546335 | 0.01272131997462779 | 0.01277696896397549 | 0.01301356496875071 | 0.01279672820535085 | 0.01287354829173953 | 0.01280253692729577 | 0.01269874170745605 | 0.01295947200808751 | 0.01284953682956092 | 0.01253295510067602 | ...
  | ko00030 | 0.007899212714671477 | 0.008445364027479132 | 0.008028830734943048 | 0.007332517165034591 | 0.007631783687762105 | 0.009085446708074731 | 0.008205193185463198 | 0.00810289702166065 | 0.00784579683693136 | 0.008496363625078196 | 0.008992206136665752 | 0.008812952522551482 | 0.00895780193436056 | ...
  | ko00040 | 0.005273205282045414 | 0.005794445567722369 | 0.005629689884939533 | 0.004822579394060071 | 0.005143860135780409 | 0.005990878669061271 | 0.005907471056088729 | 0.005857887696476533 | 0.005525408339045093 | 0.005753973326314254 | 0.006524717435242917 | 0.005685969735674631 | 0.005388305707409944 | ...
  | ko00051 | 0.004549302003061177 | 0.004430460621073507 | 0.004721375615664786 | 0.003837493000489525 | 0.004209818972205308 | 0.003902781162120537 | 0.005178434673210532 | 0.004645268304708113 | 0.004330082646646074 | 0.005545403476207962 | 0.005682827561225515 | 0.005284485643673914 | 0.006252726030496469 | ...
  | ko00052 | 0.003585673111407544 | 0.004177837961847826 | 0.004179115406585236 | 0.002706543334330387 | 0.003168412622143065 | 0.003453148141879411 | 0.004505135440551226 | 0.00378418328310598 | 0.003489046152149348 | 0.005130074189348376 | 0.005893191563406417 | 0.004942077097717578 | 0.006391823816931852 | ...
- sheet `S7G. Kruskal-Wallis test`: 257 rows x 11 cols
  | Table S7. Tumor microbial in |  |  |  |  |  |  |  |  |  | 
  | Pathways | p.value | method | mean(S1_T) | mean(S2_T) | mean(S3_T) | mean(S4_T) | SD(S1_T) | SD(S2_T) | SD(S3_T) | SD(S4_T)
  | ko00010 | 0.05936988243796805 | Kruskal-Wallis | 0.01490295850733434 | 0.01559724508462007 | 0.01615058111554878 | 0.01658085466228346 | 0.001111501393733568 | 0.001721355754558183 | 0.002240017954355854 | 0.002262298013009006
  | ko00020 | 0.3657456822970768 | Kruskal-Wallis | 0.01277199559902781 | 0.01286916963829984 | 0.01288341672344172 | 0.01280805678184706 | 0.0001760839664545216 | 0.0003500680234343293 | 0.0004233042187504135 | 0.0005596166239447909
  | ko00030 | 0.03908654534607301 | Kruskal-Wallis | 0.008303458349618731 | 0.008580240911744108 | 0.008770654136154335 | 0.009015653880911882 | 0.0004686617706425894 | 0.0006093956789717497 | 0.0008478716180343674 | 0.0009898255184671188
  | ko00040 | 0.6727724822476555 | Kruskal-Wallis | 0.005637742800461469 | 0.005742315536264453 | 0.005814599774349471 | 0.005714999406206534 | 0.0003728708429649404 | 0.0003598174652271352 | 0.0004240540287353838 | 0.0004003354686308852
  | ko00051 | 0.09272803834253993 | Kruskal-Wallis | 0.00483523846384283 | 0.005325296876790542 | 0.005487584124150754 | 0.005800212947424214 | 0.0006631425667050568 | 0.001003894141303877 | 0.001287362255545578 | 0.001232854032759255
  | ko00052 | 0.1489895753559947 | Kruskal-Wallis | 0.004286862142341278 | 0.004886933487096629 | 0.005244305179160751 | 0.005502489670648554 | 0.0009579968842493809 | 0.001348606127028574 | 0.001841864863862827 | 0.001799665486359115

### data/papers/dong2022/supp/mmc9.pdf (22138 kB)
- 49 pages
  - p3: 35 gene-like tokens; needed to facilitate the identification of suitable targets for KRAS,andIDH1/2mutations(FigureS1G;Ta / ways(Figure1E;TableS1).FurtheranalysisrevealedthatTP53 / ple)wereidentified(TableS1).Isobarictandemmasstag-based occurring in chromosomes 5q23.3 (20.2%) and  / globalproteomic/phosphoproteomicprofilingquantified10,529 (20.2%)(FigureS2A;TableS2),consistentwithp
  - p4: 101 gene-like tokens; 
    A
    B C D
    P = 7.2e-03
    100.0 P = 1.0e-04 P = 0.59
    10.0
    1.0
    0.1
    Aflatoxin AA Others
  - p5: 54 gene-like tokens; ways(Figure2C;TableS2).Amongthe723cancergenecensus (TableS3).Here,TP53mutationswereassociatedwiththe / EPS15,ERCC5,EZR,GOLGA5,KTN1,MAP2K4,PCM1,PRCC, ures3AandS3D;TableS3).KRASmutationswereassociated / hasbeenlinkedwiththehyperprogressioninimmunotherapy(Fig- clepathway(Figures3BandS3D;TableS3). / bolism(Figure2F;TableS2).Besides,14qlossshowedcisand Notably, it has been reported that KRAS and TP5
    ll
    Article
    These copynumber alterations (CNAs) had cis and trans im- Carboneetal.,2020),whileKRASandIDH1/2mutationswere
    pactsonmRNA,protein,andphosphoproteinabundance(Figures oncogenic (Aguirre and Hahn, 2018; Waitkus et al., 2018).
    2AandS2B).Totalsof3,981,1,081,and408significantciscorre- Among them, mutations in TP53 (p = 1.1e-02) and KRAS (p =
    lationswereobservedformRNA,proteins,andphosphoproteins, 5.2e-04)weresignificantlyassociatedwithpoorsurvival,while
    respectively, with only 194 significant cis effects overlapping BAP1(p=0.20)orIDH1/2(p=0.90)mutationswerenotassoci-
    across all 3 omics (Figure 2B). In total, 963 proteins showed atedwithpatientsurvivalintheFU-iCCAcohort(FiguresS3A–
  - p6: 65 gene-like tokens; 
    A B
    C
    D E F
    chr14q
    898 468 585
    mRNA Protein
    G H
    14qloss
  - p7: 61 gene-like tokens; mors,whiletheRhoGTPasepathwaywassignificantlyupregu- HuCCT1 cells (Figure S4H; Table S4D). These res / SeealsoFigureS2andTableS2.
    ll
    Article
    KRASmutation.RNAiandchemicalinhibitortreatmentwereper- phorylation,withdownregulationofGRB2expressionandS90
    formed with patient-derived primary cancer cell lines (PDPCs: phosphorylation inFGFR2-altered tumors(Figure 4G).Usually,
    ICC1370[TP53p.M246I],ICC880[KRASp.G12D],andICC772 dimeric GRB2 can bind to FGFR2 under physiological condi-
    [TP53WT;KRASWT]) established previously (Dong et al., 2018), tions,resultinginpartialphosphorylationofFGFR2andinhibiting
    and successfully validated those therapeutic targets for iCCA bothdephosphorylationofFGFR2byPTPN11andphosphoryla-
    withTP53orKRASmutations(Figures3IandS3E–S3G).Asex- tion of PTPN11 by FGFR2 (Ahmed et al., 2013). When FGFR2
  - p8: 74 gene-like tokens; SeealsoFigureS3andTableS3.
    A B
    C m p m Pr R o N te A in Log 22. 5 (FC) E p N L P L o o h A g g o 2 2 s ( ( p F F h C C o ) ) r y > < la 0 0 ti , , o F F n D D R R < < 0 0 
    D F
    G H
    I
    protein mRNA
    protein mRNA
    protein mRNA
  - p9: 4 gene-like tokens; SeealsoFigureS4andTableS4.
  - p10: 21 gene-like tokens; SeealsoFigureS4andTableS4.
  - p11: 69 gene-like tokens; maximumexpressionofadhesionandbiliary-specificproteins, was conducted on 10/15cell lines (TableS5K). / 0.981; p = 3.3e-02; Table S5). Importantly, the proteomic sub- biomarkers / CA19-9 and CEA levels (Figure S5B). Besides, we observed a (STAR Methods; Figure 7A; Table S6). Amon / Each subgroup showed distinct profiles of the recurrently pathologic features (Table S6). Moreover, 
    ll
    Article
    Proteomicsubgroupswithdistinctbiologicaland 2.8e-03, respectively) (Figure 6G). Meanwhile, by clustering of
    clinicalfeatures mRNA and phosphoprotein, wealsoidentified threetranscrip-
    Weidentified 4distinct proteomic subgroups (S1–S4) by clus- tomicsubgroupsandthreephosphoproteomicsubgroupswith
    teringusingthe1,376mostvariableproteins(Figure6A;Table significant prognostic values, respectively (Figures S5E and
    S5), which had diverse clinical, genomic, immunologic, and S5F). The transcriptomic and phosphoproteomic classification
    microenvironmental features. S1 showed the most abundant showed partial overlaps and different molecular features with
  - p12: 66 gene-like tokens; SeealsoFigureS5andTableS5.
    A B
    S1 S2 S3 S4
    mRNA
    Glucose metabolism Protein
    Cytokine signaling in immune system Phospho
    Interferon signaling Infectious disease Enrichment score Antigen processing cross presentation 2 1 Natural killer cell mediated cytotoxicity
    Neutrophil degranulation
    Innate immune system
  - p13: 72 gene-like tokens; SeealsoFigureS6andTableS6.
    A B
    uS ri avv pl robability 0 0 0 1 . . . . 2 5 7 0 5 0 5 0 ++ ++ + + + + + + +++++++ ++ + + + + + ++++ + + ++ + +++ + ++ + + + +++++ + + + ++++
    + +H Lo ig w h ( ( n n = = 1 1 0 0 1 6 ) )P = 1.8e-08 + +H Lo ig w h ( ( n n = = 1 1 0 0 5 2 ) ) P = 3.6e-09
    0.00 0.00 0 10 20 30 40 50 60 0 10 20 30 40 50 60 C Months after surgery Months after surgery
    D E
    .
    F
    HA
  - p14: 28 gene-like tokens; subgroups (Table S7). Several different methods (Kurilshikov entiated subgroup retained partial feat
  - p20: 69 gene-like tokens; 
    ll
    Article
    STAR+METHODS
    KEYRESOURCESTABLE
    REAGENTorRESOURCE SOURCE IDENTIFIER
    Antibodies
    Rabbitpolyclonalanti-MPO DAKO Cat#A0398,RRID:AB_2335676
    Rabbitmonoclonalanti-Periostin Abcam Cat#ab215199
  - p23: 9 gene-like tokens; normalizeddatafilesareprovidedasTableS1.
  - p24: 20 gene-like tokens; wereclassifiedasTNMstagesI,IIandIII-IVArespectively.Detailedclinicopathologicfeaturesaresummarizedin / of9PDPCsincludingICC772,ICC1370,ICC1969,ICC1239,ICC880,ICC892,ICC2935,ICC4715,ICC5784,islistedinTabl / were204high-qualitypairedsampleswithallfouromicsdata,andtheaveragetumorcellularityofthesesampleswas4
  - p25: 20 gene-like tokens; averageof14,255genespersample(TableS1),coveringthemajorityofthegenesinproteomics.
  - p28: 7 gene-like tokens; werequantifiedinatleasthalfsamples(TableS1)wereimputedforthemissingvaluesusingK-nearestneighbor(KNN)
  - p31: 19 gene-like tokens; panelof30antibodies(detailedantibodylistinTableS4C),toeachtubesothetotalstainingvolumewas100mL.Eacht / resultingcDNAwasusedasthetemplateforsemi-quantitativePCRamplificationusingtheprimersreportedinTableS
  - p32: 7 gene-like tokens; Theinformationof35screeneddrugsislistedinTableS5K.Thecellsweredigestedandseededin384-wellplatesatthe

## chaisaingmongkol2017

Chaisaingmongkol J et al. Common molecular subtypes among Asian hepatocellular carcinoma and cholangiocarcinoma. Cancer Cell 2017;32:57-70

- identifiers: {"doi": "10.1016/j.ccell.2017.05.009", "pmid": "28648284", "pmcid": "PMC5524207"}
- resolved title: Common Molecular Subtypes Among Asian Hepatocellular Carcinoma and Cholangiocarcinoma. Cancer Cell 2017
- want: TIGER-LC C1 (poor; PLK1 / ECT2 mitotic) vs C2 (T-cell infiltration, bile acid) signature; GSE76297 labels.

### data/papers/chaisaingmongkol2017/supp/mmc1.pdf (10833 kB)
- 17 pages
  - p8: 86 gene-like tokens; 
    A
    ICC-C1 ICC-C2 ICC-UM
    %
    C1 C2 UM
    TP53 43 15 4
    KRAS 30 17 7
    ARID1A 5 14 13
    SMAD4 13 12 0
  - p10: 56 gene-like tokens; 
    3
    T
    2
    NT
    1
    0
    −1.0 −0.5 0.0 0.5 1.0 −1.0 −0.5 0.0 0.5 1.0
    Pearson's correlation
  - p14: 60 gene-like tokens; 
    Figure S3, related to Figure 6. Relationship between ICC subtypes with
    commonly mutated genes in the Japanese cohort, somatic copy number
    alterations (SCNA), correlation with gene expression in ICC or HCC and PLK1 and
    ECT2 expression and their association with prognosis. (A) The frequency of
    commonly mutated genes in the C1 (n=77) or C2 subtype (n=59) of 182 Japanese ICC
    tumors as well as an unmatched group (UM, n=46) are shown. The percent of cases of
    each subtype with mutation are shown in the right panel and the number of cases in
    each subtype is indicated in parentheses. (B) The mutation frequency of IDH1, IDH2 or
  - p16: 53 gene-like tokens; 
    ICC-C1
    ICC-C2
    -yxoedonehcoruaT
    )2gol(
    etalohc
    30 p = 0.026
    20
    10
  - p17: 55 gene-like tokens; 
    Figure S4, related to Figure 7. BMI status and correlation of metabolite and gene
    expression are correlated in ICC and HCC identify altered bile-­acid metabolism
    and inflammation in the ICC C1 and C2 subtype. (A) The percent of patients in body
    mass index (BMI) categories among the Thai HCC, Thai ICC, Asian American (AsA)
    HCC and European American (EA) HCC cases is shown. BMI is categorized as
    underweight (UW), normal weight (NW), overweight (OW), obese (OB) or not available
    (NA) according to WHO criteria adjusted for the Asian population (underweight, BMI
    <18.5, normal weight, BMI = 18.5–23.9;; overweight, BMI =24-­27.9, obese, BMI >28) or

### data/papers/chaisaingmongkol2017/supp/mmc10.xlsx (24 kB)
- sheet `Gene list`: 57 rows x 12 cols
  - gene-symbol-like: col 0 (91% of 56)
  | Table S9, related to Figure  |  |  |  |  |  |  |  |  |  |  | 
  | Gene Symbol |  | ICC |  |  |  |  | HCC |  |  |  | 
  |  | Chromosome location | Pearson R (CNV vs. GE) | C1 mean expression a | C2 mean expression b | Mean Ratio (C1/C2) | FDR p value c | Pearson R (CNV vs. GE) | C1 mean expression a | C2 mean expression b | Mean Ratio (C1/C2) | FDR p value c
  | ECT2 | chr3: 172314275-172533511 | 0.529868 | 7.15547 | 5.94498 | 2.31416 | 1.44543e-05 | 0.466718 | 6.60563 | 4.55476 | 4.14357 | 4.40782e-07
  | NUF2 | chr1: 163096227-163460754 | 0.396648 | 5.31621 | 4.12113 | 2.28958 | 5.87539e-06 | 0.369529 | 5.55675 | 3.84169 | 3.2831 | 2.74037e-06
  | CDK1 | chr10: 62489026-62582895 | 0.353141 | 5.05158 | 3.8865 | 2.24247 | 1.20129e-05 | 0.481712 | 5.18096 | 3.41005 | 3.4127 | 1.63472e-05
  | TMEM48 | chr1: 54045364-55219524 | 0.307386 | 7.11962 | 6.19807 | 1.89414 | 8.65713e-06 | 0.468082 | 7.02669 | 6.02666 | 2.00004 | 5.39124e-06
  | BRIP1 | chr17: 59638609-59950850 | 0.464448 | 6.03674 | 5.15361 | 1.84438 | 8.37045e-05 | 0.580671 | 6.37869 | 4.99531 | 2.60878 | 2.74037e-06
- sheet `Gene networks`: 7 rows x 5 cols
  | Table S9, related to Figure  |  |  |  | 
  | ID | Molecules in Network | Score a | Focus Molecules b | Top Diseases and Functions
  | 1 | Alpha tubulin, Beta Tubulin, | 43 | 19 | Cancer, Endocrine System Dis
  | 2 | ARPC4-TTLL3, B3GALNT2, BOD1, | 36 | 16 | Cancer, Connective Tissue Di
  | 3 | AGPAT4, ARL4C, ASUN, B9D1, C | 33 | 15 | Developmental Disorder, Here
  | a The score is a numerical v |  |  |  | 
  | b Network size parameters cu |  |  |  | 

### data/papers/chaisaingmongkol2017/supp/mmc11.xlsx (212 kB)
- sheet `Aundance`: 142 rows x 180 cols
  - gene-symbol-like: col 1 (99% of 141)
  |  Table S10, related to Figur |  |  |  |  |  |  |  |  |  |  |  |  |  | ...
  | ID | Type | 1-linoleoylglycerophosphocho | 1-methylhistamine | 1-methylhistidine | 1-oleoylglycerol (1-monoolei | 1-oleoylglycerophosphocholin | 1-palmitoleoylglycerophospho | 1-palmitoylglycerophosphocho | 1-stearoylglycerophosphochol | 2-arachidonoyl glycerol | 2'-deoxyinosine | 2-hydroxy-3-methylvalerate | 2-palmitoleoylglycerophospho | ...
  | LCS_570 | ICC | 24.0684 | 20.9466 | 10.4909 | 22.5448 | 25.2623 | 21.7272 | 27.0228 | 26.4195 | 18.4457 | 20.8414 | 11.8154 | 21.3818 | ...
  | LCS_571 | ICC | 24.0387 | 14.8466 | 13.9716 | 22.8635 | 26.2266 | 23.5986 | 27.4493 | 27.0178 | 19.2882 | 19.8427 | 11.8154 | 22.9738 | ...
  | LCS_572 | ICC | 18.5361 | 22.6515 | 14.0158 | 23.1525 | 23.0189 | 20.2167 | 24.1763 | 23.6421 | 18.491 | 18.9571 | 17.3042 | 19.9021 | ...
  | LCS_573 | ICC | 24.4309 | 22.4901 | 10.4909 | 23.4849 | 25.6808 | 23.4611 | 27.5037 | 26.263 | 8.98014 | 18.1229 | 17.174 | 22.8951 | ...
  | LCS_574 | ICC | 24.9967 | 19.6266 | 14.9689 | 20.0418 | 27.1078 | 24.2899 | 27.7595 | 27.0118 | 17.4352 | 18.4646 | 15.8843 | 24.1096 | ...
  | LCS_575 | ICC | 24.7322 | 23.2453 | 10.4909 | 20.4493 | 27.0686 | 24.017 | 29.1104 | 27.3394 | 17.9774 | 16.463 | 11.8154 | 22.4791 | ...
- sheet `Molecular network`: 11 rows x 5 cols
  |  Table S10, related to Figur |  |  |  | 
  | ID | Molecules in Network | Score a | Focus Molecules b | Top Diseases and Functions
  | Network from 81 candidate me |  |  |  | 
  | 1 | 2-arachidonoylglycerol, Akt, | 45 | 18 | Cell Signaling, Nucleic Acid
  | 2 | 1-oleoyl lysophosphatidylcho | 24 | 11 | Free Radical Scavenging, Sma
  | Network from 77 candidate me |  |  |  | 
  | 1 | ADP, Akt, AMPK, Ap1, carnosi | 37 | 16 | Cell Signaling, Nucleic Acid
  | 2 | 1, 7-dimethylxanthine, 3'-ad | 19 | 9 | Amino Acid Metabolism, Lipid

### data/papers/chaisaingmongkol2017/supp/mmc12.pdf (16829 kB)
- 35 pages
  - p3: 26 gene-like tokens; Thailand,whereinfectionwithliverfluke(Opisthorchisviverrini) summarized in Table S1. Among them, 153
  - p4: 42 gene-like tokens; rows.SeealsoFigureS1;TableS1. / arankingmethodofthetranscriptomeusedbyTCGA(Cancer totheC2subtype(Figure2CandTableS2).Interestingly,c / ICC-C1 and HCC-C1 subtypes are significantly similar (p = these signatures (Figures S1F and S1G, Tab
    Figure 1. Identification of ICC and HCC
    Molecular-BasedTumorSubtypes
    (A)AheatmapofICCandHCCsamplesisshownby
    unsupervised hierarchical clustering of the most
    variable genes (±2 SD; n = 587) among tumor
    specimens.
    (B)Aprincipal-component(PC)analysisofICCand
    HCCtumorspecimensisshown.
  - p5: 49 gene-like tokens; from Europe, and 182 ICC patients from Japan (Table S4). haveadifferentoutcomethanAsianHCCandICCC1pa
    Figure 2. Identification of Common C1 and
    C2MolecularSubtypesofICCandHCC
    (A)SubclassmappingofICCandHCCsubtypesis
    shown.Significantrelationshipsbetweensubtypes
    are represented byBonferroni-adjusted pvalues.
    Significantassociationsshowingsimilaritybetween
    subtypes are shown in red, with p < 0.05, while
    differencesbetweensubtypes(Bonferroni-adjusted
  - p6: 2 gene-like tokens; fromTCGAasthereferencegroupsincetheseindividualshavethebestoverallsurvival.SeealsoFigureS2;TableS4.
  - p7: 19 gene-like tokens; getedexomesequencingofThaiICCandHCC.Theexonsand ure4B;TableS6).WenoticedthatICChasmoreC>Ttransition / genes most frequently recurrent and mutated across diverse sionmutations(Figures4C–4F;TableS6). / solidtumortypesdefinedbytheCOSMICdatabase(TableS5) Among 22 candidate driver genes in ICC and 32 can
  - p8: 40 gene-like tokens; dottedhorizontalline.SeealsoTableS7. / (TableS7).Consistentwithotherpublishedstudies,weobserved tionsamongvariouscohorts,whichwerediscovere
    Figure5. TheLandscapeofDriverGenesin
    ThaiICCandHCC
    AnoverviewofdrivergenesinICC(toppanel)and
    HCC(bottompanel).Shownaregeneswithnon-
    synonymous and indel mutations of >5% fre-
    quencies.Genesweresortedbyfrequencies(right
    bar),andtheiralterationsineachsampleclassified
    bycCluster-definedsubtypes.Genesinboldare
  - p10: 71 gene-like tokens; onecaseofThaiICCwithIDH1mutations(TableS6).Incontrast, consistent with our finding that ECT2 is a fu / origin (Figures S3E and S3F; Table S8). We found that SCNA outcometrend.Given the substantial correl / S3D and S3G; Table S8). However, when we analyzed SCNA demonstrated to phosphorylate ECT2 in vitro ( / ure6CandTableS9).Consistently,morecopy-numbergainand moreindicativeof patient outcomeand suitable fo
    onecaseofThaiICCwithIDH1mutations(TableS6).Incontrast, consistent with our finding that ECT2 is a functional driver for
    amongtheThaicohort,theC1commonsubtypescontainmore thecommonC1subtype(Figure6).
    p53mutationsthanC2subtypes(Figure5).Wealsofoundthat ThedataabovesuggestedthatECT2andPLK1couldbeclin-
    the p53 R249S mutation, an aflatoxin signature mutation, is ically relevant functional biomarkers useful to detect ICC and
    onlyassociatedwiththeHCC-C3subtype(datanotshown),sug- HCCsubtypessincebothhavebeenpreviouslylinkedtotumor
    gesting a unique environmental exposure associated with this progression (Cook et al., 2014; Strebhardt, 2010; Vigil et al.,
    subtype.Thus,targetedexomesequencingbasedontheOnco- 2010).WethusevaluatedECT2andPLK1byimmunohistochem-
    vardesigncanidentifydrivermutationswithrelativelyhighfre- istry (IHC) on tissue microarrays (TMAs) of ICC and HCC that
  - p11: 37 gene-like tokens; ICC and HCC (Table S1). It is interesting that these etiological needed to improve their outcome is  / andHCCtumortissuespecimensfromThaipatients(TableS10). Inthecurrentstudy,wefoundthatbothICCandHCC,reg / similar (Figures 7B and S4F; Table S10). We found that bile andbileacidbiogenesis.Theseresultssugges
  - p12: 5 gene-like tokens; andtopbox,respectively)withStudent’sttestpvalue.Whiskersrepresentminimumandmaximumvalues.SeealsoFigu
  - p16: 23 gene-like tokens; MetabolonDiscoverHD4Platform ThisStudy TableS10
  - p17: 14 gene-like tokens; tionnairesandmedicalchartrecords.AlistofclinicalvariablesassessedinthisstudyisprovidedinTableS1.Thec
  - p18: 19 gene-like tokens; Technologies)targeting2.93Mbofsequencein562genesfoundtobemutatedindiversesolidtumors(TableS6).Inaddi / wereselected.MetabolomicsdataisavailableinTableS10. / GSE76213.MetabolomicsdataisprovidedTableS10.SoftwareusedinthisstudyarenotedintheMethodDetailssection
  - p26: 86 gene-like tokens; 
    A
    ICC-C1 ICC-C2 ICC-UM
    %
    C1 C2 UM
    TP53 43 15 4
    KRAS 30 17 7
    ARID1A 5 14 13
    SMAD4 13 12 0
  - p28: 56 gene-like tokens; 
    3
    T
    2
    NT
    1
    0
    −1.0 −0.5 0.0 0.5 1.0 −1.0 −0.5 0.0 0.5 1.0
    Pearson's correlation
  - p32: 60 gene-like tokens; 
    Figure S3, related to Figure 6. Relationship between ICC subtypes with
    commonly mutated genes in the Japanese cohort, somatic copy number
    alterations (SCNA), correlation with gene expression in ICC or HCC and PLK1 and
    ECT2 expression and their association with prognosis. (A) The frequency of
    commonly mutated genes in the C1 (n=77) or C2 subtype (n=59) of 182 Japanese ICC
    tumors as well as an unmatched group (UM, n=46) are shown. The percent of cases of
    each subtype with mutation are shown in the right panel and the number of cases in
    each subtype is indicated in parentheses. (B) The mutation frequency of IDH1, IDH2 or
  - p34: 53 gene-like tokens; 
    ICC-C1
    ICC-C2
    -yxoedonehcoruaT
    )2gol(
    etalohc
    30 p = 0.026
    20
    10
  - p35: 55 gene-like tokens; 
    Figure S4, related to Figure 7. BMI status and correlation of metabolite and gene
    expression are correlated in ICC and HCC identify altered bile-­acid metabolism
    and inflammation in the ICC C1 and C2 subtype. (A) The percent of patients in body
    mass index (BMI) categories among the Thai HCC, Thai ICC, Asian American (AsA)
    HCC and European American (EA) HCC cases is shown. BMI is categorized as
    underweight (UW), normal weight (NW), overweight (OW), obese (OB) or not available
    (NA) according to WHO criteria adjusted for the Asian population (underweight, BMI
    <18.5, normal weight, BMI = 18.5–23.9;; overweight, BMI =24-­27.9, obese, BMI >28) or

### data/papers/chaisaingmongkol2017/supp/mmc2.xlsx (21 kB)
- sheet `Total`: 76 rows x 4 cols
  | Table S1, related to Figure  |  |  | 
  | Clinical variable | ICC  | HCC  | p value b
  |  | (n = 130) | (n = 69) | (ICC vs HCC)
  | Demographic |  |  | 
  |    Sex a |  |  | 0.6282
  |       Male | 83 (64) | 46 (67) | 
  |       Female | 39 (30) | 17 (25) | 
  |    Age  |  |  | 0.0075
- sheet `C1 and C2`: 100 rows x 7 cols
  | Table S1, related to Figure  |  |  |  |  |  | 
  |  |  | HCC |  |  | ICC | 
  | Clinical variable | C1 (n = 15) | C2 (n = 14) | p valueb | C1 (n = 33) | C2 (n = 18) | p valueb
  | Demographic |  |  |  |  |  | 
  |    Sex a |  |  | 0.2451 |  |  | 0.7647
  |       Male | 8 (53) | 11 (79) |  | 8 (53) | 11 (79) | 
  |       Female | 7 (47) | 3 (21) |  | 7 (47) | 3 (21) | 
  |    Age  |  |  | 0.0352 |  |  | 0.0045

### data/papers/chaisaingmongkol2017/supp/mmc3.xlsx (24 kB)
- sheet `Table S2`: 158 rows x 7 cols
  | Table S2, related to Figure  |  |  |  |  |  | 
  | Gene Set | Number of Genes | Enrichment Score (ES) | Normalized Enrichment Score  | NOM p value | FDR q-val | FWER p value
  | Enriched in ICC-C1 subtype  |  |  |  |  |  | 
  | MITOTIC M M G1 PHASES | 29 | 0.79914695 | 1.5496429 | 0.044265594 | 0.1704423 | 0.812
  | M PHASE OF MITOTIC CELL CYCL | 19 | 0.891496 | 1.5511049 | 0.013944224 | 0.17539054 | 0.81
  | M PHASE | 23 | 0.8674729 | 1.5511323 | 0.01996008 | 0.18265583 | 0.81
  | MITOSIS | 18 | 0.8888446 | 1.5538844 | 0.015904572 | 0.1941782 | 0.808
  | PID PLK1 PATHWAY | 16 | 0.8874492 | 1.5589253 | 0.014227643 | 0.20467909 | 0.801

### data/papers/chaisaingmongkol2017/supp/mmc4.xlsx (14 kB)
- sheet `Table S3`: 21 rows x 8 cols
  | Table S3, related to Figure  |  |  |  |  |  |  | 
  |  |  |  |  | Enrichment of samples b |  |  | 
  | Signatue name | Gene list (GSEA standard nam | Description | Reference | ICC-C1, positive to signatur | ICC-C2, negative to signatur | HCC-C1, positive to signatur | HCC-C2, negative to signatur
  | S1-S3 signature | HOSHIDA_LIVER_CANCER_SUBCLAS | Class S1 (WNT-TGFb) signatur | Hoshida et al., Cancer Res.  |  |  |  | 
  |  | HOSHIDA_LIVER_CANCER_SUBCLAS | Class S2 (AKT-MYC) signature |  | 0.0123723392886686 | 1.29e-10 | 1.23139196991197e-06 | 6.91842902836791e-10
  |  | HOSHIDA_LIVER_CANCER_SUBCLAS | Class S3 signature of hepato |  |  |  |  | 
  | Stem cell signature | LEE_LIVER_CANCER_SURVIVAL_DN | Genes highly expressed in he | Lee et al., Hepatology. 2004 | 7.45556016904675e-05 | 1.29e-10 | 0.000211234496202126 | 0.000147183901643959
  |  | LEE_LIVER_CANCER_SURVIVAL_UP | Genes highly expressed in he |  |  |  |  | 

### data/papers/chaisaingmongkol2017/supp/mmc5.xlsx (15 kB)
- sheet `Table S4`: 58 rows x 6 cols
  | Table S4, related to Figure  |  |  |  |  | 
  | Clinical variable | HCC Chinese | HCC TCGA Asian | ICC Japanese | HCC TCGA Caucasian | ICC Caucasian
  |  | (N = 247) | (N = 153) | (N = 182) | (N = 161) | (N = 104)
  | Demographic |  |  |  |  | 
  |    Sex a |  |  |  |  | 
  |       Male | 211 (85) | 122 (78) | 104 (57) | 91 (56) | 48 (46)
  |       Female | 31 (13) | 34 (22) | 60 (33) | 72 (44) | 56 (54)
  |    Age  |  |  |  |  | 

### data/papers/chaisaingmongkol2017/supp/mmc6.xlsx (18 kB)
- sheet `Table S5`: 565 rows x 1 cols
  - gene-symbol-like: col 0 (100% of 565)
  | Table S5, related to Figure 
  | Gene Symbol
  | ABL1
  | ABL2
  | ACN9
  | ACTA2
  | ACTC1
  | ACVR1

### data/papers/chaisaingmongkol2017/supp/mmc7.xlsx (119 kB)
- sheet `Table S6`: 1067 rows x 15 cols
  - gene-symbol-like: col 6 (100% of 1066), col 9 (70% of 1013)
  | Table S6, related to Figure  |  |  |  |  |  |  |  |  |  |  |  |  |  | ...
  | Sample ID | Chromosome | Position | Reference | Alternate | Gene | Transcript | Effect | Amino Acid Change | Total Read Count Normal | Total Read Count Tumor | Alternate Read Count Normal | Alternate Read Count Tumor | Alternate Read Fraction Norm | ...
  | LCS_501 | chr5 | 56189380 | C | A | MAP3K1 | ENST00000399503 | NON_SYNONYMOUS_CODING | P1471Q | 27 | 18 | 0 | 5 | 0 | ...
  | LCS_501 | chr17 | 7578257 | C | A | TP53 | ENST00000269305 | STOP_GAINED | E198* | 50 | 21 | 0 | 12 | 0 | ...
  | LCS_503 | chr3 | 41266124 | A | G | CTNNB1 | ENST00000396185 | NON_SYNONYMOUS_CODING | T41A | 27 | 21 | 0 | 6 | 0 | ...
  | LCS_503 | chr3 | 123359214 | A | G | MYLK | ENST00000360304 | NON_SYNONYMOUS_CODING | L1586P | 22 | 28 | 0 | 4 | 0 | ...
  | LCS_503 | chr8 | 113504810 | G | T | CSMD3 | ENST00000297405 | NON_SYNONYMOUS_CODING | A1729D | 28 | 46 | 0 | 12 | 0 | ...
  | LCS_503 | chr16 | 65032521 | G | A | CDH11 | ENST00000268603 | NON_SYNONYMOUS_CODING | P156L | 22 | 36 | 0 | 10 | 0 | ...

### data/papers/chaisaingmongkol2017/supp/mmc8.xlsx (13 kB)
- sheet `Table S7`: 36 rows x 5 cols
  | Table S7, related to Figure  |  |  |  | 
  | THAI ICC | JAPANESE ICC | COSMIC ICC | THAI HCC | COSMIC HCC
  | TP53 (46) | TP53 (27) | TP53 (33) | TP53 (44) | TP53 (27)
  | ARID1A (21) | KRAS (22) | KRAS (23) | CTNNB1 (21) | TERT (24)
  | KRAS (17) | ARID1A (11) | ARID1A (13) | ARID1A (15) | CTNNB1 (19)
  | SMAD4 (17) | SMAD4 (10) | SMAD4 (10) | ARID2 (15) | AXIN1 (8)
  | APC (12) | BAP1 (10) | IDH1 (9) | APOB (11) | MUC16 (8)
  | KMT2C (12) | PIK3CA (8) | BAP1 (9) | CSMD3 (10) | RYR2 (7)

### data/papers/chaisaingmongkol2017/supp/mmc9.xlsx (25 kB)
- sheet `Table S8`: 94 rows x 7 cols
  | Table S8, related to Figure  |  |  |  |  |  | 
  |  | Cytoband | FeatureID (TIGER-LC HCC) | Thai HCC | TCGA Asian | TCGA Caucasian | FeatureID (TCGA)
  |  | Amplification |  |  |  |  | 
  |  | 1p11 |  | 0.31 | 0.6445 | 0.5505 | ATF6, KMO, KPRP, NHLH1, SETD
  |  | 1p31 | NEGR1 | 0.31 | 0.668333333333333 | 0.555 | APCS, APH1A, APOA1BP, APOA2,
  |  | 1q21 | TNFAIP8L2andSCNM1, LCE3D, SE | 0.506788617886179 | 0.636825396825397 | 0.548253968253968 | ATP1A2, ATP1A4, ATP2B4, ATP6
  |  | 1q22 | ADAM15, DCST1, EFNA1, TRIM46 | 0.590833333333333 | 0.618210526315789 | 0.546315789473684 | PRRC2C, BATF3, BCAN, CDC42BP
  |  | 1q22 - 1q23 |  | 0.56 |  |  | 

## fan2024

Fan Z, Zou X et al. A transcriptome based molecular classification scheme for cholangiocarcinoma and subtype-derived prognostic biomarker. Nat Commun 2024;15

- identifiers: {"doi": "10.1038/s41467-024-44748-8", "pmcid": "PMC10784309", "pmid": "38212331"}
- resolved title: A transcriptome based molecular classification scheme for cholangiocarcinoma and subtype-derived prognostic biomarker. Nat Commun 2024
- want: Two universal CCA subtypes: the 30-gene subtype classifier and the CORE-37 prognostic biomarker (438 CCA).

### data/papers/fan2024/supp/41467_2024_44748_MOESM1_ESM.pdf (10937 kB)
- 41 pages
  - p30: 3 gene-like tokens; 160 Supplementary Table 1. Clinical characteristics of CCA patients in the
  - p31: 1 gene-like tokens; 168 Supplementary Table 2. Clinical information of 438 samples employed in
  - p32: 1 gene-like tokens; 172 Supplementary Table 3. Correlation between CCA molecular subtypes
  - p34: 2 gene-like tokens; 176 Supplementary Table 4. Liver-specific and pancreas-specific gene
  - p35: 2 gene-like tokens; 182 Supplementary Table 5. Correlation between CCA molecular subtypes
  - p36: 2 gene-like tokens; 186 Supplementary Table 6. Genes selected for the developed molecular
  - p37: 2 gene-like tokens; 192 Supplementary Table 7. The results of NTP analysis.
  - p38: 1 gene-like tokens; 195 Supplementary Table 8. Differentially expressed genes (DEGs) selected
  - p39: 11 gene-like tokens; 203 Supplementary Table 9. Net reclassification index comparison between
  - p41: 2 gene-like tokens; 209 Supplementary Table 10. The raw TPM expression data of 438 samples

### data/papers/fan2024/supp/41467_2024_44748_MOESM2_ESM.pdf (4889 kB)
- 17 pages
  - p10: 12 gene-like tokens; Table 6.

### data/papers/fan2024/supp/41467_2024_44748_MOESM3_ESM.pdf (1206 kB)
- 3 pages

### data/papers/fan2024/supp/41467_2024_44748_MOESM4_ESM.docx (14 kB)
- 0 tables; captions: 

### data/papers/fan2024/supp/41467_2024_44748_MOESM5_ESM.xlsx (201639 kB)
- sheet `Supplementary Table 1`: 83 rows x 4 cols
  | Supplementary Table 1. Clini |  |  | 
  |  | Original cohort | Purified cohort | Verification cohort
  | Sample size (N) | 438 | 164 | 274
  | Gender, n (%) |  |  | 
  | Male | 295 (67.35%) | 117 (71.34%) | 178 (64.96%)
  | Female | 143 (32.65%) | 47 (28.66%) | 96 (35.04%)
  | Age, median [min, max] | 63.00 [25.00, 82.00] | 65.00 [43.00, 82.00] | 60.15 [25, 79]
  | Anatomical location, n (%)  |  |  | 
- sheet `Supplementary Table 2`: 440 rows x 11 cols
  | Supplementary Table 2. Clini |  |  |  |  |  |  |  |  |  | 
  | SampleID | Age | Sex | histological_type | Differentiation | Hepatic contami0tion | Pancreatic contami0tion | Duode0l contami0tion | Lymphatic contami0tion | Neural contami0tion | Squamous cell carcinoma
  | 219016280FR | < 40 | female | iCCA | Medium | 33 | 0 | 0 | 0 | 0 | 
  | 219015869R1 | 40-60 | Male | dCCA | Medium_low | 0 | 20 | 0 | 0 | 0 | 
  | 219015900R1 | 40-60 | Male | dCCA | Medium_low | 0 | 50 | 0 | 0 | 0 | 
  | 219016250FR | 40-60 | Male | iCCA | Low | 10 | 0 | 0 | 0 | 0 | 
  | 219013176FR | 40-60 | Male | iCCA | Medium_low | 10 | 0 | 0 | 0 | 0 | 1
  | 219013771FR | 40-60 | Male | pCCA | Medium | 25 | 0 | 0 | 10 | 0 | 
- sheet `Supplementary Table 4`: 183 rows x 2 cols
  - gene-symbol-like: col 0 (98% of 183), col 1 (98% of 42)
  | Supplementary Table 4. Liver | 
  | Liver-specific gene | Pancreas-specific gene
  | A1BG | AMY1C
  | ABAT | AMY2A
  | ABCB11 | AQP12A
  | ABCB4 | AQP12B
  | ABCC2 | C2CD4B
  | ABHD2 | CEL
- sheet `Supplementary Table 6`: 32 rows x 2 cols
  - gene-symbol-like: col 0 (91% of 32)
  | Supplementary Table 6. Genes | 
  | Probe ID | Classifier
  | PLBD2 | Mesenchymal & Immunosupressi
  | NCKAP5L | Mesenchymal & Immunosupressi
  | TMEM104 | Mesenchymal & Immunosupressi
  | LRP1 | Mesenchymal & Immunosupressi
  | TMEM256-PLSCR3 | Mesenchymal & Immunosupressi
  | CHST14 | Mesenchymal & Immunosupressi
- sheet `Supplementary Table 7`: 166 rows x 7 cols
  | Supplementary Table 7. The r |  |  |  |  |  | 
  | SampleID | prediction | d.Mesenchymal_classifier | d.Metabolic_classifier | p.value | FDR | Corrected_molecular_prection
  | 219013101FR | Mesenchymal_classifier | 0.32269320684154 | 0.946503615554808 | 0.002 | 0.00273333333333333 | Mesenchymal and immunosupres
  | 219013103FR | Mesenchymal_classifier | 0.495381725310769 | 0.868675397503651 | 0.00798403193612774 | 0.0103919145835313 | Mesenchymal and immunosupres
  | 219013106FR | Mesenchymal_classifier | 0.310213600265842 | 0.950666882882803 | 0.002 | 0.00273333333333333 | Mesenchymal and immunosupres
  | 219013108FR | Metabolic_classifier | 0.829122893941463 | 0.559066388492578 | 0.0459081836327345 | 0.056608587336605 | unclassified (FDR>0.05)
  | 219013109FR | Mesenchymal_classifier | 0.271719783679418 | 0.962376412406918 | 0.002 | 0.00273333333333333 | Mesenchymal and immunosupres
  | 219013111FR | Mesenchymal_classifier | 0.258034626491575 | 0.966135669319456 | 0.002 | 0.00273333333333333 | Mesenchymal and immunosupres
- sheet `Supplementary Table 8`: 39 rows x 4 cols
  - gene-symbol-like: col 1 (97% of 38)
  | Supplementary Table 8. Diffe |  |  | 
  | Molecular class | Genes for prognostic biomark | log2 Fold Change | p-adj
  | Mesenchymal & Immunosupressi | CGB5 | 3.320107363 | 0.00071947
  | Mesenchymal & Immunosupressi | CGB8 | 3.059230066 | 0.00055256
  | Mesenchymal & Immunosupressi | CLDN6 | 2.608231191 | 0.00021663
  | Mesenchymal & Immunosupressi | KRT79 | 2.371446322 | 0.0004615
  | Mesenchymal & Immunosupressi | CASP14 | 2.270638627 | 3.98e-05
  | Mesenchymal & Immunosupressi | GPR78 | 2.109078581 | 2.62e-05
- sheet `Supplementary Table 10`: 55881 rows x 439 cols
  |  | 219014583FR | 219015873R1 | 219015943R1 | 219013808FR | 219016260FR | 219019500FR | 219015880R1 | 219013111FR | 219015883R1 | 219015909R1 | 219015945R1 | 219014562FR | 219015944R1 | ...
  | TSPAN6 | 8.108377 | 1.587672 | 12.350764 | 1.050151 | 8.630795 | 5.236929 | 2.064835 | 2.583362 | 2.014471 | 2.071649 | 2.764429 | 5.569269 | 5.362637 | ...
  | TNMD | 0.372799 | 0.047663 | 0.42859 | 0.027169 | 0.083603 | 0.031217 | 0.179327 | 0 | 0.066028 | 0 | 0.074649 | 0.089862 | 0.145132 | ...
  | DPM1 | 6.811759 | 2.005615 | 6.25947 | 4.432631 | 3.697636 | 2.734852 | 5.235973 | 3.518956 | 1.968386 | 5.5803 | 3.446696 | 7.672621 | 4.626081 | ...
  | SCYL3 | 4.096755 | 0.518394 | 6.718238 | 0.662133 | 2.622012 | 1.927612 | 2.35695 | 1.42652 | 0.9788 | 1.518291 | 2.237539 | 6.000973 | 2.521126 | ...
  | C1orf112 | 3.203828 | 0.309129 | 2.536865 | 0.741149 | 1.793927 | 1.132471 | 1.776724 | 0.900798 | 0.676252 | 1.021912 | 1.31846 | 5.257573 | 1.616304 | ...
  | FGR | 6.318833 | 0.525715 | 3.132703 | 0.738152 | 3.69316 | 0.467929 | 3.570028 | 5.811105 | 1.486551 | 0.480837 | 1.748724 | 4.909016 | 2.328227 | ...
  | CFH | 24.110332 | 5.038261 | 40.147633 | 4.215422 | 88.694183 | 42.003277 | 16.996922 | 14.408109 | 34.211807 | 6.854805 | 14.169064 | 14.894003 | 23.649981 | ...

## song2022

Song G et al. Single-cell transcriptomic analysis suggests two molecularly distinct subtypes of intrahepatic cholangiocarcinoma. Nat Commun 2022;13:1642

- identifiers: {"doi": "10.1038/s41467-022-29164-0", "pmcid": "PMC8960779", "pmid": "35347134"}
- resolved title: Single-cell transcriptomic analysis suggests two molecularly subtypes of intrahepatic cholangiocarcinoma. Nat Commun 2022
- want: Large-duct (S100P+ SPP1-, perihilar) vs small-duct (S100P- SPP1+, peripheral) tumour-cell signatures. Our risk score follows this axis (step 07b), so an explicit large/small-duct template is needed.

### data/papers/song2022/supp/41467_2022_29164_MOESM10_ESM.xlsx (1429 kB)
- sheet `Sheet1`: 19030 rows x 5 cols
  - gene-symbol-like: col 0 (84% of 19030)
  | Supplementary Data 7. Differ |  |  |  | 
  | Gene | logFC | logCPM | F score | P-value
  | ALB | 7.97855223416872 | 10.2649232947252 | 26337.6746214946 | 0
  | NEB | 4.44367095302462 | 8.70641202285861 | 11357.9765200498 | 0
  | AMBP | 4.1788822214842 | 8.49474731803389 | 12363.56318762 | 0
  | ORM1 | 3.93669331747348 | 8.52467604806731 | 8792.32569386291 | 0
  | RGS5 | 3.88494185814947 | 9.08442934370781 | 7943.23725485758 | 0
  | SERPINA1 | 3.66688403655433 | 12.8459872894136 | 5660.725430333 | 0

### data/papers/song2022/supp/41467_2022_29164_MOESM11_ESM.xlsx (10 kB)
- sheet `Sheet1`: 27 rows x 3 cols
  - gene-symbol-like: col 0 (85% of 27)
  | Supplementary Data 8. Anti-h |  | 
  | Antibody | Catalogue | Company
  | DRAQ5 | 4084 | CST
  | DAPI | 422801 | Biolegend
  | S100P | ab133554 | Abcam
  | SPP1 | ab214050 | Abcam
  | Hep-Par1 | ab190706 | Abcam
  | MUC5AC | ab3649 | Abcam

### data/papers/song2022/supp/41467_2022_29164_MOESM12_ESM.pdf (315 kB)
- 4 pages

### data/papers/song2022/supp/41467_2022_29164_MOESM13_ESM.xlsx (8082 kB)
- sheet `Figure 1`: 30 rows x 14 cols
  - gene-symbol-like: col 0 (93% of 30)
  | Figure 1e |  |  |  |  |  |  |  |  |  |  |  |  | 
  | Patient | Source | Monocyte | Macrophage | DC | NK | CD4 | Treg | CD8 | MAIT | B | Plasma B | Fibroblast | Endothelial
  | P02 | P | 0.02227238525206923 | 0.0004514672686230248 | 0.01203912716328066 | 0.3429646350639579 | 0.01655379984951091 | 0.001053423626787058 | 0.3367945823927765 | 0.1795334838224229 | 0.08638073739653875 | 0.001655379984951091 | 0 | 0.0003009781790820166
  | P02 | T | 0.03888366259015366 | 0.03104421448730009 | 0.02508623392913139 | 0.1323298839761681 | 0.1558482282847288 | 0.02100972091564754 | 0.2442772028849169 | 0.05801191596111634 | 0.2853559109438695 | 0.002508623392913139 | 0.002508623392913139 | 0.003135779241141424
  | P03 | P | 0.08117797695262484 | 0.001408450704225352 | 0.01946222791293214 | 0.2207426376440461 | 0.02765685019206146 | 0.0005121638924455825 | 0.2215108834827145 | 0.300640204865557 | 0.1201024327784891 | 0.002176696542893726 | 0.0006402048655569782 | 0.003969270166453265
  | P03 | T | 0.09960878724044538 | 0.09690039121275955 | 0.03942220884742703 | 0.1760457417995787 | 0.1613000300932892 | 0.03912127595546193 | 0.1898886548299729 | 0.07583508877520313 | 0.05236232320192597 | 0.00331026181161601 | 0.0111345170027084 | 0.0550707192296118
  | P04 | P | 0.03183520599250937 | 0.004280363830925628 | 0.01337613697164259 | 0.09256286784376672 | 0.02849117174959872 | 0.002541466024612092 | 0.7471910112359551 | 0.05925628678437667 | 0.01324237560192616 | 0.00227394328517924 | 0 | 0.004949170679507758
  | P04 | T | 0.1223476297968397 | 0.1647855530474041 | 0.06320541760722348 | 0.05869074492099323 | 0.07494356659142212 | 0.0744920993227991 | 0.1918735891647856 | 0.01489841986455982 | 0.0762979683972912 | 0.006772009029345372 | 0.005417607223476298 | 0.1462753950338601
- sheet `Figure 2`: 188 rows x 15 cols
  | Figure 2e |  |  | Figure 2f |  |  |  |  | Figure 2g and 2i |  |  |  |  |  | ...
  | Month to event | S100P+SPP1-  | S100P-SPP1+ | Group | CA19-9 | CEA | Ki67 | Tumor size | Sample | S100P | SPP1 | Group | Subtype | OS_event | ...
  | 64.7 | 0 |  | S100P+SPP1- | 981.9 | 6.1 | 50 | 5 | 200643150050_A | -0.7994738703548334 | 2.054719775310522 | S100P-SPP1+ | Intrahepatic | 0 | ...
  | 0.233333333333333 | 1 |  | S100P+SPP1- | 10000 | 44.69 | 80 | 13 | 200643150050_B | -0.7915127443909311 | 2.312715929860402 | S100P-SPP1+ | Intrahepatic | 0 | ...
  | 60.0666666666667 | 0 |  | S100P-SPP1+ | 9.7 | 1.56 | 20 | 5 | 200643150050_C | -0.8030846878052892 | 0.4124667534482445 | S100P-SPP1+ | Intrahepatic | 0 | ...
  | 11.4666666666667 | 1 |  | S100P-SPP1+ | 299.1 | 4.47 | 10 | 6 | 200643150050_D | -0.1963618783297481 | 1.190552721829488 | Others | Intrahepatic | 0 | ...
  | 5.4 | 1 |  | S100P+SPP1- | 128.8 | 1.5 | 80 | 2 | 200643150050_E | -0.8016406203582318 | 0.9058533146414999 | S100P-SPP1+ | Intrahepatic | 1 | ...
  | 57.1333333333333 | 0 |  | S100P-SPP1+ | 13.3 | 2.7 | 10 | 2.5 | 200643150050_F | 1.854860894918952 | -0.8024832137659156 | S100P+SPP1- | Intrahepatic | 1 | ...
- sheet `Figure 3`: 27623 rows x 34 cols
  - gene-symbol-like: col 0 (88% of 16), col 8 (100% of 23668), col 34 (68% of 27622)
  | Figure 3a |  |  |  | Figure 3d |  |  |  | Figure 3e |  |  |  |  | Figure 3g | ...
  | Sample | Subtype | Genomic_het | Transcriptomic_het | CB | CREB3L1 | S100P | Class |  | CREB3L1 0ng | CREB3L1 50ng | CREB3L1 100ng | CREB3L1 200ng |  | ...
  | P02T | S100P+SPP1- | 0.627450980392157 | 14.4643281684695 | P02T_AAACCCAGTTCACGAT | 0 | 3.988356103058554 | NP | Relative luciferase activity | 1 | 1.8427184466019417 | 5.622330097087379 | 5.929126213592233 | Number of cells | ...
  | P03T | S100P+SPP1- | 0.239669421487603 | 16.296942918542 | P02T_AAACCCATCCAACTAG | 3.097662297715274 | 3.097662297715274 | PP | Relative luciferase activity | 1 | 1.727109515260323 | 5.245062836624776 | 5.713644524236984 | Number of cells | ...
  | P04T | S100P+SPP1- | 0.428571428571429 | 17.8747526194155 | P02T_AAACCCATCTACCTTA | 1.823754632656557 | 3.081005904156288 | PP | Relative luciferase activity | 1 | 1.798206278026906 | 5.2385650224215246 | 5.787443946188341 | Number of cells | ...
  | P06T | S100P+SPP1- | 0.486486486486487 | 18.4495930779331 | P02T_AAACCCATCTTTCAGT | 2.300248433352637 | 5.542590974830722 | PP | Relative luciferase activity | 1 | 1.7727674624226348 | 5.106984969053935 | 5.76657824933687 | Number of cells | ...
  | P09T | S100P-SPP1+ | 0.6 | 13.9376464217405 | P02T_AAACGAAAGGCCTTGC | 0 | 3.343389625499562 | NP | Relative luciferase activity | 1 | 2.141459074733096 | 5.662811387900356 | 5.120996441281139 | Number of cells | ...
  | P10T | S100P-SPP1+ | 0.637931034482759 | 14.6147773735582 | P02T_AAAGAACAGCCGTTGC | 1.716564581184561 | 3.346116471445301 | PP | Relative luciferase activity | 1 | 2.175115207373272 | 6.348387096774194 | 5.595391705069124 | Number of cells | ...
- sheet `Figure 4`: 7465 rows x 9 cols
  | Figure 4e and 4f |  |  |  |  |  | Figure 4g and 4h |  | 
  | CB | Cluster | M1 | M2 | Pro-inflammatory | Anti-inflammatory | Group | CD68+SPP1+CCL18-/CD68 (%) | CD68+SPP1-CCL18+/CD68 (%)
  | P02P_AGGGTGAAGTGGAAAG | Macro_c1_SPP1 | -0.4637872786200983 | -0.2066721526057672 | -0.3209096771027086 | -0.3672080620101778 | S100P+SPP1- | 0 | 0.4
  | P02P_GCGTTTCAGGTGCTTT | Macro_c1_SPP1 | 0.1290308088033291 | 0.0361600301424414 | 0.2688425333788919 | -0.1657340346150064 | S100P+SPP1- | 0.008141112618724558 | 0.2225237449118046
  | P02P_TGAATGCAGTCGAATA | Macro_c1_SPP1 | -0.5116883159376693 | -0.1181753551706104 | 0.05809594001281226 | -0.6129560696841256 | S100P-SPP1+ | 0 | 0.2835820895522388
  | P02T_AAACCCAGTCTTCAAG | Macro_c1_SPP1 | -0.3439510682762201 | 0.08515576340939734 | -0.7166682747935355 | -0.189163523192157 | S100P-SPP1+ | 0.0027100271002710027 | 0.13008130081300814
  | P02T_AAACGAAAGGTCCCGT | Macro_c1_SPP1 | 0.06920729161935102 | 0.2300192340979063 | -0.7185669862883468 | -0.2308388134218006 | S100P+SPP1- | 0.07339449541284404 | 0.027522935779816515
  | P02T_AAAGGTATCGCTGATA | Macro_c1_SPP1 | 0.1079852676688762 | -0.1118501870939507 | -0.6801493986437007 | 0.2045338124975172 | S100P-SPP1+ | 0 | 0.2786885245901639
- sheet `Figure 5`: 37 rows x 5 cols
  | Figure 5g |  |  |  | 
  | Sample | Subtype | ID3 | ALB | MKI67
  | 200643150050_A | S100P-SPP1+ | 7.053702264370113 | 10.57059410308246 | 4.915928299985525
  | 200643150050_B | S100P-SPP1+ | 7.121127201757929 | 8.945874910394766 | 4.714005314301825
  | 200643150050_C | S100P-SPP1+ | 7.844951153786141 | 9.401535099314847 | 4.387249871230044
  | 200643150050_E | S100P-SPP1+ | 6.042767967748512 | 10.23019514241867 | 5.039298792371815
  | 200643150050_H | S100P-SPP1+ | 7.607032538551293 | 10.19988277530667 | 4.249558784214981
  | 200643150072_J | S100P-SPP1+ | 7.238046208620582 | 8.040974025015636 | 4.606379988792473
- sheet `Figure 6`: 120 rows x 9 cols
  | Figure 6d |  |  | Figure 6e |  |  |  |  | 
  | CK19+ID3+/CK19+ (%) | CK19+ID3-/CK19+ (%) | CK19-PDGFRβ+/CK19- | Month to event | CK19+ID3-/CK19+_Low | CK19+ID3-/CK19+_High | Month to event | CK19-PDGFRβ+/CK19-_Low | CK19-PDGFRβ+/CK19-_High
  | 0.0006835737234260715 | 0.9993164262765739 | 0.10589085652331044 | 27.0666666666667 | 0 |  | 27.0666666666667 | 0 | 
  | 0.0008199241570154761 | 0.9991800758429845 | 0.014978800305831654 | 23.1333333333333 | 0 |  | 23.1333333333333 | 0 | 
  | 0.0018752547900529964 | 0.998124745209947 | 0.08876371182923214 | 17.2666666666667 | 0 |  | 17.2666666666667 | 0 | 
  | 0.00435486572497348 | 0.9956451342750265 | 0.011026647732019047 | 30.5333333333333 | 1 |  | 30.5333333333333 | 1 | 
  | 0.004862236628849271 | 0.9951377633711507 | 0.02168653879384828 | 20.7666666666667 | 0 |  | 20.7666666666667 | 0 | 
  | 0.007756337495270526 | 0.9922436625047295 | 0.039611400354248295 | / | 1 |  |  | 1 | 
- sheet `Suppl. Figure 1`: 30 rows x 14 cols
  - gene-symbol-like: col 0 (93% of 30)
  | Supplementary Figure 1e |  |  |  |  |  |  |  |  |  |  |  |  | 
  | Patient | Tissue | B | CD4 | CD8 | DC | Endothelial | Fibroblast | Macrophage | MAIT | Monocyte | NK | Plasma B | Treg
  | P02 | P | 574 | 110 | 2238 | 80 | 2 | 0 | 3 | 1193 | 148 | 2279 | 11 | 7
  | P02 | T | 910 | 497 | 779 | 80 | 10 | 8 | 99 | 185 | 124 | 422 | 8 | 67
  | P03 | P | 938 | 216 | 1730 | 152 | 31 | 5 | 11 | 2348 | 634 | 1724 | 17 | 4
  | P03 | T | 174 | 536 | 631 | 131 | 183 | 37 | 322 | 252 | 331 | 585 | 11 | 130
  | P04 | P | 99 | 213 | 5586 | 100 | 37 | 0 | 32 | 443 | 238 | 692 | 17 | 19
  | P04 | T | 169 | 166 | 425 | 140 | 324 | 12 | 365 | 33 | 271 | 130 | 15 | 165
- sheet `Suppl. Figure 3`: 1443 rows x 5 cols
  | Supplementary Figure 3c |  |  |  | 
  | CB | Sample | Class | S100P_count | SPP1_count
  | AAACCTGAGGTACTCT-34 | C66 | S100P-SPP1+ | 0 | 205
  | AAACCTGAGTCCAGGA-38 | C25 | S100P-SPP1+ | 0 | 3
  | AAACCTGTCTTGAGGT-20 | C26a | S100P-SPP1+ | 0 | 10
  | AAACGGGGTTCGTGAT-28 | C46b | S100P+SPP1- | 2 | 0
  | AAAGATGCACAACTGT-20 | C26a | S100P-SPP1+ | 0 | 1
  | AAAGCAAAGCCGCCTA-28 | C46b | S100P+SPP1- | 7 | 0
- sheet `Suppl. Figure 5`: 1122 rows x 29 cols
  - gene-symbol-like: col 0 (96% of 51), col 7 (100% of 1122), col 8 (98% of 1121), col 14 (100% of 1121)
  | Supplementary Figure 5a and  |  |  |  |  |  | Figure 5c |  |  |  |  |  |  |  | ...
  | Sample | OS_days | OS_event | S100P | SPP1 | Group | Tumor_Sample_Barcode | Hugo_Symbol | Entrez_Gene_Id | Chromosome | Start_position | End_position | Variant_Classification | Variant_Type | ...
  | ICC001G | 1290 | 0 | -0.7509264743780552 | 0.2097076450152844 | S100P-SPP1+ | P02T | ST6GALNAC3 | 256435 | 1 | 77093213 | 77093213 | Missense_Mutation | SNP | ...
  | ICC002G | 5130 | 0 | 1.467384615852788 | -1 | S100P+SPP1- | P02T | DHX57 | 90957 | 2 | 39030053 | 39030053 | Missense_Mutation | SNP | ...
  | ICC003G | 210 | 0 | 1.71342406134338 | -0.8329729007940035 | S100P+SPP1- | P02T | KCNH7 | 90134 | 2 | 163374365 | 163374365 | Missense_Mutation | SNP | ...
  | ICC006G | 2340 | 1 | -0.9385140629925667 | 0.6085665746711224 | S100P-SPP1+ | P02T | DLX2 | 1746 | 2 | 172966256 | 172966256 | Missense_Mutation | SNP | ...
  | ICC008G | 3630 | 1 | -0.6187205472406492 | 0.6853165956202106 | S100P-SPP1+ | P02T | TTN | 7273 | 2 | 179440436 | 179440436 | Missense_Mutation | SNP | ...
  | ICC009G | 4110 | 0 | -0.5237186736177722 | 0.5463689388462427 | S100P-SPP1+ | P02T | TOP2B | 7155 | 3 | 25679764 | 25679764 | Missense_Mutation | SNP | ...
- sheet `Suppl. Figure 6`: 19884 rows x 20 cols
  | Supplementary Figure 6b |  |  |  |  |  |  |  | Supplementary Figure 6e |  |  |  |  |  | ...
  | CB | Class | PSCA | TFF2 | AGR2 | SERPINE2 | APOB | CPB2 | Sample | Subtype | OS_event | OS_days | PPARG | MECOM | ...
  | P02T_AAACCCAGTTCACGAT | S100P+SPP1- | 5.918255779414435 | 0 | 3.988356103058554 | 0 | 0 | 0 | 200643150050_A | Intrahepatic | 0 | 2044 | 154.361115734 | 258.203255839 | ...
  | P02T_AAACCCATCTACCTTA | S100P+SPP1- | 1.823754632656557 | 0 | 4.60223013133851 | 0 | 0 | 0 | 200643150050_B | Intrahepatic | 0 | 1531 | 117.891484774 | 325.688559683 | ...
  | P02T_AAACCCATCTTTCAGT | S100P+SPP1- | 3.21638319361331 | 0 | 5.518874691960901 | 0 | 0 | 0 | 200643150050_C | Intrahepatic | 0 | 19 | 124.575033265 | 218.473099825 | ...
  | P02T_AAACGAAAGGCCTTGC | S100P+SPP1- | 6.742601327283211 | 0 | 4.782183893672806 | 0 | 0 | 0 | 200643150050_D | Intrahepatic | 0 | 219 | 163.734603564 | 752.971065561 | ...
  | P02T_AAAGAACAGCCGTTGC | S100P+SPP1- | 6.14561887922952 | 0 | 5.755776886728985 | 0 | 0 | 0 | 200643150050_E | Intrahepatic | 1 | 777 | 127.276846512 | 180.481301402 | ...
  | P02T_AAAGAACCAGGTCCCA | S100P+SPP1- | 3.040910575495772 | 0 | 5.703330091015208 | 0 | 0 | 0 | 200643150050_F | Intrahepatic | 1 | 210 | 210.286244767 | 4691.96885364 | ...
- sheet `Suppl. Figure 7`: 188 rows x 15 cols
  - gene-symbol-like: col 11 (99% of 170)
  | Supplementary Figure 7a |  |  |  |  |  |  |  |  | Supplementary Figure 7d |  |  |  | Supplementary Figure 7c | ...
  | Group | CD3+/CD45+ (%) | CD20+/CD45+ (%) | CD56+/CD45+ (%) | CD68+/CD45+ (%) | CD8+/(CD4+CD8+) (%) | CD4+/(CD4+CD8+) (%) | (PD1+CD8+)/CD8+ (%) | (FOXP3+CD4+)/CD4+ (%) | Patient | Tissue | Subcluster | Fraction | Group | ...
  | S100P+SPP1- | 0 | 0 | 0 | 0.75 | 0.7988505747126436 | 0.20114942528735633 | 0.8581706063720452 | 0.11428571428571428 | P02 | P | Mono_FCN1 | 0.6406926406926406 | S100P+SPP1- | ...
  | S100P+SPP1- | 0 | 0.03333333333333333 | 0 | 0.2 | 0.5718601640051791 | 0.4281398359948209 | 0.5811320754716981 | 0.11088709677419355 | P02 | T | Mono_FCN1 | 0.4092409240924093 | S100P+SPP1- | ...
  | S100P+SPP1- | 0.03260869565217391 | 0.010869565217391304 | 0 | 0 | 0.6621621621621622 | 0.33783783783783783 | 0.9464285714285714 | 0.145 | P03 | P | Mono_FCN1 | 0.795483061480552 | S100P+SPP1- | ...
  | S100P+SPP1- | 0 | 0.007575757575757576 | 0.0025252525252525255 | 0.047979797979797977 | 0.41379310344827586 | 0.5862068965517241 | 0.8390151515151515 | 0.16310160427807488 | P03 | T | Mono_FCN1 | 0.4221938775510204 | S100P+SPP1- | ...
  | S100P+SPP1- | 0.01858736059479554 | 0.0037174721189591076 | 0.020446096654275093 | 0.2100371747211896 | 0.45890688259109313 | 0.5410931174089069 | 0.7212174680194089 | 0.1934156378600823 | P04 | P | Mono_FCN1 | 0.6432432432432432 | S100P+SPP1- | ...
  | S100P+SPP1- | 0.007416563658838072 | 0.0012360939431396785 | 0.05067985166872682 | 0.1433868974042027 | 0.2966233766233766 | 0.7033766233766233 | 0.37152864648486367 | 0.3052331715551804 | P04 | T | Mono_FCN1 | 0.3492268041237113 | S100P+SPP1- | ...
- sheet `Suppl. Figure 8`: 7465 rows x 12 cols
  | Supplementary Figure 8d |  |  |  |  |  |  |  | Supplementary Figure 8e |  |  | 
  | CB | Subcluster | CD163 | MARCO | CSF1R | IL1B | CCL3 | CCL4 | Sample | Subtype | Macro_c1_SPP1_score | Macro_c2_S100P_score
  | P02P_AGGGTGAAGTGGAAAG | Macro_c1_SPP1 | 0 | 0 | 2.582782656646033 | 0 | 4.12986552347496 | 2.582782656646033 | 200643150050_A | S100P-SPP1+ | 0.2605324302480468 | 0.6723067037909937
  | P02P_GCGTTTCAGGTGCTTT | Macro_c1_SPP1 | 2.670311941497889 | 0 | 4.222772540462324 | 2.670311941497889 | 4.00328677836321 | 4.555047997665728 | 200643150050_B | S100P-SPP1+ | -0.1094102576944829 | -0.3710964834423544
  | P02P_TGAATGCAGTCGAATA | Macro_c1_SPP1 | 0 | 0 | 2.609079038159743 | 2.609079038159743 | 4.937719427097325 | 4.489823607071693 | 200643150050_C | S100P-SPP1+ | 0.0201044732831456 | -0.4552580852428872
  | P02T_AAACCCAGTCTTCAAG | Macro_c1_SPP1 | 2.496471100014713 | 0 | 0 | 0 | 0 | 0 | 200643150050_E | S100P-SPP1+ | 0.1322820580357613 | 0.1818999631154188
  | P02T_AAACGAAAGGTCCCGT | Macro_c1_SPP1 | 3.560041991382398 | 6.404527224648632 | 4.238868300746997 | 0 | 0 | 0 | 200643150050_F | S100P+SPP1- | -0.07433587041911094 | 0.08733333959100437
  | P02T_AAAGGTATCGCTGATA | Macro_c1_SPP1 | 0 | 3.66823053525162 | 0 | 0 | 0 | 0 | 200643150050_G | S100P+SPP1- | 0.2427788529308934 | 0.7492642333669595

### data/papers/song2022/supp/41467_2022_29164_MOESM1_ESM.pdf (3378 kB)
- 17 pages
  - p12: 60 gene-like tokens; 
    T cell subsets, CD20+ B cells, CD68+ macrophages and CD56+ NK cells within
    CD45+ cell between S100P+SPP1- and S100P-SPP1+ iCCA in TMA cohort
    ( S100P+SPP1- n = 68, S100P-SPP1+ n = 118; **P < 0.01, ***P < 0.001; two-
    sided Mann-Whitney U test; CD3+/CD45+ (%): P = 0.0007;
    CD8+/(CD4+CD8+)(%); P < 0.0001; CD4+/(CD4+CD8+)(%); P < 0.0001;
    (PD1+CD8+)+/CD8+(%); P = 0.0042; (FOXP3+CD4+)/CD4+(%); P = 0.5196;
    CD56+/CD45(%); P < 0.0001; CD20+/CD45(%); P = 0.3454; CD68+/CD45(%);
    P = 0.8890; NS: not significant). b Representative mIHC images to show the

### data/papers/song2022/supp/41467_2022_29164_MOESM2_ESM.pdf (3016 kB)
- 34 pages

### data/papers/song2022/supp/41467_2022_29164_MOESM3_ESM.pdf (112 kB)
- 2 pages

### data/papers/song2022/supp/41467_2022_29164_MOESM4_ESM.xlsx (16 kB)
- sheet `Description`: 3 rows x 1 cols
  | Supplementary Data 1. The ba
  | 1. The characteristics of in
  | 2. Overview of the scRNA-seq
- sheet `1.Patient information`: 15 rows x 13 cols
  - gene-symbol-like: col 0 (93% of 15)
  | Patient | Sex | Age (year) | Tumor size (cm) | Vascular invasion | Hepatic Fibrosis | HBsAg | CA19-9 (U/mL) | Ki67 (%) | LNM | TNM stage | Maligant cell number | Non-maligant cell number
  | P02 | Male | 63 | 1.8 | No | No | Negative | 30.5 | 70 | Yes | III B | 2540 | 9834
  | P03 | Female | 64 | 2.7 | No | Yes | Negative | 45.3 | 10 | No | I A | 455 | 11133
  | P17 | Female | 47 | 3.5 | No | No | Negative | 194 | 40 | Yes | III B | 582 | 17320
  | P16 | Male | 49 | 4 | Yes | No | Negative | 45.8 | 80 | Yes | III B | 1816 | 1679
  | P18 | Female | 63 | 4 | No | Yes | Positive | 302 | 90 | Yes | III B | 1410 | 4749
  | P14 | Male | 62 | 5 | No | No | Negative | 56.7 | 40 | No | I A | 1074 | 11686
  | P15 | Male | 61 | 5 | No | Yes | Positive | 20.2 | 40 | No | I A | 2111 | 9777
- sheet `2.Overview of scRNA-seq data`: 29 rows x 14 cols
  | Patients | B | CD4 | CD8 | DC | Endo | Fibro | Mac | MAIT | Mono | NK | Plasma B | Treg | Malignant cells
  | P02-Peritumor | 574 | 110 | 2238 | 80 | 2 | 0 | 3 | 1193 | 148 | 2279 | 11 | 7 | 
  | P02-Tumor | 910 | 497 | 779 | 80 | 10 | 8 | 99 | 185 | 124 | 422 | 8 | 67 | 2540
  | P03-Peritumor | 938 | 216 | 1730 | 152 | 31 | 5 | 11 | 2348 | 634 | 1724 | 17 | 4 | 
  | P03-Tumor | 174 | 536 | 631 | 131 | 183 | 37 | 322 | 252 | 331 | 585 | 11 | 130 | 455
  | P04-Peritumor | 99 | 213 | 5586 | 100 | 37 | 0 | 32 | 443 | 238 | 692 | 17 | 19 | 
  | P04-Tumor | 169 | 166 | 425 | 140 | 324 | 12 | 365 | 33 | 271 | 130 | 15 | 165 | 478
  | P06-Peritumor | 76 | 101 | 760 | 183 | 3 | 0 | 10 | 1124 | 540 | 504 | 28 | 2 | 

### data/papers/song2022/supp/41467_2022_29164_MOESM5_ESM.xlsx (788 kB)
- sheet `Sheet1`: 20713 rows x 3 cols
  - gene-symbol-like: col 0 (82% of 20713)
  | Supplementary Data 2. Gene r |  | 
  | Gene | Positive in S100P- cells | Positive in S100P+ cells
  | SPP1 | 0.8571342419491015 | 0.09060080619361444
  | DCDC2 | 0.8356048727535882 | 0.07218427748761214
  | VIM | 0.8603304788324689 | 0.1510859863135972
  | DEFB1 | 0.9523579785309372 | 0.1516974645466266
  | ZBTB20 | 0.9214208177541913 | 0.2087519419989643
  | FXYD2 | 0.764202146906284 | 0.06576231200235916

### data/papers/song2022/supp/41467_2022_29164_MOESM6_ESM.xlsx (16 kB)
- sheet `Description`: 3 rows x 1 cols
  | Supplementary Data 3 Clinico
  | 1. Clinicopathologic relatio
  | 2. Survial analysis. Univari
- sheet `1.Clinicopathologic relation`: 36 rows x 5 cols
  | Characteristics | Total | S100P+SPP1- | S100P-SPP1+ | P-value
  | Age |  |  |  | 
  | ≤ 51 | 28 (15.1 %) | 9 (13.2 %) | 19 (16.1 %) | 0.599
  | > 51 | 158 (84.9 %) | 59 (86.8 %) | 99 (83.9 %) | 
  | Gender |  |  |  | 
  | Male | 80 (43.0 %) | 28 (41.2 %) | 52 (44.1 %) | 0.701
  | Female | 106 (57.0 %) | 40 (58.8 %) | 66 (55.9 %) | 
  | HBsAg |  |  |  | 
- sheet `2.Survial analysis`: 16 rows x 4 cols
  | Variables | Univariable analysis | Multivariable analysis | 
  |  | P | Hazard ratio (95% CI) | P
  | Age: > 51 vs. ≤ 51 | NS |  | 
  | Gender: male v female | NS |  | 
  | CA19-9: > 37 vs. ≤ 37 | 0.039* |  | NS
  | CEA: > 5 vs. ≤ 5 | NS |  | 
  | Tumor size: > 5 vs. ≤ 5 | < 0.001* | 2.089 (1.349-3.236) | 0.001*
  | Tumor number: multiple vs. s | 0.002* | 1.781 (1.137-2.790) | 0.012*

### data/papers/song2022/supp/41467_2022_29164_MOESM7_ESM.xlsx (34 kB)
- sheet `Description`: 3 rows x 1 cols
  | Supplementary Data 4. Classi
  | 1. Classification of patient
  | 2. Classification of patient
- sheet `1.Jusakul et al.’s dataset`: 116 rows x 14 cols
  - gene-symbol-like: col 9 (73% of 113), col 10 (85% of 100)
  | Sample | S100P | SPP1 | S100P_Class | SPP1_Class | Group | Sex | Age (year) | Subtype | TNM | Stage | Survival (days) | HBV | HCV
  | 200643150050_A | -0.799473870354833 | 2.05471977531052 | Negative | Positive | S100P-SPP1+ | F | 49 | Intrahepatic | T1NxM0 |  | 2044 | Negative | Negative
  | 200643150050_B | -0.791512744390931 | 2.3127159298604 | Negative | Positive | S100P-SPP1+ | M | 56 | Intrahepatic | T4N0M0 | IVA | 1531 | Negative | Negative
  | 200643150050_C | -0.803084687805289 | 0.412466753448245 | Negative | Positive | S100P-SPP1+ | F | 78 | Intrahepatic | T3NxM0 |  | 19 | Negative | Negative
  | 200643150050_D | -0.196361878329748 | 1.19055272182949 | Positive | Positive | Others | F | 52 | Intrahepatic | T3NxM0 |  | 219 | Negative | Positive
  | 200643150050_E | -0.801640620358232 | 0.9058533146415 | Negative | Positive | S100P-SPP1+ | M | 70 | Intrahepatic | T2bN0 |  | 777 | Negative | Negative
  | 200643150050_F | 1.85486089491895 | -0.802483213765916 | Positive | Negative | S100P+SPP1- | M | 40 | Intrahepatic | T3N2M0 | IVA | 210 |  | 
  | 200643150050_G | 0.986880552788844 | -0.772115428852828 | Positive | Negative | S100P+SPP1- | M | 70 | Extrahepatic | T3N0M0 | IIA | 1500 | Negative | Negative
- sheet `1.Job et al.’s dataset`: 79 rows x 6 cols
  - gene-symbol-like: col 5 (99% of 79)
  | S100P | SPP1 | S100P_Class | SPP1_Class | Group | Sample
  | -0.683091222141241 | 0.882863579254625 | Negative | Positive | S100P-SPP1+ | ICC018G
  | 0.0748783230814509 | -0.297426009154054 | Positive | Negative | S100P+SPP1- | ICC014G
  | -0.651060388699457 | -0.324079655904637 | Negative | Negative | Others | ICC013G
  | -0.523718673617772 | 0.546368938846243 | Negative | Positive | S100P-SPP1+ | ICC009G
  | -0.618720547240649 | 0.685316595620211 | Negative | Positive | S100P-SPP1+ | ICC008G
  | -0.938514062992567 | 0.608566574671122 | Negative | Positive | S100P-SPP1+ | ICC006G
  | 1.71342406134338 | -0.832972900794004 | Positive | Negative | S100P+SPP1- | ICC003G

### data/papers/song2022/supp/41467_2022_29164_MOESM8_ESM.xlsx (1516 kB)
- sheet `Sheet1`: 20276 rows x 5 cols
  - gene-symbol-like: col 0 (83% of 20276)
  | Supplementary Data 5. Differ |  |  |  | 
  | Gene | logFC | logCPM | F score | P-value
  | SPP1 | -8.56990355955238 | 11.5063924914239 | 23254.132665575 | 0
  | VTN | -6.33956011167301 | 9.70492195632553 | 11922.4228607465 | 0
  | CRP | -6.26090426723209 | 9.81424012333853 | 8920.36006629482 | 0
  | APCS | -5.79381038859907 | 9.4373706377517 | 10008.3237081862 | 0
  | AGT | -5.6746927022562 | 9.25691635335192 | 18940.7311050511 | 0
  | CRYAB | -5.01351290578775 | 9.41518865870728 | 7580.57089242139 | 0

### data/papers/song2022/supp/41467_2022_29164_MOESM9_ESM.xlsx (238 kB)
- sheet `Sheet1`: 2920 rows x 7 cols
  - gene-symbol-like: col 0 (96% of 2920)
  | Supplementary Data 6.   Mark |  |  |  |  |  | 
  | Gene | Avg_logFC | PCT.1 | PCT.2 | P-value | Adjusted P-value | Cluster
  | S100A12 | 3.6568001471598 | 0.783 | 0.078 | 0 | 0 | 0
  | S100A9 | 2.52119002464321 | 0.984 | 0.674 | 0 | 0 | 0
  | THBS1 | 2.48902917519541 | 0.477 | 0.154 | 0 | 0 | 0
  | FCN1 | 2.45538652245429 | 0.983 | 0.202 | 0 | 0 | 0
  | S100A8 | 2.41258164655537 | 0.948 | 0.451 | 0 | 0 | 0
  | APOBEC3A | 2.21937576698873 | 0.47 | 0.049 | 0 | 0 | 0

## lin2026

Lin Y, Peng L, Zhao H et al. Robust transcriptomic hallmarks targeting intratumor heterogeneity in intrahepatic cholangiocarcinoma. Cell Rep Med 2026

- identifiers: {"pmid": "41916296", "doi": "10.1016/j.xcrm.2026.102708", "pmcid": "PMC13130669"}
- resolved title: Robust transcriptomic hallmarks targeting intratumor heterogeneity in intrahepatic cholangiocarcinoma. Cell Rep Med 2026
- want: LIHV 1,341-gene set (low intra-, high inter-tumour variability) and its five subtypes; multi-region design.

### data/papers/lin2026/supp/mmc1.pdf (5852 kB)
- 21 pages
  - p2: 43 gene-like tokens; 
    1.0
    Low ITH (n = 22)
    Cellular High ITH (n = 23)
    component 0.8
    Development 0.6
    DNA damage 0.4
    Immune 0.2 HR = 0.730
    P = 0.391
  - p8: 106 gene-like tokens; 
    )sraey(
    egA
    *
    )mc(
    retemaid
    romuT
    nedrub
    noitatum
  - p10: 87 gene-like tokens; 
    1.00
    Subgroup
    Age
    TNM stages 0.75
    Sex
    HBV infection
    HCV infection
    0.50 Fluke
  - p12: 117 gene-like tokens; 
    Fu-iCCA
    HRA004766
    OEP002768
    GSE89749
    Fu-iCCA
    HRA004766
    OEP002768
    GSE89749
  - p14: 56 gene-like tokens; 
    A B
    4
    2 3
    1 0
    2
    Percent expressed
    0 1
    25
  - p18: 81 gene-like tokens; 
    B
    Screening and validation of histochemical biomarkers for SI and SIII iCCA
    Significantly upregulated
    genes of SI samples Top 10 genes Distribution of
    in ≥3 cohorts (log 2 fold change) gene ( e n x = p r 6 e ) ssion
    (n = 176)
    LIHV gene set
    IHC validation H-score estimation ROC curve plot
  - p20: 53 gene-like tokens; 
    10-1
    )lm/gn(
    AEC
    mureS
    103
    102
    101
    100

### data/papers/lin2026/supp/mmc2.xlsx (771 kB)
- sheet `Description`: 5 rows x 1 cols
  | Table S1. Gene expression IT
  | Table S1A. ITH index at pati
  | Table S1B. Inter- and intra-
  | Table S1C. Clinicopathologic
  | Table S1D. Mutation profiles
- sheet `Table S1A`: 46 rows x 7 cols
  - gene-symbol-like: col 0 (98% of 46)
  | Patient | Patient-level Gene expressio | Tumor purity-ITH | Immune score-ITH | Stromal score-ITH | SNV ITH | CNV ITH
  | P01 | 0.147568534847769 | 0.03326515025218157 | 168.31113413263034 | 233.80137187528217 | 0.3797327 | 0.05483925
  | P02 | 0.362033800861057 | 0.16269797030247665 | 1182.1757002116224 | 625.3285396827092 | 0.6418247 | 0.58702968
  | P03 | 0.338860199991161 | 0.0806645759883343 | 460.6897657218424 | 477.1526227990504 | 0.6810683 | 0.41132331
  | P04 | 0.490272323235914 | 0.14333856184389934 | 315.2714007641622 | 1038.6936530713467 | 0.5297657 | 0.80514717
  | P05 | 0.274785474074644 | 0.08963711080388662 | 359.4237792518478 | 375.18983595924124 | 0.3881236 | 0.77340361
  | P06 | 0.332723446236036 | 0.06173588173367903 | 345.041739118244 | 292.9013177310699 | 0.5192537 | 0.57076337
  | P07 | 0.287920086396615 | 0.1151651153816177 | 537.4453312905271 | 453.93122810066484 | 0.2402206 | 0.48771874
- sheet `Table S1B`: 17304 rows x 3 cols
  - gene-symbol-like: col 0 (95% of 17304)
  | Gene | Intratumor gene expression I | Intertumour gene expression 
  | A1BG | 0.924757518670118 | 1.69500200042704
  | A1BG-AS1 | 0.295997417892303 | 0.614388988380297
  | A1CF | 0.813408292135711 | 2.21114049195727
  | A2M | 0.56509670137157 | 1.1488228067964
  | A2M-AS1 | 0.446391876344946 | 0.740135300111961
  | A4GALT | 0.463283740912127 | 0.966070052692949
  | A4GNT | 0.438142776986936 | 1.04656069617112
- sheet `Table S1C`: 46 rows x 12 cols
  - gene-symbol-like: col 0 (98% of 46)
  | Patient | Age | Sex | CA19-9 (U/ml) | CEA (ng/ml) | Tumor diameter | HBV infection | Intraheptic metastasis | Vascular invasion | Lymphatic metastasis | Recurrence | RFS (Days)
  | P01 | 61 | Male | 102.4 | 2.9 | 7 | 1 | 1 | 0 | 0 | 1 | 175
  | P02 | 73 | Female | 11.7 | 1.1 | 4 | 0 | 0 | 0 | 0 | 1 | 172
  | P03 | 71 | Male | 10.6 | 1.5 | 11.2 | 0 | 0 | 1 | 0 | 1 | 453
  | P04 | 65 | Male | 2 | 3.1 | 4.5 | 1 | 1 | 0 | 0 | 1 | 40
  | P05 | 56 | Female | 6 | 1.3 | 5.9 | 1 | 1 | 0 | 0 | 1 | 147
  | P06 | 54 | Female | 1542 | 3 | 7.3 | 0 | 0 | 0 | 1 | 1 | 358
  | P07 | 70 | Female | 16.4 | 1.8 | 5 | 0 | 0 | 0 | 0 | 1 | 283
- sheet `Table S1D`: 46 rows x 9 cols
  - gene-symbol-like: col 0 (98% of 46)
  | Patient | TP53 | KRAS | BAP1 | ARID1A | FGFR2 alteration | IDH1/2 | SMAD4 | ATM
  | P01 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
  | P02 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
  | P03 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0
  | P04 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0
  | P05 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0
  | P06 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0
  | P07 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0

### data/papers/lin2026/supp/mmc3.xlsx (883 kB)
- sheet `Description`: 6 rows x 1 cols
  | Table S2. Published transcri
  | Table S2A. Eight published t
  | Table S2B. Application of pu
  | Table S2C. Clustering concor
  | Table S2D. Seven published p
  | Table S2E. Calculation of pr
- sheet `Table S2A`: 5076 rows x 8 cols
  - gene-symbol-like: col 0 (97% of 243), col 1 (99% of 641), col 2 (98% of 5076), col 3 (89% of 952), col 4 (97% of 1570), col 5 (97% of 175), col 6 (94% of 440), col 7 (92% of 505)
  | Andersen et al. | Oishi et al. | Dong et al. | Nakamura et al. | Sia et al. | Lin et al. | Job et al. | Martin-Serrano et al.
  | Title: Genomic and Genetic C | Title: Transcriptomic Profil | Title: Proteogenomic charact | Title: Genomic spectra of bi | Title: Integrative Molecular | Title: Multimodule character | Title: Identification of Fou | Title: Novel microenvironmen
  | Doi: 10.1053/j.gastro.2011.1 | Doi: 10.1002/hep.25890 | Doi: 10.1016/j.ccell.2021.12 | Doi: 10.1038/ng.3375 | Doi: 10.1053/j.gastro.2013.0 | Doi: 10.1136/jitc-2022-00489 | Doi: 10.1002/hep.31092 | Doi: 10.1136/gutjnl-2021-326
  | Method: Unsupervised cluster | Method: Hierarchical cluster | Method: Unsupervised K-means | Method: Unsupervised cluster | Method: Non-negative matrix  | Method: Unsupervised cluster | Method: Hierarchical cluster | Method: Nearest template pre
  | Gene set | Gene set | Gene set | Gene set | Gene set | Gene set | Gene set | Gene set
  | TMPRSS4 | CRP | SLC27A5 | A1CF | WDFY1 | ACTG1 | ZNF831 | HORMAD2-AS1
  | BIK | APCS | UGT2B10 | AASS | ZFP36L1 | ACTN4 | PARP15 | LOC101929089
  | SERPINB5 | TM4SF4 | SERPINA7 | AATK | CRY1 | ADAM12 | LCK | DCXR
- sheet `Table S2B`: 206 rows x 9 cols
  - gene-symbol-like: col 0 (100% of 206), col 6 (100% of 206)
  | Tumor region | Andersen et al. | Oishi et al. | Sia et al. | Dong et al. | Nakamura et al. | Lin et al. | Job et al. | Martin-Serrano et al.
  | P01-R1 | Cluster 1 | HpSC-like | proliferation | RNA subgroup 3 | Cluster 3 | IG2 | Immune desert | Hepati Stem-like
  | P01-R2 | Cluster 1 | HpSC-like | proliferation | RNA subgroup 3 | Cluster 3 | IG2 | Immune desert | Tumor Classical
  | P01-R3 | Cluster 1 | HpSC-like | proliferation | RNA subgroup 3 | Cluster 3 | IG2 | Immune desert | Immune Classical
  | P01-R4 | Cluster 1 | HpSC-like | proliferation | RNA subgroup 3 | Cluster 3 | IG2 | Immune desert | Immune Classical
  | P02-R1 | Cluster 1 | HpSC-like | proliferation | RNA subgroup 3 | Cluster 3 | IG2 | Immune desert | Immune Classical
  | P02-R2 | Cluster 1 | HpSC-like | proliferation | RNA subgroup 3 | Cluster 3 | IG2 | Immune desert | Hepati Stem-like
  | P02-R3 | Cluster 1 | HpSC-like | proliferation | RNA subgroup 2 | Cluster 3 | IG3 | Immunogenic | Hepati Stem-like
- sheet `Table S2C`: 17304 rows x 2 cols
  - gene-symbol-like: col 0 (95% of 17304)
  | Gene | Clustering concordance score
  | SNORA36A | 1.00583283559322e-07
  | MIR1294 | 1.27625951753094e-07
  | MIR210 | 1.27625951753094e-07
  | MIR3942 | 1.27625951753094e-07
  | RNU6-35P | 1.27625951753094e-07
  | SNORA60 | 1.29558609302584e-07
  | MIR5002 | 1.50159718511061e-07
- sheet `Table S2D`: 13 rows x 14 cols
  - gene-symbol-like: col 0 (67% of 12), col 2 (69% of 13), col 10 (64% of 11), col 12 (67% of 12)
  | Ran et al. |  | Su et al. |  | Wang ZY et al. |  | Wang ZJ et al. |  | Zou et al. |  | Guo et al. |  | Wada et al. | 
  | Title: Developing metabolic  |  | Title: Development of a Prog |  | Title: Identification of a f |  | Title: Immune infltration an |  | Title: PIWIL4 and SUPT5H com |  | Title: Prognostic values of  |  | Title: A Transcriptomic Sign | 
  | Doi: 10.1002/jcla.24107 |  | Doi: 10.3389/fgene.2020.6156 |  | Doi: 10.1080/17474124.2022.2 |  | PMID: 35273723 |  | Doi: 10.1186/s12935-021-0231 |  | Doi: 10.7150/ijbs.38846 |  | Doi: 10.1002/hep.31803 | 
  | Gene | Coefficient | Gene | Coefficient | Gene | Coefficient | Gene | Coefficient | Gene | Coefficient | Gene | Coefficient | Gene | Coefficient
  | CYP19A1 | 0.066 | SLC16A3 | -0.377 | MUC1 | 0.187 | STMN1 | 0.009000742 | PIWIL4 | -0.6601 | CD36 | -0.96873 | BIRC5 | -0.4196
  | SCD5 | -0.0186 | BNIP3L | 0.214 | ACSL4 | 0.22 | EGFR | -0.137555962 | SUPT5H | -4.8675 | GGCX | -0.03944 | CDC20 | -0.6444
  | ACOT8 | 0.02 | TPM2 | 0.235 | ACSL3 | 0.368 | ALOX5 | -0.023056411 |  |  | UBASH3B | 0.01064 | CDH2 | 0.06929
  | SRD5A3 | 0.0224 | CLEC11A | -0.265 | SLC38A1 | -0.248 | BNIP3 | 0.191038641 |  |  | DBN1 | 0.04955 | CENPW | 0.06698
- sheet `Table S2E`: 206 rows x 8 cols
  - gene-symbol-like: col 0 (100% of 206)
  | Tumor region | Ran et al. | Su et al. | Wang ZY et al. | Wang ZJ et al. | Zou et al. | Guo et al. | Wada et al.
  | P01-R1 | 0.03599938738203602 | -0.18350348789600046 | 2.563295981383 | 0.16457135300658543 | -24.4766140940202 | 3.96014314283714 | 0.5034083851402402
  | P01-R2 | 0.08523229260227203 | -0.18054743146000019 | 2.470069689329 | 0.21229254547390397 | -24.4238089902463 | 3.19383515343287 | 0.5539570885297698
  | P01-R3 | 0.0813497852814 | -0.0863187562650003 | 2.3770569826749997 | 0.14933087443816517 | -24.7079581541664 | 3.21915251294238 | 0.88010221198209
  | P01-R4 | 0.077820447140016 | -0.22217651858199972 | 2.5268096183939996 | 0.09621637421915397 | -23.734006687544 | 2.9276296413059497 | 0.8982673636890596
  | P02-R1 | 0.055654695444656024 | 0.40236113551200015 | 1.4846370126930002 | -0.05424112318295771 | -25.2069540875451 | 2.79944397139421 | 1.0259371906424501
  | P02-R2 | -0.03142668310063999 | -0.15320182638500002 | 1.5873488891079999 | -0.006823411985885208 | -25.246291796176198 | 2.77714203435541 | 1.5399606216080801
  | P02-R3 | -0.0055806724131799886 | -0.8922444348770009 | 2.3720627519749997 | 0.10764400254739692 | -23.851245048910297 | 2.1000028321621995 | 1.5708947979360106

### data/papers/lin2026/supp/mmc4.xlsx (601 kB)
- sheet `Description`: 5 rows x 1 cols
  | Table S3. Identification of 
  | Table S3A. Highly expressed 
  | Table S3B. List of LIHV gene
  | Table S3C. KEGG enrichment r
  | Table S3D. Spearman correlat
- sheet `Table S3A`: 1929 rows x 3 cols
  - gene-symbol-like: col 0 (99% of 1687), col 1 (98% of 1929), col 2 (98% of 1635)
  | Xue et al. | Song et al. | Ma et al.
  | HES4 | HES4 | C19orf33
  | AGRN | AGRN | SMIM22
  | VWA1 | ERRFI1 | SLPI
  | ARHGEF16 | AKR7A3 | PERP
  | RNF207 | CAMK2N1 | CD24
  | ERRFI1 | TCEA3 | BAIAP2L1
  | EPHA2 | GALE | KRT8
- sheet `Table S3B`: 1342 rows x 1 cols
  - gene-symbol-like: col 0 (94% of 1342)
  | LIHV gene set
  | ABCA13
  | ABCA3
  | ABCC4
  | ABHD17C
  | ABLIM1
  | ABO
  | ABR
- sheet `Table S3C`: 37 rows x 9 cols
  | ID | Description | GeneRatio | BgRatio | pvalue | p.adjust | qvalue | geneID | Count
  | KEGG_METABOLISM_OF_XENOBIOTI | KEGG_METABOLISM_OF_XENOBIOTI | 13/1303 | 70/39781 | 3.9419790565775e-07 | 2.13633615553604e-05 | 1.44955443280048e-05 | 218/222/29785/1551/2052/2944 | 13
  | KEGG_DRUG_METABOLISM_CYTOCHR | KEGG_DRUG_METABOLISM_CYTOCHR | 12/1303 | 72/39781 | 3.62882476837054e-06 | 0.000123301946900028 | 8.36632770730871e-05 | 218/222/1551/2329/2944/2948/ | 12
  | KEGG_REGULATION_OF_ACTIN_CYT | KEGG_REGULATION_OF_ACTIN_CYT | 20/1303 | 213/39781 | 2.66281356675383e-05 | 0.000592036837482641 | 0.000401710947937783 | 50649/623/26999/55740/7430/2 | 20
  | KEGG_O_GLYCAN_BIOSYNTHESIS | KEGG_O_GLYCAN_BIOSYNTHESIS | 7/1303 | 30/39781 | 4.18206212590517e-05 | 0.00080457983206996 | 0.000545926379187381 | 55568/79695/79623/11227/1122 | 7
  | KEGG_MAPK_SIGNALING_PATHWAY | KEGG_MAPK_SIGNALING_PATHWAY | 22/1303 | 267/39781 | 7.90462199297962e-05 | 0.00133684926724738 | 0.000907083736004219 | 776/782/59285/1848/2005/2257 | 22
  | KEGG_HYPERTROPHIC_CARDIOMYOP | KEGG_HYPERTROPHIC_CARDIOMYOP | 11/1303 | 83/39781 | 8.31927472573405e-05 | 0.00138848050267484 | 0.000942116746137428 | 776/782/59285/3673/3675/3655 | 11
  | KEGG_ARRHYTHMOGENIC_RIGHT_VE | KEGG_ARRHYTHMOGENIC_RIGHT_VE | 10/1303 | 74/39781 | 0.000147043493422111 | 0.00206918066233859 | 0.00140398784787938 | 776/782/59285/3673/3675/3655 | 10
- sheet `Table S3D`: 5659 rows x 4 cols
  - gene-symbol-like: col 0 (100% of 5659)
  | Gene | Corr | pVal | pAdj
  | A1BG | -0.293522822540873 | 1.4629780055702e-05 | 1.80732086364982e-05
  | A1CF | 0.919002385013526 | 1.96966427954514e-86 | 7.47943657293047e-85
  | A2M | 0.0785605702533182 | 0.255672072522444 | 0.267491232679732
  | AAAS | 0.297481640473297 | 1.10558457590766e-05 | 1.37270079668324e-05
  | AACS | 0.666921520168894 | 1.62551298857653e-28 | 5.79165773889547e-28
  | AADAC | 0.841837334317164 | 6.92469473449655e-58 | 1.35103182095798e-56
  | AAGAB | 0.488369902044672 | 4.79130907718965e-14 | 8.27509974320484e-14

### data/papers/lin2026/supp/mmc5.xlsx (2856 kB)
- sheet `Description`: 5 rows x 1 cols
  | Table S4. Distinct molecular
  | Table S4A. Identified subgro
  | Table S4B. Gisitic2 analysis
  | Table S4C. KEGG pathway and 
  | Table S4D. Overlap of transc
- sheet `Table S4A`: 257 rows x 12 cols
  - gene-symbol-like: col 1 (100% of 256), col 3 (73% of 117), col 4 (99% of 117), col 7 (99% of 85), col 9 (99% of 82), col 10 (99% of 207), col 11 (100% of 206)
  | Fu-iCCA cohort |  | HRA004766 cohort |  |  | OEP002768 cohort |  |  | GSE89749 cohort |  |  iCCA cohort with multi-regi | 
  | Patient_ID | Subgroup | Patient ID | Seq ID | Subgroup | Patient No. | Tumor (T) RNA-seq ID | Subgroup | Sample | Subgroup | Sample | Subgroup
  | 633 | SI | 2 | T102 | SI | CCA#44 | R21023786-F13-35-35 | SI | GSM2387724 | SI | P19-R3 | SI
  | 381 | SI | 39 | T181 | SI | CCA#82 | R21026687-F15-27-95 | SI | GSM2387698 | SI | P19-R1 | SI
  | 437 | SI | 16 | T129 | SI | CCA#177 | R21026745-F18-15-173 | SI | GSM2387722 | SI | P19-R2 | SI
  | 537 | SI | 34 | T167 | SI | CCA#150 | R21026731-F18-1-159 | SI | GSM2387691 | SI | P19-R4 | SI
  | 391 | SI | 1 | T101 | SI | CCA#103 | R21026694-F16-19-319-117 | SI | GSM2387762 | SI | P37-R2 | SI
  | 217 | SI | 14 | T123 | SI | CCA#152 | R21026735-F18-5-163 | SI | GSM2387685 | SI | P37-R3 | SI
- sheet `Table S4B`: 71 rows x 267 cols
  | Unique Name | Descriptor | Wide Peak Limits | Peak Limits | Region Limits | q values | Residual q values after remo | Amplitude Threshold | T327 | T233 | T447 | T611 | T957 | T837 | ...
  | Amplification Peak  1 | 1q21.3  | chr1:151500002-153300000(pro | chr1:152000002-152400000(pro | chr1:118400002-249250621(pro | 6.0233e-19 | 3.0278e-18 | 0: t<0.3; 1: 0.3<t< 0.9; 2:  | 0 | 0 | 0 | 0 | 1 | 1 | ...
  | Amplification Peak  2 | 1q42.13 | chr1:156600002-249250621(pro | chr1:228300002-228800000(pro | chr1:118400002-249250621(pro | 0.0010471 | 0.0070856 | 0: t<0.3; 1: 0.3<t< 0.9; 2:  | 1 | 1 | 0 | 1 | 1 | 0 | ...
  | Amplification Peak  3 | 2q31.3  | chr2:179200002-190400000(pro | chr2:179300002-182500000(pro | chr2:140900002-197800000(pro | 9.2852e-08 | 9.2852e-08 | 0: t<0.3; 1: 0.3<t< 0.9; 2:  | 0 | 0 | 1 | 0 | 0 | 1 | ...
  | Amplification Peak  4 | 3q26.2  | chr3:155600002-178800000(pro | chr3:167700002-170400000(pro | chr3:164600002-170700000(pro | 0.038249 | 0.038249 | 0: t<0.3; 1: 0.3<t< 0.9; 2:  | 0 | 0 | 0 | 0 | 0 | 2 | ...
  | Amplification Peak  5 | 6q11.2  | chr6:45100002-73800000(probe | chr6:62600002-63900000(probe | chr6:53900002-71900000(probe | 0.015031 | 0.015031 | 0: t<0.3; 1: 0.3<t< 0.9; 2:  | 0 | 0 | 0 | 0 | 0 | 1 | ...
  | Amplification Peak  6 | 7p21.3  | chr7:6700002-43700000(probes | chr7:7300002-8700000(probes  | chr7:6800002-40200000(probes | 0.006125 | 0.006125 | 0: t<0.3; 1: 0.3<t< 0.9; 2:  | 0 | 0 | 1 | 1 | 0 | 1 | ...
  | Amplification Peak  7 | 7q21.3  | chr7:77400002-97900000(probe | chr7:95800002-96700000(probe | chr7:76000002-98200000(probe | 2.6143e-05 | 0.00040549 | 0: t<0.3; 1: 0.3<t< 0.9; 2:  | 0 | 0 | 1 | 1 | 1 | 1 | ...
- sheet `Table S4C`: 745 rows x 238 cols
  | Sample | Cohort | KEGG_N_GLYCAN_BIOSYNTHESIS | KEGG_OTHER_GLYCAN_DEGRADATIO | KEGG_O_GLYCAN_BIOSYNTHESIS | KEGG_GLYCOSAMINOGLYCAN_DEGRA | KEGG_GLYCOSAMINOGLYCAN_BIOSY | KEGG_GLYCEROLIPID_METABOLISM | KEGG_GLYCOSYLPHOSPHATIDYLINO | KEGG_GLYCEROPHOSPHOLIPID_MET | KEGG_ETHER_LIPID_METABOLISM | KEGG_ARACHIDONIC_ACID_METABO | KEGG_LINOLEIC_ACID_METABOLIS | KEGG_ALPHA_LINOLENIC_ACID_ME | ...
  | 111 | Fu-iCCA_mRNA | 0.328059581206428 | 0.317376771299312 | 0.0126778270484816 | 0.228449237822227 | 0.133175254483758 | 0.136700264845645 | 0.209595652794783 | 0.124522369707356 | 0.103503928228569 | 0.0545009946685615 | -0.0888702900610504 | -0.0596374676013782 | ...
  | 113 | Fu-iCCA_mRNA | 0.330976509446849 | 0.312741695020613 | 0.079002502333457 | 0.238927142430004 | 0.198098111312958 | 0.0812019210926783 | 0.259885644351935 | 0.11922928678579 | 0.0656013266360418 | 0.0204175334522618 | -0.119000426696033 | -0.167065991195287 | ...
  | 115 | Fu-iCCA_mRNA | 0.353231296748575 | 0.358615234309246 | 0.0221980543070961 | 0.23694532420283 | 0.132620982994706 | 0.149280879089167 | 0.274500913390826 | 0.149401712075696 | 0.134538300233391 | 0.128625542167617 | 0.0926080044378588 | -0.0389631981647961 | ...
  | 117 | Fu-iCCA_mRNA | 0.320653530160132 | 0.313750993320686 | 0.032890717062233 | 0.255996176433182 | 0.167093824115941 | 0.153782972546636 | 0.238932148162883 | 0.141957217577661 | 0.0820495318898502 | 0.127081811139122 | 0.0947627183997218 | -0.0796957516217355 | ...
  | 121 | Fu-iCCA_mRNA | 0.348929541752914 | 0.295198887476435 | 0.0909930267228842 | 0.237783279859385 | 0.129530146124875 | 0.113632743781466 | 0.275255387530187 | 0.130007582435386 | 0.0845440784194411 | 0.10390021083296 | -0.0735714594678649 | -0.135712028608597 | ...
  | 123 | Fu-iCCA_mRNA | 0.343458028879172 | 0.328794087431329 | 0.100321435418463 | 0.245398297996757 | 0.16196392006426 | 0.141727098509221 | 0.263242166088412 | 0.150559738274913 | 0.139507966051407 | 0.152216520899386 | 0.101465355550138 | -0.0533978948735692 | ...
  | 125 | Fu-iCCA_mRNA | 0.360869110820333 | 0.315428150017421 | 0.112909597686209 | 0.21145868410687 | 0.1518068484344 | 0.100613503505725 | 0.234017820048533 | 0.13015635789621 | 0.109280285730965 | 0.0807509087491403 | -0.066946580101875 | -0.0600800003643549 | ...
- sheet `Table S4D`: 256 rows x 11 cols
  - gene-symbol-like: col 1 (100% of 256), col 8 (100% of 256), col 9 (100% of 256)
  | Patient_ID | Heterogeneity subgroups | Andersen et al. | Oishi et al. | Sia et al. | Dong et al. | Nakamura et al. | Protein | Lin J et al. | Job et al. | Martin-Serrano et al.
  | 483 | SI | Cluster 2 | HpSC | Inflammation | RNA subgroup 1 | Cluster 1 | Mesenchymal | IG1 | I3 | Inflammatory Stroma
  | 391 | SI | Cluster 2 | MH | Proliferation | RNA subgroup 1 | Cluster 2 | Inflammatory | IG1 | I2 | Tumor Classical
  | 383 | SI | Cluster 2 | MH | Proliferation | RNA subgroup 1 | Cluster 2 | Inflammatory | IG1 | I1 | Tumor Classical
  | 441 | SI | Cluster 2 | MH | Proliferation | RNA subgroup 1 | Cluster 2 | Metabolic | IG2 | I1 | Tumor Classical
  | 953 | SI | Cluster 2 | MH | Proliferation | RNA subgroup 1 | Cluster 3 | Inflammatory | IG1 | I1 | Tumor Classical
  | 385 | SI | Cluster 2 | MH | Proliferation | RNA subgroup 1 | Cluster 3 | Inflammatory | IG1 | I3 | Tumor Classical
  | 853 | SI | Cluster 2 | MH | Proliferation | RNA subgroup 1 | Cluster 3 | Inflammatory | IG1 | I1 | Tumor Classical

### data/papers/lin2026/supp/mmc6.xlsx (1061 kB)
- sheet `Description`: 6 rows x 1 cols
  | Table S5. Distinct character
  | Table S5A. Immune cell subse
  | Table S5B. Comparison of imm
  | Table S5C. Differentially ex
  | Table S5D. Prediction of iCC
  | Table S5E. Clinical informat
- sheet `Table S5A`: 537 rows x 136 cols
  | Sample | Cohort | B cell_TIMER | T cell CD4+_TIMER | T cell CD8+_TIMER | Neutrophil_TIMER | Macrophage_TIMER | Myeloid dendritic cell_TIMER | B cell naive_CIBERSORT | B cell memory_CIBERSORT | B cell plasma_CIBERSORT | T cell CD8+_CIBERSORT | T cell CD4+ naive_CIBERSORT | T cell CD4+ memory resting_C | ...
  | 111 | Fu-iCCA | 0.0667225547260539 | 0.140530232375284 | 0.0922612770624664 | 0.138353756832718 | 0.0430017863864443 | 0.534819674071595 | 0.0214161085911597 | 0.0175954888027276 | 0 | 0.0847308926622026 | 0 | 0.211477679266858 | ...
  | 113 | Fu-iCCA | 0.0581542219504822 | 0.0580679383900215 | 0.148131232906924 | 0.0667695675457919 | 0 | 0.372481707205932 | 0.0023605986149332 | 0.00277498078911267 | 0.00124749225713441 | 0 | 0 | 0.103357588612935 | ...
  | 115 | Fu-iCCA | 0.0592494677093029 | 0.109192422916041 | 0.131794711007158 | 0.0491982655082023 | 0.0134758854392738 | 0.403805275989646 | 0 | 0.0131128909807505 | 0.0384604453591945 | 0.0619056334276352 | 0 | 0.165619025511441 | ...
  | 117 | Fu-iCCA | 0.0589504074248825 | 0.110805823976907 | 0.131103999790378 | 0.0525191828017627 | 0.0254675363857199 | 0.354079567595749 | 0 | 0.0063435487828472 | 0 | 0.0611877256688692 | 0 | 0.180933043529864 | ...
  | 121 | Fu-iCCA | 0.063342227127653 | 0.154043172123091 | 0.107522531135227 | 0.0414574479946976 | 0.0612739290344555 | 0.397823839514251 | 0.0399110229535967 | 0 | 0.0404332599589131 | 0.100660820698116 | 0 | 0.228315895204136 | ...
  | 123 | Fu-iCCA | 0.16597401268445 | 0.056697772710077 | 0.265866705267404 | 0.153167787780074 | 0.0986299118300202 | 0.645098426077556 | 0.0415264066822059 | 0 | 0.0044938650635458 | 0.0919813377058497 | 0 | 0.107064947930076 | ...
  | 125 | Fu-iCCA | 0.0968311054311877 | 0.069036756760303 | 0.249405178358232 | 0.155857048864396 | 0.187343473489175 | 0.776908292164433 | 0 | 0 | 0.000952655830911863 | 0.0343143741024704 | 0 | 0.154057711429308 | ...
- sheet `Table S5B`: 2651 rows x 6 cols
  - gene-symbol-like: col 2 (100% of 2651)
  | Immune_cell_subset | Cohort | Subgroup | p-value | FDR | log2 fold change
  | B cell memory_XCELL | Fu-iCCA | SI | 0.2998903 | 0.44983545 | -0.253771175
  | B cell naive_XCELL | Fu-iCCA | SI | 0.2798242 | 0.439345452 | -0.165015883
  | B cell plasma_XCELL | Fu-iCCA | SI | 0.06072613 | 0.131944431 | -0.510080821
  | B cell_XCELL | Fu-iCCA | SI | 0.9832866 | 0.9832866 | -0.22424921
  | Cancer associated fibroblast | Fu-iCCA | SI | 4.11e-05 | 0.000422834 | -0.846641353
  | Class-switched memory B cell | Fu-iCCA | SI | 0.2124912 | 0.394626514 | 0.149683396
  | Common lymphoid progenitor_X | Fu-iCCA | SI | 0.000252643 | 0.001839092 | -0.417629368
- sheet `Table S5C`: 594 rows x 3 cols
  - gene-symbol-like: col 1 (97% of 594), col 2 (100% of 594)
  | Gene_id | Symbol | Subgourp
  | 1001 | CDH3 | SI
  | 100288077 | WTAPP1 | SI
  | 100499467 | LINC00673 | SI
  | 10103 | TSPAN1 | SI
  | 10144 | FAM13A | SI
  | 10170 | DHRS9 | SI
  | 10232 | MSLN | SI
- sheet `Table S5D`: 46 rows x 8 cols
  - gene-symbol-like: col 2 (98% of 46)
  | Cohort | sample.names | predict.label | dist.to.template | dist.to.cls1.rank | nominal.p | BH.FDR | Bonferroni.p
  | Xue | A001_ICC | SII | 0.976514920069346 | 10 | 0.000799840031993601 | 0.00137750227732231 | 0.0247950409918016
  | Xue | A002_ICC | SIII-1 | 1.09984433778491 | 14 | 0.726454709058188 | 0.938337332533493 | 1
  | Xue | A003_ICC | SI | 0.733711835996492 | 7 | 0.0001999600079984 | 0.000729265911523578 | 0.00619876024795041
  | Xue | A004_ICC | SIII-2 | 0.798674745215066 | 21 | 0.0001999600079984 | 0.000729265911523578 | 0.00619876024795041
  | Xue | A005_ICC | SIII-3 | 1.08548788065881 | 31 | 0.760647870425915 | 0.943203359328134 | 1
  | Xue | A006_ICC | SI | 0.43035501375689 | 3 | 0.0001999600079984 | 0.000729265911523578 | 0.00619876024795041
  | Xue | A008_ICC | SIII-1 | 1.18179814740109 | 15 | 0.873025394921016 | 1 | 1
- sheet `Table S5E`: 4 rows x 11 cols
  | Patient ID | Sex | Age | HCVAb | HBsAg | Liver cirrhosis  | CA19-9(U/ml) | Tumor size | Microvascular invasion | Intrahepatic metastasis | TNM staging
  | ICC2935 | male | 57 | negative | negative | no | 11.1 | 9 | 0 | no | I
  | ICC4715 | male | 64 | positive | negative | yes | 74.7 | 2.5 | 0 | no | I
  | ICC39T | Female | 72 | negative | negative | no | 5349 | 4.2 | 0 | yes | IIIB

### data/papers/lin2026/supp/mmc7.xlsx (1672 kB)
- sheet `Description`: 5 rows x 1 cols
  | Table S6. Therapeutic opport
  | Table S6A. Prediction of iCC
  | Table S6B. Prediction of the
  | Table S6C. Prediction of mur
  | Table S6D. Raw RNA-seq count
- sheet `Table S6A`: 13 rows x 7 cols
  - gene-symbol-like: col 0 (92% of 13), col 1 (92% of 13)
  | Sample.names | Predict.label | dist.to.template | dist.to.cls1.rank | nominal.p | BH.FDR | Bonferroni.p
  | ICCO1 | SIII-3 | 0.963087509109507 | 12 | 0.355928814237153 | 0.355928814237153 | 1
  | ICCO2 | SIII-2 | 0.84400849885987 | 10 | 0.000599880023995201 | 0.000799840031993601 | 0.00719856028794241
  | ICCO3 | SIII-2 | 0.63826071618253 | 9 | 0.0001999600079984 | 0.000533226687995734 | 0.0023995200959808
  | ICCO4 | SI | 0.641520310106621 | 4 | 0.0001999600079984 | 0.000533226687995734 | 0.0023995200959808
  | ICCO5 | SI | 0.750359070007536 | 5 | 0.0001999600079984 | 0.000533226687995734 | 0.0023995200959808
  | ICCO7 | SI | 0.39939315308004 | 1 | 0.0001999600079984 | 0.000533226687995734 | 0.0023995200959808
  | ICCO8 | SI | 0.50012387109647 | 2 | 0.0001999600079984 | 0.000533226687995734 | 0.0023995200959808
- sheet `Table S6B`: 537 rows x 11 cols
  | Sample | Cohort | IPRES_score | Miracle_score | INFγ_score | T.cell.inflamed_score | IMPRES_score | TIDE_score | INFγ/IMS_score | Inflammatory_score | TRS_score
  | 111 | Fu-iCCA | 0.767851285217282 | 0.7 | 35.1853333333333 | 29.555 | 7 | 0.93 | 0.519144912444492 | -5.6540698232 | 0.341789732056288
  | 113 | Fu-iCCA | -0.194342005434166 | 0.7 | 8.544 | 9.34 | 4 | 1.39 | 0.228424567452599 | -7.4209063196 | 0.111799788219382
  | 115 | Fu-iCCA | -0.72334451568572 | 0.76 | 53.438 | 54.9835714285714 | 5 | 0.34 | 1.68546579983368 | -6.9307536944 | 0.338516385277619
  | 117 | Fu-iCCA | -0.820531300252368 | 0.86 | 71.8246666666667 | 78.5114285714286 | 6 | 0.18 | 3.66537496630798 | -8.9880133942 | 0.209812353297501
  | 121 | Fu-iCCA | -0.480175819384257 | 0.74 | 24.3006666666667 | 24.5142857142857 | 5 | 1.09 | 1.02675153621436 | -3.8790587056 | 0.29205755218495
  | 123 | Fu-iCCA | 0.405927896611344 | 0.96 | 79.754 | 80.2692857142857 | 7 | -0.53 | 4.56486880612673 | -3.55959255419999 | 0.589268338563892
  | 125 | Fu-iCCA | 0.420802881934374 | 0.81 | 20.8226666666667 | 25.0428571428571 | 7 | 0.07 | 0.343550163241807 | -3.7500930696 | 0.487056735766267
- sheet `Table S6C`: 19 rows x 7 cols
  - gene-symbol-like: col 1 (95% of 19)
  | Sample.names | Predict.label | dist.to.template | dist.to.cls1.rank | nominal.p | BH.FDR | Bonferroni.p
  | KTP103.KRASTrp53 | SIII-3 | 0.919860486 | 18 | 0.149570086 | 0.175964807 | 1
  | KTP102.KRASTrp53 | SI | 0.754238626 | 5 | 0.00019996 | 0.001333067 | 0.0039992
  | KTP101.KRASTrp53 | SI | 0.635428533 | 4 | 0.00019996 | 0.001333067 | 0.0039992
  | MS117.Ctrl | SII | 1.014029257 | 9 | 0.297740452 | 0.330822724 | 1
  | MS33.Ctrl | SII | 1.015931418 | 10 | 0.337532494 | 0.355297362 | 1
  | MS36.Ctrl | SII | 0.969208315 | 8 | 0.099180164 | 0.123975205 | 1
  | MS119.Fbxw7 | SIII-3 | 0.893579252 | 16 | 0.00979804 | 0.019596081 | 0.195960808
- sheet `Table S6D`: 55336 rows x 4 cols
  | gene_ID | KTP101 | KTP102 | KTP103
  | ENSMUSG00000028180 | 6368 | 5628 | 5710
  | ENSMUSG00000028182 | 41 | 26 | 32
  | ENSMUSG00000028185 | 0 | 0 | 0
  | ENSMUSG00000028184 | 2724 | 2837 | 2806
  | ENSMUSG00000028187 | 1883 | 1973 | 1573
  | ENSMUSG00000028186 | 14 | 8 | 9
  | ENSMUSG00000028189 | 1080 | 851 | 677

### data/papers/lin2026/supp/mmc8.xlsx (861 kB)
- sheet `Description`: 10 rows x 1 cols
  | Table S7. Identification of 
  | Table S7A. Significantly upr
  | Table S7B. Significantly upr
  | Table S7C. Significantly upr
  | Table S7D. Significantly upr
  | Table S7E. Significantly upr
  | Table S7F. Significantly upr
  | Table S7G. Significantly upr
- sheet `Table S7A`: 1206 rows x 9 cols
  - gene-symbol-like: col 1 (97% of 1206)
  | gene_id | symbol | baseMean | log2FoldChange | lfcSE | stat | pvalue | padj | UpDown
  | 8000 | PSCA | 546.047916112424 | 7.08847072182841 | 0.289358086822502 | 24.497226946958 | 1.58115799620497e-132 | 3.0617543438513e-128 | Up
  | 55808 | ST6GALNAC1 | 690.113453539056 | 6.0550200285119 | 0.259438586526887 | 23.338933924867 | 1.78523664261225e-120 | 1.72846611737718e-116 | Up
  | 3853 | KRT6A | 5609.88643513874 | 7.91057469601306 | 0.345165916242824 | 22.9181802830381 | 3.06105704097233e-116 | 1.97581028471294e-112 | Up
  | 144568 | A2ML1 | 344.232833737596 | 8.02242302286144 | 0.353370010310218 | 22.7026142252951 | 4.22133719928612e-114 | 2.04354933817441e-110 | Up
  | 135656 | DPCR1 | 1596.4386792629 | 6.73396223777119 | 0.305178160781306 | 22.0656754091811 | 6.75522589563529e-108 | 2.61616388486164e-104 | Up
  | 6273 | S100A2 | 305.287355258213 | 5.59455273682467 | 0.27315941408347 | 20.4809076619088 | 3.18664907796645e-93 | 1.02843787909571e-89 | Up
  | 84951 | TNS4 | 1106.26568714565 | 6.28806802840256 | 0.309852821964097 | 20.2937252226516 | 1.46094732592484e-91 | 4.04139771702981e-88 | Up
- sheet `Table S7B`: 596 rows x 9 cols
  - gene-symbol-like: col 1 (97% of 596)
  | Gene_id | Symbol | baseMean | log2FoldChange | lfcSE | stat | pvalue | padj | UpDown
  | 80310 | PDGFD | 5317.65379631399 | 2.81419 | 0.150509824676843 | -18.6977357528409 | 5.16519124298757e-78 | 7.69375101763164e-75 | Up
  | 80760 | ITIH5 | 11173.6047679274 | 3.52435 | 0.19155339145829 | -18.3987809683797 | 1.34353349166105e-75 | 1.73441216883497e-72 | Up
  | 5314 | PKHD1 | 10242.9218752091 | 2.54843 | 0.150538455489847 | -16.9287654618312 | 2.76110464617775e-64 | 1.90950108459235e-61 | Up
  | 51473 | DCDC2 | 15702.3840932696 | 2.84125 | 0.169528112393761 | -16.7597859620508 | 4.80350313209706e-63 | 3.00048498870734e-60 | Up
  | 285016 | FAM150B | 225.183404215579 | 3.68989 | 0.225822337070179 | -16.3398105558387 | 5.14123953114359e-60 | 2.55269134054011e-57 | Up
  | 26137 | ZBTB20 | 3773.23024340909 | 1.45354 | 0.0906780914690551 | -16.029685647921 | 7.92827958300783e-58 | 3.48916376921281e-55 | Up
  | 79674 | VEPH1 | 1340.29812897247 | 2.69587 | 0.168598232331974 | -15.9899064646275 | 1.5025643863062e-57 | 6.46570150587404e-55 | Up
- sheet `Table S7C`: 1734 rows x 9 cols
  - gene-symbol-like: col 1 (93% of 1734)
  | gene_id | symbol | baseMean | log2FoldChange | lfcSE | stat | pvalue | padj | UpDown
  | ENSG00000167653 | PSCA | 1693.40818169389 | 7.43216949189102 | 0.419021872464106 | 17.7369487854782 | 2.17425332741966e-70 | 5.12428024206265e-66 | Up
  | ENSG00000070526 | ST6GALNAC1 | 489.25538323728 | 6.27830846634531 | 0.357463900662952 | 17.5634755137555 | 4.69128544437531e-69 | 5.52821076765186e-65 | Up
  | ENSG00000073756 | PTGS2 | 1123.73371516938 | 4.91177019622175 | 0.310276601639384 | 15.8302951955443 | 1.92316821991365e-56 | 1.51084095356416e-52 | Up
  | ENSG00000134757 | DSG3 | 283.058403832513 | 7.25902364761823 | 0.499373047868427 | 14.5362743916664 | 7.13727821692177e-48 | 3.36422746032825e-44 | Up
  | ENSG00000196352 | CD55 | 3208.67365558555 | 2.6454912368998 | 0.183354198428174 | 14.4283101209494 | 3.43391849703949e-47 | 1.34884318563711e-43 | Up
  | ENSG00000189377 | CXCL17 | 196.434038899995 | 7.75401715028212 | 0.557792839994382 | 13.9012489840497 | 6.22456089922225e-44 | 1.83375564091087e-40 | Up
  | ENSG00000277585 | MUC4 | 69.3055210521149 | 8.07515039146449 | 0.592172465693149 | 13.6364840638316 | 2.42996695157784e-42 | 5.72694611147866e-39 | Up
- sheet `Table S7D`: 877 rows x 9 cols
  - gene-symbol-like: col 1 (81% of 877)
  | Gene_id | Symbol | baseMean | log2FoldChange | lfcSE | stat | pvalue | padj | UpDown
  | ENSG00000142149 | HUNK | 787.325797115008 | 2.45310555305041 | 0.183457359058932 | 13.3715298510451 | 8.86975867491643e-41 | 9.08880315001871e-38 | Up
  | ENSG00000119283 | TRIM67 | 106.9862578978 | 3.90979175071517 | 0.315754252601901 | 12.3823882607991 | 3.25510046349999e-35 | 2.47471637818606e-32 | Up
  | ENSG00000148468 | FAM171A1 | 4172.06279713344 | 2.34996463389253 | 0.198746530622898 | 11.8239278267018 | 2.93627726080321e-32 | 1.68785810933195e-29 | Up
  | ENSG00000164287 | CDC20B | 150.223380901123 | 4.55128784795513 | 0.405871498621975 | 11.2136177667261 | 3.49605563010566e-29 | 1.55462337906283e-26 | Up
  | ENSG00000070729 | CNGB1 | 157.901359633203 | 4.31709900117668 | 0.388229487338221 | 11.1199667773192 | 1.00309338801038e-28 | 4.22159017296938e-26 | Up
  | ENSG00000081800 | SLC13A1 | 104.167370781489 | 5.69280705196954 | 0.51472062659617 | 11.0599940196993 | 1.96110599782116e-28 | 7.33640415184905e-26 | Up
  | ENSG00000111785 | RIC8B | 884.352717779897 | 1.3642014491711 | 0.125882729320597 | 10.8370819137291 | 2.29680596660735e-27 | 7.84509029289886e-25 | Up
- sheet `Table S7E`: 430 rows x 9 cols
  - gene-symbol-like: col 1 (99% of 430)
  | gene_id | symbol | logFC | AveExpr | t | P.Value | adj.P.Val | B | UpDown
  | 1048 | CEACAM5 | 6.53666136021593 | 3.85495653637254 | 20.9534477913247 | 5.04010822001998e-36 | 6.17715663445649e-32 | 69.7498073827745 | Up
  | 56649 | TMPRSS4 | 4.89144081870221 | 3.75097466563329 | 17.1759985239097 | 6.8391911632974e-30 | 2.79403756324577e-26 | 56.7083227516602 | Up
  | 10595 | ERN2 | 4.87352536598961 | 3.44133627602718 | 17.2661974651138 | 4.78341970763288e-30 | 2.79403756324577e-26 | 57.0605060328398 | Up
  | 80736 | SLC44A4 | 4.98912554657661 | 3.81070279951953 | 16.3553083995461 | 1.85465665957817e-28 | 5.6826680049475e-25 | 53.5691686178812 | Up
  | 8537 | BCAS1 | 3.41902425396581 | 3.26052413575421 | 13.2465925787156 | 1.07593073449286e-22 | 2.63732141638889e-19 | 40.8338726986818 | Up
  | 9052 | GPRC5A | 5.00278316440695 | 5.25295073621471 | 13.0403880565716 | 2.70465808058071e-22 | 5.52471490593287e-19 | 39.9595890871574 | Up
  | 29785 | CYP2S1 | 3.90892922740201 | 3.95809151512683 | 12.8903178839901 | 5.30603849599008e-22 | 9.29011540097921e-19 | 39.352640175461 | Up
- sheet `Table S7F`: 250 rows x 9 cols
  - gene-symbol-like: col 1 (99% of 250)
  | gene_id | Symbol | logFC | AveExpr | t | P.Value | adj.P.Val | B | UpDown
  | 51473 | DCDC2 | 2.99473521628919 | 6.12561299043474 | 8.97473675286669 | 4.56177585498188e-14 | 2.7954562439329e-10 | 21.4418756269284 | Up
  | 80114 | BICC1 | 2.35288737911928 | 6.44864395406482 | 9.08800821587758 | 2.66475395848025e-14 | 2.7954562439329e-10 | 22.0072599000986 | Up
  | 80760 | ITIH5 | 3.31973967545492 | 5.70351200128145 | 8.7829145221435 | 1.13331874246546e-13 | 4.62998483588556e-10 | 20.5481925699788 | Up
  | 92126 | DSEL | 2.04487017318971 | 4.6572326473733 | 8.61857914250399 | 2.46973927310046e-13 | 7.56728113277982e-10 | 19.7879428694784 | Up
  | 80310 | PDGFD | 2.51860799672139 | 4.26916055465612 | 8.12824375081108 | 2.5073812941766e-12 | 6.14609302828569e-09 | 17.5697078738985 | Up
  | 5314 | PKHD1 | 2.66384138283949 | 7.20374402068862 | 7.93856798027632 | 6.12224736643344e-12 | 9.58809386538492e-09 | 16.8261578758525 | Up
  | 51053 | GMNN | 2.10010685544282 | 5.50103360787607 | 7.95651343511153 | 5.62706442965536e-12 | 9.58809386538492e-09 | 16.8699364460797 | Up
- sheet `Table S7G`: 235 rows x 9 cols
  - gene-symbol-like: col 1 (99% of 235)
  | gene_id | symbol | logFC | AveExpr | t | P.Value | adj.P.Val | B | UpDown
  | 9052 | GPRC5A | 2.91284487075246 | 7.83931579053588 | 14.9769306293755 | 3.31528378320348e-25 | 7.08940284200233e-21 | 46.5205214706871 | Up
  | 6286 | S100P | 5.20909385197487 | 9.80896628808249 | 13.5819077900038 | 1.2053963732447e-22 | 8.5558359501286e-19 | 40.8424962982541 | Up
  | 55808 | ST6GALNAC1 | 2.28253431397026 | 7.29965580806605 | 13.4312111038154 | 1.96790370428576e-22 | 8.5558359501286e-19 | 40.3692132187502 | Up
  | 56649 | TMPRSS4 | 1.35905394774241 | 7.11513370403863 | 12.7313950791515 | 3.1642600224317e-21 | 9.66636233138279e-18 | 37.6825338421861 | Up
  | 54854 | FAM83E | 1.75246017192336 | 7.06546884302364 | 12.2142909675083 | 3.565271384864e-20 | 7.62397632939319e-17 | 35.3372019450778 | Up
  | 2524 | FUT2 | 2.42935003685435 | 7.92454120260027 | 11.7621313259457 | 2.7349359224405e-19 | 4.87365581378896e-16 | 33.361231713898 | Up
  | 148170 | CDC42EP5 | 2.20620886109566 | 9.35742539955819 | 11.3423229309711 | 1.63980294655792e-18 | 2.50468187208533e-15 | 31.620877832139 | Up
- sheet `Table S7H`: 185 rows x 9 cols
  - gene-symbol-like: col 1 (99% of 185)
  | gene_id | Symbol | logFC | AveExpr | t | P.Value | adj.P.Val | B | UpDown
  | 8416 | ANXA9 | 2.75010963080381 | 8.33720937076783 | 13.3838598798588 | 2.4194751927115e-22 | 2.58690287604714e-18 | 40.0299493959381 | Up
  | 51473 | DCDC2 | 2.92135725351861 | 9.24397188006877 | 12.8183620105597 | 2.80868333076142e-21 | 2.00202947816674e-17 | 37.6780633877959 | Up
  | 5314 | PKHD1 | 1.28575384994625 | 7.16002770169532 | 12.6250191663903 | 5.08193946926989e-21 | 2.71680484027168e-17 | 37.1088742257479 | Up
  | 81788 | NUAK2 | 1.8206294545231 | 8.19559138859129 | 12.1769094703356 | 3.63468739006423e-20 | 1.55448310298267e-16 | 35.2163285344725 | Up
  | 9514 | GAL3ST1 | 2.08523582573532 | 8.47813866675255 | 11.8279914357151 | 1.84388904629881e-19 | 6.57162056100895e-16 | 33.6523959193462 | Up
  | 486 | FXYD2 | 4.58035768209941 | 11.0323289238121 | 11.47859629515 | 1.03764421790302e-18 | 3.16985485080547e-15 | 31.9877071696671 | Up
  | 8195 | MKKS | 1.18721033008275 | 10.6222874177708 | 10.8516975365361 | 1.34434264843991e-17 | 3.19415813269322e-14 | 29.5117296192353 | Up
- sheet `Table S7I`: 14 rows x 10 cols
  - gene-symbol-like: col 1 (93% of 14)
  | Cohort | Gene | Type | Cut-off | Sensitivity% | 95% CI | Specificity% | 95% CI | Likelihood ratio | Youden index
  | Fu-iCCA | GRPC5A | Immunohistochemical marker | H-score >36.25 | 72.34 | 58.24% to 83.06% | 90.55 | 84.21% to 94.51% | 7.656 | 0.6288999999999999
  | Fu-iCCA | S100P | Immunohistochemical marker | H-score >127.5 | 71.43 | 57.59% to 82.15% | 88.89 | 82.21% to 93.27% | 6.429 | 0.6032
  | Fu-iCCA | CEACAM5 | Immunohistochemical marker | H-score >62.5 | 74.42 | 59.76% to 85.07% | 74.6 | 66.35% to 81.40% | 2.93 | 0.4901999999999998
  | Fu-iCCA | VTCN1 | Immunohistochemical marker | H-score >197.5 | 68.69 | 59.00% to 76.98% | 80.56 | 69.97% to 88.05% | 3.532 | 0.4925
  | Fu-iCCA | FXYD2 | Immunohistochemical marker | H-score >93.75 | 87.76 | 79.81% to 92.85% | 55.56 | 44.09% to 66.46% | 1.974 | 0.4331999999999999
  | Fu-iCCA | CHST9 | Immunohistochemical marker | H-score >76.25 | 65.66 | 55.88% to 74.27% | 75.34 | 64.36% to 83.80% | 2.663 | 0.41
  | Fu-iCCA | ANXA9 | Immunohistochemical marker | H-score >248.8 | 51 | 41.35% to 60.58% | 86.67 | 77.17% to 92.59% | 3.825 | 0.37670000000000015

### data/papers/lin2026/supp/mmc9.pdf (20772 kB)
- 50 pages
  - p1: 64 gene-like tokens; 
    Article
    Robust transcriptomic hallmarks targeting
    intratumor heterogeneity in intrahepatic
    cholangiocarcinoma
    Graphical abstract Authors
    YoupeiLin,LihuaPeng,HaichaoZhao,...,
    Targeting gene expression intratumor heterogeneity in iCCA QiangGao,KuiWu,JiaFan
    Gene A
  - p3: 41 gene-like tokens; (Table S2). Each tumor subregion was assigned a molecular sub- / scores at the gene and patient levels19(Table S1). At the patient subregions into 2–45 clusters in t
    ll
    OPEN ACCESS Article
    treatment.6 Addressing these complexities remains a critical weak (Figure S1E), implicating the tumor microenvironment as
    challenge for precision oncology in iCCA. a major contributor to gene expression ITH. Additionally, we
    High-throughput sequencing has enabled numerous tumor simulated patient-level gene expression ITH using varying
    classifications aimed at capturing intertumor heterogeneity. numbers of subregions per tumor to assess the impact of sam-
    Transcriptome profiling, which reflects both tumor and immune pling number on gene expression ITH. The results showed that
    cell states, offers insights into oncogenic signaling and the tumor the ITH scores plateaued after approximately four samples in
  - p4: 19 gene-like tokens; See also Figure S1and Table S1.
  - p5: 3 gene-like tokens; See also Figure S2and Table S2.
  - p6: 38 gene-like tokens; (Figure S2A; Table S2), and the clustering concordance scores genes located below the regression lin / To explore the underlying mechanisms, we analyzed tran- (Figure 3A; Table S3). The resulting gene se / lated risk scores for each tumor subregion (Table S2). Tumor gest that the LIHV gene set exhibits bo
  - p7: 33 gene-like tokens; See also Figure S3and Table S3. / group (SIII-3) (Table S4). Each subgroup exhibited significant dif- lymphatic metastasis, elevated l
  - p9: 52 gene-like tokens; (n = 27, 87.1%, p < 0.001; Figure S5A), indicating the specific in- in iCCA (Figure 4F; Table S4). I / Fu-iCCA cohort (p = 0.001 and 0.004, respectively; significance (p < 0.05; Figures 5A and S6A; Table / subgroups had higher frequencies of 3p21.3 (BAP1) copy-num- Table S5). In contrast, no consistent di / See also Figures S4and S5and Table S4.
    ll
    OPEN ACCESS Article
    observed in both the Fu-iCCA cohort (p = 0.017, Figure S4A) and tumor subregions classified as metabolic subgroups and one
    the OEP002768 cohort (p = 0.009; Figure S4E). In the GSE89749 as neurodegenerative subgroup (Figure 4E). This demonstrates
    cohort (n = 81), which included 38.3% of patients infected by that our classification system effectively minimizes the impact
    liver flukes (n = 31), we observed a significant enrichment of of ITH at the expression level. The defined subgroups also
    fluke-infected iCCA patients in the inflammatory subgroup partially correlated with previously identified molecular subtypes
    (n = 27, 87.1%, p < 0.001; Figure S5A), indicating the specific in- in iCCA (Figure 4F; Table S4). Inflammatory subgroup aligned
  - p11: 75 gene-like tokens; (Table S5), we classified the tumor samples from the scRNA- in vitro drug response data of iCCA orga / cohort (Figures S7A and S7B), indicating that tumor cells and fied (Table S6). Both ICCO5 and ICCO10 / See also Figures S6and S7and Table S5.
    ll
    OPEN ACCESS Article
    (Figure 5C), pointing to an immunosuppressive tumor microenvi- tively, and were selected for subsequent CXCL5 knockdown and
    ronment. The SIII subgroups (atypical, immune-silent, and overexpression experiments (Figures S7C and S7D). The effi-
    neurodegenerative) demonstrated higher expression of B7-H4 ciency of knockdown and overexpression was confirmed by
    (VTCN1) and B7-H3 (CD276), with the neurodegenerative sub- both qPCR and western blot, with siCXCL5-1 showing the
    group in particular showing pronounced upregulation of TIM-3 most significant knockdown and being chosen for further studies
    (HAVCR2) expression (Figure 5C). Furthermore, comparison (Figures 5H and S7E). Neutrophils were isolated from two healthy
  - p13: 106 gene-like tokens; groups based on the NTP method (Table S6). Prediction analysis biomarkers capable of distinguishing  / See also Figure S8and Table S6.
    ll
    OPEN ACCESS Article
    YM155 (p = 0.024), which aligns with their increased apoptosis bination (Figure S8D). Consistently, the anti-PD1-treated groups
    signaling (Figure 4D) and reduced expression of the apoptosis showed comparable tumor volumes and weights to the control
    suppressor gene BCL2 (Figure S8A). Additionally, inflammatory group, while Ganetespib and combination therapy significantly
    iCCA organoids were more sensitive to drugs targeting heat inhibited tumor growth (Figures 6H and S8E). These findings
    shock protein 90 (HSP90) and receptor tyrosine kinase (RTK) suggest that HSP90 inhibition effectively suppresses tumor pro-
    signaling (Figure 6A), consistent with alterations in transcrip- gression in inflammatory iCCA and may enhance the efficacy of
  - p15: 73 gene-like tokens; of >36.3 (Table S7), underscoring its potential for subtype iden- DISCUSSION / the optimal H-score cutoff of >62.5 (Table S7). findings not only enhance the biological understandi / iCCA (Table S7). Collectively, these findings reveal a panel of gemcitabine, making patients with in / See also Figures S9and S10and Table S7.
    ll
    OPEN ACCESS Article
    the highest diagnostic efficiency among specific immunohisto- with substantial potential to improve iCCA stratification in clinical
    chemical markers for inflammatory iCCA, with a sensitivity of practice.
    72.3% and specificity of 90.6% at the optimal H-score cutoff
    of >36.3 (Table S7), underscoring its potential for subtype iden- DISCUSSION
    tification in clinical settings. S100P, a well-established immuno-
    histochemical biomarker for large duct-type iCCA,54 exhibited Intertumor heterogeneity necessitates tailored treatment strate-
  - p16: 41 gene-like tokens; 
    ll
    Article OPEN ACCESS
    In metabolic iCCA, elevated expression of co-stimulatory mol- Materials availability
    ecules and immune checkpoints suggests a state of lymphocyte This study did not generate new, unique reagents.
    exhaustion. Whether this subgroup benefits from immune
    Data and code availability
    checkpoint inhibitors warrants further clinical investigation. In
    • Raw RNA sequencing data of three subcutaneous tumor tissues
  - p21: 79 gene-like tokens; 
    ll
    OPEN ACCESS Article
    STAR★METHODS
    KEY RESOURCES TABLE
    REAGENT or RESOURCE SOURCE IDENTIFIER
    Antibodies
    Rabbit polyclonal anti-CD66b Abcam Cat# ab197678; RRID: AB_3644234
    Rabbit monoclonal anti-CD68 Cell Signaling Technology Cat# 76437; RRID: AB_2799882
  - p22: 44 gene-like tokens; 
    ll
    Article OPEN ACCESS
    Continued
    REAGENT or RESOURCE SOURCE IDENTIFIER
    Chemicals, peptides, and recombinant proteins
    Recombinant human EGF Peprotech Cat# PHG0311
    Insulin-Transferrin-Selenium- Gibco Cat# 51300044
    Sodium Pyruvate
  - p25: 75 gene-like tokens; these PDPCs is summarized in Table S5. All human iCCA cell lines and the murine KTP cells were cultu
    ll
    OPEN ACCESS Article
    (n = 12),22OEP003191 (n = 12),42and GSE171443(n = 12).14For OEP002768, GSE89749, PRJCA007744 and GSE151530cohorts,
    only iCCA samples were included in the analysis, with extrahepatic cholangiocarcinoma (eCCA) and hepatocellular carcinoma (HCC)
    excluded.
    Animal experiments
    All animal experiments were approved by the Research Ethics Committee of Zhongshan Hospital and conducted in accordance with
    institutional guidelines (2024-073). Male C57BL/6 mice (6–8 weeks old) were maintained under specific pathogen-free (SPF) condi-
  - p26: 52 gene-like tokens; the average ITH score across all expressed genes in the Lin’s iCCA cohort (Table S1). To assess the  / score for each gene (Table S1). We applied the same method to the Fu-iCCA cohort, where the intertum / ologies (Table S2). In four independent iCCA cohorts with single-region sampling, tumor-infiltrating / tool36(Table S5).
    ll
    Article OPEN ACCESS
    17504044), 1:100 N2 supplement (Gibco, 17502048), 1.25 mM N-acetylcysteine (Sigma, A9165), 500 ng/mL R-spondin 1 (Sino Bio-
    logical, 11083-HNAS), 25 ng/mL Noggin (Sino Biological, 50688-M02H), 10 mM nicotinamide (Sigma, N0636), 10 nM Gastrin (Sigma,
    G9145), 50 ng/mL recombinant human EGF (Peprotech, AF-100-15-500), 100 ng/mL recombinant human FGF10 (Peprotech, 100-
    26-25), 10 μM forskolin (MCE, HY-15371), 10 μM Y27632 (Selleck, S1049), and 5 μM A83-01 (MCE, HY-10432). The culture medium
    was refreshed every 3–4 days and organoids were passaged with TrypLE Express (Gibco, 12604021) every 1–3 weeks, depending on
    the density.
  - p27: 54 gene-like tokens; 
    ll
    OPEN ACCESS Article
    models. Pathway enrichment analysis of LIHV genes (n = 1,341) was conducted using the clusterProfiler in R package.89Pathways
    with a q-value less than 0.05 were considered statistically significant.
    Copy-number variant analysis
    For temporal CNV analysis in the Lin’s iCCA cohort with multi-region sampling, FACETS76was used to detect CNV segments for each
    sample with default parameters and regions overlapping the centromeres were removed based on the whole-exome sequencing
    (WES) data. CNV segments were subsequently annotated using AnnotSV (v2.0).77 Gene-level copy-number gain, amplification,
  - p28: 42 gene-like tokens; fold change ≥1. DEGs overlapping with the LIHV gene set (Table S5) were subsequently selected for Ne / (NTP) analysis.41This approach was applied to classify corresponding subgroups in iCCA organoids (Ta / (Table S6), and scRNA-seq pseudo-bulk samples (Table S5). / applied (Table S6): T cell-inflamed score (T.cell.inflamed),43IFN-γ expanded immune signature (IFNγ.
    ll
    Article OPEN ACCESS
    annotations. Genes were classified into three categories: (1) highly expressed in tumor cells (log fold change ≥0.25 and adjusted
    2
    p-value <0.05); (2) lowly expressed in tumor cells (log fold change ≤-0.25 and adjusted p-value <0.05); (3) others (genes not meeting
    2
    either criterion).
    For analysis of gene expression within specific cell subsets, Ma’s scRNA-seq cohort was excluded due to a limited number of tu-
  - p29: 69 gene-like tokens; 
    ll
    OPEN ACCESS Article
    Cell transfection
    Small interfering RNAs (siRNAs) and a human CXCL5 expression plasmid were designed and synthesized by Genomeditech
    (Shanghai, China). Transient transfection was performed using Lipofectamine 3000 (Invitrogen, L3000001) according to the manu-
    facturer’s instructions. Cells were harvested 48 h post-transfection for downstream functional assays, including neutrophil migration,
    RNA extraction, and western blot analysis. A CXCL5-expressing lentiviral vector was constructed by Genomeditech, and the murine
    iCCA cell line KTP with stable CXCL5 overexpression was generated via lentiviral infection. Stable transfectants were validated by
  - p31: 43 gene-like tokens; 
    1.0
    Low ITH (n = 22)
    Cellular High ITH (n = 23)
    component 0.8
    Development 0.6
    DNA damage 0.4
    Immune 0.2 HR = 0.730
    P = 0.391
  - p37: 106 gene-like tokens; 
    )sraey(
    egA
    *
    )mc(
    retemaid
    romuT
    nedrub
    noitatum
  - p39: 87 gene-like tokens; 
    1.00
    Subgroup
    Age
    TNM stages 0.75
    Sex
    HBV infection
    HCV infection
    0.50 Fluke
  - p41: 117 gene-like tokens; 
    Fu-iCCA
    HRA004766
    OEP002768
    GSE89749
    Fu-iCCA
    HRA004766
    OEP002768
    GSE89749
  - p43: 56 gene-like tokens; 
    A B
    4
    2 3
    1 0
    2
    Percent expressed
    0 1
    25
  - p47: 81 gene-like tokens; 
    B
    Screening and validation of histochemical biomarkers for SI and SIII iCCA
    Significantly upregulated
    genes of SI samples Top 10 genes Distribution of
    in ≥3 cohorts (log 2 fold change) gene ( e n x = p r 6 e ) ssion
    (n = 176)
    LIHV gene set
    IHC validation H-score estimation ROC curve plot
  - p49: 53 gene-like tokens; 
    10-1
    )lm/gn(
    AEC
    mureS
    103
    102
    101
    100

