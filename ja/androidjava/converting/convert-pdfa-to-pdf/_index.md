---
title: PDF/AをPDFに変換
linktitle: PDF/AをPDFに変換
type: docs
weight: 350
url: ja/androidjava/convert-pdfa-to-pdf/
lastmod: "2021-06-05"
description: PDF/AをPDFに変換するには、元のドキュメントから制限を取り除く必要があります。Aspose.PDF for Android via Javaを使用すると、この問題を簡単に解決できます。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF/AドキュメントをPDFに変換するということは、元のドキュメントから<abbr title="Portable Document Format Archive
">PDF/A</abbr>の制限を取り除くことを意味します。クラス[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)には、入力/ソースファイルからPDFの準拠情報を削除するためのメソッドRemovePdfaCompliance(..)があります。

```java

    public void convertPDFAtoPDF() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        try {
            // Documentオブジェクトを作成
            document = new Document(pdfaDocumentFileName);

            // PDF/Aの準拠情報を削除
            document.removePdfaCompliance();

            // 結果をXML形式で保存
            document.save(pdfDocumentFileName);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);

    }
```


この情報は、ドキュメントに変更を加えた場合（例：ページを追加）にも削除されます。次の例では、ページを追加した後、出力ドキュメントはPDF/Aの適合性を失います。

```java
   public void convertPDFAtoPDFAdvanced() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        // Documentオブジェクトを作成
        document = new Document(pdfaDocumentFileName);

        // 新しい（空の）ページを追加するとPDF/A適合情報が削除されます。
        document.getPages().add();

        // 更新されたドキュメントを保存
        document.save(pdfDocumentFileName);
    }
```