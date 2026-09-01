---
title: Remplir AcroForm - Remplir un formulaire PDF en utilisant Java
linktitle: Remplir AcroForm
type: docs
weight: 20
url: /java/fill-form/
description: Remplissez les champs AcroForm dans un document PDF à l'aide d'Aspose.PDF pour Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remplissez les champs AcroForm dans les fichiers PDF avec Java
Abstract: Cet article explique comment remplir les champs AcroForm à l'aide d'Aspose.PDF pour Java. L'exemple charge un PDF via la façade du formulaire, fait correspondre les noms de champs avec une carte de valeurs, met à jour les champs correspondants et enregistre le document complété.
---
La façade `Form` peut être utilisée pour automatiser le remplissage des champs dans un AcroForm existant.


## 
Remplissez les champs AcroForm avec de nouvelles valeurs


1. 
Ouvrez le document de formulaire PDF avec la façade [Form] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/).

1. 
Parcourez les champs du formulaire et mettez à jour les entrées correspondantes avec les valeurs fournies.

1. 
Enregistrez le document PDF mis à jour.

```java
public static void fillForm(Path inputFile, Path outputFile) {
    Map<String, String> newFieldValues = Map.of(
            "First Name", "Alexander_New",
            "Last Name", "Greenfield_New",
            "City", "Yellowtown_New",
            "Country", "Redland_New");

    Form form = new Form(inputFile.toString());
    try {
        for (String fieldName : form.getFieldNames()) {
            if (newFieldValues.containsKey(fieldName)) {
                form.fillField(fieldName, newFieldValues.get(fieldName));
            }
        }
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
