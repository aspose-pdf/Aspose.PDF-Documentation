---
title: Supprimer Forms du PDF en Python
linktitle: Supprimer Forms
type: docs
weight: 70
url: /fr/python-net/remove-form/
description: Supprimer les objets form des pages PDF en utilisant Aspose.PDF for Python via .NET, y compris le nettoyage complet et la suppression ciblée.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Supprimer Forms du PDF avec Aspose.PDF for Python via .NET
Abstract: Cet article présente deux approches pour supprimer les éléments form des documents PDF en utilisant Aspose.PDF for Python via .NET. La première méthode efface tous les objets form d'une page sélectionnée, tandis que la deuxième méthode ne supprime que les ressources form Typewriter correspondantes. Ces exemples aident dans le nettoyage des form, la préparation de modèles et les flux de travail de normalisation des documents.
---

## Supprimer tous les Forms d'une page

Ce code supprime tous les objets de formulaire de la page spécifiée par `page_num` et enregistre le document mis à jour.

1. Chargez le document PDF.
1. Accéder aux ressources de la page.
1. Effacer les objets de formulaire.
1. Enregistrer le document mis à jour.

```python
import aspose.pdf as ap

def remove_all_forms(input_file_name, page_num, output_file_name):
    document = ap.Document(input_file_name)
    forms = document.pages[page_num].resources.forms
    forms.clear()
    document.save(output_file_name)
```

## Supprimer un type de formulaire spécifique

Le prochain exemple parcourt les objets de formulaire sur une page PDF donnée, identifie les annotations de formulaire de machine à écrire, les supprime, puis enregistre le PDF mis à jour en utilisant Aspose.PDF for Python via .NET.

1. Chargez le document PDF.
1. Accéder aux formulaires de la page.
1. Itérer sur les formulaires.
1. Vérifier les formulaires de machine à écrire.
1. Supprimer le formulaire correspondant.
1. Enregistrer le document mis à jour.

```python
import aspose.pdf as ap

def remove_specified_form(input_file_name, page_num, output_file_name):
    document = ap.Document(input_file_name)
    forms = document.pages[page_num].resources.forms
    for form in forms:
        if form.it == "Typewriter" and form.subtype == "Form":
            name = forms.get_form_name(form)
            forms.delete(name)
    document.save(output_file_name)
```

## Sujets associés

- [Créer AcroForm](/pdf/fr/python-net/create-form/)
- [Remplir AcroForm](/pdf/fr/python-net/fill-form/)
- [Modification d'AcroForm](/pdf/fr/python-net/modifying-form/)
- [Publication de formulaires](/pdf/fr/python-net/posting-form/)
