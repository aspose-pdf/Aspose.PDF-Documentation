---
title: Extraire le tableau d'un document PDF
linktitle: Extraire le tableau
type: docs
weight: 20
url: /fr/python-net/extracting-table/
description: Aspose.PDF pour Python via .NET permet d'effectuer diverses manipulations des tableaux contenus dans votre document PDF.
lastmod: "2025-09-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment extraire un tableau d'un PDF avec Python
Abstract: Cet article décrit le processus d'extraction de tableaux à partir de documents PDF à l'aide de Python, en tirant spécifiquement parti de la bibliothèque Aspose.PDF pour Python via .NET. Il fournit un exemple de code montrant comment charger un document PDF, parcourir ses pages et utiliser la classe `TableAbsorber` pour identifier et extraire les données du tableau. Le code parcourt chaque tableau, chaque ligne et chaque cellule, collecte les fragments de texte et affiche le texte extrait. Cette méthode est présentée comme un outil puissant pour les tâches d'extraction et d'analyse de données impliquant des données tabulaires dans les PDFs.
---

## Extraire le tableau d'un PDF

L'extraction de tableaux à partir de PDFs à l'aide de Python peut être extrêmement utile pour l'extraction et l'analyse de données. Avec la bibliothèque Aspose.PDF pour Python via .NET, vous pouvez travailler efficacement avec les tableaux intégrés dans les documents PDF pour diverses tâches liées aux données.

Cet extrait de code ouvre un fichier PDF existant, analyse chaque page à la recherche de tableaux et extrait le contenu texte de leurs cellules. Il utilise le 'TableAbsorber' pour détecter les tableaux, puis parcourt les lignes et les cellules pour afficher le texte à l'intérieur.

1. Charge le PDF dans un objet ap.Document.
1. Parcourt les pages.
1. Crée un objet TableAbsorber.
1. Parcourt les tableaux.
1. Parcourt les lignes et les cellules.
1. Extrait et affiche le texte des cellules.

Cet exemple lit un PDF, trouve tous les tableaux et affiche le contenu de leurs cellules ligne par ligne.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.data_dir, infile)
    document = ap.Document(path_infile)
    for page in document.pages:
        absorber = ap.text.TableAbsorber()
        absorber.visit(page)
        for table in absorber.table_list:
            print("Table ----")
            for row in table.row_list:
                print("Row")
                for cell in row.cell_list:
                    text_fragment_collection = cell.text_fragments
                    for fragment in text_fragment_collection:
                        txt = ""
                        for seg in fragment.segments:
                            txt += seg.text
                        print(txt)
```


