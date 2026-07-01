---
title: Convertir le PDF en texte
linktitle: Convertir le PDF en texte
type: docs
weight: 120
url: /fr/androidjava/convert-pdf-to-txt/
lastmod: "2026-07-01"
description: Avec Aspose.PDF for Android via Java, vous pouvez convertir l'intégralité d'un document PDF en fichier texte ou convertir uniquement une page PDF en fichier texte.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---


{{% alert color="primary" %}} 

Essayez en ligne. Vous pouvez vérifier la qualité de la conversion Aspose.PDF et voir les résultats en ligne à ce lien [products.aspose.app/pdf/conversion/pdf-to-txt](https://products.aspose.app/pdf/conversion/pdf-to-txt)

{{% /alert %}}

## Convertir la page PDF en fichier texte

Vous pouvez convertir un document PDF en fichier TXT avec Aspose.PDF for Android via Java. Vous devez utiliser la méthode Visit de [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) classe pour résoudre cette tâche.

Le fragment de code suivant explique comment extraire le texte des pages particulières.

```java
public void convertPDFPagesToTXT() {
        // Open document
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

        // Save the extracted text in text file
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

