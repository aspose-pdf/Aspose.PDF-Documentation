---
title: Convertir PDF en texte 
linktitle: Convertir PDF en texte
type: docs
weight: 120
url: fr/androidjava/convert-pdf-to-txt/
lastmod: "2021-06-05"
description: Avec Aspose.PDF pour Android via Java, vous pouvez convertir un document PDF entier en un fichier texte ou convertir uniquement une page PDF en un fichier texte.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}} 

Essayez en ligne. Vous pouvez vérifier la qualité de la conversion Aspose.PDF et voir les résultats en ligne à ce lien [products.aspose.app/pdf/conversion/pdf-to-txt](https://products.aspose.app/pdf/conversion/pdf-to-txt)

{{% /alert %}}

## Convertir une page PDF en fichier texte

Vous pouvez convertir un document PDF en fichier TXT avec Aspose.PDF pour Android via Java. Vous devez utiliser la méthode Visit de la classe [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) pour résoudre cette tâche.

Le code suivant explique comment extraire les textes des pages particulières.

```java
public void convertPDFPagesToTXT() {
        // Ouvrir le document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        TextAbsorber ta = new TextAbsorber();
        int[] pages = new int[] { 1, 3, 4 };

        for (int page : pages) {
            ta.visit(document.getPages().get_Item(page));
        }
        File txtFileName = new File(fileStorage, "PDF-to-Text.txt");

        // Enregistrer le texte extrait dans un fichier texte
        BufferedWriter writer;
        try {
            writer = new BufferedWriter(new FileWriter(txtFileName));
            writer.write(ta.getText());
            writer.close();
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```