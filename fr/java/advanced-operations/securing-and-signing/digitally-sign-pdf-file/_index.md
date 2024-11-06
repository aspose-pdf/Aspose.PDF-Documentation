---
title: Comment signer numériquement un PDF
linktitle: Signer numériquement un PDF
type: docs
weight: 10
url: fr/java/digitally-sign-pdf-file/
description: Signez numériquement des documents PDF en utilisant Java. Vérifiez ou validez les PDF signés numériquement avec une application basée sur Java avec la bibliothèque PDF. Vous pouvez certifier un fichier PDF avec un certificat PKCS1.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Lors de la signature d'un document PDF à l'aide d'une signature, vous confirmez essentiellement que son contenu doit rester "tel quel". Par conséquent, toute modification apportée par la suite invalide la signature et ainsi, vous savez si le document a été modifié. Certifier d'abord un document vous permet de spécifier les modifications qu'un utilisateur peut apporter au document sans invalider la certification.

En d'autres termes, le document serait toujours considéré comme conservant son intégrité et le destinataire pourrait toujours faire confiance au document. Pour plus de détails, veuillez visiter Certifier et signer un PDF.

Pour accomplir l'exigence mentionnée ci-dessus, les changements suivants de l'API publique ont été effectués.

isCertified(…) méthode est ajoutée à la classe PdfFileSignature.

## Signer un PDF avec des signatures numériques

```java
public class ExampleDigitallySign {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Secure-Sign/";

    public static void SignDocument() {
        String inFile = _dataDir + "DigitallySign.pdf";
        String outFile = _dataDir + "DigitallySign_out.pdf";
        Document document = new Document(inFile);

        PdfFileSignature signature = new PdfFileSignature(document);

        PKCS7 pkcs = new PKCS7("/home/aspose/pdf-examples/Samples/test.pfx", "Pa$$w0rd2020"); // Utiliser des objets
                                                                                              // PKCS7/PKCS7Detached
        signature.sign(1, true, new java.awt.Rectangle(300, 100, 400, 200), pkcs);
        // Enregistrer le fichier PDF de sortie
        signature.save(outFile);
    }
```

## Ajouter un horodatage à la signature numérique

Aspose.PDF pour Java prend en charge la signature numérique du PDF avec un serveur d'horodatage ou un service Web.

Afin de répondre à cette exigence, la classe [TimestampSettings](https://reference.aspose.com/pdf/java/com.aspose.pdf/TimestampSettings) a été ajoutée à l'espace de noms Aspose.PDF. Veuillez consulter l'extrait de code suivant qui obtient un horodatage et l'ajoute au document PDF :

```java
    public static void SignWithTimeStampServer() {
        Document document = new Document(_dataDir + "SimpleResume.pdf");
        PdfFileSignature signature = new PdfFileSignature(document);

        PKCS7 pkcs = new PKCS7("/home/aspose/pdf-examples/Samples/test.pfx", "Start2020");
        TimestampSettings timestampSettings = new TimestampSettings("https://freetsa.org/tsr", ""); // L'utilisateur/le mot de passe peuvent
                                                                                                    // être omis
        pkcs.setTimestampSettings(timestampSettings);
        java.awt.Rectangle rect = new java.awt.Rectangle(100, 100, 200, 100);
        // Créer l'un des trois types de signature
        signature.sign(1, "Motif de la signature", "Contact", "Emplacement", true, rect, pkcs);
        // Enregistrer le fichier PDF de sortie
        signature.save(_dataDir + "DigitallySignWithTimeStamp_out.pdf");
    }
```