---
title: Convertir PDF/x en formats PDF en Python
linktitle: Convertir PDF/x en formats PDF
type: docs
weight: 120
url: /fr/python-net/convert-pdf_x-to-pdf/
lastmod: "2025-09-27"
description: Ce sujet vous montre comment convertir les formats PDF/x en PDF en utilisant Aspose.PDF pour Python via .NET.
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Comment convertir PDF/x en formats PDF
Abstract: L'article fournit un guide complet sur la conversion de PDF/UA et de PDF/A en fichier PDF à l'aide d'Aspose.PDF pour Python.
---

**Le format PDF/x en PDF signifie la capacité de convertir PDF/UA et PDF/A en fichier PDF.**

## Convertir PDF/A en PDF

1. Chargez le document PDF en utilisant 'ap.Document'.
1. Appelez 'remove_pdfa_compliance()' pour supprimer tous les paramètres de conformité et métadonnées liés à PDF/A.
1. Enregistrez le PDF résultant vers le chemin de sortie.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.remove_pdfa_compliance()
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## Suppression de la conformité PDF/UA

Cette fonction montre un processus de conversion en deux étapes : d'abord la suppression de la conformité PDF/UA (Accessibilité Universelle), puis la conversion du PDF résultant au format PDF/A-1B avec un balisage automatique pour l'accessibilité et la structure sémantique.

1. Chargez le document PDF en utilisant 'ap.Document()'.
1. Appelez 'document.remove_pdfa_compliance()' pour supprimer toutes les restrictions ou paramètres de conformité PDF/A.
1. Enregistrez le PDF modifié dans 'path_outfile'.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.remove_pdfa_compliance()
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```
