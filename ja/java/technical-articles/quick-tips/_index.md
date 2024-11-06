---
title: クイックヒント
type: docs
weight: 50
url: ja/java/quick-tips/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

このページには、Aspose.PDF for Java API に関連するいくつかのクイックヒントが含まれています

{{% /alert %}}

## PDFにJavaScriptを追加

次のコードスニペットを使用して、PDFファイルにJavaScriptを設定/追加できます。

```java

String path = "D:\\";
String fileOut = path + "JavaScript.pdf";
IDocument document = null;
try
{

    document = new Document();
    document.getPages().add();
    document.getPages().add();

    // ドキュメントレベルでのJavaScriptの追加
    // 希望するJavaScript文を持つJavascriptActionをインスタンス化
    JavascriptAction javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

    // JavascriptActionオブジェクトをDocumentの希望するアクションに割り当てる
    document.setOpenAction(javaScript);
    document.setOpenAction(new JavascriptAction("app.alert('Hello PDF')"));

    // ページレベルでのJavaScriptの追加
    document.getActions().setBeforeClosing(new JavascriptAction("app.alert('document is closing')"));

    document.getPages().get_Item(1).getActions().setOnOpen(new JavascriptAction("app.alert('page 1 is opened')"));

    document.getPages().get_Item(2).getActions().setOnOpen(new JavascriptAction("app.alert('page 2 is opened')"));

    document.getPages().get_Item(2).getActions().setOnClose(new JavascriptAction("app.alert('page 2 is closed')"));

    document.save(fileOut);

}
finally { if (document != null) document.dispose(); document = null; }

```


**いくつかの例**

```java

// 印刷後
document.getActions().setAfterPrinting(new JavascriptAction("app.alert('ファイルが印刷されました')"));

// 保存後
document.getActions().setAfterSaving(new JavascriptAction("app.alert('ファイルが保存されました')"));


```

## 使用されていないメモリの解放

Aspose.PDF for Javaを使用し終わった後に、他のプロセスのために最大限のメモリを確保したい場合は、次のコード行を実行する必要があります。

```java

 com.aspose.pdf.MemoryCleaner.clear();

```

## ByteArrayInputStreamからPDFを読み込む

次のコードスニペットは、PDFファイルをByteArrayに読み込み、その後ByteArrayInputStreamでDocumentオブジェクトをインスタンス化する手順を示しています。

```java

 // ソースPDFファイル

java.io.File file = new java.io.File("c:/pdftest/result.pdf");

java.io.FileInputStream fis = new java.io.FileInputStream(file);

//System.out.println(file.exists() + "!!");

//InputStream in = resource.openStream();

java.io.ByteArrayOutputStream bos = new java.io.ByteArrayOutputStream();

byte[] buf = new byte[1024];

try {

    for (int readNum; (readNum = fis.read(buf)) != -1;) {

        bos.write(buf, 0, readNum); //ここでは確かに0です

        //指定されたバイト配列からオフセットoffで始まるlenバイトを書き込みます。

        System.out.println("read " + readNum + " bytes,");

    }

} catch (java.io.IOException ex) {


}

byte[] bytes = bos.toByteArray();

// バイト配列を引数として渡しながらByteArrayInputStreamでDocumentオブジェクトをインスタンス化

com.aspose.pdf.Document doc = new 
com.aspose.pdf.Document(new java.io.ByteArrayInputStream(bytes));

// PDFファイルのページ数を取得

 System.out.println(doc.getPages().size());

```


## PDFをByteArrayOutputStreamに保存する

以下のコードスニペットは、結果のPDFファイルをByteArrayOutputStreamに保存する手順を示しています。

```java

 com.aspose.pdf.Document pdfDocument = new 
com.aspose.pdf.Document("source.pdf");

java.io.InputStream is = null;

java.io.ByteArrayOutputStream os = new java.io.ByteArrayOutputStream();

try{

pdfDocument.save(os,com.aspose.pdf.SaveFormat.Doc);

System.out.println(os.size());

is = new java.io.ByteArrayInputStream(os.toByteArray());

            os.close();

            os.flush();

pdfDocument.close();

}catch (Throwable e) {}

```