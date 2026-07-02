---
title:  AcroFormからデータを抽出する
linktitle:  AcroFormからデータを抽出する
type: docs
weight: 50
url: /ja/androidjava/extract-data-from-acroform/
description: AcroForm は多くの PDF ドキュメントに存在します。本記事では、Aspose.PDF を使用して AcroForm からデータを抽出する方法を理解できるよう支援することを目的としています。
lastmod: "2026-07-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF ドキュメントからフォームフィールドを抽出する

Aspose.PDF for Android via Java は、フォームフィールドを作成および入力できるだけでなく、PDF ファイルからフォームフィールド データやフォームフィールド 情報を簡単に抽出できるようにします。

フォームフィールドの名前を事前に知らないと仮定します。その場合、PDF の各ページを反復処理して、PDF 内のすべての AcroForms の情報とフォームフィールドの値を抽出する必要があります。フォームにアクセスするには、次のメソッドを使用する必要があります。 [getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--) メソッド。

```java
 public void extractFormFields () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Get values from all fields
        StringBuilder sb=new StringBuilder();
        for (com.aspose.pdf.Field formField : document.getForm().getFields()) {
            sb.append("Field Name: ");
            sb.append(formField.getPartialName());
            sb.append(" Value: ");
            sb.append(formField.getValue());
            sb.append('\n');
        }
        resultMessage.setText(sb);
    }
```

抽出したい値があるフォームフィールドの名前が分かっている場合は、Documents.Form コレクションのインデクサーを使用してこのデータをすばやく取得できます。

## タイトルでフォームフィールドの値を取得する

フォームフィールドの Value プロパティを使用すると、特定のフィールドの値を取得できます。値を取得するには、フォームフィールドを取得します [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトの [フォームフィールドコレクション](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--). この例は a を選択します [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) そして、その値を使用して取得します [getValue](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) メソッド。

```java

    public void extractFormDataByName () {
        // Open document
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

## PDFファイルからXMLへデータを抽出

Form クラスを使用すると、ExportXml メソッドにより PDF ファイルから XML ファイルへデータをエクスポートできます。XML へエクスポートするには、Form クラスのオブジェクトを作成し、FileStream オブジェクトを使用して ExportXml メソッドを呼び出す必要があります。最後に、FileStream オブジェクトを閉じ、Form オブジェクトを破棄できます。以下のコード スニペットは、XML ファイルへエクスポートする方法を示しています。

```java
public void extractFormFieldsToXML () {
        // Open document
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
            // Create xml file.
            FileOutputStream xmlOutputStream;
            xmlOutputStream=new FileOutputStream(file.toString());
            // Export data
            form.exportXml(xmlOutputStream);

            // Close file stream
            xmlOutputStream.close();
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Close the document
        form.dispose();
    }
```

## PDF ファイルから FDF へデータをエクスポート

PDF フォームデータを XFDF ファイルにエクスポートするには、次のものを使用できます [exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-) メソッドは [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) クラス。

ご注意ください、これは〜からのクラスです `com.aspose.pdf.facades`．類似した名前にもかかわらず、このクラスはわずかに異なる目的を持っています。

FDF にデータをエクスポートするには、オブジェクトを作成する必要があります `Form` クラスを作成し、次に呼び出す `exportXfdf` メソッドを使用する `OutputStream` オブジェクト。以下のコードスニペットは、データをXFDFファイルにエクスポートする方法を示しています。

```java
public void extractFormExportFDF () {
        // Open document
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

            // Export data
            form.exportFdf(fdfOutputStream);

            // Close file stream
            fdfOutputStream.close();

        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## PDFファイルからXFDFへデータをエクスポート

PDF フォームデータを XFDF ファイルにエクスポートするには、次のものを使用できます [exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-) メソッドは [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) クラス。

XFDF にデータをエクスポートするには、オブジェクトを作成する必要があります `Form` クラスを作成し、次に呼び出す `exportXfdf` メソッドを使用する `OutputStream` オブジェクト。 
以下のコードスニペットは、データを XFDF ファイルにエクスポートする方法を示しています。

```java
    public void extractFormExportXFDF () {
        // Open document
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

            // Export data
            form.exportXfdf(fdfOutputStream);

            // Close file stream
            fdfOutputStream.close();

        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

