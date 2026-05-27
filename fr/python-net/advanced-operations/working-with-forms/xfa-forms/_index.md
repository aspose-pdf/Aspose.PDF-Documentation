---
title: Travailler avec les formulaires XFA
linktitle: Formulaires XFA
type: docs
weight: 20
url: /fr/python-net/xfa-forms/
description: Aspose.PDF for Python via .NET API vous permet de travailler avec les champs XFA et XFA AcroForm dans un document PDF.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Convertir XFA en AcroForm

{{% alert color="primary" %}}

Essayer en ligne
Vous pouvez vérifier la qualité de la conversion Aspose.PDF et voir les résultats en ligne à ce lien : [products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

Le snippet de code suivant montre comment convertir un formulaire XFA dynamique (XML Forms Architecture) en un AcroForm standard.

**Les étapes clés comprennent :**

1. Chargement du document PDF d'entrée.
1. Modification du type de formulaire en STANDARD.
1. Enregistrement du PDF converti dans un nouveau fichier.

Cette conversion permet une meilleure compatibilité et une gestion cohérente des formulaires entre différents lecteurs et applications PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def convert_dynamic_xfa_to_acroform(infile: str, outfile: str):
    """Convert dynamic XFA form to standard AcroForm."""
    with ap.Document(infile) as document:
        document.form.type = ap.forms.FormType.STANDARD
        document.save(outfile)
```

## Utilisation de IgnoreNeedsRendering

Cet exemple montre comment convertir un formulaire dynamique XFA en AcroForm standard à l'aide d'Aspose.PDF for Python. Le code vérifie si le PDF d'entrée contient un formulaire XFA et surcharge le rendu si nécessaire. Il définit ensuite le type de formulaire sur STANDARD et enregistre le PDF mis à jour.

```python
import aspose.pdf as ap
import sys
from os import path

def convert_xfa_form_with_ignore_needs_rendering(infile: str, outfile: str):
    """Convert XFA form ignoring needs rendering flag."""
    with ap.Document(infile) as document:
        if not document.form.needs_rendering and document.form.has_xfa:
            document.form.ignore_needs_rendering = True
        document.form.type = ap.forms.FormType.STANDARD
        document.save(outfile)
```
