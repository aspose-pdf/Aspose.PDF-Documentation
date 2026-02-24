---
title: Supprimer les tableaux d'un PDF existant
linktitle: Supprimer les tableaux
type: docs
weight: 50
url: /fr/python-net/removing-tables/
lastmod: "2025-09-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment supprimer les tableaux d'un PDF avec Python
Abstract: Cet article examine les fonctionnalités d'Aspose.PDF pour Python via .NET, en se concentrant spécifiquement sur la manipulation des tableaux dans les documents PDF. La bibliothèque permet aux utilisateurs d'insérer ou de créer des tableaux tant dans des fichiers PDF nouveaux que existants, ainsi que de manipuler ou de supprimer des tableaux de PDF existants. L'article présente la classe `TableAbsorber`, qui est essentielle pour identifier et interagir avec les tableaux dans un PDF. Une nouvelle méthode, `remove()`, a été ajoutée pour permettre la suppression des tableaux. Le document fournit deux extraits de code l'un montrant comment supprimer un tableau unique d'un PDF, et l'autre illustrant la suppression de plusieurs tableaux. Ces exemples mettent en évidence l'application pratique de la classe `TableAbsorber` pour supprimer des tableaux des documents PDF.
---

## Supprimer le tableau du document PDF

Aspose.PDF pour Python vous permet de supprimer un tableau d'un PDF. Il ouvre un PDF existant, détecte le premier tableau de la première page avec TableAbsorber, supprime ce tableau en utilisant le [remove_one_table](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods). Après avoir enregistré le PDF mis à jour dans un nouveau fichier.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    # Load existing PDF document
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit first page with absorber
    absorber.visit(document.pages[1])
    # Get first table on the page
    table = absorber.table_list[0]
    # Remove the table
    absorber.remove(table)
    # Save PDF
    document.save(path_outfile)
```

## Supprimer tous les tableaux du document PDF

Avec notre bibliothèque, vous pouvez supprimer tous les tableaux d'une page spécifique d'un PDF. Le code ouvre un PDF existant, détecte tous les tableaux de la deuxième page avec TableAbsorber, parcourt les tableaux détectés, supprime chacun d'eux, puis enregistre le PDF modifié dans un nouveau fichier. Cela est utile lorsque vous devez supprimer en masse les tableaux d'une page tout en conservant le reste du contenu du PDF intact.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    # Load existing PDF document
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit second page with absorber
    absorber.visit(document.pages[1])
    #  Loop through the copy of collection and removing tables
    tables = list(absorber.table_list)
    for table in tables:
        absorber.remove(table)

    # Save document
    document.save(path_outfile)
```


