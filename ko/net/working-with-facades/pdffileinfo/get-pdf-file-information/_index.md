---
title: PDF 파일 정보 가져오기
type: docs
weight: 50
url: ko/net/get-pdf-file-information/
description: 이 섹션에서는 Aspose.PDF Facades를 사용하여 PDF 파일 정보를 가져오는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

PDF 파일의 특정 정보를 얻으려면 [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) 클래스의 객체를 생성해야 합니다. 그런 다음, Subject, Title, Keywords, Creator 등의 개별 속성 값을 얻을 수 있습니다.

다음 코드 스니펫은 PDF 파일 정보를 얻는 방법을 보여줍니다.

```csharp
 public static void GetPdfInfo()
        {
            // 문서 열기
            PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf");
            // PDF 정보 가져오기
            Console.WriteLine("Subject: {0}", fileInfo.Subject);
            Console.WriteLine("Title: {0}", fileInfo.Title);
            Console.WriteLine("Keywords: {0}", fileInfo.Keywords);
            Console.WriteLine("Creator: {0}", fileInfo.Creator);
            Console.WriteLine("Creation Date: {0}", fileInfo.CreationDate);
            Console.WriteLine("Modification Date: {0}", fileInfo.ModDate);
            // 유효한 PDF인지 및 암호화 여부 찾기
            Console.WriteLine("Is Valid PDF: {0}", fileInfo.IsPdfFile);
            Console.WriteLine("Is Encrypted: {0}", fileInfo.IsEncrypted);

            Console.WriteLine("Page width:{0}", fileInfo.GetPageWidth(1));
            Console.WriteLine("Page height:{0}", fileInfo.GetPageHeight(1));
        }
```

## 메타 정보 가져오기

정보를 얻기 위해, 우리는 [Header](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/properties/header) 속성을 사용합니다. 'Hashtable'을 사용하여 모든 가능한 값을 얻습니다.

```csharp
public static void GetMetaInfo()
        {
            // PdfFileInfo 객체의 인스턴스 생성
            Aspose.Pdf.Facades.PdfFileInfo fInfo = new Aspose.Pdf.Facades.PdfFileInfo(_dataDir + "SetMetaInfo_out.pdf");
            // 모든 기존 사용자 정의 속성 검색
            Hashtable hTable = new Hashtable(fInfo.Header);

            IDictionaryEnumerator enumerator = hTable.GetEnumerator();
            while (enumerator.MoveNext())
            {
                string output = enumerator.Key.ToString() + " " + enumerator.Value;
                Console.WriteLine(output);
            }

            // 하나의 사용자 정의 속성 검색
            Console.WriteLine(fInfo.GetMetaInfo("Reviewer"));
```