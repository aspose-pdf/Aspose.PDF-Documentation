---
title: Remover Assinatura de Arquivo PDF
type: docs
weight: 20
url: /pt/net/remove-signature-from-pdf/
description: Esta seção explica como remover a assinatura de um arquivo PDF usando a classe PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Remover Assinatura Digital do Arquivo PDF

Quando uma assinatura é adicionada a um arquivo PDF, é possível removê-la. Você pode remover uma assinatura específica ou todas as assinaturas em um arquivo. O método mais rápido para remover a assinatura também remove o campo de assinatura, mas é possível apenas remover a assinatura, mantendo o campo de assinatura para que o arquivo possa ser assinado novamente.

O método RemoveSignature da classe [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) permite que você remova uma assinatura de um arquivo PDF. Este método recebe o nome da assinatura como entrada. Ou especifique o nome da assinatura diretamente, para remover todas as assinaturas, obtenha os nomes das assinaturas usando o método [GetSignNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/getsignername).

O trecho de código a seguir mostra como remover a assinatura digital do arquivo PDF.

```csharp
 public static void RemoveSignature()
        {
            // Cria objeto PdfFileSignature
            PdfFileSignature pdfSign = new PdfFileSignature();
            // Abre documento PDF
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");
            // Obter lista de nomes de assinaturas
            var sigNames = pdfSign.GetSignNames();
            // Remove todas as assinaturas do arquivo PDF
            for (int index = 0; index < sigNames.Count; index++)
            {
                Console.WriteLine($"Removido {sigNames[index]}");
                pdfSign.RemoveSignature(sigNames[index]);
            }
            // Salva arquivo PDF atualizado
            pdfSign.Save(_dataDir + "RemoveSignature_out.pdf");
        }
```
### Remover Assinatura mas Manter o Campo de Assinatura

Conforme mostrado acima, o método [RemoveSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/removesignature) da classe [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) permite remover campos de assinatura de arquivos PDF. Ao usar este método com versões anteriores à 9.3.0, tanto a assinatura quanto o campo de assinatura são removidos. Alguns desenvolvedores desejam remover apenas a assinatura e manter o campo de assinatura para que ele possa ser usado para re-assinar o documento. Para manter o campo de assinatura e remover apenas a assinatura, por favor, use o seguinte trecho de código.

```csharp
public static void RemoveSignatureButKeepField()
        {
            // Create PdfFileSignature object
            PdfFileSignature pdfSign = new PdfFileSignature();

            // Open PDF document
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");

            pdfSign.RemoveSignature("Signature1", false);

            // Save updated PDF file
            pdfSign.Save(_dataDir + "RemoveSignature_out.pdf");
        }
```

O exemplo a seguir mostra como remover todas as assinaturas dos campos.

```csharp
public static void RemoveSignatureButKeepField2()
        {
            // Criar objeto PdfFileSignature
            PdfFileSignature pdfSign = new PdfFileSignature();

            // Abrir documento PDF
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");

            var sigNames = pdfSign.GetSignNames();
            foreach (var sigName in sigNames)
            {
                pdfSign.RemoveSignature(sigName, false);
            }

            // Salvar arquivo PDF atualizado
            pdfSign.Save(_dataDir + "RemoveSignature_out.pdf");
        }

```