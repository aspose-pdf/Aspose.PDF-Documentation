---
title: PDF 파일에서 서명 제거
type: docs
weight: 20
url: /ko/net/remove-signature-from-pdf/
description: 이 섹션은 PdfFileSignature 클래스를 사용하여 PDF 파일에서 서명을 제거하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## PDF 파일에서 디지털 서명 제거

PDF 파일에 서명이 추가되었을 때, 이를 제거할 수 있습니다. 특정 서명만 제거하거나 파일 내 모든 서명을 제거할 수 있습니다. 서명을 제거하는 가장 빠른 방법은 서명 필드도 제거하는 것이지만, 파일을 다시 서명할 수 있도록 서명 필드를 유지하면서 서명만 제거할 수도 있습니다.

[PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) 클래스의 RemoveSignature 메서드는 PDF 파일에서 서명을 제거할 수 있게 해줍니다. 이 메서드는 서명 이름을 입력으로 받습니다. 서명 이름을 직접 지정하거나, [GetSignNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/getsignername) 메서드를 사용하여 모든 서명을 제거하고 서명 이름을 가져옵니다.

다음 코드 스니펫은 PDF 파일에서 디지털 서명을 제거하는 방법을 보여줍니다.

```csharp
 public static void RemoveSignature()
        {
            // PdfFileSignature 객체 생성
            PdfFileSignature pdfSign = new PdfFileSignature();
            // PDF 문서 열기
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");
            // 서명 이름 목록 가져오기
            var sigNames = pdfSign.GetSignNames();
            // PDF 파일에서 모든 서명 제거
            for (int index = 0; index < sigNames.Count; index++)
            {
                Console.WriteLine($"Removed {sigNames[index]}");
                pdfSign.RemoveSignature(sigNames[index]);
            }
            // 업데이트된 PDF 파일 저장
            pdfSign.Save(_dataDir + "RemoveSignature_out.pdf");
        }
```
### 서명 제거하지만 서명 필드 유지

위에서 설명한 것처럼, [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) 클래스의 [RemoveSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/removesignature) 메소드는 PDF 파일에서 서명 필드를 제거할 수 있게 합니다. 이 메소드를 9.3.0 버전 이전에서 사용할 때는 서명과 서명 필드가 모두 제거됩니다. 일부 개발자는 서명만 제거하고 서명 필드를 유지하여 문서를 다시 서명할 수 있도록 하기를 원합니다. 서명 필드를 유지하고 서명만 제거하려면, 다음 코드 스니펫을 사용하십시오.

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

다음 예제는 필드에서 모든 서명을 제거하는 방법을 보여줍니다.

```csharp
public static void RemoveSignatureButKeepField2()
        {
            // PdfFileSignature 객체 생성
            PdfFileSignature pdfSign = new PdfFileSignature();

            // PDF 문서 열기
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");

            var sigNames = pdfSign.GetSignNames();
            foreach (var sigName in sigNames)
            {
                pdfSign.RemoveSignature(sigName, false);
            }

            // 업데이트된 PDF 파일 저장
            pdfSign.Save(_dataDir + "RemoveSignature_out.pdf");
        }

```