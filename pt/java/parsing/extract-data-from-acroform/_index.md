---
title: Extrair dados de AcroForm
linktitle: Extrair dados de AcroForm
type: docs
weight: 50
url: pt/java/extract-data-from-acroform/
description: AcroForms existem em muitos documentos PDF. Este artigo visa ajudá-lo a entender como extrair dados de AcroForms usando Java e o Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extrair campos de formulário do documento PDF

Aspose.PDF para Java não apenas permite criar e preencher campos de formulário, mas também facilita a extração de dados de campos de formulário ou informações de campos de formulário de arquivos PDF.

Suponha que não sabemos os nomes dos campos do formulário com antecedência. Então devemos iterar sobre cada página no PDF para extrair informações sobre todos os AcroForms no PDF, bem como os valores dos campos do formulário. Para acessar o formulário, precisamos usar o método [getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--).

```java
public static void ExtractFormFields() {
    String path= "/home/admin/pdf-examples/Samples/StudentInfoFormElectronic.pdf";
    com.aspose.pdf.Document document = new com.aspose.pdf.Document(path);
    // Obter valores de todos os campos
    for (com.aspose.pdf.Field formField : document.getForm().getFields()) {
        System.out.println("Nome do Campo :" + formField.getPartialName());
        System.out.println("Valor : " + formField.getValue());
    }
}
```


Se você souber o nome dos campos do formulário dos quais deseja extrair valores, pode usar o indexador na coleção Documents.Form para recuperar rapidamente esses dados.

## Recuperar valor do campo do formulário por título

A propriedade Value do campo do formulário permite obter o valor de um campo específico. Para obter o valor, obtenha o campo do formulário da [coleção de campos do formulário](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--) do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Este exemplo seleciona um [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) e recupera seu valor usando o método [getValue](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--).

```java
public static void ExtractFormDataByName() {
    String fileName = _dataDir+"/StudentInfoFormElectronic.pdf";
    com.aspose.pdf.Document document = new com.aspose.pdf.Document(fileName);        
    com.aspose.pdf.TextBoxField textBoxField1 = (com.aspose.pdf.TextBoxField)document.getForm().get("Last Name");

    System.out.println("Last Name :" + textBoxField1.getValue());
}
```


## Extrair campos de formulário de documento PDF para JSON

Para exportar dados de formulário para JSON, recomendamos usar a biblioteca de terceiros como [Gson](https://github.com/google/gson).
Os trechos a seguir mostram como exportar `Name` e `Value` para JSON:

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

Neste exemplo, usamos uma classe adicional

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


## Extrair Dados para XML a partir de um Arquivo PDF

A classe Form permite exportar dados para um arquivo XML a partir do arquivo PDF usando o método ExportXml. Para exportar dados para XML, você precisa criar um objeto da classe Form e então chamar o método ExportXml usando o objeto FileStream. Finalmente, você pode fechar o objeto FileStream e descartar o objeto Form. O trecho de código a seguir mostra como exportar dados para um arquivo XML.

```java
public static void ExtractFormFieldsToXML() {

    String dataDir = "/home/admin/pdf-examples/Samples/StudentInfoFormElectronic.pdf";

    // Abrir documento
    com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form();
    form.bindPdf(dataDir + "input.pdf");

    try {
        // Criar arquivo XML.
        FileOutputStream xmlOutputStream;

        xmlOutputStream = new FileOutputStream(dataDir + "input.xml");
        // Exportar dados
        form.exportXml(xmlOutputStream);

        // Fechar fluxo de arquivo
        xmlOutputStream.close();

    } catch (IOException e) {

        e.printStackTrace();
    }

    // Fechar o documento
    form.dispose();
    ;
}
```


## Exportar Dados para FDF de um Arquivo PDF

Para exportar dados de formulários PDF para um arquivo XFDF, podemos usar o método [exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-) na classe [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form).

Por favor, note que é uma classe do `com.aspose.pdf.facades`. Apesar do nome similar, esta classe tem um propósito ligeiramente diferente.

Para exportar dados para FDF, você precisa criar um objeto da classe `Form` e depois chamar o método `exportXfdf` usando o objeto `OutputStream`. O seguinte trecho de código mostra como exportar dados para um arquivo XFDF.

```java
 public static void ExtractFormExportFDF() {
        String pdfFileName = Paths.get(_dataDir, "StudentInfoFormElectronic.pdf").toString();
        String fdfFileName = Paths.get(_dataDir, "student.fdf").toString();
        com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form(pdfFileName);

        OutputStream fdfOutputStream;
        try {

            fdfOutputStream = new FileOutputStream(fdfFileName);

            // Exportar dados
            form.exportFdf(fdfOutputStream);

            // Fechar fluxo de arquivo
            fdfOutputStream.close();

        } catch (IOException e) {
            // TODO: tratar exceção
            e.printStackTrace();
        }

    }
```


## Exportar Dados para XFDF de um Arquivo PDF

Para exportar dados de formulários PDF para um arquivo XFDF, podemos usar o método [exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-) na classe [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form).

Para exportar dados para XFDF, você precisa criar um objeto da classe `Form` e então chamar o método `exportXfdf` usando o objeto `OutputStream`. 
O trecho de código a seguir mostra como exportar dados para um arquivo XFDF.

```java
public static void ExtractFormExportXFDF() {
        String pdfFileName = Paths.get(_dataDir, "StudentInfoFormElectronic.pdf").toString();
        String fdfFileName = Paths.get(_dataDir, "student.xfdf").toString();
        com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form(pdfFileName);

        OutputStream fdfOutputStream;
        try {

            fdfOutputStream = new FileOutputStream(fdfFileName);

            // Exportar dados
            form.exportXfdf(fdfOutputStream);

            // Fechar fluxo de arquivo
            fdfOutputStream.close();

        } catch (IOException e) {
            // TODO: lidar com a exceção
            e.printStackTrace();
        }
    }
```