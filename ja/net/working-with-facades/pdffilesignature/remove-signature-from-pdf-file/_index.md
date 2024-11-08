---
title: PDFファイルから署名を削除
type: docs
weight: 20
url: /ja/net/remove-signature-from-pdf/
description: このセクションでは、PdfFileSignatureクラスを使用してPDFファイルから署名を削除する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

## PDFファイルからデジタル署名を削除

PDFファイルに署名が追加された場合、それを削除することが可能です。特定の署名、またはファイル内のすべての署名を削除することができます。署名を削除する最も迅速な方法は署名フィールドも削除しますが、署名フィールドを保持して署名だけを削除することも可能であり、ファイルを再び署名可能にします。

[PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) クラスの RemoveSignature メソッドを使用すると、PDFファイルから署名を削除することができます。 このメソッドは、署名名を入力として受け取ります。署名名を直接指定するか、すべての署名を削除するためには、[GetSignNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/getsignername) メソッドを使用して署名名を取得します。

次のコードスニペットは、PDFファイルからデジタル署名を削除する方法を示しています。

```csharp
 public static void RemoveSignature()
        {
            // PdfFileSignatureオブジェクトを作成
            PdfFileSignature pdfSign = new PdfFileSignature();
            // PDFドキュメントを開く
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");
            // 署名名のリストを取得
            var sigNames = pdfSign.GetSignNames();
            // PDFファイルからすべての署名を削除
            for (int index = 0; index < sigNames.Count; index++)
            {
                Console.WriteLine($"Removed {sigNames[index]}");
                pdfSign.RemoveSignature(sigNames[index]);
            }
            // 更新されたPDFファイルを保存
            pdfSign.Save(_dataDir + "RemoveSignature_out.pdf");
        }
```
### 署名を削除するが、署名フィールドを保持

上記のように、[PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) クラスの [RemoveSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/removesignature) メソッドを使用すると、PDFファイルから署名フィールドを削除できます。このメソッドをバージョン9.3.0以前で使用すると、署名と署名フィールドの両方が削除されます。一部の開発者は署名のみを削除し、署名フィールドを保持して、ドキュメントに再署名できるようにしたいと考えています。署名フィールドを保持し、署名のみを削除するには、次のコードスニペットを使用してください。

```csharp
public static void RemoveSignatureButKeepField()
        {
            // PdfFileSignatureオブジェクトを作成
            PdfFileSignature pdfSign = new PdfFileSignature();

            // PDFドキュメントを開く
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");

            pdfSign.RemoveSignature("Signature1", false);

            // 更新されたPDFファイルを保存
            pdfSign.Save(_dataDir + "RemoveSignature_out.pdf");
        }
```

次の例は、フィールドからすべての署名を削除する方法を示しています。

```csharp
public static void RemoveSignatureButKeepField2()
        {
            // PdfFileSignatureオブジェクトを作成
            PdfFileSignature pdfSign = new PdfFileSignature();

            // PDF文書を開く
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");

            var sigNames = pdfSign.GetSignNames();
            foreach (var sigName in sigNames)
            {
                pdfSign.RemoveSignature(sigName, false);
            }

            // 更新されたPDFファイルを保存
            pdfSign.Save(_dataDir + "RemoveSignature_out.pdf");
        }

```