---
title: Convertir PDF en DOC 
linktitle: Convertir PDF en DOC
type: docs
weight: 70
url: fr/androidjava/convert-pdf-to-doc/
lastmod: "2021-06-05"
description: Convertissez le fichier PDF en format DOC facilement et avec un contrôle total avec Aspose.PDF pour Android via Java. Apprenez-en plus sur comment ajuster la conversion de fichier Microsoft Word Doc en PDF.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

L'une des fonctionnalités les plus populaires est la conversion de PDF en Microsoft Word DOC, ce qui rend le contenu facile à manipuler. Aspose.PDF pour Android via Java vous permet de convertir des fichiers PDF en DOC.

**Aspose.PDF pour Android via Java** peut créer des documents PDF à partir de zéro et est un excellent outil pour mettre à jour, éditer et manipuler des documents PDF existants.
 Une fonctionnalité importante est la capacité de convertir des pages et des documents PDF entiers en images. Une autre fonctionnalité populaire est la conversion de PDF en DOC Microsoft Word, ce qui rend le contenu facile à manipuler. (La plupart des utilisateurs ne peuvent pas éditer des documents PDF mais peuvent facilement travailler avec des tableaux, du texte et des images dans Microsoft Word.)

Pour simplifier les choses, Aspose.PDF pour Android via Java fournit un code en deux lignes pour transformer un fichier PDF source en un fichier DOC.

{{% alert color="primary" %}}

Essayez en ligne. Vous pouvez vérifier la qualité de conversion d'Aspose.PDF et voir les résultats en ligne à ce lien [products.aspose.app/pdf/conversion/pdf-to-doc](https://products.aspose.app/pdf/conversion/pdf-to-doc)

{{% /alert %}}

Le fragment de code suivant montre le processus de conversion d'un fichier PDF en format DOC.

```java
 public void convertPDFtoDOC() {
        // Ouvrir le document PDF source
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File docFileName = new File(fileStorage, "PDF-to-Word.doc");

        try {
            // Enregistrer le fichier au format document MS
            document.save(docFileName.toString(), SaveFormat.Doc);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```