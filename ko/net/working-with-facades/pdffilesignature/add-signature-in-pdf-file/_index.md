---
title: PDF 파일에 서명 추가
type: docs
weight: 10
url: ko/net/add-signature-in-pdf/
description: 이 섹션에서는 PdfFileSignature 클래스를 사용하여 PDF 파일에 서명을 추가하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## PDF 파일에 디지털 서명 추가

[PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) 클래스는 PDF 파일에 서명을 추가할 수 있게 합니다. 당신은 입력 및 출력 PDF 파일을 사용하여 [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) 클래스의 객체를 생성해야 합니다. 또한 서명을 추가하고자 하는 위치에 [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle) 객체를 생성해야 하며, [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) 객체의 [SignatureAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/properties/signatureappearance) 속성을 사용하여 이미지를 지정하여 외관을 설정할 수 있습니다. Aspose.Pdf.Facades는 PKCS#1, PKCS#7 및 PKCS#7Detached와 같은 다양한 종류의 서명을 제공합니다. 특정 유형의 서명을 만들기 위해서는 인증서 파일과 비밀번호를 사용하여 **PKCS1**, **PKCS7** 또는 **PKCS7Detached**와 같은 특정 클래스의 객체를 생성해야 합니다.

특정 서명 유형의 객체가 생성되면, [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) 클래스의 [Sign](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/sign/index) 메서드를 사용하여 PDF에 서명하고 이 클래스에 특정 서명 객체를 전달할 수 있습니다. 당신은 이 메서드에 대해 다른 속성을 지정할 수도 있습니다. 마지막으로, [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) 클래스의 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) 메서드를 사용하여 서명된 PDF를 저장해야 합니다. 다음 코드 스니펫은 PDF 파일에 서명을 추가하는 방법을 보여줍니다.

```csharp
public static void AddPdfFileSignature()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // 서명 위치를 위한 사각형 생성
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);
            // 서명 모양 설정
            pdfSign.SignatureAppearance = _dataDir + "aspose-logo.png";

            // 세 가지 서명 유형 중 하나 생성
            PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(1, "I'm document author", "test01@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect, signature);
            // 출력 PDF 파일 저장
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```
다음 코드 예제는 두 개의 서명을 사용하여 문서에 서명하는 기능을 보여줍니다. 예제에서는 첫 번째 서명을 첫 번째 페이지에, 두 번째 서명을 두 번째 페이지에 넣습니다. 필요한 페이지를 지정할 수 있습니다.

```csharp
 public static void AddTwoSignature()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();

            // 1번째 서명으로 서명

            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // 1번째 서명 위치를 위한 사각형 생성
            System.Drawing.Rectangle rect1 = new System.Drawing.Rectangle(10, 10, 300, 50);

            // 1번째 서명 객체 생성
            PKCS1 signature1 = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(1, "저는 문서 작성자입니다", "test@aspose-pdf-demo.local", "Aspose Pdf Demo, 호주", true, rect1, signature1);
            pdfSign.Save(_dataDir + "DigitallySign.pdf");


            // 2번째 서명으로 서명

            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");

            // 2번째 서명 위치를 위한 사각형 생성
            System.Drawing.Rectangle rect2 = new System.Drawing.Rectangle(10, 10, 300, 50);

            // 2번째 서명 객체 생성
            PKCS1 signature2 = new PKCS1(_dataDir + "test02.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(2, "저는 문서 검토자입니다", "test02@aspose-pdf-demo.local", "Aspose Pdf Demo, 호주", true, rect2, signature2);

            // 출력 PDF 파일 저장
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

문서나 서명해야 할 아크로폼이 있는 경우, 다음 예제를 참조하세요. 입력 및 출력 PDF 파일을 사용하여 [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) 클래스의 객체를 생성해야 합니다. 바인딩에는 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesignature/bindpdf/methods/1)를 사용하세요. 필요한 속성을 추가할 수 있는 서명을 만드세요. 예제에서는 'Reason'과 'CustomAppearance'입니다.

```csharp
 public static void AddPdfFileSignatureField()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample02.pdf");

            // 세 가지 서명 유형 중 하나를 만듭니다.
            PKCS1 signature = new PKCS1(_dataDir + "test02.pfx", "Aspose2021")
            {
                Reason = "Sign as Author",
                CustomAppearance = new SignatureCustomAppearance
                {
                    FontSize = 6,
                    FontFamilyName = "Calibri"
                }
            }; // PKCS#1
            pdfSign.Sign("Signature1", signature);
            // 출력 PDF 파일을 저장합니다.
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

우리 문서에 두 개의 필드가 있는 경우, 서명을 위한 알고리즘은 첫 번째 예제와 유사합니다.

```csharp
public static void AddPdfFileSignatureField2()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample03.pdf");

            // 세 가지 서명 유형 중 하나를 생성합니다
            PKCS1 signature1 = new PKCS1(_dataDir + "test01.pfx", "Aspose2021")
            {
                Reason = "저자로 서명",
                CustomAppearance = new SignatureCustomAppearance
                {
                    FontSize = 6
                }
            }; // PKCS#1
            pdfSign.Sign("Signature1", signature1);
            // 출력 PDF 파일 저장
            pdfSign.Save(_dataDir + "DigitallySign.pdf");

            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");

            // 세 가지 서명 유형 중 하나를 생성합니다
            PKCS1 signature2 = new PKCS1(_dataDir + "test02.pfx", "Aspose2021")
            {
                Reason = "검토자로 서명",
                CustomAppearance = new SignatureCustomAppearance
                {
                    FontSize = 6
                }
            }; // PKCS#1
            pdfSign.Sign("Signature2", signature2);
            // 출력 PDF 파일 저장
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```