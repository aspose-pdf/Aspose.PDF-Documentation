---
title: Convertir PDF en DOC
linktitle: Convertir PDF en DOC
type: docs
weight: 70
url: /fr/androidjava/convert-pdf-to-doc/
lastmod: "2026-07-01"
description: Convertir un fichier PDF au format DOC avec facilité et plein contrôle grâce à Aspose.PDF for Android via Java. En savoir plus sur la façon d'optimiser la conversion de fichier Microsoft Word Doc en PDF.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

L'une des fonctionnalités les plus populaires est la conversion PDF vers Microsoft Word DOC, ce qui facilite la manipulation du contenu. Aspose.PDF for Android via Java vous permet de convertir des fichiers PDF en DOC.

**Aspose.PDF for Android via Java** peut créer des documents PDF à partir de zéro et constitue une excellente boîte à outils pour mettre à jour, éditer et manipuler des documents PDF existants. Une fonctionnalité importante est la capacité de convertir des pages et des documents PDF entiers en images. Une autre fonctionnalité populaire est la conversion PDF vers Microsoft Word DOC, ce qui facilite la manipulation du contenu. (La plupart des utilisateurs ne peuvent pas modifier les documents PDF mais peuvent travailler facilement avec des tableaux, du texte et des images dans Microsoft Word.)

Pour simplifier et rendre les choses compréhensibles, Aspose.PDF for Android via Java fournit un code en deux lignes pour transformer un fichier PDF source en fichier DOC.

{{% alert color="primary" %}}

Essayez en ligne. Vous pouvez vérifier la qualité de la conversion Aspose.PDF et voir les résultats en ligne à ce lien [products.aspose.app/pdf/conversion/pdf-to-doc](https://products.aspose.app/pdf/conversion/pdf-to-doc)

{{% /alert %}}

L'extrait de code suivant montre le processus de conversion d'un fichier PDF en format DOC.

```java
 public void convertPDFtoDOC() {
        // Open the source PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File docFileName = new File(fileStorage, "PDF-to-Word.doc");

        try {
            // Save the file into MS document format
            document.save(docFileName.toString(), SaveFormat.Doc);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


