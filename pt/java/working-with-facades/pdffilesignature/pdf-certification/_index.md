---
title: Certificação PDF
linktitle: Certificação PDF
type: docs
weight: 30
url: /pt/java/pdf-certification/
description: Saiba como certificar documentos PDF em Java com PdfFileSignature e DocMDPSignature.
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Certifique documentos PDF com permissões DocMDP em Java
Abstract: Saiba como certificar documentos PDF com Aspose.PDF for Java. O exemplo Java usa PdfFileSignature juntamente com DocMDPSignature e DocMDPAccessPermissions para certificar um documento para preenchimento de formulários e assinatura, ao mesmo tempo restringindo outros tipos de modificação.
---
## Certifique documentos PDF

Use a certificação quando o documento deve permanecer confiável, mas ainda permitir uma classe definida de alterações após a assinatura.

### Etapas

1. Crie um `PdfFileSignature` instancie e vincule o PDF de origem.
2. Construa um objeto `PKCS7` de assinatura com o certificado e a senha do certificado.
3. Envolva essa assinatura em um `DocMDPSignature` com o necessário `DocMDPAccessPermissions` valor.
4. Chame `certify` com a página de destino, metadados da assinatura, retângulo visível e assinatura MDP.
5. Salve o PDF certificado e feche o objeto de fachada.

### Exemplo Java

```java
public static void certifyPdfWithMdpSignature(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        DocMDPSignature signature = new DocMDPSignature(
                createPkcs7(certificateFile, "Certified for form filling and signing"),
                DocMDPAccessPermissions.FillingInForms);
        pdfSignature.certify(1, "Certified for form filling and signing", "security@example.com", "New York, USA", true, signatureRectangle(), signature);
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```
