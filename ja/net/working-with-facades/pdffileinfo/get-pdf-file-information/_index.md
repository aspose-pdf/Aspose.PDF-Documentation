---
title: PDFファイル情報を取得する
type: docs
weight: 50
url: ja/net/get-pdf-file-information/
description: このセクションでは、Aspose.PDF Facadesを使用してPDFファイル情報を取得する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

PDFファイルの特定の情報を取得するには、[PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo)クラスのオブジェクトを作成する必要があります。その後、Subject、Title、Keywords、Creatorなどの個々のプロパティの値を取得できます。

次のコードスニペットは、PDFファイル情報を取得する方法を示しています。

```csharp
 public static void GetPdfInfo()
        {
            // ドキュメントを開く
            PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf");
            // PDF情報を取得
            Console.WriteLine("Subject: {0}", fileInfo.Subject);
            Console.WriteLine("Title: {0}", fileInfo.Title);
            Console.WriteLine("Keywords: {0}", fileInfo.Keywords);
            Console.WriteLine("Creator: {0}", fileInfo.Creator);
            Console.WriteLine("Creation Date: {0}", fileInfo.CreationDate);
            Console.WriteLine("Modification Date: {0}", fileInfo.ModDate);
            // 有効なPDFであるか、および暗号化されているかどうかを確認
            Console.WriteLine("Is Valid PDF: {0}", fileInfo.IsPdfFile);
            Console.WriteLine("Is Encrypted: {0}", fileInfo.IsEncrypted);

            Console.WriteLine("Page width:{0}", fileInfo.GetPageWidth(1));
            Console.WriteLine("Page height:{0}", fileInfo.GetPageHeight(1));
        }
```

## メタ情報を取得する

情報を取得するために、[Header](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/properties/header) プロパティを使用します。'Hashtable' で可能なすべての値を取得します。

```csharp
public static void GetMetaInfo()
        {
            // PdfFileInfo オブジェクトのインスタンスを作成
            Aspose.Pdf.Facades.PdfFileInfo fInfo = new Aspose.Pdf.Facades.PdfFileInfo(_dataDir + "SetMetaInfo_out.pdf");
            // 既存のカスタム属性をすべて取得
            Hashtable hTable = new Hashtable(fInfo.Header);

            IDictionaryEnumerator enumerator = hTable.GetEnumerator();
            while (enumerator.MoveNext())
            {
                string output = enumerator.Key.ToString() + " " + enumerator.Value;
                Console.WriteLine(output);
            }

            // 1つのカスタム属性を取得
            Console.WriteLine(fInfo.GetMetaInfo("Reviewer"));
```