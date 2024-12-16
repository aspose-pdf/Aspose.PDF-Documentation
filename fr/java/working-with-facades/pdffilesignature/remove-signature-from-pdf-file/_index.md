---
title: Supprimer la signature du fichier PDF
type: docs
weight: 20
url: /fr/java/remove-signature-from-pdf/
description: Cette section explique comment travailler avec la signature dans un fichier PDF en utilisant la classe PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Supprimer la signature numérique du fichier PDF

Lorsqu'une signature a été ajoutée à un fichier PDF, il est possible de la supprimer. Vous pouvez supprimer soit une signature particulière, soit toutes les signatures d'un fichier. La méthode la plus rapide pour supprimer la signature supprime également le champ de signature, mais il est possible de simplement supprimer la signature, en gardant le champ de signature afin que le fichier puisse être signé à nouveau.

La méthode RemoveSignature de la classe [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) vous permet de supprimer une signature d'un fichier PDF.
 Cette méthode prend le nom de la signature comme entrée. Soit spécifiez directement le nom de la signature, pour supprimer toutes les signatures, obtenez les noms de signature en utilisant la méthode [getSignNames](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature#getSignNames--).

Le code suivant montre comment supprimer la signature numérique du fichier PDF.

```java
 public static void RemoveSignature() {
        // Créer un objet PdfFileSignature
        PdfFileSignature pdfSign = new PdfFileSignature();
        // Ouvrir le document PDF
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        // Obtenir la liste des noms de signature
        List<String> sigNames = pdfSign.getSignNames();
        // Supprimer toutes les signatures du fichier PDF
        for (int index = 0; index < sigNames.size(); index++) {
            System.out.println("Supprimé " + sigNames.get(index));
            pdfSign.removeSignature(sigNames.get(index));
        }
        // Enregistrer le fichier PDF mis à jour
        pdfSign.save(_dataDir + "RemoveSignature_out.pdf");
    }
```

### Supprimer la signature mais conserver le champ de signature

Comme indiqué ci-dessus, la méthode [removeSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature#removeSignature-java.lang.String-) de la classe [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) vous permet de supprimer les champs de signature des fichiers PDF. Lors de l'utilisation de cette méthode avec les versions antérieures à 9.3.0, à la fois la signature et le champ de signature sont supprimés. Certains développeurs souhaitent supprimer uniquement la signature et conserver le champ de signature afin qu'il puisse être réutilisé pour signer à nouveau le document. Pour conserver le champ de signature et ne supprimer que la signature, veuillez utiliser l'extrait de code suivant.

```java
 public static void RemoveSignatureButKeepField() {
        // Créer un objet PdfFileSignature
        PdfFileSignature pdfSign = new PdfFileSignature();

        // Ouvrir le document PDF
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");

        pdfSign.removeSignature("Signature1", false);

        // Enregistrer le fichier PDF mis à jour
        pdfSign.save(_dataDir + "RemoveSignature_out.pdf");
    }
```


L'exemple suivant montre comment supprimer toutes les signatures des champs.

```java
public static void RemoveSignatureButKeepField2() {
        // Créer un objet PdfFileSignature
        PdfFileSignature pdfSign = new PdfFileSignature();

        // Ouvrir le document PDF
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");

        List<String> sigNames = pdfSign.getSignNames();
        for (String sigName : sigNames) {
            pdfSign.removeSignature(sigName, false);
        }

        // Enregistrer le fichier PDF mis à jour
        pdfSign.save(_dataDir + "RemoveSignature_out.pdf");
    }
```