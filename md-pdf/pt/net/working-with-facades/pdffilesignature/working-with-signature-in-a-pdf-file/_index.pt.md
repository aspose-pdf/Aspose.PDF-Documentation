---
title: Trabalhando com Assinatura em Arquivo PDF
type: docs
weight: 40
url: /net/working-with-signature-in-a-pdf-file/
description: Esta seção explica como extrair informações de assinatura, extrair imagem da assinatura, mudar idioma, etc. usando a classe PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Como Extrair Informações de Assinatura

Aspose.PDF para .NET suporta a funcionalidade de assinar digitalmente arquivos PDF usando a classe PdfFileSignature. Atualmente, também é possível determinar a validade de um certificado, mas não podemos extrair o certificado inteiro. As informações que podem ser extraídas são a chave pública, impressão digital e emissor, etc.

Para extrair informações de assinatura, introduzimos o método ExtractCertificate(..) na classe PdfFileSignature. Por favor, veja o exemplo de código a seguir que demonstra as etapas para extrair o certificado do objeto PdfFileSignature:

```csharp
public static void ExtractSignatureInfo()
        {
            string input = _dataDir + "DigitallySign.pdf";
            string certificateFileName = "extracted_cert.pfx";
            using (PdfFileSignature pdfFileSignature = new PdfFileSignature())
            {
                pdfFileSignature.BindPdf(input);
                var sigNames = pdfFileSignature.GetSignNames();
                if (sigNames.Count > 0)
                {
                    string sigName = sigNames[0];
                    if (!string.IsNullOrEmpty(sigName))
                    {
                        Stream cerStream = pdfFileSignature.ExtractCertificate(sigName);
                        if (cerStream != null)
                        {
                            using (cerStream)
                            {
                                using (FileStream fs = new FileStream(_dataDir + certificateFileName, FileMode.CreateNew))
                                {
                                    cerStream.CopyTo(fs);
                                }
                            }
                        }
                    }
                }
            }
        }
```

## Extraindo Imagem do Campo de Assinatura (PdfFileSignature)

Aspose.PDF para .NET suporta o recurso de assinar digitalmente os arquivos PDF usando a classe PdfFileSignature e, ao assinar o documento, você também pode definir uma imagem para SignatureAppearance. Agora, esta API também fornece a capacidade de extrair informações de assinatura, bem como a imagem associada ao campo de assinatura.

Para extrair informações de assinatura, introduzimos o método ExtractImage(..) na classe PdfFileSignature. Por favor, veja o seguinte trecho de código que demonstra os passos para extrair a imagem do objeto PdfFileSignature:

```csharp
public static void ExtractSignatureImage()
        {
            using (PdfFileSignature signature = new PdfFileSignature())
            {
                signature.BindPdf(_dataDir + "DigitallySign.pdf");

                if (signature.ContainsSignature())
                {
                    foreach (string sigName in signature.GetSignNames())
                    {
                        string outFile = _dataDir + "ExtractImages_out.jpg";
                        using (Stream imageStream = signature.ExtractImage(sigName))
                        {
                            if (imageStream != null)
                            {
                                imageStream.Position = 0;
                                using (FileStream fs = new FileStream(outFile, FileMode.OpenOrCreate))
                                {
                                    imageStream.CopyTo(fs);
                                }
                            }
                        }
                    }
                }
            }
        }
```

## Suprimir Localização e Razão

A funcionalidade Aspose.PDF permite configuração flexível para instância de assinatura digital. A classe [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) fornece a capacidade de assinar um arquivo PDF. A implementação do método de assinatura permite assinar o PDF e passar o objeto de assinatura particular para esta classe. O método de assinatura contém um conjunto de atributos para a personalização da assinatura digital de saída. Caso você precise suprimir alguns atributos de texto da assinatura resultante, você pode deixá-los vazios. O snippet de código a seguir demonstra como suprimir as duas linhas de Localização e Razão do bloco de assinatura:

```csharp
public static void SupressLocationReason()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // Create a rectangle for signature location
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);
            // Set signature appearance
            pdfSign.SignatureAppearance = _dataDir + "aspose-logo.png";

            // Create any of the three signature types
            PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(1, string.Empty, "test01@aspose-pdf-demo.local", string.Empty, true, rect, signature);
            // Save output PDF file
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

## Recursos de Personalização para Assinatura Digital

Aspose.PDF para .NET permite recursos de personalização para uma assinatura digital. O método Sign da classe [SignatureCustomAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturecustomappearance) é implementado com 6 sobrecargas para seu uso confortável. Por exemplo, você pode configurar a assinatura resultante apenas pela instância da classe SignatureCustomAppearance e seus valores de propriedades. O trecho de código a seguir demonstra como ocultar a legenda "Assinado digitalmente por" da assinatura digital de saída do seu PDF.

```csharp
  public static void CustomizationFeaturesForDigitalSign()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // Criar um retângulo para a localização da assinatura
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);

            // Criar qualquer um dos três tipos de assinatura
            PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance
            {
                FontSize = 6,
                FontFamilyName = "Times New Roman",
                DigitalSignedLabel = "Assinado por:"
            };
            signature.CustomAppearance = signatureCustomAppearance;

            pdfSign.Sign(1, true, rect, signature);
            // Salvar o arquivo PDF de saída
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

## Alterar Idioma no Texto de Assinatura Digital

Usando a API Aspose.PDF para .NET, você pode assinar um arquivo PDF usando qualquer um dos três tipos de assinaturas a seguir:

- PKCS#1
- PKCS#7
- PKCS#7

Cada uma das assinaturas fornecidas contém um conjunto de propriedades de configuração implementadas para sua conveniência (localização, formato de data e hora, família de fontes, etc.). A classe [SignatureCustomAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturecustomappearance) fornece a funcionalidade correspondente. O trecho de código a seguir demonstra como alterar o idioma no texto da assinatura digital:

```csharp
     public static void ChangeLanguageInDigitalSignText()
        {
            string inFile = _dataDir + "sample01.pdf";
            string outFile = _dataDir + "DigitallySign.pdf";

            using (Aspose.Pdf.Facades.PdfFileSignature pdfSign = new Aspose.Pdf.Facades.PdfFileSignature())
            {
                pdfSign.BindPdf(inFile);
                //criar um retângulo para a localização da assinatura
                System.Drawing.Rectangle rect = new System.Drawing.Rectangle(310, 45, 200, 50);

                //criar qualquer um dos três tipos de assinatura
                PKCS7 pkcs = new PKCS7(_dataDir + "test01.pfx", "Aspose2021")
                {
                    Reason = "Pruebas Firma",
                    ContactInfo = "Contacto Pruebas",
                    Location = "Población (Provincia)",
                    Date = DateTime.Now
                };
                SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance
                {
                    DateSignedAtLabel = "Fecha",
                    DigitalSignedLabel = "Digitalmente firmado por",
                    ReasonLabel = "Razón",
                    LocationLabel = "Localización",
                    FontFamilyName = "Arial",
                    FontSize = 10d,
                    Culture = System.Globalization.CultureInfo.InvariantCulture,
                    DateTimeFormat = "yyyy.MM.dd HH:mm:ss"
                };
                pkcs.CustomAppearance = signatureCustomAppearance;
                // assinar o arquivo PDF
                pdfSign.Sign(1, true, rect, pkcs);
                //salvar o arquivo PDF de saída
                pdfSign.Save(outFile);
            }
        }
```