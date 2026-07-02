---
title: PDF/A を PDF に変換
linktitle: PDF/A を PDF に変換
type: docs
weight: 350
url: /ja/androidjava/convert-pdfa-to-pdf/
lastmod: "2026-07-01"
description: PDF/A を PDF に変換するには、元のドキュメントから制限を削除する必要があります。Aspose.PDF for Android via Java を使用すれば、この問題を簡単かつシンプルに解決できます。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF/A ドキュメントを PDF に変換するとは、削除することを意味します <abbr title="Portable Document Format Archive
" >PDF/A</abbr> 元のドキュメントからの制限。クラス [ドキュメント](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) RemovePdfaCompliance(..) メソッドを持ち、削除します
入力/ソースファイルからの PDF コンプライアンス情報です。

```java

    public void convertPDFAtoPDF() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        try {
            // Create Document object
            document = new Document(pdfaDocumentFileName);

            // Remove PDF/A compliance information
            document.removePdfaCompliance();

            // Save output in XML format
            document.save(pdfDocumentFileName);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);

    }
```

この情報は、ドキュメントに変更を加えると（例：ページを追加する）削除されます。以下の例では、ページを追加した後、出力ドキュメントのPDF/A準拠が失われます。

```java
   public void convertPDFAtoPDFAdvanced() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        // Create Document object
        document = new Document(pdfaDocumentFileName);

        // Adding a new (empty) page removes PDF/A compliance information.
        document.getPages().add();

        // Save updated document
        document.save(pdfDocumentFileName);
    }
```




