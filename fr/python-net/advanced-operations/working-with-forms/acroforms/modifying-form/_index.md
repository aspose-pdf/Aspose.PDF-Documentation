---
title: Modification d'AcroForm
linktitle: Modification d'AcroForm
type: docs
weight: 45
url: /fr/python-net/modifying-form/
description: Modification du formulaire dans votre fichier PDF avec la bibliothèque Aspose.PDF pour Python via .NET. Vous pouvez ajouter ou supprimer des champs dans un formulaire existant, obtenir et définir la limite des champs, etc.
lastmod: "2025-02-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gestion et personnalisation des champs de formulaire PDF
Abstract: Cette collection d'exemples présente diverses techniques de gestion et de personnalisation des champs de formulaire PDF à l'aide d'Aspose.PDF pour Python via .NET. Elle comprend des méthodes pour effacer le texte des champs de formulaire de type machine à écrire à l'aide de TextFragmentAbsorber, définir et récupérer les limites de caractères avec FormEditor, appliquer des polices personnalisées et du style aux champs de zone de texte, ainsi que supprimer des champs de formulaire spécifiques par leur nom. Ces opérations permettent aux développeurs de nettoyer, formater et adapter les formulaires PDF pour la redistribution, le branding ou la validation de données, en soutenant à la fois le raffinement esthétique et fonctionnel dans les flux de travail documentaires automatisés.
---

## Effacer le texte du formulaire

Cet exemple montre comment effacer le texte des champs de formulaire de type machine à écrire dans un PDF en utilisant Aspose.PDF pour Python via .NET. Il analyse la première page du PDF, identifie les formulaires de type machine à écrire, supprime leur contenu et enregistre le document mis à jour. Cette approche est utile pour réinitialiser ou nettoyer les champs de formulaire avant de redistribuer un PDF.

1. Chargez le document PDF d'entrée.
1. Accédez aux formulaires de la première page.
1. Parcourez chaque formulaire et vérifiez s'il s'agit d'un formulaire `Typewriter`.
1. Utilisez TextFragmentAbsorber pour trouver les fragments de texte dans le formulaire.
1. Effacez le texte de chaque fragment.
1. Enregistrez le PDF modifié dans le fichier de sortie.

```python

    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable

    dataDir = "path/to/your/data/dir/"
    path_infile = dataDir + infile
    path_outfile = dataDir + outfile
    document = ap.Document(path_infile)

    # Get the forms from the first page
    forms = document.pages[1].resources.forms

    for form in forms:
        # Check if the form is of type "Typewriter" and subtype "Form"
        if (form.it == "Typewriter" and form.subtype == "Form"):
            # Create a TextFragmentAbsorber to find text fragments
            absorber = ap.Text.TextFragmentAbsorber()
            absorber.visit(form)

            # Clear the text in each fragment
            for fragment in absorber.text_fragments:
                fragment.Text = ""

    # Save PDF document
    document.save(path_outfile)
```

## Obtenir ou définir la limite du champ

La méthode set_field_limit(field, limit) de la classe FormEditor vous permet de définir une limite de champ, le nombre maximal de caractères pouvant être saisis dans un champ.

```python

    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable

    # The path to the documents directory
    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    # Create FormEditor instance
    form = ap.facades.FormEditor()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Set field limit for "First Name"
    form.set_field_limit("First Name", 15)

    # Save PDF document
    form.save(path_outfile)
```

De même, Aspose.PDF possède une méthode qui récupère la limite du champ.

```python

    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable

    # The path to the documents directory
    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)

    document = ap.Document(path_infile)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        textBoxField = cast(ap.forms.TextBoxField, document.form[1])
        print(f"Limit: {textBoxField.max_len}")
```

## Définir une police personnalisée pour le champ du formulaire

Les champs de formulaire dans les fichiers PDF Adobe peuvent être configurés pour utiliser des polices par défaut spécifiques. Dans les premières versions d'Aspose.PDF, seules les 14 polices par défaut étaient prises en charge. Les versions ultérieures ont permis aux développeurs d'appliquer n'importe quelle police.

Ce code met à jour l'apparence d'un champ de zone de texte dans un formulaire PDF en définissant une police, une taille et une couleur personnalisées, puis enregistre le document modifié à l'aide d'Aspose.PDF pour Python via .NET.

L'extrait de code suivant montre comment définir la police par défaut pour les champs de formulaire PDF.

```python

    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    document = ap.Document(path_infile)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        textBoxField = cast(ap.forms.TextBoxField, document.form[1])
        font = ap.text.FontRepository.find_font("Calibri")
        textBoxField.default_appearance = ap.annotations.DefaultAppearance(font, 10, ap.Color.black.to_rgb())

    document.save(path_outfile)
```

## Supprimer des champs dans un formulaire existant

Ce code supprime un champ de formulaire spécifique (par son nom) d'un document PDF et enregistre le fichier mis à jour à l'aide d'Aspose.PDF pour Python via .NET.

1. Chargez le document PDF.
1. Supprimez un champ de formulaire par son nom.
1. Enregistrez le PDF mis à jour.

```python

    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    document = ap.Document(path_infile)
    # Delete a particular field by name
    document.form.delete("First Name")
    # Save PDF document
    document.save(path_outfile)
```

