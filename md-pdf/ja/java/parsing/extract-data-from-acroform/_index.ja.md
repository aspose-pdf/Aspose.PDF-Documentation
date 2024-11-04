---
title: AcroFormからデータを抽出する
linktitle: AcroFormからデータを抽出する
type: docs
weight: 50
url: /java/extract-data-from-acroform/
description: AcroFormsは多くのPDFドキュメントに存在します。この記事は、JavaとAspose.PDFを使用してAcroFormsからデータを抽出する方法を理解するのに役立つことを目的としています。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDFドキュメントからフォームフィールドを抽出する

Aspose.PDF for Javaは、フォームフィールドを作成および入力するだけでなく、PDFファイルからフォームフィールドデータやフォームフィールド情報を簡単に抽出することもできます。

フォームフィールドの名前を事前に知らない場合を考えます。その場合、PDF内の各ページを反復処理して、PDF内のすべてのAcroFormsやフォームフィールドの値についての情報を抽出する必要があります。フォームにアクセスするには、[getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--) メソッドを使用する必要があります。

```java
public static void ExtractFormFields() {
    String path= "/home/admin/pdf-examples/Samples/StudentInfoFormElectronic.pdf";
    com.aspose.pdf.Document document = new com.aspose.pdf.Document(path);
    // すべてのフィールドから値を取得
    for (com.aspose.pdf.Field formField : document.getForm().getFields()) {
        System.out.println("フィールド名 :" + formField.getPartialName());
        System.out.println("値 : " + formField.getValue());
    }
}
```


ドキュメントのフォームフィールドの名前がわかっている場合は、Documents.Form コレクションのインデクサーを使用してこのデータを迅速に取得できます。

## タイトルでフォームフィールドの値を取得する

フォームフィールドの Value プロパティを使用すると、特定のフィールドの値を取得できます。値を取得するには、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトの [フォームフィールドコレクション](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--)からフォームフィールドを取得します。この例では、[TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) を選択し、[getValue](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) メソッドを使用してその値を取得します。

```java
public static void ExtractFormDataByName() {
    String fileName = _dataDir+"/StudentInfoFormElectronic.pdf";
    com.aspose.pdf.Document document = new com.aspose.pdf.Document(fileName);        
    com.aspose.pdf.TextBoxField textBoxField1 = (com.aspose.pdf.TextBoxField)document.getForm().get("Last Name");

    System.out.println("Last Name :" + textBoxField1.getValue());
}
```


## PDFドキュメントからフォームフィールドをJSONに抽出

フォームデータをJSONにエクスポートするためには、[Gson](https://github.com/google/gson)のようなサードパーティライブラリを使用することをお勧めします。以下のスニペットは、`Name`と`Value`をJSONにエクスポートする方法を示しています：

```java
public static void ExtractFormFieldsToJson() {
    String path = "/home/admin/pdf-examples/Samples/StudentInfoFormElectronic.pdf";
    com.aspose.pdf.Document document = new com.aspose.pdf.Document(path);

    java.util.List<FormElement> formData = new java.util.ArrayList<FormElement>();
    for (com.aspose.pdf.Field formField : document.getForm().getFields()) {
        formData.add(new FormElement(formField.getPartialName(), formField.getValue()));
    }

    Gson gson = new Gson();
    String jsonString = gson.toJson(formData);
    System.out.println(jsonString);
}
```

この例では、追加のクラスを使用しました

```java
public class FormElement {
    public FormElement(String partialName, String Value) {
        this.Name = partialName;
        this.Value = Value;
    }
    public String Name;
    public String Value;
}
```


## PDFファイルからXMLへのデータ抽出

Formクラスは、ExportXmlメソッドを使用してPDFファイルからXMLファイルにデータをエクスポートすることを可能にします。データをXMLにエクスポートするには、まずFormクラスのオブジェクトを作成し、その後FileStreamオブジェクトを使用してExportXmlメソッドを呼び出します。最後に、FileStreamオブジェクトを閉じ、Formオブジェクトを破棄します。以下のコードスニペットは、データをXMLファイルにエクスポートする方法を示しています。

```java
public static void ExtractFormFieldsToXML() {

    String dataDir = "/home/admin/pdf-examples/Samples/StudentInfoFormElectronic.pdf";

    // ドキュメントを開く
    com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form();
    form.bindPdf(dataDir + "input.pdf");

    try {
        // XMLファイルを作成
        FileOutputStream xmlOutputStream;

        xmlOutputStream = new FileOutputStream(dataDir + "input.xml");
        // データをエクスポート
        form.exportXml(xmlOutputStream);

        // ファイルストリームを閉じる
        xmlOutputStream.close();

    } catch (IOException e) {

        e.printStackTrace();
    }

    // ドキュメントを閉じる
    form.dispose();
    ;
}
```


## PDFファイルからFDFへのデータのエクスポート

PDFフォームのデータをXFDFファイルにエクスポートするには、[Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form)クラスの[exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-)メソッドを使用できます。

これは`com.aspose.pdf.facades`のクラスであることに注意してください。似た名前ですが、このクラスは少し異なる目的を持っています。

データをFDFにエクスポートするには、`Form`クラスのオブジェクトを作成し、`OutputStream`オブジェクトを使用して`exportXfdf`メソッドを呼び出す必要があります。以下のコードスニペットは、データをXFDFファイルにエクスポートする方法を示しています。

```java
 public static void ExtractFormExportFDF() {
        String pdfFileName = Paths.get(_dataDir, "StudentInfoFormElectronic.pdf").toString();
        String fdfFileName = Paths.get(_dataDir, "student.fdf").toString();
        com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form(pdfFileName);

        OutputStream fdfOutputStream;
        try {

            fdfOutputStream = new FileOutputStream(fdfFileName);

            // データをエクスポート
            form.exportFdf(fdfOutputStream);

            // ファイルストリームを閉じる
            fdfOutputStream.close();

        } catch (IOException e) {
            // 例外を処理する
            e.printStackTrace();
        }

    }
```


## PDFファイルからXFDFへデータをエクスポートする

PDFフォームのデータをXFDFファイルにエクスポートするには、[Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form)クラスの[exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-)メソッドを使用します。

データをXFDFにエクスポートするには、`Form`クラスのオブジェクトを作成し、`OutputStream`オブジェクトを使用して`exportXfdf`メソッドを呼び出す必要があります。以下のコードスニペットは、XFDFファイルにデータをエクスポートする方法を示しています。

```java
public static void ExtractFormExportXFDF() {
        String pdfFileName = Paths.get(_dataDir, "StudentInfoFormElectronic.pdf").toString();
        String fdfFileName = Paths.get(_dataDir, "student.xfdf").toString();
        com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form(pdfFileName);

        OutputStream fdfOutputStream;
        try {

            fdfOutputStream = new FileOutputStream(fdfFileName);

            // データをエクスポート
            form.exportXfdf(fdfOutputStream);

            // ファイルストリームを閉じる
            fdfOutputStream.close();

        } catch (IOException e) {
            // TODO: 例外を処理
            e.printStackTrace();
        }
    }
```