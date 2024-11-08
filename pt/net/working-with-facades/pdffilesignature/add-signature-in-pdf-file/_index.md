---  
title: Adicionar Assinatura em Arquivo PDF  
type: docs  
weight: 10  
url: /pt/net/add-signature-in-pdf/  
description: Esta seção explica como adicionar assinatura a um arquivo PDF usando a classe PdfFileSignature.  
lastmod: "2021-06-05"  
draft: false  
---

## Adicionar Assinatura Digital em um Arquivo PDF

A classe [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) permite que você adicione assinatura em um arquivo PDF. Você precisa criar um objeto da classe [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) usando arquivos PDF de entrada e saída. Você também precisa criar um objeto [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle) no qual deseja adicionar a assinatura e, para definir a aparência, você pode especificar uma imagem usando a propriedade [SignatureAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/properties/signatureappearance) do objeto [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature). Aspose.Pdf.Facades também oferece diferentes tipos de assinaturas como PKCS#1, PKCS#7, e PKCS#7Detached. Para criar uma assinatura de um tipo específico, você precisa criar um objeto da classe particular como **PKCS1**, **PKCS7** ou **PKCS7Detached** usando o arquivo de certificado e a senha.

Uma vez que o objeto de um tipo de assinatura particular é criado, você pode usar o método [Sign](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/sign/index) da classe [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) para assinar o PDF e passar o objeto de assinatura particular para esta classe. Você também pode especificar outros atributos para este método. Finalmente, você precisa salvar o PDF assinado usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) da classe [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature). O trecho de código a seguir mostra como adicionar assinatura em um arquivo PDF.

```csharp
public static void AddPdfFileSignature()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // Criar um retângulo para a localização da assinatura
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);
            // Definir aparência da assinatura
            pdfSign.SignatureAppearance = _dataDir + "aspose-logo.png";

            // Criar qualquer um dos três tipos de assinatura
            PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(1, "Sou o autor do documento", "test01@aspose-pdf-demo.local", "Aspose Pdf Demo, Austrália", true, rect, signature);
            // Salvar arquivo PDF de saída
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```
O exemplo de código a seguir nos mostra a capacidade de assinar um documento com duas assinaturas. Em nosso exemplo, colocamos a primeira assinatura na primeira página e a segunda na segunda página. Você pode especificar as páginas que precisar.

```csharp
 public static void AddTwoSignature()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();

            // Assinar com a 1ª assinatura

            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // Criar um retângulo para a localização da 1ª assinatura
            System.Drawing.Rectangle rect1 = new System.Drawing.Rectangle(10, 10, 300, 50);

            // Criar objeto da 1ª assinatura
            PKCS1 signature1 = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(1, "Eu sou o autor do documento", "test@aspose-pdf-demo.local", "Aspose Pdf Demo, Austrália", true, rect1, signature1);
            pdfSign.Save(_dataDir + "DigitallySign.pdf");


            // Assinar com a 2ª assinatura

            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");

            // Criar um retângulo para a localização da 2ª assinatura
            System.Drawing.Rectangle rect2 = new System.Drawing.Rectangle(10, 10, 300, 50);

            // Criar objeto da 2ª assinatura
            PKCS1 signature2 = new PKCS1(_dataDir + "test02.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(2, "Eu sou o revisor do documento", "test02@aspose-pdf-demo.local", "Aspose Pdf Demo, Austrália", true, rect2, signature2);

            // Salvar arquivo PDF de saída
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

Para um documento com formulários ou acroforms que precisam ser assinados, veja o exemplo a seguir.  
Você precisa criar um objeto da classe [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) usando arquivos PDF de entrada e saída. Use [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesignature/bindpdf/methods/1) para vinculação. Crie uma assinatura com a capacidade de adicionar as propriedades necessárias. Em nosso exemplo, elas são 'Reason' e 'CustomAppearance'.

```csharp
 public static void AddPdfFileSignatureField()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample02.pdf");

            // Crie qualquer um dos três tipos de assinatura
            PKCS1 signature = new PKCS1(_dataDir + "test02.pfx", "Aspose2021")
            {
                Reason = "Assinar como Autor",
                CustomAppearance = new SignatureCustomAppearance
                {
                    FontSize = 6,
                    FontFamilyName = "Calibri"
                }
            }; // PKCS#1
            pdfSign.Sign("Signature1", signature);
            // Salve o arquivo PDF de saída
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

Se o nosso documento tiver dois campos, o algoritmo para assiná-lo é semelhante ao primeiro exemplo.

```csharp
public static void AddPdfFileSignatureField2()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample03.pdf");

            // Crie qualquer um dos três tipos de assinatura
            PKCS1 signature1 = new PKCS1(_dataDir + "test01.pfx", "Aspose2021")
            {
                Reason = "Assinar como Autor",
                CustomAppearance = new SignatureCustomAppearance
                {
                    FontSize = 6
                }
            }; // PKCS#1
            pdfSign.Sign("Signature1", signature1);
            // Salvar arquivo PDF de saída
            pdfSign.Save(_dataDir + "DigitallySign.pdf");

            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");

            // Crie qualquer um dos três tipos de assinatura
            PKCS1 signature2 = new PKCS1(_dataDir + "test02.pfx", "Aspose2021")
            {
                Reason = "Assinar como Revisor",
                CustomAppearance = new SignatureCustomAppearance
                {
                    FontSize = 6
                }
            }; // PKCS#1
            pdfSign.Sign("Signature2", signature2);
            // Salvar arquivo PDF de saída
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```