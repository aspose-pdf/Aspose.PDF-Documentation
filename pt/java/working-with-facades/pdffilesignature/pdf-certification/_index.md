---
title: Certificação PDF
linktitle: Certificação PDF
type: docs
weight: 30
url: /java/pdf-certification/
description: Aprenda como certificar documentos PDF em Java com PdfFileSignature e DocMDPSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Certifique documentos PDF com permissões DocMDP em Java
Abstract: Aprenda como certificar documentos PDF com Aspose.PDF para Java. O exemplo Java usa PdfFileSignature junto com DocMDPSignature e DocMDPAccessPermissions para certificar um documento para preenchimento e assinatura de formulário, ao mesmo tempo que restringe outros tipos de modificação.
---
## Certificar documentos PDF

Use a certificação quando o documento deve permanecer confiável, mas ainda permitir uma classe definida de alterações após a assinatura.

### Passos

1. Crie uma instância `PdfFileSignature` e vincule o PDF de origem.
2. Crie um objeto de assinatura `PKCS7` com o certificado e a senha do certificado.
3. Envolva essa assinatura em `DocMDPSignature` com o valor `DocMDPAccessPermissions` necessário.
4. Chame `certify` com a página de destino, metadados de assinatura, retângulo visível e assinatura MDP.
5. Salve o PDF certificado e feche o objeto fachada.

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
