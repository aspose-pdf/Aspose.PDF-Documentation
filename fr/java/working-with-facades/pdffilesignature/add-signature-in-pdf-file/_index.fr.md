---
title: Ajouter une Signature dans un Fichier PDF
type: docs
weight: 10
url: /java/add-signature-in-pdf/
description: Cette section explique comment travailler avec la Signature dans un fichier PDF en utilisant la classe PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Ajouter une Signature Numérique dans un Fichier PDF (facades)

La classe [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) vous permet d'ajouter une signature dans un fichier PDF. Vous devez créer un objet de la classe [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) en utilisant des fichiers PDF d'entrée et de sortie. Vous devez également créer un objet Rectangle à l'endroit où vous souhaitez ajouter la signature et, afin de définir l'apparence, vous pouvez spécifier une image en utilisant la propriété setSignatureAppearance de l'objet [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature).

Aspose.Pdf.Facades fournit également différents types de signatures comme PKCS#1, PKCS#7, et PKCS#7Detached.
 Afin de créer une signature d'un type spécifique, vous devez créer un objet de la classe particulière comme PKCS1, PKCS7 ou PKCS7Detached en utilisant le fichier de certificat et le mot de passe.

Une fois l'objet d'un type de signature particulier créé, vous pouvez utiliser la méthode sign de la classe [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) pour signer le PDF et passer l'objet de signature particulier à cette classe. Vous pouvez également spécifier d'autres attributs pour cette méthode. Enfin, vous devez enregistrer le PDF signé en utilisant la méthode save de la classe [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature). Le code suivant montre comment ajouter une signature dans un fichier PDF.

```java
public static void AddPdfFileSignature() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // Créer un rectangle pour l'emplacement de la signature
        java.awt.Rectangle rect = new java.awt.Rectangle(10, 10, 300, 50);
        // Définir l'apparence de la signature
        pdfSign.setSignatureAppearance(_dataDir + "aspose-logo.png");

        // Créer l'un des trois types de signature
        PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(1, "Je suis l'auteur du document", "test01@aspose-pdf-demo.local", "Aspose Pdf Demo, Australie", true, rect,
                signature);
        // Enregistrer le fichier PDF de sortie
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```

Le code suivant nous montre la capacité de signer un document avec deux signatures. Dans notre exemple, nous mettons la première signature sur la première page, et la seconde sur la deuxième page. Vous pouvez spécifier les pages dont vous avez besoin.

```java
    public static void AddTwoSignature() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        // Signer avec la 1ère signature

        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // Créer un rectangle pour l'emplacement de la 1ère signature
        java.awt.Rectangle rect1 = new java.awt.Rectangle(10, 10, 300, 50);

        // Créer un objet pour la 1ère signature
        PKCS1 signature1 = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(1, "Je suis l'auteur du document", "test@aspose-pdf-demo.local", "Aspose Pdf Demo, Australie", true, rect1,
                signature1);
        pdfSign.save(_dataDir + "DigitallySign.pdf");

        // Signer avec la 2ème signature

        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");

        // Créer un rectangle pour l'emplacement de la 2ème signature
        java.awt.Rectangle rect2 = new java.awt.Rectangle(10, 10, 300, 50);

        // Créer un objet pour la 2ème signature
        PKCS1 signature2 = new PKCS1(_dataDir + "test02.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(2, "Je suis le réviseur du document", "test02@aspose-pdf-demo.local", "Aspose Pdf Demo, Australie", true,
                rect2, signature2);

        // Enregistrer le fichier PDF de sortie
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```


Pour un document avec des formulaires ou acroformes qui doivent être signés, voir l'exemple suivant. Vous devez créer un objet de la classe [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) en utilisant les fichiers PDF d'entrée et de sortie. Utilisez bindPdf pour la liaison. Créez une signature avec la capacité d'ajouter les propriétés requises. Dans notre exemple, elles sont 'Reason' et 'CustomAppearance'.

```java
  public static void AddPdfFileSignatureField() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample02.pdf");

        // Créez n'importe lequel des trois types de signature
        PKCS1 signature = new PKCS1(_dataDir + "test02.pfx", "Aspose2021");
        signature.setReason("Signer en tant qu'auteur");

        SignatureCustomAppearance sca = new SignatureCustomAppearance();
        signature.setCustomAppearance(sca);
        sca.setFontSize(6);
        sca.setFontFamilyName("Calibri");

        // PKCS#1
        pdfSign.sign("Signature1", signature);
        // Enregistrez le fichier PDF de sortie
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```


Si notre document a deux champs, l'algorithme pour le signer est similaire au premier exemple.

```java
   public static void AddPdfFileSignatureField2() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample03.pdf");

        // Créer l'un des trois types de signature
        PKCS1 signature1 = new PKCS1(_dataDir + "test01.pfx", "Aspose2021");
        SignatureCustomAppearance sca = new SignatureCustomAppearance();
        signature1.setCustomAppearance(sca);
        sca.setFontSize(6);
        sca.setFontFamilyName("Calibri");

        signature1.setReason("Signer en tant qu'auteur"); // PKCS#1
        pdfSign.sign("Signature1", signature1);

        // Enregistrer le fichier PDF de sortie
        pdfSign.save(_dataDir + "DigitallySign.pdf");

        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");

        // Créer l'un des trois types de signature
        PKCS1 signature2 = new PKCS1(_dataDir + "test02.pfx", "Aspose2021");
        signature2.setReason("Signer en tant que réviseur"); // PKCS#1
        signature2.setCustomAppearance(sca);
        pdfSign.sign("Signature2", signature2);
        // Enregistrer le fichier PDF de sortie
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```