---
title: "Java での PDF に添付ファイルの追加"
linktitle: "PDF ドキュメントへの添付ファイルの追加"
type: docs
weight: 10
url: /ja/java/add-attachment-to-pdf-document/
description: Aspose.PDF を使用して Java で PDF ドキュメントにファイル添付を追加する方法を学びます。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java を使用して PDF ドキュメントに埋め込みファイルの追加"
Abstract: この記事では、Aspose.PDF for Java を使用して外部ファイルを PDF ドキュメントに添付する方法を示します。サンプルでは既存の PDF を開き、添付用に FileSpecification を作成し、それをドキュメントの EmbeddedFiles コレクションに追加し、更新されたファイルを保存します。
---
PDF にファイルを添付するには、ソース文書をロードし、`FileSpecification` を作成して埋め込みファイルコレクションに追加し、結果を保存してください。

## PDF ドキュメントへの添付ファイルの追加

外部ファイルを既存の PDF に埋め込む必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 埋め込みたいファイル用に [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) を作成してください。
1. `EmbeddedFiles` コレクションにファイル仕様を追加し、更新されたドキュメントを保存してください。

```java
public static void addAttachments(Path inputFile, Path attachmentPath, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FileSpecification fileSpecification = new FileSpecification(attachmentPath.toString(), "Sample text file");
        document.getEmbeddedFiles().add(attachmentPath.getFileName().toString(), fileSpecification);
        document.save(outputFile.toString());
    }
}
```
