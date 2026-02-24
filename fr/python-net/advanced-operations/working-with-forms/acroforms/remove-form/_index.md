---
title: Supprimer les formulaires du PDF en Python
linktitle: Supprimer les formulaires
type: docs
weight: 70
url: /fr/python-net/remove-form/
description: Supprimer le texte basé sur le sous-type/formulaire avec la bibliothèque Aspose.PDF pour Python via .NET. Supprimer tous les formulaires du PDF.
lastmod: "2025-09-17"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Supprimer les formulaires du PDF avec Aspose.PDF pour Python via .NET
Abstract: Ce document présente deux approches basées sur Python pour supprimer les éléments de formulaire des fichiers PDF à l'aide d'Aspose.PDF pour Python via .NET. La première méthode montre comment vider tous les objets de formulaire d'une page spécifique en accédant à son dictionnaire de ressources et en appelant la méthode clear() sur la collection de formulaires. La deuxième méthode offre une solution plus ciblée en parcourant les annotations de formulaire, en identifiant les formulaires de type machine à écrire, et en les supprimant sélectivement en fonction de leurs attributs. Les deux techniques se terminent par l'enregistrement du PDF mis à jour vers un chemin de sortie spécifié, offrant des options flexibles pour le nettoyage des formulaires et le raffinement des documents dans des flux de travail automatisés.
---

## Supprimer tous les formulaires du PDF

Ce code supprime tous les éléments de formulaire de la première page d'un document PDF, puis enregistre le document modifié vers le chemin de sortie spécifié.

1. Charger le document PDF.
1. Accéder aux ressources de la page.
1. Vider les objets de formulaire.
1. Enregistrer le document mis à jour.

```python

    import aspose.pdf as ap
    import os

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(data_dir, infile)
    path_outfile = os.path.join(data_dir, outfile)

    document = ap.Document(path_infile)
    forms = document.pages[page_num].resources.forms
    forms.clear()
    document.save(path_outfile)
```

## Supprimer le formulaire spécifié

L'exemple suivant parcourt les objets de formulaire d'une page PDF donnée, identifie les annotations de formulaire de type machine à écrire, les supprime, puis enregistre le PDF mis à jour en utilisant Aspose.PDF pour Python via .NET.

1. Charger le document PDF.
1. Accéder aux formulaires de la page.
1. Parcourir les formulaires.
1. Vérifier les formulaires de type machine à écrire.
1. Supprimer le formulaire correspondant.
1. Enregistrer le document mis à jour.

```python

    import aspose.pdf as ap
    import os

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    document = ap.Document(path_infile)
    forms = document.pages[page_num].resources.forms
    for form in forms:
        if (form.it == "Typewriter" and form.subtype == "Form"):
            name = forms.get_form_name(form)
            forms.delete(name)
    document.save(path_outfile)
```
