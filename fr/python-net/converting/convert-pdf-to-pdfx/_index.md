---
title: Convertir PDF aux formats PDF/x en Python
linktitle: Convertir PDF aux formats PDF/x
type: docs
weight: 120
url: /fr/python-net/convert-pdf-to-pdf_x/
lastmod: "2025-09-27"
description: Ce sujet vous montre comment convertir un PDF aux formats PDF/x en utilisant Aspose.PDF pour Python via .NET.
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Comment convertir PDF aux formats PDF/x
Abstract: L'article fournit un guide complet sur la conversion de PDF aux formats PDF/A, PDF/E et PDF/X en utilisant Aspose.PDF pour Python.
---

**Le format PDF vers PDF/x signifie la capacité de convertir un PDF en formats supplémentaires, à savoir PDF/A, PDF/E et PDF/X.**

## Convertir PDF en PDF/A

**Aspose.PDF for Python** vous permet de convertir un fichier PDF en un fichier PDF conforme au <abbr title="Portable Document Format / A">PDF/A</abbr>. Avant cela, le fichier doit être validé. Ce sujet explique comment.

{{% alert color="primary" %}}

Veuillez noter que nous nous conformons à Adobe Preflight pour la validation de la conformité PDF/A. Tous les outils du marché ont leur propre « représentation » de la conformité PDF/A. Veuillez consulter cet article sur les outils de validation PDF/A pour référence. Nous avons choisi les produits Adobe pour vérifier comment Aspose.PDF produit les fichiers PDF parce qu'Adobe est au centre de tout ce qui est lié au PDF.

{{% /alert %}}

Convertissez le fichier en utilisant la méthode Convert de la classe Document. Avant de convertir le PDF en fichier conforme PDF/A, validez le PDF à l'aide de la méthode Validate. Le résultat de la validation est stocké dans un fichier XML et ce résultat est également passé à la méthode Convert. Vous pouvez également spécifier l'action pour les éléments qui ne peuvent pas être convertis en utilisant l'énumération ConvertErrorAction.

{{% alert color="success" %}}
**Essayez de convertir PDF en PDF/A en ligne**

Aspose.PDF for Python vous propose une application en ligne gratuite ["PDF vers PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Conversion Aspose.PDF PDF vers PDF/A avec application gratuite](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

La méthode 'document.validate()' valide si un fichier PDF est conforme à la norme PDF/A-1B (une version standardisée par l'ISO du PDF conçue pour l'archivage à long terme). Les résultats de la validation sont enregistrés dans un fichier journal.

1. Chargez le document PDF en utilisant 'ap.Document'.
1. Appelez la méthode validate avec le niveau de conformité cible (ap.PdfFormat.PDF_A_1B).
1. Les résultats de la validation sont écrits dans le fichier journal spécifié.

```python

    path_infile = path.join(self.data_dir, infile)
    path_logfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.validate(path_logfile, ap.PdfFormat.PDF_A_1B)
```

### Convertir PDF en PDF/A-1B

Le fragment de code suivant montre comment convertir des fichiers PDF au format PDF/A-1B :

1. Chargez le document PDF en utilisant 'ap.Document'.
1. Appelez la méthode convert avec les paramètres suivants :
- Chemin du fichier journal - stocke les détails du processus de conversion et des vérifications de conformité.
- Format cible - 'ap.PdfFormat.PDF_A_1B' (norme d'archivage).
- Action d'erreur - 'ap.ConvertErrorAction.DELETE' — supprime automatiquement les éléments qui empêchent la conformité.
1. Enregistrez le fichier PDF/A conforme dans le chemin de sortie.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.convert(
        self.data_dir + "pdf_pdfa.log",
        ap.PdfFormat.PDF_A_1B,
        ap.ConvertErrorAction.DELETE,
    )
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

### Convertir PDF en PDF 2.0 et PDF/A-4

Cet exemple montre comment convertir un document PDF en formats standardisés plus récents : PDF 2.0 et PDF/A-4.
Les deux conversions aident à garantir la conformité aux spécifications modernes et aux exigences d'archivage.

1. Chargez le document d'entrée en utilisant ap.Document.
1. Effectuez la première conversion en PDF 2.0 en appelant document.convert avec :
- Chemin du fichier journal pour les détails de conversion.
- Format cible - 'ap.PdfFormat.V_2_0'.
- Action d'erreur - 'ap.ConvertErrorAction.DELETE' pour supprimer les éléments non conformes.
1. Effectuez une seconde conversion en PDF/A-4 en utilisant la même méthode, en veillant à ce que le fichier soit également conforme aux standards d'archivage.
1. Enregistrez le document résultant dans le chemin de sortie spécifié.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    document = ap.Document(path_infile)
    document.convert(path_logfile, ap.PdfFormat.V_2_0, ap.ConvertErrorAction.DELETE)

    document.convert(path_logfile, ap.PdfFormat.PDF_A_4, ap.ConvertErrorAction.DELETE)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

### Convertir PDF en PDF/A-3A avec fichiers intégrés

Le fragment de code suivant montre comment intégrer des fichiers externes dans un PDF puis convertir le PDF au format PDF/A-3A, qui prend en charge les pièces jointes et convient à l'archivage à long terme avec du contenu intégré.

1. Chargez le PDF d'entrée en utilisant 'ap.Document'.
1. Créez un objet 'FileSpecification' pointant vers le fichier à intégrer (par ex., "aspose-logo.jpg") avec une description.
1. Ajoutez la spécification de fichier à la collection 'embedded_files' du PDF.
1. Convertissez le document en PDF/A-3A en utilisant 'document.convert', en spécifiant :
- Chemin du fichier journal.
- Format cible - 'ap.PdfFormat.PDF_A_3A'.
- Action en cas d'erreur - 'ap.ConvertErrorAction.DELETE' pour supprimer les éléments non conformes.
1. Enregistrez le PDF converti vers le chemin de sortie.
1. Affichez un message de confirmation.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    document = ap.Document(path_infile)

    fileSpecification = ap.FileSpecification(self.data_dir + "aspose-logo.jpg", "Large Image file")
    document.embedded_files.add(fileSpecification)
    document.convert(path_logfile, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

### Convertir un PDF en PDF/A-1B avec substitution de police

Cette fonction convertit un PDF au format PDF/A-1B tout en gérant les polices manquantes en les substituant par des polices disponibles. Cela garantit que le PDF converti reste visuellement cohérent et conforme aux normes d'archivage.

1. Chargez le PDF en utilisant 'ap.Document'.
1. Convertissez le PDF en PDF/A-1B en utilisant 'document.convert', en spécifiant :
- Chemin du fichier journal.
- Format cible - 'ap.PdfFormat.PDF_A_1B'.
- Action en cas d'erreur - 'ap.ConvertErrorAction.DELETE' pour supprimer les éléments non conformes.
1. Enregistrez le PDF converti vers le chemin de sortie.
1. Affichez un message de confirmation.

```python

    from os import path
    import aspose.pdf as ap 

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    try:
        ap.text.FontRepository.find_font("AgencyFB")

    except ap.FontNotFoundException:
        font_substitution = ap.text.SimpleFontSubstitution("AgencyFB", "Arial")
        ap.text.FontRepository.Substitutions.append(font_substitution)

    document = ap.Document(path_infile)
    document.convert(path_logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

### Convertir un PDF en PDF/A-1B avec étiquetage automatique

Cette fonction convertit un document PDF au format PDF/A-1B tout en étiquetant automatiquement le contenu pour l'accessibilité et la cohérence structurelle. L'étiquetage automatique améliore l'utilisabilité du document pour les lecteurs d'écran et assure une structure sémantique appropriée.

1. Chargez le PDF en utilisant 'ap.Document'.
1. Créez 'PdfFormatConversionOptions' en spécifiant :
- Chemin du fichier journal.
- Format cible - 'ap.PdfFormat.PDF_A_1B'.
- Action en cas d'erreur - 'ap.ConvertErrorAction.DELETE' pour supprimer les éléments non conformes.
1. Configurez 'AutoTaggingSettings' :
- Activez 'enable_auto_tagging = True'.
- Définissez 'heading_recognition_strategy = AUTO' pour détecter automatiquement les titres.
1. Assignez les paramètres d'étiquetage automatique aux options de conversion.
1. Convertissez le PDF en utilisant 'document.convert(options)'.
1. Enregistrez le PDF converti vers le chemin de sortie.
1. Affichez un message de confirmation.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    document = ap.Document(path_infile)
    options =  ap.PdfFormatConversionOptions(path_logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE)

    auto_tagging_settings = ap.AutoTaggingSettings()
    auto_tagging_settings.enable_auto_tagging = True

    auto_tagging_settings.heading_recognition_strategy = ap.HeadingRecognitionStrategy.AUTO

    options.auto_tagging_settings = auto_tagging_settings
    document.convert(options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Convertir un PDF en PDF/E

Cet extrait vérifie si un document PDF est conforme à la norme PDF/E-1, qui est une norme ISO adaptée aux documents d'ingénierie et techniques. Les résultats de la validation sont enregistrés dans un fichier journal.

1. Chargez le document PDF en utilisant 'ap.Document'.
1. Appelez la méthode validate en spécifiant :
- Chemin du fichier journal pour stocker les résultats de validation.
- Format cible - 'ap.PdfFormat.PDF_E_1'.
1. Les résultats de validation sont enregistrés dans le fichier journal pour examen.

```python

    path_infile = path.join(self.data_dir, infile)
    path_logfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.validate(path_logfile, ap.PdfFormat.PDF_E_1)
```

L'exemple suivant montre comment convertir un PDF au format PDF/E-1, qui est une norme ISO adaptée à la documentation d'ingénierie et technique. Ce format préserve la mise en page précise, les graphiques et les métadonnées nécessaires aux flux de travail d'ingénierie.

1. Chargez le PDF source en utilisant 'ap.Document'.
1. Créez 'PdfFormatConversionOptions' en spécifiant :
- Chemin du fichier journal pour suivre les problèmes de conversion.
- Format cible - 'ap.PdfFormat.PDF_E_1'.
- Action en cas d'erreur - 'ap.ConvertErrorAction.DELETE' pour supprimer les éléments non conformes.
1. Convertissez le PDF en utilisant 'document.convert(options)'.
1. Enregistrez le PDF converti vers le chemin de sortie spécifié.
1. Affichez un message de confirmation.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    document = ap.Document(path_infile)
    options =  ap.PdfFormatConversionOptions(path_logfile, ap.PdfFormat.PDF_E_1, ap.ConvertErrorAction.DELETE)

    document.convert(options)

    # Save PDF document
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Convertir un PDF en PDF/X

Le fragment de code suivant convertit un document PDF au format PDF/X-4, qui est une norme ISO couramment utilisée dans l'industrie de l'impression et de l'édition. PDF/X-4 garantit la précision des couleurs, maintient la transparence et intègre des profils ICC pour une sortie cohérente sur tous les appareils.

1. Chargez le PDF source en utilisant 'ap.Document'.
1. Créez 'PdfFormatConversionOptions' en spécifiant :
- Chemin du fichier journal.
- Format cible - 'ap.PdfFormat.PDF_X_4'.
- Action d'erreur - 'ap.ConvertErrorAction.DELETE' pour supprimer les éléments non conformes.
1. Fournissez le **fichier de profil ICC** pour la gestion des couleurs via 'icc_profile_file_name'.
1. Spécifiez un **OutputIntent** avec un identifiant de condition (par ex., "FOGRA39") pour les exigences d'impression.
1. Convertissez le PDF en utilisant 'document.convert()'.
1. Enregistrez le PDF converti à l'emplacement de sortie spécifié.
1. Affichez un message de confirmation.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    document = ap.Document(path_infile)
    options =  ap.PdfFormatConversionOptions(path_logfile, ap.PdfFormat.PDF_X_4, ap.ConvertErrorAction.DELETE)

    # Provide the name of the external ICC profile file (optional)
    options.icc_profile_file_name = path.join(self.data_dir,"ISOcoated_v2_eci.icc")
    # Provide an output condition identifier and other necessary OutputIntent properties (optional)
    options.output_intent = ap.OutputIntent("FOGRA39")

    document.convert(options)

    # Save PDF document
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```
