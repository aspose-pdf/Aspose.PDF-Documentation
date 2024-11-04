---
title: Remover Assinatura de Arquivo PDF
type: docs
weight: 20
url: /java/remove-signature-from-pdf/
description: Esta seção explica como trabalhar com Assinatura em um Arquivo PDF usando a classe PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Remover Assinatura Digital do Arquivo PDF

Quando uma assinatura é adicionada a um arquivo PDF, é possível removê-la. Você pode remover uma assinatura específica ou todas as assinaturas em um arquivo. O método mais rápido para remover a assinatura também remove o campo de assinatura, mas é possível apenas remover a assinatura, mantendo o campo de assinatura para que o arquivo possa ser assinado novamente.

O método RemoveSignature da classe [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) permite que você remova uma assinatura de um arquivo PDF.
 Este método recebe o nome da assinatura como entrada. Ou especifique diretamente o nome da assinatura, para remover todas as assinaturas, obtenha os nomes das assinaturas usando o método [getSignNames](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature#getSignNames--).

O snippet de código a seguir mostra como remover a assinatura digital do arquivo PDF.

```java
 public static void RemoveSignature() {
        // Criar objeto PdfFileSignature
        PdfFileSignature pdfSign = new PdfFileSignature();
        // Abrir documento PDF
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        // Obter lista de nomes de assinaturas
        List<String> sigNames = pdfSign.getSignNames();
        // Remover todas as assinaturas do arquivo PDF
        for (int index = 0; index < sigNames.size(); index++) {
            System.out.println("Removido " + sigNames.get(index));
            pdfSign.removeSignature(sigNames.get(index));
        }
        // Salvar arquivo PDF atualizado
        pdfSign.save(_dataDir + "RemoveSignature_out.pdf");
    }
```

### Remover Assinatura mas Manter o Campo de Assinatura

Como mostrado acima, o método [removeSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature#removeSignature-java.lang.String-) da classe [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) permite remover campos de assinatura de arquivos PDF. Ao usar este método com versões anteriores à 9.3.0, tanto a assinatura quanto o campo de assinatura são removidos. Alguns desenvolvedores querem remover apenas a assinatura e manter o campo de assinatura para que ele possa ser usado para reassinar o documento. Para manter o campo de assinatura e remover apenas a assinatura, por favor, use o trecho de código a seguir.

```java
 public static void RemoveSignatureButKeepField() {
        // Criar objeto PdfFileSignature
        PdfFileSignature pdfSign = new PdfFileSignature();

        // Abrir documento PDF
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");

        pdfSign.removeSignature("Signature1", false);

        // Salvar arquivo PDF atualizado
        pdfSign.save(_dataDir + "RemoveSignature_out.pdf");
    }
```


O exemplo a seguir mostra como remover todas as assinaturas dos campos.

```java
public static void RemoveSignatureButKeepField2() {
        // Criar objeto PdfFileSignature
        PdfFileSignature pdfSign = new PdfFileSignature();

        // Abrir documento PDF
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");

        List<String> sigNames = pdfSign.getSignNames();
        for (String sigName : sigNames) {
            pdfSign.removeSignature(sigName, false);
        }

        // Salvar arquivo PDF atualizado
        pdfSign.save(_dataDir + "RemoveSignature_out.pdf");
    }
```