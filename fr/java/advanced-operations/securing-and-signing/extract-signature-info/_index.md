---
title: Extraire des Informations sur l'Image et la Signature
linktitle: Extraire des Informations sur l'Image et la Signature
type: docs
weight: 30
url: fr/java/extract-image-and-signature-information/
description: Vous pouvez extraire des images du champ de signature et extraire des informations sur la signature en utilisant la classe SignatureField avec Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraction de l'Image du Champ de Signature

Aspose.PDF pour Java prend en charge la fonctionnalité de signer numériquement les fichiers PDF en utilisant la classe [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField) et lors de la signature du document, vous pouvez également définir une image pour l'apparence de la signature. Désormais, cette API offre également la possibilité d'extraire des informations sur la signature ainsi que l'image associée au champ de signature.

Afin d'extraire des informations sur la signature, nous avons introduit la méthode [ExtractImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField#extractImage--) dans la classe [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField).
 Veuillez jeter un coup d'œil à l'extrait de code suivant qui démontre les étapes pour extraire une image de l'objet SignatureField :

```java
public class ExampleExtractImageAndSignature {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Secure-Sign/";

    public static void ExtractingImageFromSignatureField() {
        Document pdfDocument = new Document(_dataDir + "ExtractingImage.pdf");

        int i = 0;
        try {
            for (WidgetAnnotation field : pdfDocument.getForm()) {
                SignatureField sf = (SignatureField) field;
                if (sf != null) {
                    FileOutputStream output = new FileOutputStream(_dataDir + "im" + i + ".jpeg");
                    InputStream tempStream = sf.extractImage();
                    byte[] b = new byte[tempStream.available()];
                    tempStream.read(b);
                    output.write(b);
                    output.close();
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (pdfDocument != null)
                pdfDocument.dispose();
        }

    }
```

### Remplacer l'image de la signature

Parfois, vous pouvez avoir besoin de seulement remplacer l'image d'un champ de signature déjà présent à l'intérieur d'un fichier PDF. Pour accomplir cette tâche, nous devons d'abord rechercher les champs de formulaire à l'intérieur du fichier PDF, identifier les champs de signature, obtenir les dimensions (dimensions rectangulaires) du champ de signature et ensuite tamponner une image sur les mêmes dimensions.

## Extraire les informations de la signature

Aspose.PDF pour Java prend en charge la fonctionnalité de signer numériquement les fichiers PDF en utilisant la classe [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField). Actuellement, nous pouvons également déterminer la validité du certificat, mais nous ne pouvons pas extraire le certificat complet. Les informations qui peuvent être extraites sont une clé publique, une empreinte, un émetteur, etc.

Pour extraire les informations de la signature, nous avons introduit la méthode [ExtractCertificate](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField#extractCertificate--) dans la classe [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField).
 Veuillez examiner l'extrait de code suivant qui démontre les étapes pour extraire le certificat de l'objet SignatureField :

```java
    public static void ExtractSignatureInformation() throws IOException {
        String input = _dataDir + "ExtractSignatureInfo.pdf";
        Document pdfDocument = new Document(input);

        for (WidgetAnnotation field : pdfDocument.getForm()) {
            SignatureField sf = (SignatureField) field;
            if (sf != null) {
                InputStream cerStream = sf.extractCertificate();
                if (cerStream != null) {

                    byte[] buffer = new byte[cerStream.available()];
                    cerStream.read(buffer);

                    File targetFile = new File(_dataDir+"targetFile.cer");
                    OutputStream outStream = new FileOutputStream(targetFile);
                    outStream.write(buffer);
                    outStream.close();
                }
            }
        }
    }
}
```