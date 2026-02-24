---
title: Travailler avec les formulaires XFA
linktitle: Formulaires XFA
type: docs
weight: 20
url: /fr/python-net/xfa-forms/
description: Aspose.PDF pour Python via l'API .NET vous permet de travailler avec les champs XFA et XFA Acroform dans un document PDF.
lastmod: "2025-02-17"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## Convertir XFA en Acroform

{{% alert color="primary" %}}

Essayer en ligne
Vous pouvez vérifier la qualité de la conversion Aspose.PDF et voir les résultats en ligne à ce lien : [products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

Le fragment de code suivant montre comment convertir un formulaire XFA dynamique (XML Forms Architecture) en un AcroForm standard.

**Les étapes clés comprennent :**

1. Chargement du document PDF d'entrée.
1. Changement du type de formulaire en STANDARD.
1. Enregistrement du PDF converti dans un nouveau fichier.

Cette conversion permet une meilleure compatibilité et une gestion cohérente des formulaires à travers différents lecteurs PDF et applications.

```python

    import aspose.pdf as ap


    path_infile = self.data_dir + "DynamicXFAToAcroForm.pdf.pdf"
    path_outfile = self.data_dir + "StandardAcroForm_out.pdf"

    # Load dynamic XFA form
    with ap.Document(path_infile) as document:
        # Set the form fields type as standard AcroForm
        document.form.type = ap.forms.FormType.STANDARD
        # Save PDF document
        document.save(path_outfile)
```

## Utilisation de IgnoreNeedsRendering

Cet exemple montre comment convertir un formulaire XFA dynamique en un AcroForm standard en utilisant Aspose.PDF pour Python. Le code vérifie si le PDF d'entrée contient un formulaire XFA et surcharge le rendu si nécessaire. Il définit ensuite le type de formulaire sur STANDARD et enregistre le PDF mis à jour.

```python

    import aspose.pdf as ap


    path_infile = self.data_dir + "DynamicXFAToAcroForm.pdf.pdf"
    path_outfile = self.data_dir + "StandardAcroForm_out.pdf"

    # Load dynamic XFA form
    with ap.Document(path_infile) as document:
        # check if XFA is present & if rendering should be overwritten
        if not document.form.needs_rendering and document.form.has_xfa:
            document.form.ignore_needs_rendering = True
        # Set the form fields type as standard AcroForm
        document.form.type = ap.forms.FormType.STANDARD
        # Save the resultant PDF
        document.save(path_outfile)
```

