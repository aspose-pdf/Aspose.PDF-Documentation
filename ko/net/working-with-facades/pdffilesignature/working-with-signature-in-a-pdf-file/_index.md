---
title: PDF 파일에서 서명 처리
type: docs
weight: 40
url: ko/net/working-with-signature-in-a-pdf-file/
description: 이 섹션에서는 PdfFileSignature 클래스를 사용하여 서명 정보 추출, 서명에서 이미지 추출, 언어 변경 등을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## 서명 정보 추출 방법

Aspose.PDF for .NET은 PdfFileSignature 클래스를 사용하여 PDF 파일에 디지털 서명을 지원합니다. 현재 인증서의 유효성을 확인할 수 있지만 전체 인증서를 추출할 수는 없습니다. 추출할 수 있는 정보는 공개 키, 지문, 발급자 등이 있습니다.

서명 정보를 추출하기 위해, PdfFileSignature 클래스에 ExtractCertificate(..) 메서드를 도입했습니다. PdfFileSignature 객체에서 인증서를 추출하는 단계를 보여주는 다음 코드 스니펫을 살펴보세요:

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

## 서명 필드에서 이미지 추출 (PdfFileSignature)

Aspose.PDF for .NET은 PdfFileSignature 클래스를 사용하여 PDF 파일을 디지털 서명하는 기능을 지원하며, 문서에 서명하는 동안 SignatureAppearance에 이미지를 설정할 수도 있습니다. 이제 이 API는 서명 필드와 관련된 서명 정보 및 이미지를 추출하는 기능도 제공합니다.

서명 정보를 추출하기 위해, 우리는 PdfFileSignature 클래스에 ExtractImage(..) 메서드를 도입했습니다. PdfFileSignature 객체에서 이미지를 추출하는 단계에 대한 다음 코드 스니펫을 참조하십시오:

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

## 위치 및 이유 숨기기

Aspose.PDF 기능은 디지털 서명 인스턴스를 유연하게 구성할 수 있습니다. [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) 클래스는 PDF 파일에 서명할 수 있는 기능을 제공합니다. 서명 메서드 구현은 PDF에 서명하고 특정 서명 개체를 이 클래스에 전달할 수 있게 해줍니다. 서명 메서드는 출력 디지털 서명의 사용자 지정을 위한 속성 세트를 포함합니다. 결과 서명에서 일부 텍스트 속성을 숨기려면 해당 속성을 비워둘 수 있습니다. 다음 코드 스니펫은 서명 블록에서 위치 및 이유 두 행을 숨기는 방법을 보여줍니다:

```csharp
public static void SupressLocationReason()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // 서명 위치를 위한 사각형 생성
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);
            // 서명 모양 설정
            pdfSign.SignatureAppearance = _dataDir + "aspose-logo.png";

            // 세 가지 서명 유형 중 하나 생성
            PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(1, string.Empty, "test01@aspose-pdf-demo.local", string.Empty, true, rect, signature);
            // 출력 PDF 파일 저장
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

## 디지털 서명의 사용자 정의 기능

Aspose.PDF for .NET은 디지털 서명을 위한 사용자 정의 기능을 제공합니다. [SignatureCustomAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturecustomappearance) 클래스의 Sign 메서드는 편리한 사용을 위해 6개의 오버로드로 구현됩니다. 예를 들어, SignatureCustomAppearance 클래스 인스턴스와 그 속성 값을 통해 결과 서명을 구성할 수 있습니다. 다음 코드는 PDF의 출력 디지털 서명에서 "Digitally signed by" 캡션을 숨기는 방법을 보여줍니다.

```csharp
  public static void CustomizationFeaturesForDigitalSign()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // 서명 위치를 위한 사각형 생성
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);

            // 세 가지 서명 유형 중 하나 생성
            PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance
            {
                FontSize = 6,
                FontFamilyName = "Times New Roman",
                DigitalSignedLabel = "Signed by:"
            };
            signature.CustomAppearance = signatureCustomAppearance;

            pdfSign.Sign(1, true, rect, signature);
            // 출력 PDF 파일 저장
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

## 디지털 서명 텍스트에서 언어 변경

Aspose.PDF for .NET API를 사용하여 다음 세 가지 유형의 서명을 사용하여 PDF 파일에 서명할 수 있습니다:

- PKCS#1
- PKCS#7
- PKCS#7

제공된 각 서명에는 사용자의 편의를 위해 구현된 구성 속성 집합(현지화, 날짜 시간 형식, 글꼴 등)이 포함되어 있습니다. 클래스 [SignatureCustomAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturecustomappearance)는 해당 기능을 제공합니다. 다음 코드 스니펫은 디지털 서명 텍스트에서 언어를 변경하는 방법을 보여줍니다:

```csharp
     public static void ChangeLanguageInDigitalSignText()
        {
            string inFile = _dataDir + "sample01.pdf";
            string outFile = _dataDir + "DigitallySign.pdf";

            using (Aspose.Pdf.Facades.PdfFileSignature pdfSign = new Aspose.Pdf.Facades.PdfFileSignature())
            {
                pdfSign.BindPdf(inFile);
                //서명 위치를 위한 사각형 생성
                System.Drawing.Rectangle rect = new System.Drawing.Rectangle(310, 45, 200, 50);

                //세 가지 서명 유형 중 하나를 생성
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
                // PDF 파일에 서명
                pdfSign.Sign(1, true, rect, pkcs);
                //출력 PDF 파일 저장
                pdfSign.Save(outFile);
            }
        }
```