---

title: 将PDF/A转换为PDF格式  
linktitle: 将PDF/A转换为PDF格式  
type: docs  
weight: 110  
url: /java/convert-pdfa-to-pdf/  
lastmod: "2021-11-19"  
description: 本主题向您展示如何使用Aspose.PDF通过Java库将PDF/A文件转换为PDF文档。  
sitemap:  
    changefreq: "monthly"  
    priority: 0.8  
---

## 将PDF/A文档转换为PDF

将PDF/A文档转换为PDF意味着从原始文档中去除<abbr title="Portable Document Format Archive">PDF/A</abbr>限制。[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)类具有方法RemovePdfaCompliance(..)，用于从输入/源文件中移除PDF合规性信息。

```java
public static void runPDFA_to_PDF() {
    String pdfaDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF.pdf").toString();
    String documentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF_out.pdf").toString();

    // 创建Document对象
    Document document = new Document(pdfaDocumentFileName);

    // 移除PDF/A合规性信息
    document.removePdfaCompliance();

    // 以XML格式保存输出
    document.save(documentFileName);
    document.close();
}
```


该信息在您对文档进行任何更改时也会被移除（例如，添加页面）。在以下示例中，输出文档在添加页面后失去了 PDF/A 合规性。

```java
public static void runPDFAtoPDFAdvanced() {
    String pdfaDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF.pdf").toString();
    String documentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF_out.pdf").toString();

    // 创建 Document 对象
    Document document = new Document(pdfaDocumentFileName);

    // 添加新的（空白）页面会移除 PDF/A 合规性信息。
    document.getPages().add();

    // 保存更新后的文档
    document.save(documentFileName);
    document.close();
}
```