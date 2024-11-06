---
title: 添付ファイルの抽出と保存
linktitle: 添付ファイルの抽出と保存
type: docs
weight: 20
url: ja/java/extract-and-save-an-attachment/
description: Aspose.PDF for Javaを使用すると、PDFドキュメントからすべての添付ファイルを取得できます。また、ドキュメントから個々の添付ファイルを取得することもできます。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFドキュメントから添付ファイルを取得する

Aspose.PDFを使用すると、PDFドキュメントからすべての添付ファイルを取得することが可能です。これは、ドキュメントをPDFから別々に保存したい場合や、PDFから添付ファイルを削除する必要がある場合に便利です。

次のコードスニペットは、PDFドキュメントからすべての添付ファイルを取得する方法を示しています。

```java
   public static void GetAttachmentsFromPDFDocument() {
// ドキュメントを開く
Document pdfDocument = new Document(_dataDir+"input.pdf");
  // 特定の埋め込みファイルを取得
  FileSpecification fileSpecification = pdfDocument.getEmbeddedFiles().get_Item(1);
  // ファイルのプロパティを取得
  System.out.printf("Name: - " + fileSpecification.getName());
  System.out.printf("\nDescription: - " + fileSpecification.getDescription());
  System.out.printf("\nMime Type: - " + fileSpecification.getMIMEType());
  // PDFファイルから添付ファイルを取得
  try {
   InputStream input = fileSpecification.getContents();
   File file = new File(fileSpecification.getName());
   // pdfからファイルのパスを作成
   file.getParentFile().mkdirs();
   // pdfからファイルを作成して抽出
   java.io.FileOutputStream output = new java.io.FileOutputStream(fileSpecification.getName(), true);
   byte[] buffer = new byte[4096];
   int n = 0;
   while (-1 != (n = input.read(buffer)))
    output.write(buffer, 0, n);
   // InputStreamオブジェクトを閉じる
   input.close();
   output.close();
  } catch (IOException e) {
   e.printStackTrace();
  }
  // Documentオブジェクトを閉じる
  pdfDocument.dispose();
        
    }

```


## 添付ファイル情報の取得

[PDFドキュメントから添付ファイルを取得する](/pdf/java/get-attachments-from-a-pdf-document/)で説明されているように、添付ファイル情報は[FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification)オブジェクトに保持され、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)オブジェクトのEmbeddedFilesコレクションに他の添付ファイルと一緒に収集されます。

[FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification)オブジェクトは、添付ファイルに関する情報を取得するメソッドを提供します。例えば：

- getName() – ファイル名を取得します。
- [getDescription()](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification#getDescription--) – ファイルの説明を取得します。
- getMIMEType() – ファイルのMIMEタイプを取得します。
- getParams() – ファイルのパラメーターに関する情報を取得します。例えば、CheckSum、CreationDate、ModDate、Sizeなどです。

これらのパラメーターを取得するには、まずgetParams()メソッドがnullを返さないことを確認します。

forループを使用してEmbeddedFilesコレクション内のすべての添付ファイルをループするか、インデックス値を指定して個々の添付ファイルを取得します。
 以下のコードスニペットは、特定の添付ファイルに関する情報を取得する方法を示しています。

```java
    public static void GetAttachmentInformation() {
  // ドキュメントを開く
  Document pdfDocument = new Document(_dataDir+"input.pdf");
  // 特定の埋め込みファイルを取得
  FileSpecification fileSpecification = pdfDocument.getEmbeddedFiles().get_Item(1);
  // ファイルプロパティを取得
  System.out.println("Name:-" + fileSpecification.getName());
  System.out.println("Description:- " + fileSpecification.getDescription());
  System.out.println("Mime Type:-" + fileSpecification.getMIMEType());
  // パラメータオブジェクトがパラメータを含んでいるかチェック
  if (fileSpecification.getParams() != null) {
   System.out.println("CheckSum:- " + fileSpecification.getParams().getCheckSum());
   System.out.println("Creation Date:- " + fileSpecification.getParams().getCreationDate());
   System.out.println("Modification Date:- " + fileSpecification.getParams().getModDate());
   System.out.println("Size:- " + fileSpecification.getParams().getSize());
  } 
```