---
title: PDF/AをPDF形式に変換する
linktitle: PDF/AをPDF形式に変換する
type: docs
weight: 110
url: /java/convert-pdfa-to-pdf/
lastmod: "2021-11-19"
description: このトピックでは、Aspose.PDFがJavaライブラリを使用してPDF/AファイルをPDFドキュメントに変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## PDF/AドキュメントをPDFに変換する

PDF/AドキュメントをPDFに変換することは、元のドキュメントから<abbr title="Portable Document Format Archive">PDF/A</abbr>の制限を取り除くことを意味します。[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)クラスには、入力/ソースファイルからPDF適合情報を削除するためのメソッドRemovePdfaCompliance(..)があります。

```java
public static void runPDFA_to_PDF() {
    String pdfaDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF.pdf").toString();
    String documentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF_out.pdf").toString();

    // Documentオブジェクトを作成
    Document document = new Document(pdfaDocumentFileName);

    // PDF/A適合情報を削除
    document.removePdfaCompliance();

    // 出力をXML形式で保存
    document.save(documentFileName);
    document.close();
}
```


この情報は、ドキュメントに変更を加えた場合（例：ページを追加）にも削除されます。次の例では、ページを追加すると、出力ドキュメントはPDF/A準拠を失います。

```java
public static void runPDFAtoPDFAdvanced() {
    String pdfaDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF.pdf").toString();
    String documentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF_out.pdf").toString();

    // Documentオブジェクトを作成
    Document document = new Document(pdfaDocumentFileName);

    // 新しい（空の）ページを追加すると、PDF/A準拠情報が削除されます。
    document.getPages().add();

    // 更新されたドキュメントを保存
    document.save(documentFileName);
    document.close();
}
```