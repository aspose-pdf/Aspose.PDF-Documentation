---
title: アノテーションの削除（ファサード）
type: docs
weight: 10
url: ja/java/delete-annotations/
description: このセクションでは、Aspose.PDF ファサードを使用して PdfAnnotationEditor クラスでアノテーションを削除する方法を説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) クラスを使用して、指定されたアノテーションタイプに基づいて既存の PDF ファイルからアノテーションを削除することができます。
 そのためには、[PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) オブジェクトを作成し、bindPdf メソッドを使用して入力 PDF ファイルをバインドする必要があります。その後、文字列パラメータを使用して [deleteAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#deleteAnnotation-java.lang.String-) メソッドを呼び出し、ファイルからすべての注釈を削除します。文字列パラメータは削除する注釈タイプを表します。最後に、save メソッドを使用して更新された PDF ファイルを保存します。

次のコードスニペットは、指定された注釈タイプによって注釈を削除する方法を示しています。

```java
public static void DeleteAnnotation() {
        // ドキュメントを開く
        Scanner consoleScanner = new Scanner(System.in);
        Document document = new Document(_dataDir + "sample_cats_dogs.pdf");
        int index;
        for (index = 1; index <= document.getPages().get_Item(1).getAnnotations().size(); index++) {
            System.out.println(index + ". " + document.getPages().get_Item(1).getAnnotations().get_Item(index).getName()
                    + " " + document.getPages().get_Item(1).getAnnotations().get_Item(index).toString());
        }
        System.out.print("番号を入力してください:");
        index = consoleScanner.nextInt();

        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(document);
        annotationEditor.deleteAnnotation(document.getPages().get_Item(1).getAnnotations().get_Item(1).getName());

        // 更新された PDF を保存
        annotationEditor.save(_dataDir + "DeleteAnnotation.pdf");
        consoleScanner.close();
    }
```
[PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) は、既存のPDFファイルからすべての注釈を削除することができます。

まず、[PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) を作成し、BindPdfメソッドを使用して入力PDFファイルをバインドします。

その後、[deleteAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#deleteAnnotation-java.lang.String-) メソッドを呼び出して、ファイルからすべての注釈を削除し、Saveメソッドを使用して更新されたPDFファイルを保存します。次のコードスニペットは、PDFファイルからすべての注釈を削除する方法を示しています。

```java
public static void DeleteAllAnnotations() {
    // ドキュメントを開く
    PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
    annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
    // すべての注釈を削除
    annotationEditor.deleteAnnotations();
    // 更新されたPDFを保存
    annotationEditor.save(_dataDir + "DeleteAllAnnotations_out.pdf");
}
```