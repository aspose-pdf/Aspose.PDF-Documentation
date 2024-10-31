---
title: AcroFormからデータを抽出する
linktitle: AcroFormからデータを抽出する
type: docs
weight: 50
url: /androidjava/extract-data-from-acroform/
description: AcroFormsは多くのPDFドキュメントに存在します。この記事は、Aspose.PDFを使用してAcroFormsからデータを抽出する方法を理解するのに役立ちます。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDFドキュメントからフォームフィールドを抽出する

Aspose.PDF for Android via Javaでは、フォームフィールドを作成および入力するだけでなく、PDFファイルからフォームフィールドデータやフォームフィールド情報を簡単に抽出することもできます。

フォームフィールドの名前を事前に知らないと仮定します。この場合、PDF内の各ページを反復し、PDF内のすべてのAcroFormsおよびフォームフィールドの値に関する情報を抽出する必要があります。フォームにアクセスするには、[getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--) メソッドを使用する必要があります。

```java
 public void extractFormFields () {
        // ドキュメントを開く
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // すべてのフィールドから値を取得
        StringBuilder sb=new StringBuilder();
        for (com.aspose.pdf.Field formField : document.getForm().getFields()) {
            sb.append("フィールド名: ");
            sb.append(formField.getPartialName());
            sb.append(" 値: ");
            sb.append(formField.getValue());
            sb.append('\n');
        }
        resultMessage.setText(sb);
    }
```


フォームフィールドの名前を知っている場合は、Documents.Form コレクションのインデクサーを使用して、このデータをすばやく取得できます。

## タイトルでフォームフィールドの値を取得

フォームフィールドの Value プロパティを使用して、特定のフィールドの値を取得できます。値を取得するには、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトの [フォームフィールドコレクション](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--) からフォームフィールドを取得します。この例では、[TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) を選択し、[getValue](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) メソッドを使用してその値を取得します。

```java

    public void extractFormDataByName () {
        // ドキュメントを開く
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        com.aspose.pdf.TextBoxField textBoxField1
                =(com.aspose.pdf.TextBoxField) document.getForm().get("Last Name");

        resultMessage.setText("Last Name: " + textBoxField1.getValue());

    }
```


## PDFファイルからXMLへデータを抽出する

Formクラスは、ExportXmlメソッドを使用してPDFファイルからXMLファイルにデータをエクスポートすることを可能にします。データをXMLにエクスポートするためには、まずFormクラスのオブジェクトを作成し、次にFileStreamオブジェクトを使用してExportXmlメソッドを呼び出す必要があります。最後に、FileStreamオブジェクトを閉じ、Formオブジェクトを破棄します。以下のコードスニペットは、データをXMLファイルにエクスポートする方法を示しています。

```java
public void extractFormFieldsToXML () {
        // ドキュメントを開く
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        com.aspose.pdf.facades.Form form=new com.aspose.pdf.facades.Form();
        form.bindPdf(document);
        File file=new File(fileStorage, "output.xml");
        try {
            // XMLファイルを作成する。
            FileOutputStream xmlOutputStream;
            xmlOutputStream=new FileOutputStream(file.toString());
            // データをエクスポートする
            form.exportXml(xmlOutputStream);

            // ファイルストリームを閉じる
            xmlOutputStream.close();
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // ドキュメントを閉じる
        form.dispose();
    }
```


## PDFファイルからFDFへデータをエクスポートする

PDFフォームデータをXFDFファイルにエクスポートするには、[Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form)クラスの[exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-)メソッドを使用します。

これは`com.aspose.pdf.facades`のクラスであることに注意してください。同じ名前ですが、このクラスは目的が少し異なります。

データをFDFにエクスポートするには、`Form`クラスのオブジェクトを作成し、`OutputStream`オブジェクトを使用して`exportXfdf`メソッドを呼び出す必要があります。次のコードスニペットは、データをXFDFファイルにエクスポートする方法を示しています。

```java
public void extractFormExportFDF () {
        // ドキュメントを開く
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        File file=new File(fileStorage, "student.fdf");

        com.aspose.pdf.facades.Form form=new com.aspose.pdf.facades.Form(document);
        FileOutputStream fdfOutputStream;
        try {

            fdfOutputStream=new FileOutputStream(file.toString());

            // データをエクスポートする
            form.exportFdf(fdfOutputStream);

            // ファイルストリームを閉じる
            fdfOutputStream.close();

        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


## PDFファイルからXFDFへのデータエクスポート

PDFフォームのデータをXFDFファイルにエクスポートするには、[Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form)クラスの[exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-)メソッドを使用できます。

データをXFDFにエクスポートするためには、まず`Form`クラスのオブジェクトを作成し、次に`OutputStream`オブジェクトを使用して`exportXfdf`メソッドを呼び出す必要があります。
以下のコードスニペットは、データをXFDFファイルにエクスポートする方法を示しています。

```java
    public void extractFormExportXFDF () {
        // ドキュメントを開く
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        File file=new File(fileStorage, "student.xfdf");

        com.aspose.pdf.facades.Form form=new com.aspose.pdf.facades.Form(document);
        FileOutputStream fdfOutputStream;
        try {

            fdfOutputStream=new FileOutputStream(file.toString());

            // データをエクスポート
            form.exportXfdf(fdfOutputStream);

            // ファイルストリームを閉じる
            fdfOutputStream.close();

        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```