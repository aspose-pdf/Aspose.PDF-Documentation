---
title: Travailler avec des formulaires en utilisant Python
linktitle: Formulaires dans un document PDF
type: docs
weight: 60
url: fr/python-java/forms/
lastmod: "2023-05-19"
description: Cette section contient des articles relatifs au travail avec des formulaires dans des documents PDF en utilisant l'API Python.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

Les formulaires sont des fichiers avec des zones pour que les utilisateurs sélectionnent ou remplissent des informations dans le but de collecter et de stocker des informations.

Les AcroForms sont des fichiers PDF qui contiennent des champs de formulaire. Les données peuvent être saisies dans ces champs (manuellement ou par un processus automatisé) par les utilisateurs finaux ou l'auteur du formulaire. En interne, les AcroForms sont des annotations ou des champs appliqués à un document PDF.

Cette section décrit une approche rapide et simple pour remplir un document PDF de manière programmatique à l'aide d'Aspose.PDF. La section discute également de la façon dont on pourrait utiliser Aspose.PDF pour Java pour découvrir et mapper les champs disponibles au sein d'un PDF existant avec des AcroForms.

**Notre bibliothèque Aspose.PDF pour Python via Java** vous permet de travailler avec succès, rapidement et facilement avec des formulaires dans des documents PDF.

- **AcroForms** - créer un formulaire, remplir un champ de formulaire, extraire des données du formulaire, modifier des champs dans votre PDF avec une bibliothèque Java.
- **XFA Forms** - remplir des champs XFA, convertir XFA, obtenir les propriétés des champs XFA.

## Les fonctions suivantes sont disponibles :

- exportation/importation fdf
- exportation/importation xfdf
- exportation/importation xml
- exportation/définition XfaData
- remplir des champs
- aplatir des champs
- déterminer les valeurs valides des boutons radio
- obtenir les noms, drapeaux, types, valeurs des champs
- renommer des champs

```python

from asposepdf import Api, Forms


# initialiser la licence
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

DIR_INPUT = baseDir+"testdata/forms/"
DIR_OUTPUT = baseDir+"testout/"

# exemple de remplissage de champ

input_pdf1 = DIR_INPUT + "Testing.pdf"
output_pdf = DIR_OUTPUT + "test5_1.pdf"

form = Forms.Form(sourceFileName=input_pdf1)
print(form.getFieldType("form1[0].Page1[0].fldBarCode1[0]"))
form.fillField("form1[0].Page1[0].fldBarCode1[0]", "54321")

form.save(output_pdf)
```