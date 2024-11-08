---
title: Extrair Informações de Imagem e Assinatura
linktitle: Extrair Informações de Imagem e Assinatura
type: docs
weight: 30
url: /pt/java/extract-image-and-signature-information/
description: Você pode extrair imagens do campo de assinatura e extrair informações de assinatura usando a classe SignatureField com Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraindo Imagem do Campo de Assinatura

Aspose.PDF para Java suporta o recurso de assinar digitalmente os arquivos PDF usando a classe [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField) e, ao assinar o documento, você também pode definir uma imagem para SignatureAppearance. Agora, esta API também fornece a capacidade de extrair informações de assinatura, bem como a imagem associada ao campo de assinatura.

Para extrair informações de assinatura, introduzimos o método [ExtractImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField#extractImage--) na classe [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField).
 Por favor, dê uma olhada no seguinte trecho de código que demonstra as etapas para extrair uma imagem do objeto SignatureField:

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

### Substituir Imagem da Assinatura

Às vezes, pode ser necessário substituir apenas a imagem de um campo de assinatura já presente dentro de um arquivo PDF. Para atender a esse requisito, primeiro precisamos pesquisar os campos de formulário dentro do arquivo PDF, identificar os campos de Assinatura, obter as dimensões (dimensões retangulares) do campo de assinatura e, em seguida, estampar uma imagem sobre as mesmas dimensões.

## Extrair Informações da Assinatura

O Aspose.PDF para Java suporta o recurso de assinar digitalmente os arquivos PDF usando a classe [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField). Atualmente, também podemos determinar a validade do certificado, mas não podemos extrair o certificado completo. As informações que podem ser extraídas são chave pública, impressão digital, emissor, etc.

Para extrair informações da assinatura, introduzimos o método [ExtractCertificate](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField#extractCertificate--) na classe [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField).
 Por favor, veja o seguinte trecho de código que demonstra as etapas para extrair o certificado do objeto SignatureField:

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