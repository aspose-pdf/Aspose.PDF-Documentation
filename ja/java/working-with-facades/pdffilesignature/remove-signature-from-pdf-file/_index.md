---
title: PDFファイルから署名を削除する
type: docs
weight: 20
url: /ja/java/remove-signature-from-pdf/
description: このセクションでは、PdfFileSignatureクラスを使用してPDFファイルの署名を操作する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

## PDFファイルからデジタル署名を削除する

PDFファイルに署名が追加された場合、それを削除することが可能です。特定の署名を削除することも、ファイル内のすべての署名を削除することもできます。署名を削除する最も迅速な方法は署名フィールドも削除しますが、署名フィールドを保持して署名を削除するだけで、再度署名できるようにすることも可能です。

[PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) クラスの RemoveSignature メソッドは、PDFファイルから署名を削除することを可能にします。
 このメソッドは、署名名を入力として受け取ります。署名名を直接指定するか、すべての署名を削除するには、[getSignNames](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature#getSignNames--) メソッドを使用して署名名を取得します。

次のコードスニペットは、PDFファイルからデジタル署名を削除する方法を示しています。

```java
 public static void RemoveSignature() {
        // PdfFileSignatureオブジェクトを作成
        PdfFileSignature pdfSign = new PdfFileSignature();
        // PDFドキュメントを開く
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        // 署名名のリストを取得
        List<String> sigNames = pdfSign.getSignNames();
        // PDFファイルからすべての署名を削除
        for (int index = 0; index < sigNames.size(); index++) {
            System.out.println("Removed " + sigNames.get(index));
            pdfSign.removeSignature(sigNames.get(index));
        }
        // 更新されたPDFファイルを保存
        pdfSign.save(_dataDir + "RemoveSignature_out.pdf");
    }
```

### 署名を削除するが、署名フィールドは保持する

上記のように、[PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) クラスの [removeSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature#removeSignature-java.lang.String-) メソッドを使用すると、PDFファイルから署名フィールドを削除できます。このメソッドをバージョン9.3.0以前で使用すると、署名と署名フィールドの両方が削除されます。開発者の中には、署名だけを削除し、署名フィールドは保持しておきたいという人もいます。これにより、文書を再署名することができます。署名フィールドを保持し、署名のみを削除するには、以下のコードスニペットを使用してください。

```java
 public static void RemoveSignatureButKeepField() {
        // PdfFileSignatureオブジェクトを作成
        PdfFileSignature pdfSign = new PdfFileSignature();

        // PDFドキュメントを開く
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");

        pdfSign.removeSignature("Signature1", false);

        // 更新されたPDFファイルを保存
        pdfSign.save(_dataDir + "RemoveSignature_out.pdf");
    }
```


以下の例は、フィールドからすべての署名を削除する方法を示しています。

```java
public static void RemoveSignatureButKeepField2() {
        // PdfFileSignatureオブジェクトを作成
        PdfFileSignature pdfSign = new PdfFileSignature();

        // PDFドキュメントを開く
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");

        List<String> sigNames = pdfSign.getSignNames();
        for (String sigName : sigNames) {
            pdfSign.removeSignature(sigName, false);
        }

        // 更新されたPDFファイルを保存
        pdfSign.save(_dataDir + "RemoveSignature_out.pdf");
    }
```