---
title: Travailler avec la Signature dans un Fichier PDF
type: docs
weight: 40
url: /fr/java/working-with-signature-in-a-pdf-file/
description: Cette section explique comment travailler avec la Signature dans un fichier PDF en utilisant la classe PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Comment Extraire les Informations de Signature

Aspose.PDF pour Java prend en charge la fonctionnalité de signer numériquement des fichiers PDF en utilisant la classe PdfFileSignature. Actuellement, il est également possible de déterminer la validité d'un certificat mais nous ne pouvons pas extraire le certificat entier. Les informations qui peuvent être extraites sont la clé publique, l'empreinte digitale et l'émetteur, etc.

Pour extraire les informations de signature, nous avons introduit la méthode extractCertificate(..) dans la classe PdfFileSignature. Veuillez consulter le code ci-dessous qui démontre les étapes pour extraire le certificat de l'objet PdfFileSignature :

```java
public static void ExtractSignatureInfo() {
        String input = _dataDir + "DigitallySign.pdf";
        String certificateFileName = "extracted_cert.pfx";
        PdfFileSignature pdfFileSignature = new PdfFileSignature();
        pdfFileSignature.bindPdf(input);
        List<String> sigNames = pdfFileSignature.getSignNames();

        if (sigNames.size() > 0) {
            String sigName = sigNames.get(0);
            if (sigName != "") {
                InputStream cerStream = pdfFileSignature.extractCertificate(sigName);
                if (cerStream != null) {
                    FileOutputStream fs;
                    try {
                        fs = new FileOutputStream(_dataDir + certificateFileName);
                        cerStream.transferTo(fs);
                    } catch (IOException e) {
                        e.printStackTrace();
                    }

                }
            }
        }
    }
```


## Extraction d'image depuis le champ de signature (PdfFileSignature)

Aspose.PDF pour Java prend en charge la fonctionnalité de signer numériquement les fichiers PDF en utilisant la classe PdfFileSignature et lors de la signature du document, vous pouvez également définir une image pour SignatureAppearance. Désormais, cette API offre également la possibilité d'extraire les informations de signature ainsi que l'image associée au champ de signature.

Afin d'extraire les informations de signature, nous avons introduit la méthode [extractImage(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature#extractImage-java.lang.String-) dans la classe PdfFileSignature. Veuillez consulter le snippet de code suivant qui démontre les étapes pour extraire une image à partir de l'objet PdfFileSignature :

```java
public static void ExtractSignatureImage() {
    PdfFileSignature signature = new PdfFileSignature();
    signature.bindPdf(_dataDir + "DigitallySign.pdf");
    if (signature.containsSignature()) {
        for (String sigName : signature.getSignNames()) {
            String outFile = _dataDir + sigName + "_ExtractImages_out.jpg";
            InputStream imageStream = signature.extractImage(sigName);
            if (imageStream != null) {
                FileOutputStream fs;
                try {
                    fs = new FileOutputStream(outFile);
                    imageStream.transferTo(fs);
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
```


## Supprimer l'emplacement et la raison

La fonctionnalité Aspose.PDF permet une configuration flexible pour l'instance de signature numérique. La classe [PdfFileSignature ](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) fournit la capacité de signer un fichier PDF. L'implémentation de la méthode Sign permet de signer le PDF et de passer l'objet de signature particulier à cette classe. La méthode Sign contient un ensemble d'attributs pour la personnalisation de la signature numérique de sortie. Dans le cas où vous avez besoin de supprimer certains attributs de texte de la signature résultante, vous pouvez les laisser vides. Le code suivant montre comment supprimer les deux lignes Emplacement et Raison du bloc de signature :

```java
public static void SupressLocationReason() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // Créer un rectangle pour l'emplacement de la signature
        java.awt.Rectangle rect = new java.awt.Rectangle(10, 10, 300, 50);

        // Définir l'apparence de la signature
        pdfSign.setSignatureAppearance(_dataDir + "aspose-logo.png");

        // Créer l'un des trois types de signature
        PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(1, "", "test01@aspose-pdf-demo.local", "", true, rect, signature);
        // Enregistrer le fichier PDF de sortie
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```


## Fonctionnalités de Personnalisation pour Signature Numérique

Aspose.PDF pour Java permet des fonctionnalités de personnalisation pour une signature numérique. La méthode Sign de la classe SignatureCustomAppearance est implémentée avec 6 surcharges pour votre utilisation confortable. Par exemple, vous pouvez configurer la signature de résultat uniquement par l'instance de la classe SignatureCustomAppearance et les valeurs de ses propriétés. Le code suivant montre comment masquer la légende "Signé numériquement par" de la signature numérique de sortie de votre PDF.

```java
    public static void CustomizationFeaturesForDigitalSign() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // Créez un rectangle pour l'emplacement de la signature
        java.awt.Rectangle rect = new java.awt.Rectangle(10, 10, 300, 50);

        // Créez l'un des trois types de signature
        PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance();
        signatureCustomAppearance.setFontSize(6);
        signatureCustomAppearance.setFontFamilyName("Times New Roman");
        signatureCustomAppearance.setDigitalSignedLabel("SIGNÉ PAR :");
        signature.setCustomAppearance(signatureCustomAppearance);

        pdfSign.sign(1, true, rect, signature);
        // Enregistrer le fichier PDF de sortie
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```


## Changer la langue dans le texte de signature numérique

En utilisant Aspose.PDF pour l'API Java, vous pouvez signer un fichier PDF en utilisant l'un des trois types de signatures suivants :

- PKCS#1
- PKCS#7
- PKCS#7

Chacune des signatures fournies contient un ensemble de propriétés de configuration implémentées pour votre convenance (localisation, format de date et heure, famille de polices, etc.). La classe SignatureCustomAppearance fournit la fonctionnalité correspondante. Le code suivant montre comment changer la langue dans le texte de la signature numérique :

```java
     public static void ChangeLanguageInDigitalSignText() {
        String inFile = _dataDir + "sample01.pdf";
        String outFile = _dataDir + "DigitallySign.pdf";

        PdfFileSignature pdfSign = new PdfFileSignature();

        pdfSign.bindPdf(inFile);
        // créer un rectangle pour l'emplacement de la signature
        java.awt.Rectangle rect = new java.awt.Rectangle(310, 45, 200, 50);

        // créer l'un des trois types de signature
        PKCS7 pkcs = new PKCS7(_dataDir + "test01.pfx", "Aspose2021");
        pkcs.setReason("Pruebas Firma");
        pkcs.setContactInfo("Contacto Pruebas");
        pkcs.setLocation("Población (Provincia)");
        pkcs.setDate(new Date());
        SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance();
        signatureCustomAppearance.setDateSignedAtLabel("Fecha");
        signatureCustomAppearance.setDigitalSignedLabel("Digitalmente firmado por");
        signatureCustomAppearance.setReasonLabel("Razón");
        signatureCustomAppearance.setLocationLabel("Localización");
        signatureCustomAppearance.setFontFamilyName("Arial");
        signatureCustomAppearance.setFontSize(10);
        signatureCustomAppearance.setCulture(new Locale("es", "ES"));
        // signatureCustomAppearance.setCulture (Locale.ROOT);
        signatureCustomAppearance.setDateTimeFormat("yyyy.MM.dd HH:mm:ss");
        pkcs.setCustomAppearance(signatureCustomAppearance);
        // signer le fichier PDF
        pdfSign.sign(1, true, rect, pkcs);
        // enregistrer le fichier PDF de sortie
        pdfSign.save(outFile);
    }
```